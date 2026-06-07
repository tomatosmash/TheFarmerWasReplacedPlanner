---
name: expansion-2
description: 扩张2 — 农场变为方形网格，解锁 for 循环和 get_world_size()
metadata:
  type: project
---

# 扩张 2 (Expansion 2)

## 解锁内容

### 农场形状变化
- 地块不再是一行，变为**方形网格**（square grid）
- 需要遍历整个网格来操作所有地块

### For 循环
引入 `for` 循环来在固定次数内重复执行代码：

```python
# 做 n 次翻转
for i in range(5):
    do_a_flip()
```

- `range(n)` 表示从 `0` 到 `n-1` 的数字范围，共 `n` 个元素
- `for` 循环对序列中的每个元素执行一次循环体
- 变量 `i` 在每次迭代中依次取 range 中的值

### get_world_size() 函数
- 返回农场的**边长**
- 使用此函数编写的代码在农场后续扩张时仍然有效（无需修改硬编码的数值）

## 示例代码

```python
# 收获农场第一列的每一个格子（无论农场多大）
for i in range(get_world_size()):
    harvest()
    move(North)
```

## 相关记忆
- [[game-overview]]
- [[expansion-1]]
