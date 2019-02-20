日常使用中经验记录
===


#### 1. DataFrame 列数据类型操作

##### Pandas所支持的数据类型: 

- 1. float 
- 2. int 
- 3. bool 
- 4. datetime64[ns] 
- 5. datetime64[ns, tz] 
- 6. timedelta[ns] 
- 7. category 
- 8. object 
默认的数据类型是int64,float64.

##### 查看数据类型
```python
df.dtypes
series.dtype
get_dtype_counts()
```
 
如果一列中含有多个类型,则该列的类型会是object,同样字符串类型的列也会被当成object类型. 
不同的数据类型也会被当成object,比如int32,float32

**示例**

```python
import pandas as pd

data = pd.DataFrame([[1, "2"], [2, "2"]])
data.columns = ["one", "two"]

print(data)

# 当前类型
print("----\n修改前类型：")
print(data.dtypes)

# 类型转换
data[["two"]] = data[["two"]].astype(int)

# 修改后类型
print("----\n修改后类型")
print(data.dtypes)

```


#### 2. pandas 对象类型转换

##### Series转为DataFrame

```python
# 转换为DataFrame
df=s.to_frame()
```
虽然Series有一个to_frame()方法，但是当Series的index也需要转变为DataFrame的一列时，这个方法转换会有一点问题。所以，下面我采用将Series对象转换为list对象，然后将list对象转换为DataFrame对象。

**实例**

它的index为月份，values为数量，下面将这两列都转换为DataFrame的columns。
```python

import pandas as pd

month = Series 
# type(month) pandas.core.series.Series

dict_month = {'month':month.index,'numbers':month.values}
df_month = pd.DataFrame(dict_month)
```


##### Groupby参象转换

```python
# GroupBy对象转换list
print(list(grouped1))

# GroupBy对象转换dict
print(dict(list(grouped1)))
```