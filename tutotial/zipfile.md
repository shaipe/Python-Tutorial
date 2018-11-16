文件压缩（zipfile模块）
---

目录
==

### 1. zipfile模块包含的类
顾名思义，zipfile模块用于文件的压缩操作，该模块包含以下几个类：

类名|描述
--|--
zipfile.ZipFile	|用于ZIP文件的读写操作
zipfile.PyZipFile|	用于创建包含Python库的ZIP归档文件
zipfile.ZipInfo	|用于表示归档文件中的一个成员信息

zipfile.ZipInfo类的实例可以通过ZipFile对象的getinfo()和infolist()方法获取。

### 2. zipfile模块中的函数和常量
函数/常量名	|描述
--|--
zipfile.is_zipfile(filename)	|判断filename是否是一个有效的ZIP文件，并返回一个布尔类型的值
zipfile.ZIP_STORED	|表示一个压缩的归档成员
zipfile.ZIP_DEFLATED	|表示普通的ZIP压缩方法，需要zlib模块的支持
zipfile.ZIP_BZIP2	|表示BZIP2压缩方法，需要bz2模块的支持；Python3.3新增
zipfile.ZIP_LZMA	|表示LZMA压缩方法，需要lzma模块的支持；Python3.3新增

### 3. zipfile.ZipFile类
类的构造方法
```python
class zipfile.ZipFile(file, mode='r', compression=ZIP_STORED, allowZip64=True)
# 创建一个ZipFile实例，表示打开一个ZIP文件。
```
参数：

- file：可以是一个文件的路径（字符串），也可以是一个file-like对象；
- mode：表示文件代开模式，可取值有：r（读）, w（写）, a（添加）, x（创建和写一个唯一的新文件，如果文件已存在会引发FileExistsError）
- compression：表示对归档文件进行写操作时使用的ZIP压缩方法，可取值有：ZIP_STORED, ZIP_DEFLATED, ZIP_BZIP2, ZIP_LZMA, 传递其他无法识别的值将会引起RuntimeError；如果取ZIP_DEFLATED, ZIP_BZIP2， ZIP_LZMA，但是相应的模块（zlib, bz2, lzma）不可用，也会引起RuntimeError；
- allowZip64：如若zipfile大小超过2GiB且allowZip64的值为False，则将会引起一个异常

说明：

- 从Python 3.2开始支持使用ZipFile作为上下文管理器（with语法）
- 从Python 3.3开始支持bzip2和lzma压缩
- 从Python 3.4开始allowZip64默认值改为True
- 从Python 3.5开始添加对unseekable streams的写操作支持以及对‘x’ mode的支持

实例方法列表

```python
# 打印该归档文件的内容
printdir()

# 从归档文件中展开一个成员到当前工作目录，memeber必须是一个完整的文件名称或者ZipInfo对象，path可以用来指定一个不同的展开目录，pwd用于加密文件的密码
extract(memeber, path=None, pwd=None)

# 从归档文件展开所有成员到当前工作目录，path和pwd参数作用同上，memebers必须是namelist()返回的list的一个子集
extractall(path=None, members=None, pwd=None)

# 返回一个与每一个归档成员对应的ZipInfo对象的列表
infolist()

# 返回归档成员名称列表
namelist()

# 返回一个包含压缩成员name相关信息的ZipInfo对象，如果name没有被包含在该压缩文档中将会引发KeyError
getinfo(name)

# 将归档文件中的一个成员作为一个file-like对象展开；name是归档文件中的文件名或者一个ZipInfo对象
open(name, mode='r', pwd=None)

# 关闭该压缩文件；退出程序前必须调用close()方法，否则一些必要记录不会被写入
close()

# 设置pwd作为展开加密文件的默认密码
setpassword(pwd)

# 读取归档文件中所有文件并检查它们的完整性，返回第一个被损坏的文件名称，或者None。对已关闭的ZipFile调用testzip()将会引发RuntimeError
testzip()

# 返回归档文件中name所指定的成员文件的字节。name是归档文件中的文件名称或一个ZipInfo对象。该归档文件必须以读(r)或追加(a)的模式打开。如果设置了pwd参数，则其将会覆盖setpassword(pwd)方法设置的默认密码。对一个已经关闭的ZipFile调用read()方法将会引发RuntimeError
read(name, pwd=Noneds)

# 将filename文件写入归档文件，可以通过arcname指定新文件名（需要注意的是文件名中磁盘盘符和开头的路径分隔符都会被移除）；compress_type表示压缩方法，如果指定了该参数则会覆盖ZipFile构造方法中的compression参数指定的值；要调用此方法，归档文件必须以'w', 'a'或'x'模式打开，如果对以'r'模式打开的ZipFile调用write()方法或者对已关闭的ZipFile调用write()方法将会引发RuntimeError
write(filename, arcname=None, compress_type=None)

# 将一个字节串写入归档文件；zinfo_or_arcname可以是归档文件中的文件名称，也可以是一个ZipInfo实例
writestr(zinfo_or_arcname, bytes[, compress_type])
```

### 4. zipfile.PyZipFile类
PyZipFile类用于创建包含Python库的ZIP存档

类的构造方法
PyZipFile的构造方法与ZipFile的构造方法参数基本一致，只是多了一个optimize参数
```python
class zipfile.PyZipFile(file, mode='r', compression=ZIP_STORED, allowZip64=True, optimize=-1)
```
说明：

- Python 3.2 新增optimize参数
- Python 3.4 allowZip64默认值改为True

实例方法列表
PyZipFile类的实例方法与ZipFile类的实例方法一致，只是多了一个writepy()方法：
```python
# 搜索*.py文件并将相应的文件添加到归档文件
writepy(pathname, basename='', filterfunc=None)
```
说明：

- 如果该PyZipFile实例的构造方法中的optimize参数没有被给出，或者被设置为-1，那么这里所指的“相应文件”是一个*.pyc文件，如果需要，会进行编译。
- 如果该PyZipFile实例的构造方法中的optimize参数值为0, 1或2，只有那些同样优化等级（参考compile()函数）的文件会被添加到归档文件。
- 如果pathname是一个文件，文件名必须以.py结尾，且仅仅是这些（*.py[co]）文件被添加，不包含路径信息；如果pathname是一个文件，但是不以.py结尾，将会引发RuntimeError。
- 如若pathname是一个目录，且这个目录不是一个package目录，则所有的（不包含路径信息）.py[co]文件将被添加；如果pathname是一个package目录，则所有的.py[co]都会作为一个文件路径被添加到这个package名称下，并且如果任何子文件夹是package目录，则会被递归添加。
- basename仅供内部使用
- filterfunc参数如果被给出，则其必须是一个只接收一个字符串参数的函数。每个文件路径在被添加到归档之前都会作为参数传递给filterfunc所指定的函数。如果filterfunc返回False，则这个路径将不会被添加，如果是一个目录，则它的内容将会被忽略。
- filterfunc参数是Python 3.4新加的。

### 5. zipfile.ZipInfo类
ZipInfo类的实例时通过ZipFile对象的getinfo()和infolist()方法返回的，其本身没有对外提供构造方法和其他方法。每一个ZipInfo对象存储的是ZIP归档文件中一个单独成员的相关信息，因此该实例仅仅提供了以下属性用于获取归档文件中成员的信息。

属性名称|描述
--|--
ZipInfo.filename|	文件名称
ZipInfo.date_time	|文件的最后修改日期和时间，这是一个tuple：(年, 月, 日, 时, 分, 秒)
ZipInfo.compress_type	|压缩类型
ZipInfo.comment	|文件备注
ZipInfo.extra	|扩展字段数据
ZipInfo.create_system	|ZIP归档的创建系统
ZipInfo.create_version	|创建ZIP归档的PKZIP版本
ZipInfo.extract_version	|展开ZIP归档所需要的PKZIP版本
ZipInfo.reserved	|必须是0
ZipInfo.flag_bits	|ZIP标志位
ZipInfo.volume	|文件头的Volume号码
ZipInfo.internal_attr	|内部属性
ZipInfo.external_attr	|外部属性
ZipInfo.header_offset	|文件头的字节偏移量
ZipInfo.CRC	|未压缩文件的CRC-32
ZipInfo.compress_size	|压缩后的数据大小
ZipInfo.file_size	|未压缩文件大小

### 6. 实例
实例1：文件归档与解压缩操作
```python
import zipfile

# 归档
z = zipfile.ZipFile('test.zip', 'w')
z.write('a.txt')
z.write('b.log')
z.close()

# 解压
z = zipfile.ZipFile('test.zip', 'r')
z.extractall()
z.close()

# 文件信息读取
z = zipfile.ZipFile('test.zip', 'r')
z.printdir()
z.namelist()
z.infolist()
zinfo = z.getinfo('a.txt')
print(zinfo.filename)
print(zinfo.date_time)
print(zinfo.file_size)
print(zinfo.compress_size)
z.close()
```
实例2：python文件归档

工程目录结构

MYPROG
│  hello.py
│
├─account
│      login.py
│      __init__.py
│
├─test
│      test_print.py
│
└─tools

tool.py代码
```python
import zipfile
 
pyz = zipfile.PyZipFile('myprog.zip', 'w')
pyz.writepy('MYPROG/hello.py')
pyz.writepy('MYPROG/tools')
pyz.writepy('MYPROG/test')
pyz.writepy('MYPROG/account')
pyz.close()

pyz.printdir()
```
输出结果：

```console
File Name                                             Modified             Size
hello.pyc                                      2017-02-16 11:46:20          130
tool.pyc                                       2017-02-16 11:55:44          135
test_print.pyc                                 2017-02-16 11:55:48          140
account/__init__.pyc                           2017-02-16 11:55:54          118
account/login.pyc                              2017-02-16 11:55:54          138
```