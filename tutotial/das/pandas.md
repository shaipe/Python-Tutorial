Python Data Analysis Library - pandas
===

pandas是一个开源的，BSD许可的库，为Python编程语言提供高性能，易于使用的数据结构和数据分析工具。

pandas是NumFOCUS赞助的项目。这将有助于确保pandas成为世界级开源项目的成功，并有可能捐赠给该项目。



## 安装

```
pip3 install pandas
```

### Pandas库的亮点

- 一个快速、高效的DataFrame对象，用于数据操作和综合索引；
- 用于在内存数据结构和不同格式之间读写数据的工具：CSV和文本文件、Microsoft Excel、SQL数据库和快速HDF 5格式；
- 智能数据对齐和丢失数据的综合处理：在计算中获得基于标签的自动对齐，并轻松地将凌乱的数据操作为有序的形式；
- 数据集的灵活调整和旋转；
- 基于智能标签的切片、花哨的索引和大型数据集的子集；
- 可以从数据结构中插入和删除列，以实现大小可变；
- 通过引擎与强大的组聚合或转换数据，允许对数据集进行拆分-应用-组合操作；
- 数据集的高性能合并和连接；
- 层次轴索引提供了在低维数据结构中处理高维数据的直观方法；
- 时间序列-功能：日期范围生成和频率转换、移动窗口统计、移动窗口线性回归、日期转换和滞后。甚至在不丢失数据的情况下创建特定领域的时间偏移和加入时间序列；
- 对性能进行了高度优化，用Cython或C编写了关键代码路径。
- Python与Pandas在广泛的学术和商业领域中使用，包括金融，神经科学，经济学，统计学，广告，网络分析，等等。

### 常用功能及函数简介

#### 包导入

一般我们需要做如下导入，numpy和pandas一般需要联合使用：
```python
import pandas as pd
import numpy as np
```
本文采用如下缩写：

df：Pandas DataFrame对象
s：  Pandas Series对象

#### 数据导入

pd.read_csv(filename)：从CSV文件导入数据
pd.read_table(filename)：从限定分隔符的文本文件导入数据
pd.read_excel(filename)：从Excel文件导入数据
pd.read_sql(query, connection_object)：从SQL表/库导入数据
pd.read_json(json_string)：从JSON格式的字符串导入数据
pd.read_html(url)：解析URL、字符串或者HTML文件
pd.read_clipboard()：从粘贴板获取内容
pd.DataFrame(dict)：从字典对象导入数据
#### 数据导出

df.to_csv(filename)：导出数据到CSV文件
df.to_excel(filename)：导出数据到Excel文件
df.to_sql(table_name, connection_object)：导出数据到SQL表
df.to_json(filename)：以Json格式导出数据到文本文件
#### 创建对象

pd.DataFrame(np.random.rand(20,5))：创建20行5列的随机数组成的DataFrame对象
pd.Series(my_list)：从可迭代对象my_list创建一个Series对象
df.index = pd.date_range('1900/1/30', periods=df.shape[0])：增加一个日期索引
index和reindex联合使用很有用处，index可作为索引并且元素乱排序之后，所以跟着元素保持不变，因此，当重拍元素时，只需要对index进行才重排即可:reindex。

另外， reindex时，还可以增加新的标为NaN的元素。

#### 数据查看

df.head(n)：查看DataFrame对象的前n行
df.tail(n)：查看DataFrame对象的最后n行
df.shape()：查看行数和列数
df.info()：查看索引、数据类型和内存信息
df.describe()：查看数值型列的汇总统计
s.value_counts(dropna=False)：查看Series对象的唯一值和计数
df.apply(pd.Series.value_counts)：查看DataFrame对象中每一列的唯一值和计数
apply的用处很多，比如可以通过跟lambda函数联合，完成很多功能：将包含某个部分的元素挑出来等等。

 

cities['Is wide and has saint name'] = (cities['Area square miles'] > 50) & cities['City name'].apply(lambda name: name.startswith('San'))

 
#### 数据选取

df[col]：根据列名，并以Series的形式返回列
df[[col1, col2]]：以DataFrame形式返回多列
s.iloc[0]：按位置选取数据
s.loc['index_one']：按索引选取数据
df.iloc[0,:]：返回第一行

#### 数据清洗

df.columns = ['a','b','c']：重命名列名
pd.isnull()：检查DataFrame对象中的空值，并返回一个Boolean数组
pd.notnull()：检查DataFrame对象中的非空值，并返回一个Boolean数组
df.dropna()：删除所有包含空值的行
df.fillna(x)：用x替换DataFrame对象中所有的空值
s.astype(float)：将Series中的数据类型更改为float类型
s.replace(1,'one')：用‘one’代替所有等于1的值
df.rename(columns=lambda x: x + 1)：批量更改列名
df.set_index('column_one')：更改索引列

#### 数据处理：Filter, Sort, GroupBy

df[df[col] > 0.5]：选择col列的值大于0.5的行
df.sort_values(col1)：按照列col1排序数据，默认升序排列
df.groupby(col)：返回一个按列col进行分组的Groupby对象
df.groupby(col1).agg(np.mean)：返回按列col1分组的所有列的均值
df.pivot_table(index=col1, values=[col2,col3], aggfunc=max)：创建一个按列col1进行分组，并计算col2和col3的最大值的数据透视表
data.apply(np.mean)：对DataFrame中的每一列应用函数np.mean
数据合并

df1.append(df2)：将df2中的行添加到df1的尾部
df.concat([df1, df2],axis=1)：将df2中的列添加到df1的尾部
df1.join(df2,on=col1,how='inner')：对df1的列和df2的列执行SQL形式的join

#### 数据统计

df.describe()：查看数据值列的汇总统计
df.mean()：返回所有列的均值
df.corr()：返回列与列之间的相关系数
df.count()：返回每一列中的非空值的个数
df.max()：返回每一列的最大值
df.min()：返回每一列的最小值
df.median()：返回每一列的中位数
df.std()：返回每一列的标准差

#### Pandas支持的数据类型

int 整型
float 浮点型
bool 布尔类型
object 字符串类型
category 种类
datetime 时间类型

#### 补充：

df.astypes: 数据格式转换
df.value_counts:相同数值的个数统计
df.hist(): 画直方图
df.get_dummies: one-hot编码，将类型格式的属性转换成矩阵型的属性。比如：三种颜色RGB，红色编码为[1 0 0]
 

#### 参考文章：

[Pandas官网](http://pandas.pydata.org/)

[Pandas官方文档](http://pandas.pydata.org/pandas-docs/stable/index.html)

[Pandas Cheat Sheet -- Python for Data Science](https://link.zhihu.com/?target=https%3A//www.dataquest.io/blog/pandas-cheat-sheet/)

[10 minutes to Pandas](http://pandas.pydata.org/pandas-docs/stable/10min.html)

