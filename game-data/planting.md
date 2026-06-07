---
name: planting
description: 种植系统 — plant() 函数、clear() 重置、混合种植
metadata:
  type: project
---

# 种植系统

## 自动生长
- **草 (Grass)** 会自动生长，无需种植

## plant() 函数
```python
plant(Entities.<作物名>)
```
- 在无人机**下方地块**种植指定作物
- 可以种植多种作物（如胡萝卜、灌木等），通过 `Entities` 枚举指定类型
- **注意**：部分作物（如胡萝卜）种植前需要先耕地 `till()`

## clear() 函数
```python
clear()
```
- 将整个农场重置为**草地**（Grassland）
- 无人机位置重置回 **(0, 0)**

## 混合种植 (Companion Planting)
- 当农场上**同时生长多种植物**时，可能会**提高产量**
- 具体机制需要进一步研究

## 相关记忆
- [[game-overview]]
- [[carrot]]
- [[bush]]
