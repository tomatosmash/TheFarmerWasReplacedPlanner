---
name: fertilizer
description: 肥料和奇异物质 — 加速生长、感染机制与物品使用
metadata:
  type: project
---

# 肥料 (Fertilizer) 与奇异物质 (Weird Substance)

## 肥料 (Items.Fertilizer)

### 获取方式
- 每 **10 秒**自动获得 **1 份**肥料
- 每次升级后获取数量**翻倍**

### 效果
```python
use_item(Items.Fertilizer)
```
- 将无人机下方植物的**剩余生长时间缩短 2 秒**

### 副作用：感染
- 使用肥料加速生长的植物会被**感染**

## 感染机制

### 感染后效果
- 收获受感染植物时，**一半的产量**会变成奇异物质 `Items.Weird_Substance`

### 奇异物质 (Items.Weird_Substance)
```python
use_item(Items.Weird_Substance)
```
- 作用是**切换感染状态**（toggle）
- 影响范围：**目标植物 + 所有相邻植物**
- 在受感染植物上使用 → **治愈**该植物，同时感染其健康邻居
- 在健康植物上使用 → **感染**该植物，同时治愈其受感染邻居
- 效果是双向的：对自己和邻居同时生效

## 总结表

| 物品 | 效果 | 副作用 |
|------|------|--------|
| `Items.Fertilizer` | 缩短生长时间 2 秒 | 植物被感染 |
| `Items.Weird_Substance` | 切换植物及邻居的感染状态 | — |

## 相关记忆
- [[game-overview]]
