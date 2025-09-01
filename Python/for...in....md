在 Python 里，`for ... in ...` 背后依赖的就是 **迭代器协议**。  
如果你想要让自己的类能被 `for` 遍历，就必须实现一种“迭代机制”。

---

### 1. for 循环是怎么工作的？

当你写：
```python
for x in obj:
	...
```
Python 做的事情是：

1. 调用 `iter(obj)` 来获取一个迭代器。
            
    - 如果 `obj` 实现了 `__iter__`，就会调用 `obj.__iter__()`。
        
    - 否则会看 `obj` 有没有实现 `__getitem__`（从索引 `0` 开始一个个取值，直到 `IndexError`）。
        
2. 得到迭代器对象后，Python 会不停调用它的 `__next__()` 方法，获取下一个元素，直到抛出 `StopIteration`。
    

所以：**要支持 for 循环，类至少要满足下面两种情况之一**：

- 实现 `__iter__`（最常见、推荐）。
    
- 或者实现 `__getitem__`（老方式，不推荐）。
    

---

### 2. 举例：链表里实现 `__iter__`

假设你有一个链表类：

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        current = self.head
        while current:
            yield current   # 这里返回的是节点对象
            current = current.next
```
这样就能直接：
```python
ll = LinkedList()
# 假设已经插入了几个节点
for node in ll:
    print(node.data)
```