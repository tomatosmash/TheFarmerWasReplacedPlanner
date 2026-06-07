---
name: game-overview
description: 编程农场游戏的基本设定和核心机制
metadata:
  type: project
---

# 编程农场游戏概述

这是一个通过 Python 代码控制无人机进行作物培育和种植的编程游戏。

## 核心概念

- 通过 Python 代码控制无人机
- 使用不同的函数来进行农耕操作
- 每种作物有各自的种植要求和耗材

## 通用机制

### 耕地
- 调用 `till()` 函数进行耕地
- 第一次调用：将地块变为 `Grounds.Soil`（耕地）
- 再次调用：将地块变回 `Grounds.Grassland`（草地）
- 种植前必须先耕地（将地块变为 Soil）

### 种植
- 使用 `plant(Entities.<作物名>)` 函数种植作物
- 种植会消耗一定的耗材

### 相关枚举
- `Entities` - 作物/实体类型枚举
- `Grounds` - 地块类型枚举（Soil, Grassland 等）
