<div align="center">

# WarshipGirlsR Speed Calculator

[简体中文](README.md) | **English**

_A command-line tool to calculate the `Combat Speed` of the fleet in the game `Warship Girls R`_

[![GitHub License](https://img.shields.io/github/license/syzomnia-el/WarshipGirlsR-Speed-Calculator)](https://github.com/syzomnia-el/WarshipGirlsR-Speed-Calculator/main/LICENSE)
[![GitHub Release (latest by date)](https://img.shields.io/github/v/release/syzomnia-el/WarshipGirlsR-Speed-Calculator?include_prereleases&sort=date&display_name=release)](https://github.com/syzomnia-el/WarshipGirlsR-Speed-Calculator/releases)
[![Python Version](https://img.shields.io/badge/python-3.11%20%7C%203.12%20%7C%203.13-blue)](https://www.python.org)
[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/syzomnia-el/WarshipGirlsR-Speed-Calculator/codecov.yml)](https://github.com/syzomnia-el/WarshipGirlsR-Speed-Calculator/actions/workflows/codecov.yml)
[![Codecov](https://img.shields.io/codecov/c/gh/syzomnia-el/WarshipGirlsR-Speed-Calculator?token=T3Q72DSMHL)](https://codecov.io/gh/syzomnia-el/WarshipGirlsR-Speed-Calculator)

</div>

## Features

- Calculate the `Combat Speed` of the fleet in the game `Warship Girls R`. Formula
  reference: [Combat Mechanics - Warship Girls R Wiki](https://www.zjsnrwiki.com/wiki/%E6%88%98%E6%96%97%E6%9C%BA%E5%88%B6#%E6%88%98%E6%9C%AF%E8%BF%82%E5%9B%9E).

## Supported Platforms

-[x] Windows

## Dependencies

- [Python 3.13+](https://www.python.org)
- [uv](https://docs.astral.sh/uv)
- [PyInstaller](https://pyinstaller.org)
- [Coverage](https://coverage.readthedocs.io)

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

## Development

- Clone the repository:

```bash
git clone https://github.com/syzomnia-el/WarshipGirlsR-Speed-Calculator.git
```

- Install Package Manager `uv` & dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install uv
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
.\pkg.ps1
```

or

```bash
uv run pyinstaller -F --optimize 2 src/mean.py -n mean --distpath bin/ --clean
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
