# Desu

Desu adds common keys to cli commands.

## Quick usage example

### Without desu
```bash
$ mkdir some/subdir
mkdir: cannot create directory ‘some/subdir’: No such file or directory

$ mount /dev/sdb1 /mnt/usb
mount: mount point /mnt/usb does not exist

$ mkdir /mnt/usb
mkdir: cannot create directory ‘/mnt/usb‘: Permission denied

$ pacman cheese
error: no operation specified (use -h for help)

$ pacman -S cheese
error: you cannot perform this operation unless you are root.

$ ./a.out
zsh: permission denied: ./a.out (no x flag)

$ rm dir
rm: cannot remove 'dir': Is a directory
```

### With desu
```bash
$ desu mkdir some/subdir
# Ok. Desu adds -p flag to mkdir

$ desu mount /dev/sdb1 /mnt/usb
# Ok. Desu creates mount point before executing mount

$ desu mkdir /mnt/usb
# Ok. Desu adds sudo automatically for operations, that required root permissions

$ desu pacman cheese
# Ok. Desu allow to install packages without keys

$ desu pacman -S cheese
# Ok. Again sudo

$ desu ./a.out
# Ok. Desu adds +x flag, before execution local script

$ desu rm dir
# Ok. Desu automatically adds -r flag for directories
```

## Usage

Just type `desu` before command you use.

```bash
desu mount /dev/sdb3 /mnt/data/external
```

Also you can use following arguments:
* `-v`, `--verbose` - enables verbose output
* `-p<PLUGINS_DIR>`, `--plugins-dir<PLUGINSDIR>` - sets aditionaly plugins dir (can be used to add own plugins for each user)
* `-n`, `--no-global-plugins` - disables globally installed plugins

### Applying desu for all commands (without typing desu)

You may want to use desu automatically without typing desu, just typing commands. Here is common solutions for different shells.

#### Zsh

This solution isn't ideal, so make it only if you know that are you doing.

Append this lines to .zshrc:
```
add-desu() { [[ $BUFFER = desu* ]] || [[ $BUFFER = for* ]] || [[ $BUFFER = while* ]] || [[ $BUFFER = cd* ]] || [[ $BUFFER = *\=* ]] || BUFFER="desu $BUFFER"; zle .$WIDGET "$@"; }
zle -N accept-line add-desu
```

## Desu and The Fuck

If you interesting in desu you maybe already know about [The Fuck](https://github.com/nvbn/thefuck).

Desu's and fuck's goals are similar - help user to working in terminal without pain, but desu is preventive solution, that **helping with keys**. On the other hand fuck is late-decision solution that **helping with errors**.

So you just can use both on desu and fuck.

Also you can use desu as late-decision solution with `!!`:
```bash
$ mkdir /mnt/usb
mkdir: cannot create directory ‘/mnt/usb‘: Permission denied
$ desu !!
# Ok
```

And as you know, you can use desu in transparent mode (desu will automatically modify every command you type). Fuck can't work in that mode.

## Installation

1. `$ git clone ...`
1. `$ cd desu`
1. `$ ./install desu` **as root**
1. `$ ./install extra-plugins` (if you want)
1. `$ ./install zsh-transparency` **only if you need it**, see [transparent mode](https://github.com/d3adc0d3/desu#applying-desu-for-all-commands-without-typing-desu) for details

### Dependencies
* Python 3x
* Git (to install default plugins)

## Plugins

Desu based on plugin-driven model, so desu's core is tuny and easy to undestand, and all matching/modifying functionality is in plugins.

So desu functionality depends on plugins you install.

### Desu plugins repositories
* [Default plugins repository](https://github.com/d3adc0d3/desu-default-plugins) - contains usefull plugins for common commands. Automatically installed with default installation script
* [Extra plugins repository]() - contains usefull plugins, but for non-common commands

At the moment, I still working on the extra repository. Once it is ready, there will be placed a link to it.

### Writing your own plugins
TODO :D
