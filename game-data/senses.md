---
name: senses
description: 感官系统 — 位置、物品数量、实体/地块检测、解锁查询
metadata:
  type: project
---

# 感官 (Senses)

无人机解锁视觉能力，可以获取周围环境信息。

## 位置函数

| 函数 | 返回值 | 说明 |
|------|--------|------|
| `get_pos_x()` | 当前 x 坐标 | 起始为 0，向 East（右）每格 +1 |
| `get_pos_y()` | 当前 y 坐标 | 起始为 0，向 North（上）每格 +1 |

初始位置为 **(0, 0)**。

## 物品查询

```python
num_items(Items.Hay)  # 返回当前拥有的干草数量
```
- 返回指定物品的**持有数量**

## 地块检测

| 函数 | 返回值 | 说明 |
|------|--------|------|
| `get_entity_type()` | 实体类型 或 `None` | 无人机下方是什么植物/实体 |
| `get_ground_type()` | 地块类型 | 无人机下方是什么地面 |

### None 关键字
- `None` 表示**没有值**
- 没有 `return` 语句的函数实际返回 `None`
- 无人机下方没有实体时，`get_entity_type()` 返回 `None`

### 使用示例
```python
# 如果在灌木上方就翻转一次
if get_entity_type() == Entities.Bush:
    do_a_flip()
```

## 解锁查询

```python
num_unlocked(unlock)
```
返回某个科技/解锁项目的等级或数量。

### 用法区别

| 调用方式 | 返回值 | 示例 |
|----------|--------|------|
| `num_unlocked(Unlocks.xxx)` | **等级**（可以是 >1） | `num_unlocked(Unlocks.Speed)` → 速度等级 |
| `num_unlocked(Unlocks.Senses)` | 1（已解锁）或 0 | — |
| `num_unlocked(Items.xxx)` | **0 或 1**（仅表示是否解锁） | `num_unlocked(Items.Carrot)` → 胡萝卜是否解锁 |
| `num_unlocked(Unlocks.Carrots)` | **等级** | 胡萝卜的解锁等级 |

> 关键区别：`Unlocks.Carrots` 返回等级，`Items.Carrot` 只返回 0 或 1。其他植物同理。

## 相关记忆
- [[game-overview]]
- [[expansion-1]]
- [[expansion-2]]
