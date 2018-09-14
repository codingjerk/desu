#!/usr/bin/env python


import os
import sys
import subprocess
import glob
import importlib
import argparse
import time


def get_plugin_filenames(plugins_dirs):
    result = []
    for plugins_dir in plugins_dirs:
        plugins_glob = os.path.join(plugins_dir, '*.py')
        result += glob.glob(plugins_glob)

    return result


def get_module_name_by_filename(plugins_filename):
    basename = os.path.basename(plugins_filename)
    name_without_ext = os.path.splitext(basename)[0]

    return name_without_ext


def load_plugin(plugin_filename):
    module_name = get_module_name_by_filename(plugin_filename)
    module_dir = os.path.dirname(plugin_filename)

    sys.path.append(module_dir)
    module = importlib.import_module(module_name)
    sys.path.pop()

    return module


def load_plugins(plugins_dir):
    plugin_names = get_plugin_filenames(plugins_dir)
    return (load_plugin(p) for p in plugin_names)


def modify_args(args, plugins, verbose=False):
    result = args[:]
    for plugin in plugins:
        if plugin.match(result):
            if verbose:
                print('desu: applying %s' % plugin.name, file=sys.stderr)

            result = plugin.modify(result)

    return result


def get_plugins_dir():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    plugins_subdir = 'plugins'

    return os.path.join(script_dir, plugins_subdir)


def run_command(args):
    process = subprocess.Popen(args)
    while True:
        try:
            if process.poll() is not None: break
            process.wait(5)
        except (subprocess.TimeoutExpired, KeyboardInterrupt):
            pass # Nothing to do there

    return process.returncode


def split_args(args):
    for desu_arg_index, arg in enumerate(args):
        if arg.find('-') != 0: # desu args ended
            break
    else:
        desu_arg_index = len(args)

    desu_args = args[:desu_arg_index]
    cmd_args = args[desu_arg_index:]

    return desu_args, cmd_args


def make_settings(args):
    parser = argparse.ArgumentParser(description='Desu adds common keys to commands')
    parser.add_argument('-v', '--verbose', action='store_true', help='enables verbose output')
    parser.add_argument('-p', '--plugins-dir', nargs='?', help='sets additionaly plugins dir')
    parser.add_argument('-n', '--no-global-plugins', action='store_true', help='disables globally installed plugins')
    parser.add_argument('COMMAND', nargs='*', help='command to execute')
    settings = parser.parse_args(args)

    settings.plugins_dirs = []
    if not settings.no_global_plugins:
        default_plugins_dir = get_plugins_dir()
        settings.plugins_dirs.append(default_plugins_dir)

    if settings.plugins_dir is not None:
        settings.plugins_dirs.append(settings.plugins_dir)

    return parser, settings


def main(args):
    desu_args, cmd_args = split_args(args)
    parser, settings = make_settings(desu_args)
    if len(cmd_args) == 0:
        parser.print_help()
        return 1

    plugins = load_plugins(settings.plugins_dirs)

    newargs = modify_args(cmd_args, plugins, settings.verbose)

    if settings.verbose:
        cmd_str = ' '.join(newargs)
        print('\ndesu: running as %s\n' % cmd_str, file=sys.stderr)

    try:
        return run_command(newargs)
    except FileNotFoundError as e:
        print(e.strerror, file=sys.stderr)
        return 1


if __name__ == '__main__':
    exit_code = main(sys.argv[1:])
    exit(exit_code)

