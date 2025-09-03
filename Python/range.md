`range()` 函数返回可迭代对象
```python
range(stop)
range(start, stop[, step])
```
- `start`: 计数从 `start` 开始，默认是从 `0` 开始。例如 `range(5)` 等价于 `range(0, 5)`
- `stop`: 计数到 `stop` 结束，但不包括 `stop`。例如：`range(0, 5) `是` [0, 1, 2, 3, 4]` 没有 `5`
- `step`：步长，默认为 `1`。例如：`range(0, 5) `等价于 `range(0, 5, 1)`
