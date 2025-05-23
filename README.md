<div align="center">

# WarshipGirlsR Speed Calculator

**简体中文** | [English](README_en.md)

_用于游戏《战舰少女R》中舰队作战航速计算的命令行工具_

[![GitHub License](https://img.shields.io/github/license/syzomnia-el/WarshipGirlsR-Speed-Calculator)](https://github.com/syzomnia-el/WarshipGirlsR-Speed-Calculator/main/LICENSE)
[![GitHub Release (latest by date)](https://img.shields.io/github/v/release/syzomnia-el/WarshipGirlsR-Speed-Calculator?include_prereleases&sort=date&display_name=release)](https://github.com/syzomnia-el/WarshipGirlsR-Speed-Calculator/releases)
[![Python Version](https://img.shields.io/badge/python-3.11%20%7C%203.12%20%7C%203.13-blue)](https://www.python.org)
[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/syzomnia-el/WarshipGirlsR-Speed-Calculator/codecov.yml)](https://github.com/syzomnia-el/WarshipGirlsR-Speed-Calculator/actions/workflows/codecov.yml)
[![Codecov](https://img.shields.io/codecov/c/gh/syzomnia-el/WarshipGirlsR-Speed-Calculator?token=T3Q72DSMHL)](https://codecov.io/gh/syzomnia-el/WarshipGirlsR-Speed-Calculator)

</div>

## 功能

- 计算游戏《战舰少女R》中舰队的`作战航速`，公式参考：[战斗机制 - 舰R百科](https://www.zjsnrwiki.com/wiki/%E6%88%98%E6%96%97%E6%9C%BA%E5%88%B6#%E6%88%98%E6%9C%AF%E8%BF%82%E5%9B%9E)。

## 平台支持

-[x] Windows

## 依赖

- [Python 3.13+](https://www.python.org)
- [uv](https://docs.astral.sh/uv)
- [PyInstaller](https://pyinstaller.org)
- [Coverage](https://coverage.readthedocs.io)

## 下载

从 [**发布页面**](https://github.com/syzomnia-el/WarshipGirlsR-Speed-Calculator/releases) 下载最新版本。

## 用法

1. 查看提示：

```bash
mean
# <提示信息>
```

2. 计算仅由`主力舰`或`护卫舰`组成的舰队的`作战航速`：

```bash
mean 34,39,36
# 36.33
```

3. 计算由`主力舰`和`护卫舰`共同组成的舰队的`作战航速`：

```bash
mean 34,39,36 35,36
# 35
```

4. 错误示例：

```bash
mean 34 39 36
# TypeError: too many arguments, required 1 or 2 but got 3: ['34', '39', '36']

mean sss
# ValueError: could not convert string to float: 'sss'
```

## 开发

- 克隆仓库：

```bash
git clone https://github.com/syzomnia-el/WarshipGirlsR-Speed-Calculator.git
```

- 安装包管理工具 `uv` 及其他依赖：

```bash
python -m pip install --upgrade pip
python -m pip install uv
uv sync
```

- 运行程序：

```bash
uv run src/mean.py
```

- 使用覆盖率工具 `coverage` 运行测试：

```bash
uv run coverage run --parallel-mode -m unittest discover -s tests
uv run coverage report -m
uv run coverage html
```

- 打包可执行文件：

```bash
.\pkg.ps1
```

或

```bash
uv run pyinstaller -F --optimize 2 src/mean.py -n mean --distpath bin/ --clean
```

## 许可证

本项目采用MIT许可证授权，详情请参阅[LICENSE](LICENSE)文件。
