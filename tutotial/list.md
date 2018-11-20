Python对列表进行操作
---

目录
===
- [条件替换](#条件替换)
- [批量替换](#批量替换)
- [映射替换](#映射替换)

Python里字符串有replace方法，但是List没有replace的方法：
```python
>>> lst = ['1','2','3']
>>> lst.replace('1', '4')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'replace'
```

### 条件替换
可以用列表解析的方法实现元素替换，下例里把 ‘1’ 替换成 ‘4’ ：
```python
>>> lst = ['1', '2', '3']
>>> rep = ['4' if x == '1' else x for x in lst]
>>> rep
['4', '2', '3']
```

### 批量替换
批量替换，即把一个列表里的元素全部替换成同一个元素，下例里把 ‘3’ 和 ‘4’ 都替换成’d‘：

```python
>>> lst = ['1', '2', '3', '4', '5']
>>> pattern = ['3', '4']
>>> rep = ['d' if x in pattern else x for x in lst]
>>> rep
['1', '2', 'd', 'd', '5']
```

### 映射替换

根据一个字典的映射关系替换，下例里把 ‘3’ 和 ‘4’ 都替换成英文：

```python
>>> lst = ['1', '2', '3', '4', '5']
>>> pattern = {'3':'three', '4':'four'}
>>> rep = [pattern[x] if x in pattern else x for x in lst]
>>> rep
['1', '2', 'three', 'four', '5']
```
