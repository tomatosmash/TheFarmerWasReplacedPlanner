# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

这是一个**编程农场游戏**的自动化项目。通过 Python 代码控制无人机在 6×6 网格农场中进行作物种植、收获和资源管理。代码在游戏的嵌入式 Python 环境中运行（非标准 Python）。

## 游戏知识库

`game-data/` 目录包含所有已记录的游戏机制和作物信息，是编写自动化代码的权威参考。修改代码前应先查阅相关文件：

| 文件 | 内容 |
|------|------|
| `game-overview.md` | 核心机制：till()、plant()、Grounds/Entities 枚举 |
| `game-rules.md` | Python 语法限制 |
| `planting.md` | plant()、clear()、混合种植 |
| `expansion-1.md` | move()、North/East/South/West、边界回绕 |
| `expansion-2.md` | for 循环、get_world_size() |
| `senses.md` | get_pos_x/y()、get_entity_type()、get_ground_type()、num_items()、num_unlocked()、None |
| `watering.md` | get_water()、use_item(Items.Water)、含水量 0~1、生长速度 1×~5× |
| `fertilizer.md` | use_item(Items.Fertilizer)、感染机制、Weird_Substance |
| `carrot.md` | Entities.Carrot、需耕地、消耗干草+木材 |
| `tree.md` | Entities.Tree、产出 5 木材、相邻树生长翻倍、棋盘格最优 |
| `pumpkin.md` | Entities.Pumpkin、消耗胡萝卜、巨型南瓜合并、20% 枯萎、6×6 最优 |
| `sunflower.md` | Entities.Sunflower、产出能量、花瓣 7~15、measure()、8 倍加成 |

## Python 语法限制

游戏环境是受限 Python，已知限制：
- **不支持 `is` 关键字**：必须用 `== None` 和 `!= None` 替代 `is None` 和 `is not None`
- **不支持 `"""` 三引号**：只能用 `#` 写注释，不能用 docstring
- 遇到其他语法错误时，优先尝试更基础的写法

## 核心 API 速查

```python
# 移动（边界回绕）
move(North)  # 还有 East, South, West

# 地块操作
till()                     # 切换 Soil ↔ Grassland
get_ground_type()          # 返回 Grounds.Soil 或 Grounds.Grassland
get_water()                # 返回 0~1 的含水量

# 种植与收获
plant(Entities.Carrot)     # 种植（不同作物消耗不同资源）
harvest()                  # 收获当前地块
can_harvest()              # 是否可收获（枯萎南瓜始终 False）
clear()                    # 重置农场为草地，无人机回 (0,0)

# 物品
use_item(Items.Water)      # 浇水 +0.25 含水量
use_item(Items.Fertilizer) # 加速生长 2 秒，但会感染植物
num_items(Items.Hay)       # 查询物品数量

# 感知
get_pos_x() / get_pos_y()  # 当前位置
get_entity_type()          # 下方实体类型，无则返回 None
get_world_size()           # 农场边长

# 向日葵专用
measure()                  # 返回花瓣数 7~15
```

## 关键游戏机制

- **棋盘格种树**：树在 4 个相邻方向有邻居时生长翻倍，满种 = 16×。用 `(x+y)%2` 做棋盘格让树互不相邻，生长最快。
- **南瓜合并**：n×n 全成熟时合并为巨型南瓜，n≥6 时产量 = n²×6。一个枯萎就阻止整块合并，需及时替换。
- **向日葵 8 倍**：≥10 株 + 收花瓣最多的那株。先收高花瓣再收低花瓣，否则损失加成。
- **含水量**：线性影响生长速度（1×~5×），蒸发量与当前含水量成正比。

## 当前代码

`farming.py` — 棋盘格（树+胡萝卜）自动耕种，无限循环收获并补种，含水量低于 0.5 自动浇水。
