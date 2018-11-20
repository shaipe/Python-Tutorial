Python对字典(dict)操作
---

目录
===

## sorted对dict排序

**语法:** `sorted(iterable, key=None, reverse=False) `, 返回一个有序的列表

- iterable: 一个可以迭代的对象
- key:  用来比较的对象，可以省略
- reverse: 指定是否颠倒，即是否逆序，默认是正序， 可以省略

#### 根据key进行排序

```python
>>> dic = {"a": 121, "d": 231, "c": 111, "f": 343}
# 对字典的key值列表排序，返回列表
print(sorted(dic.keys()))
['a', 'c', 'd', 'f']

# 对字典的键值对元组列表排序，按元组的第1个元素排序，也就是 key
# 返回的是一个元组列表
>>> print(sorted(dic.items(), key=lambda x: x[0]))
[('a', 121), ('c', 111), ('d', 231), ('f', 343)]

>>> print(dict(sorted(dic.items(), key=lambda x: x[0])))
{'a': 121, 'c': 111, 'd': 231, 'f': 343}

#  使用reverse=True可以实现倒序
>>> print(sorted(dic.items(), key=lambda x: x[0], reverse=True))
[('f', 343), ('d', 231), ('c', 111), ('a', 121)]
```

### 根据value进行排序
```python
>>> dic = {"a": 121, "d": 231, "c": 111, "f": 343}

# 对字典的键值对元组列表排序，按元组的第2个元素排序，也就是 value
# 返回的是一个元组列表
>>> print(sorted(dic.items(), key=lambda x: x[1]))
[('c', 111), ('a', 121), ('d', 231), ('f', 343)]

# 此处使用dict函数转为dict时又对key进行排序了,还没有搞定
>>> print(dict(sorted(dic.items(), key=lambda x: x[1])))
{'a': 121, 'c': 111, 'd': 231, 'f': 343}
```