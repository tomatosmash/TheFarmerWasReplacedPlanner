---
name: game-rules
description: 游戏中的 Python 语法限制和特殊规则
metadata:
  type: project
---

# 游戏规则与语法限制

## Python 语法限制

### 不支持的关键字
- **`is`** — 游戏中不支持 `is` 关键字，不能使用 `is None` 或 `is not None`
- 替代方案：使用 `== None` 和 `!= None`

### 不支持的注释方式
- **`"""`**（三引号）— 游戏中不支持三引号注释/文档字符串
- 只能使用 **`#`** 进行注释

### 注意事项
- 游戏的 Python 环境是受限的，并非标准 Python
- 遇到不支持的语法时，需要用更基础的方式替代

## 相关记忆
- [[game-overview]]
