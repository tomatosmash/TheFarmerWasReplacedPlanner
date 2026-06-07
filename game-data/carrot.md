---
name: carrot
description: 胡萝卜的种植方法、耗材和相关信息
metadata:
  type: project
---

# 胡萝卜 (Carrot)

## 基本信息
- 实体名称：`Entities.Carrot`
- 游戏内名称：胡萝卜

## 种植方法
1. 先调用 `till()` 函数耕地，将地块变为 `Grounds.Soil`
2. 调用 `plant(Entities.Carrot)` 种植胡萝卜

## 耗材需求
- **干草 (Hay)** - 需要一定数量
- **木材 (Wood)** - 需要一定数量
- 具体消耗数量可在游戏内植物的专属页面上查看

## 注意事项
- 种植前必须确保地块已耕地（Soil 状态）
- 种植时会自动消耗所需耗材
- `till()` 是切换函数：Soil ↔ Grassland

## 相关记忆
- [[game-overview]]
