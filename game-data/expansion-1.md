---
name: expansion-1
description: 扩张1 — 农场变大，无人机移动系统解锁
metadata:
  type: project
---

# 扩张 1 (Expansion 1)

## 解锁内容

### 农场扩大
- 农场范围变大，无人机有更多活动空间

### 移动系统
- 解锁 `move()` 函数，无人机可以移动
- 移动范围为每次 1 格

### 方向常量
引入四个方向常量：

| 常量 | 方向 | 说明 |
|------|------|------|
| `North` | 向上 | 向北/向上移动 |
| `East` | 向右 | 向东/向右移动 |
| `South` | 向下 | 向南/向下移动 |
| `West` | 向左 | 向西/向左移动 |

## 使用方法

```python
move(North)  # 向上移动 1 格
move(East)   # 向右移动 1 格
move(South)  # 向下移动 1 格
move(West)   # 向左移动 1 格
```

## 边界行为
- 无人机移动超过农场边缘时，会**回绕**（wrap around）到对面一侧继续移动
- 例：向上移动超出上边界 → 从下方重新出现，继续向上

## 示例代码
```python
# 无人机持续向上移动，碰到边界回绕
while True:
    move(North)
```

## 相关记忆
- [[game-overview]]
- [[expansion-2]] (下一级扩张)
