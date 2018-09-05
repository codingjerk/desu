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
* `-v`, `--verbose` -- e

### Applying desu for all commands (without typing desu)

You may want to use desu automatically without typing desu, just typing commands. Here is common solutions for different shells.

#### Zsh

## Desu and thef\*\*k

If you interesting in desu you maybe already know about thef\*\*k (link).

Desu's and thef\*\*k's goals are similar - help user to working in terminal without pain, but desu is preventive solution, that **helping with keys**. On the other hand thef\*\*k is late-decision solution that **helping with errors**.

So you just can use both on desu and thef\*\*k.

Also you can use desu as late-decision solution with `!!`:
```bash
$ mkdir /mnt/usb
mkdir: cannot create directory ‘/mnt/usb‘: Permission denied
$ desu !!
# Ok
```

And as you know, you can use desu in transparent mode (desu will automatically modify every command you type). Thef\*\*k can't work in that mode.

## Installation

### Dependencies
* Python 3x
* pexpect
* Git (for installation)

## Examples (with default plugins)

## Plugins

### Default plugins repository
Default plugins repository (link) contains usefull plugins for common commands.

### Extra plugins repository
Extra plugins repository contains usefull plugins, but for non-common commands.

At the moment, still is working on the extra repository. Once it is ready, there will be placed a link to it.

### Writing your own plugins

#### Example plugins repository
