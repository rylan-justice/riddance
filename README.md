# riddance

A tool designed to remove bloatware and restore freedom

## Features

- Remove pre-installed packages

- Enhance operating system privacy

## Prerequisites

- [Python](https://www.python.org/downloads/)

- [pip](https://pip.pypa.io/en/stable/installation/)

## Installation

```
python -m pip install --user riddance
```

## Usage

```
python -m riddance -h
```

| Command           | Description                                          |
| :---              | :---                                                 |
| `-h`, `--help`    | display help                                         |
| `-v`, `--version` | show version                                         |
| `-l`, `--list`    | list compatible operating systems and their versions |
| `-c`, `--check`   | check operating system and version compatibility     |
| `-d`, `--debloat` | debloat a compatible operating system                |

## Support

```
python -m riddance -l
```

|              |                                                    |
| :---:        | :---:                                              |
| **Linux**    |                                                    |
|              |                                                    |
| Fedora Linux | 38 (Workstation Edition), 39 (Workstation Edition) |

## License

[GNU General Public License v3.0 or later](https://github.com/rylan-justice/riddance/blob/main/COPYING)
