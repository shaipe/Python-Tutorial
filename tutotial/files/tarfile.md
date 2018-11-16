文件打包（tarfile模块）
---
tarfile模块用于读写tar归档文件，它也可以同时实现压缩功能。与zipfile模块相比，tarfile模块 可以直接将一个目录进行归档并压缩。另外，tarfile模块提供的api更“面向对象”化。

目录
---
[tarfile模块包含的两个主要的类](#tarfile模块包含的两个主要的类)
[tarfile模块包含的方法和常量](#tarfile模块包含的方法和常量)
[tarfile.TarFile类](#tarfile.TarFile类)


### 1.  tarfile模块包含的两个主要的类
类名|描述
--|--
TarFile	|该类提供了操作一个tar归档的接口
TarInfo	|一个TarInfo对象代表TarFile中的一个成员

这两个类的关系类似于zipfile.ZipFile与zipfile.ZipInfo的关系，TarInfo对象中保存了一个文件所需要的所有属性，比如：文件类型、文件大小、修改时间、权限、属主等，但是它不包含文件的数据。

### 2. tarfile模块包含的方法和常量

方法/常量名|	描述
--|--
tarfile.open(name=None, mode='r', fileobj=None, bufsize=10240, **kwargs)	|为指定的路径名name返回一个TarFile对象
tarfile.is_tarfile(name)	|如果name是一个tarfile模块可以读的tar归档文件则返回True，否则返回False
tarfile.ENCODING	|表示默认字符编码，在windows上为'utf-8'，否则为sys.getfilesystemencoding()的返回值
tarfile.USTAR_FORMAT	|POSIX.1-1922(ustar)格式
tarfile.GUN_FORMAT	|GUN tar格式
tarfile.PAX_FORMAT|	POSIX.1-2001(pax)格式
tarfile.DEFAULT_FORMAT	|表示创建归档的默认格式，当前值为GUN_FORMAT

关于open()函数的说明：
```python
tarfile.open(name=None, mode='r', fileobj=None, bufsize=10240, **kwargs)
```
该函数用于创建并返回一个TarFile对象。Python官方文档不建议直接使用TarFile的构造方法构建示例，而是建议使用这个open()函数来操作TarFile对象。下面我们来说说它的参数：

- name：表示要创建的归档文件的名称，通常为.tar, .tar.gz, .tar.bz2, .tar.xz，具体后缀应该与mode的值对应
- mode：必须是一个filemode[:compression]格式的字符串，默认值为'r'。filemode的可取值为'r', 'w', 'a', 'x'; compression表示压缩方式，可取值为'gz', 'bz2', 'xz'；需要注意的是'a:gz', 'a:bz2', 'a:xz'是不允许的格式。

下面是mode所有可取值的列表：

mode	|行为
--|--
'r:'	|以读模式打开一个未压缩的归档文件（通常后缀为*.tar）
'r:gz'	|以读模式打开一个通过gzip方式进行压缩的归档文件（通常后缀为*.tar.gz）
'r:bz2'	|以读模式打开一个通过bzip2方式进行压缩的归档文件（通常后缀为*.tar.bz2）
'r:xz'	|以读模式打开一个通过lzma方式进行压缩的归档文件（通常后缀为*.tar.xz）
'r' 或 'r:*'	|以读模式打开归档文件，可以打开以上任意方式压缩的归档文件，且会自动判断应该使用的压缩方式。推荐使用这个mode。
'w'或'w:'	|以写模式打开一个不进行压缩的归档文件
'w:gz'	|以写模式打开一个以gzip方式进行压缩的归档文件
'w:bz2'	|以写模式打开一个以bzip2方式进行压缩的归档文件
'w:xz'	|以写模式打开一个以lzma方式进行压缩的归档文件
'x'或'x:'|	同'w'或'w:'，但是如果归档文件已经存在会引发FileExistsError
'x:gz'	|同'w:gz'，但是如果归档文件已经存在会引发FileExistsError
'x:bz2'	|同'w:bz2''，但是如果归档文件已经存在会引发FileExistsError
'x:xz'	|同'w:xz'，但是如果归档文件已经存在会引发FileExistsError
'a'或'a:'	|以追加方式打开一个不进行压缩的股低昂文件，如果文件不存在则创建

对于 'w:gz', 'r:gz', 'w:bz2', 'r:bz2', 'x:gz', 'x:bz2'这些模式, tarfile.open() 接收关键字参数 compresslevel (默认值为9) 来指定该归档文件的压缩级别.

### 3. tarfile.TarFile类
类构的造方法
```python
class tarfile.TarFile(name=None, mode='r', fileobj=None, format=DEFAULT_FORMAT, tarinfo=TarInfo, dereference=False, ignore_zeros=False, encoding=ENCODING, errors='surrogateescape', pax_headers=None, debug=0, errorlevel=0)
```
参数说明：

下面所有的参数都是可选的，且可以作为TarFile类实例的属性被访问；
- name：指定归档文件路径名称；如果fileobj参数被指定该参数可以被忽略，且如果fileobj的name属性存在则取该属性的值；
- mode：：指定文档打开模式；r：读取已存在的归档，a：向一个已存在的文件追加数据，w：创建一个新的文件覆盖已经存在的文件，x：如果文件不存在才创建一个新文件
- fileobj：指定要读写的文件对象；如果指定了该参数，那么mode参数的值会被fileojb的mode属性值覆盖，且name参数可以被忽略；
- format：用于控制归档格式；必须是这些值中的一个：USTAR_FORMAT, GUN_FORMAT, PAX_FORMAT
- tarinfo：
- dereference：如果该参数值为False，则直接将软连接和硬链接添加到归档中；如果该参数值为True，则将目标文件的内容添加到归档中；
- ignore_zeros：该参数值对读取连续或损坏的归档时有效；如果值为False，则会把一个空block当做归档文件的结束位置；如果值为Ture，则会跳过空或无效的block并尝试获取尽可能多的归档成员
- debug：设置调试级别，可取值为0（不输出任何调试信息）至 3（输出所有调试信息），调试信息会被写到sys.stderr；
- errorlevel：设置错误级别；如果值为0，则使用TarFile.extract()方法时出现的所有错误都会被忽略，否则，如果debug可用，这些信息会作为错误信息出现在debug输出中。如果值为1，则所有fatal错误将会引发OSError；如果值为2，则所有非fatal错误将会引发TarError；
- encoding 和 errors：这两个参数定义了读写归档时使用的字符编码和如何处理转换错误

类方法
```python
classmethod TarFile.open(...)
```
这是个可选的构造方法，实际上tarfile.open()函数就是这个函数的快捷方式

实例方法
```python
# 将name文件添加到归档；name可以是任何类型的文件（如：目录，fifo管道，软连接等），arcname用于指定name文件被添加到归档后的新名字，arcname默认为None，表示文件名称保持不变。recursive值为Trur表示如果name文件是一个目录，则该目录中文件会被递归添加到归档中。exclude参数如果被指定，则其值必须是一个接受文件名作为参数的函数，且该函数必须返回一个布尔值，返回值为True表示该文件将不会被添加到归档中，反之则会被添加到归档中。filter参数如果被提供，则它必须是一个关键字参数且它应该是一个接收TarInfo对象作为参数的函数，该函数应该返回被修改后的TarInfo对象；如果它的返回值为None，那么该TarInfo将不会被添加到归档中。需要说明的是，从Python 3.2开始 exclude参数被废弃，新增filter参数，且使用filter代替exclude的功能
add(name, arcname=None, recursive=True, exclude=None, *, filter=None)

# 添加指定TarInfo对象到归档中。如果fileobj被提供，它应该是一个二进制文件，且会从这个二进制文件中读取tarinfo.size字节的内容添加到这个归档中。你可以通过gettarinfo()直接创建TarInfo对象
addfile(tarinfo, fileobj=None)

# 返回归档成员name对应的TarInfo对象（类似zipfile.ZipFile实例的getinfo(name)方法）；如果name无法在归档中找到会引发KeyError，如果一个成员在归档中不仅出现一次，则最后一次出现将被当做最新版本
getmemeber(name)

# 将归档中所有成员作为TarInfo对象的列表返回（类似zipfile.ZipFile实例的infolist()方法）
getmemebers()

# 将归档中所有成员的名称以列表形式返回（类似zipfile.ZipFile实例的namelist()方法）
getnames()

# 打印内容列表到sys.stdout（类似zipfile.ZipFile实例的printdir()方法）；如果verbose值为False，则仅打印成员的名称；如果verbose值为True，则打印的内容类似'ls -l'命令的输出；如果可选参数members被给出，它必须是getmembers()方法返回的列表的子集；Python 3.5新增memebers参数
list(verbose=True, *, memebers=None)

# （当以读模式打开归档时）该方法以TarInfo对象的形式返回归档的下一个成员，如果已经没有可用的成员则返回None
next()

# 将归档中的所有成员提取到当前工作目录或path参数指定的目录；如果memebers参数被指定，它必须是getmemebers()函数返回列表的子集；所有者、更改时间和权限等目录信息会在所有成员被提取后设置；如果numberic_owner值为True，将使用tarfile的uid和gid数字来设置提取后文件的属主和属组，否则将使用叔叔和属组的名字。Python 3.5中新增了number_owner参数
extractall(path=".", memebers=None, *, numeric_owner=False)

# 提取归档中的一个成员到当前工作目录或path指定的目录，member参数的值可以是一个文件名或一个TarInfo对象；Python 3.2添加了set_attrs参数，Python 3.5添加了numberic_owner参数
extract(member, path="", set_attrs=True, *, numberic_owner=False)

# 提取归档中的一个成员为一个文件对象，member参数的值可以是一个文件名或一个TarInfo对象；从Python 3.3开始，如果member是一个普通文件或是一个链接，该方法会返回一个io.BufferedReader对象，否则会返回None
extractfile(member)

# 通过对现有文件执行os.stat()操作的结果创建一个TarInfo对象；这个已存在的文件可以通过文件名name来指定，也而已通过文件对象fileobj来指定（文件描述符），文件被添加到归档后的文件名取值优先级为：arcname参数的值，fileobj.name属性的值，name参数的值；你可以在通过addfile()方法将该文件添加到归档之前对TarInfo对象的一些属性值进行修改
gettarinfo(name=None, arcname=None, fileobj=None)

# 关闭TarFile对象
close()
```

### 4. tarfile.TarInfo类

一个TarInfo对象表示TarFile中的一个成员。TarInfo对象中除了保存了一个文件所需要的所有属性（比如：文件类型、文件大小、修改时间、权限、属主等）之外，它还提供了一些用于判断其文件类型的方法。需要注意的是，它不包含文件的数据。TarInfo对象可以通过TarFile的getmember()、getmembers()和gettarinfo()方法获取。

类构造方法
```python
class tarfile.TarInfo(name="")
#类方法
# 从字符串缓冲区创建一个TarInfo对象并返回
classmethod TarInfo.frombuf(buf, encoding, errors)

从TarFile对象中读取一个成员并将其作为一个TarInfo对象返回
classmethod TarInfo.fromtarfile(tarfile)
```
**对象方法和属性**

方法/属性名	|描述
--|--
name	|归档成员名称
size|	字节大小
mtime|	最后更改时间
mode|	权限位
type|	文件类型，通常是以下几个常量中的一个：REGTYPE, AREGTYPE, LINKTYPE, SYMTYPE, DIRTYPE, FIFOTYPE, CONTTYPE, CHRTYPE, BLKTYPE, GUNTYPE_SPARSE。判断一个TarInfo对象类型的更方便的方式是使用下面的is*()方法
linkname	|目标文件名称，这只是在TarInfo对象的类型是LINKTYPE和SYMTYPE时有效
uid	|最初存储该成员的用户ID
gid	|最初存储该成员的组ID
uname|	用户名
gname|	组名
pax_headers	|一个包含pax扩展头的key-value字典
isfile() / isreg()	|判断TarInfo对象是否是一个普通文件
isdir()	|判断TarInfo对象是否是一个目录
issym()	|判断TarInfo对象是否是一个软链接
islnk()	|判断TarInfo对象是否是一个硬链接
ischr()	|判断TarInfo对象是否是一个字符设备
isblk()	|判断TarInfo对象是否是一个块设备
isfifo()|	判断TarInfo对象是否是一个FIFO管道
isdev()	|判断TarInfo对象是否是一个字符设备 或 块设备 或 FIFO管道
tobuf(format=DEFAULT_FORMAT, encoding=ENCODING, errors='surrogateescape')	|从一个TarInfo对象生成一个字符串缓冲区

### 5. 实例
工程目录结构：
```
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
```
tool.py
Python工程归档及解压操作：
```python
import tarfile

# 归档压缩
tf = tarfile.open('myprog.tar.gz', 'w:gz')
tf.add("MYPROG")
tf.close()

# 解压
tf = tarfile.open('myprog.tar.gz')
tf.extractall()
tf.close()

# 读取归档文件内容
tf = tarfile.open('myprog.tar.gz')
tf.list()
print(tf.getmembers())
f = tf.getmember('MYPROG/hello.py')
print(f.name)
print(f.size)
f.isfile()
tf.close()
```