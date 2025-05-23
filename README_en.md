# WarshipGirlsR Speed Calculator

[简体中文](README.md) | **English**

[![Python](https://img.shields.io/badge/python-3.13+-blue?style=flat-square)](https://www.python.org/)
[![uv](https://img.shields.io/badge/uv-0.7+-blue?style=flat-square)](https://docs.astral.sh/uv/)
[![License](https://img.shields.io/github/license/syzomnia-el/WarshipGirlsR-Speed-Calculator?style=flat-square)](LICENSE)
[![Code Coverage](https://img.shields.io/codecov/c/github/syzomnia-el/WarshipGirlsR-Speed-Calculator?style=flat-square)](https://codecov.io/gh/syzomnia-el/WarshipGirlsR-Speed-Calculator)

[![GitHub Repo stars](https://img.shields.io/github/stars/syzomnia-el/WarshipGirlsR-Speed-Calculator?style=social)](https://github.com/syzomnia-el/WarshipGirlsR-Speed-Calculator)
[![GitHub Release (latest by date)](https://img.shields.io/github/v/release/syzomnia-el/WarshipGirlsR-Speed-Calculator?style=flat-square)](https://github.com/syzomnia-el/WarshipGirlsR-Speed-Calculator/releases)
[![GitHub Issues](https://img.shields.io/github/issues/syzomnia-el/WarshipGirlsR-Speed-Calculator?style=flat-square)](https://github.com/syzomnia-el/WarshipGirlsR-Speed-Calculator/issues)

A command-line tool to calculate the `Combat Speed` of the fleet in the game `Warship Girls R`

## Features

- Calculate the `Combat Speed` of the fleet in the game `Warship Girls R`. Formula reference: [Combat Mechanics - Warship Girls R Wiki](https://www.zjsnrwiki.com/wiki/%E6%88%98%E6%96%97%E6%9C%BA%E5%88%B6#%E6%88%98%E6%9C%AF%E8%BF%82%E5%9B%9E).

## Supported Platforms

-[x] Windows
-[ ] macOS
-[ ] Linux

## Download

Download the latest release from
the [**Release Page**](https://github.com/syzomnia-el/WarshipGirlsR-Speed-Calculator/releases).

## Usage

1. View prompt:

```bash
mean
# <prompt info>
```

2. Calculate the `Combat Speed` of the fleet consists solely of `capital ships` or `escort ships`:

```bash
mean 34,39,36
# 36.33
```

3. Calculate the `Combat Speed` of the fleet consists of both `capital ships` and `escort ships`:

```bash
mean 34,39,36 35,36
# 35
```

4. Error examples:

```bash
mean 34 39 36
# TypeError: too many arguments, required 1 or 2 but got 3: ['34', '39', '36']

mean sss
# ValueError: could not convert string to float: 'sss'
```

## Dependencies

- [Python 3.13+](https://www.python.org/)
- [uv](https://docs.astral.sh/uv/)
- [PyInstaller](https://pyinstaller.org/)
- [Coverage](https://coverage.readthedocs.io/)

## Development

- Clone the repository:

```bash
git clone https://github.com/syzomnia-el/WarshipGirlsR-Speed-Calculator.git
```

- Install dependencies:

```bash
uv sync
```

- Run the program:

```bash
uv run src/main.py
```

- Run tests:

```bash
uv run coverage run -m unittest discover -s tests
uv run coverage report -m
uv run coverage html
```

- Build the executable:

```bash
./pkg.ps1
```

or

```bash
uv run pyinstaller -F --optimize 2 src/mean.py -n mean --distpath bin/ --clean
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
