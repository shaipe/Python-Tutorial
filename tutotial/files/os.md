文件路径操作（os.path模块)
---

Python中可以用于对文件和目录进行操作的内置模块包括：

模块/函数名称	|功能描述
--|--
open()函数	|文件读取或写入
os.path模块	|文件路径操作
os模块	|文件和目录简单操作
zipfile模块	|文件压缩
tarfile模块	|文件归档压缩
shutil模块	|高级文件和目录处理及归档压缩
fileinput模块	|读取一个或多个文件中的所有行
tempfile模块	|创建临时文件和目录

os.path模块主要用于对文件路径的操作，如：路径分割和拼接、取文件相对路径和绝对路径、获取文件路径对应文件的时间属性、判断文件路径对应文件的类型、判断两个路径是否为同一个文件等。

### 1. 函数列表
```python
# 返回指定文件的绝对路径名
os.path.abspath(path)

# 将路径名称分割成两部分(head, tail)，tail是路径名称path中的最后一部分且不包含斜线（路径风格符），head是tail之前的所有部分；如果path以斜线结尾则 tail为空字符串，如果path中没有斜线则head为空字符串
os.path.split(path)

# 将路径名称分割成两部分(root, ext)， ext表示后缀名
os.path.splitext(path)  

# 返回path路径名的基名称，实际上就是os.path.split(path)函数返回值的第二个值
os.path.basename(path)  

# 返回path路径名的目录名称，实际上就是os.path.split(path)函数返回值的第一个值
os.path.dirname(path)  

# 将一个或多个路径中的非空值通过路径分隔符拼接成一个新的路径名称，如果在拼接过程中遇到绝对路径将会丢弃前面的部分并从该绝对路径重新开始拼接
os.path.join(path, *paths)  

# 指定的文件路径存在则返回Ture，否则返回False。如果是失效的链接文件则返回False
os.path.exists(path)  

# 返回该路径对应文件的最近一次访问时间的时间戳（秒），如果文件不存在或无法访问，则引发OSError
os.path.getatime(path)  

# 返回该路径对应文件的最后修改时间的时间戳（秒），如果文件不存在或无法访问，则引发OSError
os.path.getmtime(path)  

# 返回该路径对应文件的ctime，在某些系统上（如Unix上）是最后一次元数据更改时间，在其他系统上（如Windows）是路径的创建时间；如果文件不存在或无法访问，则引发OSError
os.path.getctime(path)  

# 返回指定路径对应文件的字节大小
os.path.getsize(path)  

# 返回path相对于start的相对路径
os.path.relpath(path, start=os.curdir)  

# 获取path的真实、绝对路径（可用于获取软链接文件指向的文件路径）
os.path.realpath(path)  

# 判断path是否是绝对路径，是则返回True，否则返回False
os.path.isabs(path)  

# 判断path是否是一个文件
os.path.isfile(path)  

# 判断path是否是一个目录
os.path.isdir(path) 

# 判断path是否是一个链接
os.path.islink(path)  

# 判断path是否是一个挂载点
os.path.ismount(path)  

# 判断path1和path2是否为同一个文件
os.path.samefile(path1, path2)  
```

注意： os.path.basename(path)函数与Unix 中的basename程序的不同之处在于，当path以路径分隔符结尾时（如'/usr/local/'），basename(path)返回值为空字符串('')，而basename程序返回值为倒数第二个路径分隔符之后的目录名称('local')


2. 实例
```python
>>> import os
>>> 
>>> os.path.abspath('test.sh')
'/root/test.sh'

>>> os.path.split('/root/test.sh')
('/root', 'test.sh')
>>> os.path.split('/usr/local')
('/usr', 'local')
>>> os.path.split('/usr/local/')
('/usr/local', '')
>>> os.path.split('test.sh')
('', 'test.sh')

>>> os.path.basename('/root/test.sh')
'test.sh'
>>> os.path.dirname('/root/test.sh')
'/root'

>>> os.path.splitext('test.sh')
('test', '.sh')
>>> os.path.splitext('/root/test.sh')
('/root/test', '.sh')
>>> os.path.splitext('/usrl/local')
('/usrl/local', '')

>>> os.path.join('/root')
'/root'
>>> os.path.join('/root', '1', '', '2', ' ', '3' )
'/root/1/2/ /3'
>>> os.path.join('/root', '/usr/local', 'test.sh')
'/usr/local/test.sh'
>>> os.path.join('/root', '/usr/local', '1', '')
'/usr/local/1/'

>>> os.path.exists('/root/test.sh')
True
>>> os.path.exists('/root/test.txt')
False
>>> os.path.exists('/etc/rc0.d')
True

>>> os.path.getatime('/etc/my.cnf')
1483433424.62325
>>> os.path.getmtime('/etc/my.cnf')
1472825145.4308648
>>> os.path.getctime('/etc/my.cnf')
1472825145.432865

>>> os.path.relpath('/etc/my.cnf')
'../etc/my.cnf'
>>> os.path.relpath('/etc/my.cnf', start='/etc')
'my.cnf

>>> os.path.realpath('/etc/rc0.d')
'/etc/rc.d/rc0.d'
>>> os.path.realpath('test.sh')
'/root/test.sh'

>>> os.system('ls -l /etc/my.cnf')
-rw-r--r-- 1 root root 597 Sep  2 22:05 /etc/my.cnf
>>> os.path.getsize('/etc/my.cnf')
597

>>> os.path.isabs('/etc/my.cnf')
True
>>> os.path.isabs('my.cnf')
False
>>> os.path.isfile('/etc/my.cnf')
True
>>> os.path.isdir('/etc/my.cnf')
False
>>> os.path.islink('/etc/my.cnf')
False
>>> os.path.islink('/etc/rc0.d')
True
>>> os.path.islink('/etc/rc0.d/')
False
>>> os.path.isdir('/etc/rc0.d/')
True
>>> os.path.isdir('/etc/rc0.d')
True

>>> os.system('df -Th')
Filesystem     Type      Size  Used Avail Use% Mounted on
/dev/vda1      ext4       40G  8.7G   29G  24% /
devtmpfs       devtmpfs  3.9G     0  3.9G   0% /dev
tmpfs          tmpfs     3.9G     0  3.9G   0% /dev/shm
tmpfs          tmpfs     3.9G  401M  3.5G  11% /run
tmpfs          tmpfs     3.9G     0  3.9G   0% /sys/fs/cgroup
tmpfs          tmpfs     783M     0  783M   0% /run/user/0
0
>>> os.path.ismount('/')
True
>>> os.path.ismount('/dev')
True
>>> os.path.ismount('/usr')
False

>>> os.path.samefile('/etc/rc0.d', '/etc/rc0.d')
True
>>> os.path.samefile('/etc/rc0.d', '/etc/rc0.d/')
True
```

### os模块

需要说明的是： os模块是一个混杂的操作系统接口模块，它提供了各种操作系统相关的功能，文件及目录操作只是其中一部分，而非全部。

在一些Unix平台上，这个模块的许多文件或目录的操作函数都支持下面的一个或多个特性：

指定一个文件描述符 对于某些函数，path参数不仅仅可以是一个字符串，还可以是一个文件描述符。该函数会操作这个文件描述符引用的文件。我们可以通过os.supports_fd来检查当前平台path参数是否可以指定为一个文件描述符，如果不可用将会引发一个NotImplementedError。如果该函数还支持dir_fd或follow_symlinks参数，当path被以文件描述符的方式提供时，指定dir_fd或follow_symlinks参数是错误的。
相对于目录描述符的路径 如果dir_fd不是None，它应该是一个指向某个目录的文件描述符，并且要操作的path应该是一个相对于该目录的相对路径；如果path是一个绝对路径，dir_fd将会被忽略。
不遵循符号链接 如果follow_symlinks是False，并且要操作的路径中最后一个元素是一个符号链接时，该函数将会操作这个链接文件，而不是操作这个链接文件指向的文件。

### os相关方法列表

```python
# 测试当前用户是否对path所对应文件有某种访问权限
# Python2
os.access(path, mode)
# Python3
os.access(path, mode, *, dir_fd=None, effective_ids=False, follow_symlinks=True)

# 更改当前工作目录，从Python3.3开始path参数允许是一个目录的文件描述符
os.chdir(path)

# 更改当前工作目录，从Python3.3开始该函数等价于os.chdir(fd)
os.chfdir(fd)

# 更改文件或目录权限，dir_fd和follow_symlinks是Python3.3新增的参数
os.chmod(path, mode, *, dir_fd=None, follow_symlinks=True)

# 更改文件或目录权限，如果path是个链接文件则影响是链接文件本身；Python3.3开始该函数等价于os.chmod(path, mode, follow_symlinks=False)
os.lchmod(path, mode)

# 更改文件或目录的属主和属组，如果不改变则设置为-1；dir_fd和follow_symlinks是Python3.3新增的参数
os.chown(path, uid, gid, *， dir_fd=None, follow_symlinks=True)

# 更改文件或目录的属主和属组，如果不改变则设置为-1；如果path是个链接文件则影响是链接文件本身；Python3.3开始该函数等价于os.chown(path, uid, gid, follow_symlinks=False)
os.lchown(path, uid, gid)

# 更改当前进程主目录
os.chroot(path)

# 返回一个表示当前目录的字符串
os.getcwd()

# 返回一个表示当前目录的字节串，Python3新添加的函数
os.getcwdb()

# 创建硬链接, *后面的参数都是Python3.3新增的
os.link(src, dst, *, src_dir_fd=None, dst_dir_fd=None, follow_symlinks=True)

# 创建软链接，*后面的参数都是Python3.3新增的
os.symlink(src, dst, target_is_directory=False, * dir_fd=None)

# 返回指定目录中所有文件列表，顺序不固定，且不包含‘.’和‘..’；注意path在Python2中没有默认值
os.listdir(path='.')

# 返回指定目录中所有文件条目对应的DirEntry对象迭代器，顺序不固定，则不包含'.'和‘..’；Python3.5新增的函数
os.scandir(path='.')

# 获取文件或文件描述的状态信息，染回一个stat_result对象，dir_fd和follow_symlinks都是Python3.3新增的参数
os.stat(path, *, dir_fd=None, follow_symlinks=True)

# 获取文件或文件描述的状态信息，如果path是一个链接文件则获取的是链接文件本身的状态信息；Python3.3开始，该函数等价于os.stat(path, dir_fd=dir_fd, folow_symlinks=False)
os.lstat(path, *, dir_fd=None)

# 创建一个名为path的目录并指定目录权限，如果目录已经存在则会引起FileExistsError；dir_fd是Python3.3开始新加的参数。需要说明的是该函数与os.makedirs()、os.mkfifo()函数创建的目或逛到文件的权限会受到umask的影响，比如指定mode为0777，实际目录权限为 0777 - umask = 0755
os.mkdir(path, mode=0o777, *, dir_fd=None)

# 递归创建目录，该函数功能与mkdir()相似，但是会递归创建所有的中间目录；exist_ok为Python3.2新增参数，表示当目录已经存在时是否正常返回，如果exist_ok为False（默认）且目标目录已经存在则会引发OSError
os.makedirs(name, mode=0o777, exists_ok=False)

# 创建一个FIFO(命名管道)文件，FIFO可以被当做正常文件那样访问；通常FIFOs被用作‘client’和‘server’类型进程的汇集点，server打开FIFO读取数据，client打开FIFO写入数据。
os.mkfifo(path, mode=0o666, *, dir_fd=None)

# 删除指定的文件，如果path是个目录将会引发OSError
os.remove(path, *, dir_fd=None)
os.unlink(path, *, dir_fd=None)

# 删除指定的空目录，如果目录不为空会引发OSError
os.rmdir(path, *, dir_fd=None)

# 递归删除指定路径中的所有空目录
os.removedirs(name)

# 目录或文件重命名，如果dst是一个目录将会引发OSError。在Unix平台上，如果dst存在且是一个文件，那么只要用户有权限就将会被静默替换；而在Windows平台上，如果dst存在，即使它是一个文件也会引发OSError
os.rename(src, dst, *, src_dir_fd=-None, dst_dir_fd=None)

# 目录或文件递归重命名
os.renames(old, new)

# 与os.rename()功能相同，区别在于：对于os.replace()来说，如果dst存在且是一个文件，那么只要用户有权限就将会被静默替换，而没有平台上的差别
os.replace(src, dst, *, src_dir_fd=None, dst_dir_fd=None)

# 返回链接文件指向的真实路径，类似于os.path.relpath(path)，但是该方法可能返回相对路径
os.readlink(path, *, dir_fd=None)

# 返回一个文件的某个系统配置信息，name表示配置项名称，可以通过os.pathconf_names来查看可用的值
os.pathconf(path, name)
```
关于os.access()函数的说明：默认以用户的真实uid（RUID）和gid来对文件的访问权限做检测，但是大部分操作将会使用有效uid（EUID）或gid去做检测，且Python3中可以通过将effective_ids参数设置为Ture来使用有效uid/gid来做权限检测（关于RUID/EUID/SUID的概念可以参考<<这篇文章>>
）。mode可取值为：os.F_OK（文件存在）、os.R_OK（可读）、os.W_OK（可写）、os.X_OK（可执行）中的一个或用逻辑运算符‘|’连接起来的多个。

2. 实例

```python
>>> import os
>>> 
>>> os.access('/bin/passwd', os.F_OK)
True
>>> os.access('/bin/passwd', os.F_OK|os.X_OK)
True
>>> os.access('/bin/passwd', os.F_OK|os.W_OK)
True

>>> os.getcwd()
'/root'
>>> os.chdir('/tmp')
>>> os.getcwd()
'/tmp'

>>> os.system('ls -l test*')
-rw-r--r-- 1 root root 0 Feb  9 09:02 test1.txt
lrwxrwxrwx 1 root root 9 Feb  9 09:02 test.txt -> test1.txt
0
>>> os.chmod('/tmp/test.txt', 0666)
>>> os.system('ls -l test*')
-rw-rw-rw- 1 root root 0 Feb  9 09:02 test1.txt
lrwxrwxrwx 1 root root 9 Feb  9 09:02 test.txt -> test1.txt
0

>>> os.link('test.txt', 'test')
>>> os.system('ls -li test*')
271425 lrwxrwxrwx 2 root  root  9 Feb  9 09:02 test -> test1.txt
271379 -rw-rw-rw- 1 mysql mysql 0 Feb  9 09:02 test1.txt
271425 lrwxrwxrwx 2 root  root  9 Feb  9 09:02 test.txt -> test1.txt
0

>>> os.listdir('.')
['zabbix_proxy.log', 'test.txt', 'zabbix_agentd.log', '.Test-unix', 'systemd-private-14bb029ad4f340d5ac49a6fb3c2ca6c9-systemd-machined.service-gJk0Cd', 'hsperfdata_root', 'wrapper-31124-1-out', 'a', 'test1.txt', 'zabbix_proxy.log.old', 'zabbix_agentd.log.old', 'systemd-private-14bb029ad4f340d5ac49a6fb3c2ca6c9-mariadb.service-kudcMu', 'test', '.X11-unix', '.font-unix', 'wrapper-31124-1-in', '.XIM-unix', '.ICE-unix', 'Aegis-<Guid(5A2C30A2-A87D-490A-9281-6765EDAD7CBA)>']
>>> os.listdir('/tmp')
['zabbix_proxy.log', 'test.txt', 'zabbix_agentd.log', '.Test-unix', 'systemd-private-14bb029ad4f340d5ac49a6fb3c2ca6c9-systemd-machined.service-gJk0Cd', 'hsperfdata_root', 'wrapper-31124-1-out', 'a', 'test1.txt', 'zabbix_proxy.log.old', 'zabbix_agentd.log.old', 'systemd-private-14bb029ad4f340d5ac49a6fb3c2ca6c9-mariadb.service-kudcMu', 'test', '.X11-unix', '.font-unix', 'wrapper-31124-1-in', '.XIM-unix', '.ICE-unix', 'Aegis-<Guid(5A2C30A2-A87D-490A-9281-6765EDAD7CBA)>']

>>> os.mkdir('/tmp/testdir')
>>> os.system('ls -l /tmp')
lrwxrwxrwx 2 root   root         9 Feb  9 09:02 test -> test1.txt
-rw-rw-rw- 1 mysql  mysql        0 Feb  9 09:02 test1.txt
drwxr-xr-x 2 root   root      4096 Feb  9 09:47 testdir
lrwxrwxrwx 2 root   root         9 Feb  9 09:02 test.txt -> test1.txt
>>> os.mkdir('/tmp/testdir')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
OSError: [Errno 17] File exists: '/tmp/testdir'
>>> os.mkdir('/tmp/a/b/c')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
OSError: [Errno 2] No such file or directory: '/tmp/a/b/c'
>>> os.makedirs('/tmp/a/b/c')  # mode默认为0777，结果却是0755，bug？
>>> os.makedirs('/tmp/b/c/d', 0700)
>>> os.system('ls -l /tmp')
total 2316
drwxr-xr-x 3 root   root      4096 Feb  9 10:16 a
drwx------ 3 root   root      4096 Feb  9 10:16 b
lrwxrwxrwx 2 root   root         9 Feb  9 09:02 test -> test1.txt
-rw-rw-rw- 1 mysql  mysql        0 Feb  9 09:02 test1.txt
drwxr-xr-x 2 root   root      4096 Feb  9 09:47 testdir
lrwxrwxrwx 2 root   root         9 Feb  9 09:02 test.txt -> test1.txt

>>> os.rename('/tmp/test1.txt', '/tmp/test3.txt')
>>> os.system('ls -l /tmp')
lrwxrwxrwx 2 root   root         9 Feb  9 09:02 test -> test1.txt
prw-r--r-- 1 root   root         0 Feb  9 10:21 test1.fifo
-rw-rw-rw- 1 mysql  mysql        0 Feb  9 09:02 test3.txt
drwxr-xr-x 2 root   root      4096 Feb  9 09:47 testdir
prw-r--r-- 1 root   root         0 Feb  9 10:20 test.fifo
lrwxrwxrwx 2 root   root         9 Feb  9 09:02 test.txt -> test1.txt

>>> os.readlink('/tmp/test.txt')
'test1.txt'

>>> os.rmdir('/tmp/testdir')
>>> os.rmdir('/tmp/a/b/c')  # 只删除空目录/tmp/a/b/c
>>> os.removedirs('/tmp/b/c/d')  # 先删除空目录/tmp/a/b/c，然后删除空目录/tmp/a/b，最后删除目录/tmp/a，而目录/tmp非空，因此不会被删除

>>> os.unlink('/tmp/test')
>>> os.unlink('/tmp/test.fifo')
>>> os.unlink('/tmp/test.txt')
>>> os.system('ls -l /tmp')
>>> os.remove('/tmp/test3.txt')
>>> os.remove('/tmp/test1.fifo')
```

### open 模式：

代码|说明
--|--
w|以写方式打开
a|以追加模式打开 (从 EOF 开始 必要时创建新文件)
r+|以读写模式打开
w+|以读写模式打开 (参见 w )
a+|以读写模式打开 (参见 a )
rb|以二进制读模式打开
wb|以二进制写模式打开 (参见 w )
ab|以二进制追加模式打开 (参见 a )
rb+|以二进制读写模式打开 (参见 r+ )
wb+|以二进制读写模式打开 (参见 w+ )
ab+|以二进制读写模式打开 (参见 a+ )
 
### open文件的操作方法

方法名|说明
--|--
fp.read([size]) |size为读取的长度，以byte为单位
fp.readline([size]) |读一行，如果定义了size，有可能返回的只是一行的一部分
fp.readlines([size]) |把文件每一行作为一个list的一个成员，并返回这个list。其实它的内部是通过循环调用readline()来实现的。如果提供size参数，size是表示读取内容的总长，也就是说可能只读到文件的一部分。
fp.write(str) |把str写到文件中，write()并不会在str后加上一个换行符
fp.writelines(seq) |把seq的内容全部写到文件中(多行一次性写入)。这个函数也只是忠实地写入，不会在每行后面加上任何东西。
fp.close() |关闭文件。python会在一个文件不用后自动关闭文件，不过这一功能没有保证，最好还是养成自己关闭的习惯。 如果一个文件在关闭后还对其进行操作会产生ValueError
fp.flush() |把缓冲区的内容写入硬盘
fp.fileno() |返回一个长整型的”文件标签“
fp.isatty() |文件是否是一个终端设备文件（unix系统中的）
fp.tell() |返回文件操作标记的当前位置，以文件的开头为原点
fp.next() |返回下一行，并将文件操作标记位移到下一行。把一个file用于for … in file这样的语句时，就是调用next()函数来实现遍历的。
fp.seek(offset[,whence]) |将文件打操作标记移到offset的位置。这个offset一般是相对于文件的开头来计算的，一般为正数。但如果提供了whence参数就不一定了，whence可以为0表示从头开始计算，1表示以当前位置为原点计算。2表示以文件末尾为原点进行计算。需要注意，如果文件以a或a+的模式打开，每次进行写操作时，文件操作标记会自动返回到文件末尾。
fp.truncate([size]) |把文件裁成规定的大小，默认的是裁到当前文件操作标记的位置。如果size比文件的大小还要大，依据系统的不同可能是不改变文件，也可能是用0把文件补到相应的大小，也可能是以一些随机的内容加上去。



### 4. 文件综合操作实例
示例功能，将文件夹下所有图片名称加上'_fc'

```python
# -*- coding:utf-8 -*-
import re
import os
import time
#str.split(string)分割字符串
#'连接符'.join(list) 将列表组成字符串
def change_name(path):
    global i
    if not os.path.isdir(path) and not os.path.isfile(path):
        return False
    if os.path.isfile(path):
        file_path = os.path.split(path) #分割出目录与文件
        lists = file_path[1].split('.') #分割出文件与文件扩展名
        file_ext = lists[-1] #取出后缀名(列表切片操作)
        img_ext = ['bmp','jpeg','gif','psd','png','jpg']
        if file_ext in img_ext:
            os.rename(path,file_path[0]+'/'+lists[0]+'_fc.'+file_ext)
            i+=1 #注意这里的i是一个陷阱
        #或者
        #img_ext = 'bmp|jpeg|gif|psd|png|jpg'
        #if file_ext in img_ext:
        #    print('ok---'+file_ext)
    elif os.path.isdir(path):
        for x in os.listdir(path):
            change_name(os.path.join(path,x)) #os.path.join()在路径处理上很有用
  
img_dir = 'D:\\xx\\xx\\images'
img_dir = img_dir.replace('\\','/')
start = time.time()
i = 0
change_name(img_dir)
c = time.time() - start
print('程序运行耗时:%0.2f'%(c))
print('总共处理了 %s 张图片'%(i))

```