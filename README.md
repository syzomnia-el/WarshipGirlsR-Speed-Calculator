<div align="center">

# WarshipGirlsR Speed Calculator

**简体中文** | [English](README_en.md)

_一款用于游戏《战舰少女R》中舰队 `作战航速` 计算的命令行工具_

[![GitHub License](https://img.shields.io/github/license/syzomnia-el/WarshipGirlsR-Speed-Calculator)](LICENSE)
[![GitHub Release (latest by date)](https://img.shields.io/github/v/release/syzomnia-el/WarshipGirlsR-Speed-Calculator?include_prereleases&sort=date&display_name=release)](https://github.com/syzomnia-el/WarshipGirlsR-Speed-Calculator/releases)
[![Python Version](https://img.shields.io/badge/python-3.11%20%7C%203.12%20%7C%203.13-blue)](https://www.python.org)
[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/syzomnia-el/WarshipGirlsR-Speed-Calculator/codecov.yml)](https://github.com/syzomnia-el/WarshipGirlsR-Speed-Calculator/actions/workflows/codecov.yml)
[![Codecov](https://img.shields.io/codecov/c/gh/syzomnia-el/WarshipGirlsR-Speed-Calculator?token=T3Q72DSMHL)](https://codecov.io/gh/syzomnia-el/WarshipGirlsR-Speed-Calculator)

</div>

## 作战航速

游戏《战舰少女R》中用于 `战术迂回` 及 `航向判定` 的机制，舰队的 `作战航速` 由舰队中所有舰船的 `航速` 决定。

> 参考：
> [战斗机制 - 舰R百科](https://www.zjsnrwiki.com/wiki/%E6%88%98%E6%96%97%E6%9C%BA%E5%88%B6#%E6%88%98%E6%9C%AF%E8%BF%82%E5%9B%9E)

游戏中的舰船类型如下：

- **主力舰**：

  | 中文全称    | 中文简称 | 英文全称                                | 英文简称 | 
  |---------|------|-------------------------------------|------|
  | 战列舰     | 战列   | Battleship                          | BB   |
  | 航空战列舰   | 航战   | Aviation Battleship                 | BBV  |
  | 战列巡洋舰   | 战巡   | Battlecruiser                       | BC   |
  | 导弹战列舰   | 导战   | Battleship, guided missile          | BBG  |
  | 导弹大型巡洋舰 | 大巡   | Large Cruiser, guided missile       | BG   |
  | 航空母舰    | 航母   | Standard Aircraft Carrier           | CV   |
  | 装甲航母    | 装母   | Armored Aircraft Carrier            | AV   |
  | 导弹巡洋舰   | 导巡   | Крейсер，ракета                      | KP   |
  | 导弹驱逐舰   | 导驱   | Destroyer, anit-ship guided missile | ASDG |
  | 导弹潜水艇   | 导潜   | Submarine, guided missile           | SSG  |
  | 旗舰      | /    | Elite                               | /    |
  | 岸防要塞    | 要塞   | Fortress                            | /    |
  | 海军基地    | 港口   | Port                                | /    |
  | 空军基地    | 机场   | Airfield                            | /    |
  | 调谐舰     | 调谐   | ? ? ?                               | /    |

- **护卫舰**：

  | 中文全称    | 中文简称 | 英文全称                               | 英文简称 |
  |---------|------|------------------------------------|------|
  | 轻型航空母舰  | 轻母   | Light Aircraft Carrier             | CVL  |
  | 重巡洋舰    | 重巡   | Heavy Cruiser                      | CA   |
  | 轻巡洋舰    | 轻巡   | Light Cruiser                      | CL   |
  | 重雷装巡洋舰  | 雷巡   | Torpedo Cruiser                    | CLT  |
  | 航空巡洋舰   | 航巡   | Aviation Cruiser                   | CAV  |
  | 防空导弹巡洋舰 | 防巡   | Cruiser, guided missile            | CG   |
  | 浅水重炮舰   | 重炮   | Monitor                            | BM   |
  | 驱逐舰     | 驱逐   | Destroyer                          | DD   |
  | 防空导弹驱逐舰 | 防驱   | Destroyer, anit-air guided missile | AADG |
  | 潜水艇     | 潜艇   | Submarine                          | SS   |
  | 重炮潜艇    | 炮潜   | Submarine Monitor                  | SC   |
  | 补给舰     | 补给   | Replenishment Oiler                | AP   |

此外还分为：

- **水下舰艇**：潜艇、炮潜、导潜
- **水面舰艇**：其他类型舰船

计算 `作战航速` 时，遵循以下规则：

- 有水面舰艇时，水下舰艇不参与计算
- 轻母、防驱、防巡虽然是护卫舰，但作为主力舰参与计算

计算公式如下：

$$
\text{作战航速} = \begin{cases}
round \left(\cfrac{\sum \text{航速}}{n}, 2 \right), & \text{仅由主力舰或护卫舰组成}\\
\\
floor \left(\min \left(\cfrac{\sum \text{航速}_\text{主力舰}}{n_\text{主力舰}}, \cfrac{\sum \text{航速}_\text{护卫舰}}{n_{\text{护卫舰}}} \right) \right), & \text{由主力舰和护卫舰共同组成}
\end{cases}
$$

## 平台支持

- [x] Windows

## 下载

从 [发布页面](https://github.com/syzomnia-el/WarshipGirlsR-Speed-Calculator/releases) 下载最新版本。

## 用法

1. 查看提示：

```bash
mean
# <提示信息>
```

2. 计算仅由 `主力舰` 或 `护卫舰` 组成的舰队的 `作战航速`：

```bash
mean 34,39,36
# 36.33
```

3. 计算由 `主力舰` 和 `护卫舰` 共同组成的舰队的 `作战航速`：

```bash
mean 34,39,36 35,36
# 35
```

4. 错误示例：

```bash
mean 34 39 36
# TypeError: too many arguments, required 0, 1 or 2 but got 3: ['34', '39', '36']

mean sss
# ValueError: could not convert string to float: 'sss'
```

## 依赖

- [Python 3.11+](https://www.python.org)
- [uv](https://docs.astral.sh/uv)
- [PyInstaller](https://pyinstaller.org)
- [Coverage](https://coverage.readthedocs.io)

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
./pkg.ps1
```

或

```bash
uv run pyinstaller -F --optimize 2 src/mean.py -n mean --distpath bin/ --clean
```

## 许可证

本项目采用MIT许可证授权，详情请参阅 [LICENSE](LICENSE) 文件。
