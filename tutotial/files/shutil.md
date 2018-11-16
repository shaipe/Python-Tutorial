高级文件和目录处理(shutil模块)
---

上面我们介绍了路径操作（os.path模块）、文件和目录操作（os模块）和 文件归档压缩操作（zipfile模块和tarfile模块），但是还是这些模块要么缺少一些常用的功能（如：文件复制、删除非空文件夹），要么使用起来不是那么方便，而shutil模块shutil提供了一些文件和文件集合的高级操作，可以弥补这些不足。

需要注意的是：虽然shutil.copy()和shutil.copy2()是高级复制函数，但是它们并不能拷贝所有的文件元数据(metadata)，例如在POSIX平台上，文件的属主、属组和ACLs等信息都会丢失。

### 1. 文件和目录操作
```python
# 文件内容（部分或全部）复制，参数是两个已经打开的文件对象；length是一个整数，用于指定缓冲区大小，如果其值是-1表示一次性复制，这可能会引起内存问题
shutil.copyfileobj(fsrc, fdst[, length])

# 文件内容全部复制（不包括metadata状态信息）， 参数是两个文件名，且dst必须是完整的目标文件名称；如果dst已经存在则会被替换；follow_symlinks是Python 3.3新增的参数，且如果它的值为False则将会创建一个新的软链接文件
shutil.copyfile(src, dst, *, follow_symlinks=True)

# 仅拷贝文件权限（mode bits），文件内容、属组、属组均不变，参数是两个文件名；follow_symlinks是Python 3.3新增的参数
shutil.copymode(src, dst, *, follow_symlinks=True)

# 仅拷贝文件状态信息（包括文件权限，但不包含属主和属组）：mode bits, atime, mtime, flags，参数是两个文件名；follow_symlinks是Python 3.3新增的参数
shutil.copystat(src, dst, *, follow_symlinks=True)

# 拷贝文件内容和权限，并返回新创建的文件路径；相当于copyfile + copymode，参数是两个路径字符串，且dst可以是一个目录的路径；follow_symlinks是Python 3.3新增的参数
shutil.copy(src, dst, *, follow_symlinks=True)

# 与copy函数功能一致，只是会把所有的文件元数据都复制；相当于copyfile + copystat，也相当于 'cp -p'（不包括属主和属组）；follow_symlinks是Python 3.3新增的参数
shutil.copy2(src, dst, *, follow_symlinks=True)

# 这个工厂方法接收一个或多个通配符字符串，然后创建一个可以被传递给copytree()方法的'ignore'参数的函数。文件名与指定的通配符匹配时，则不会被赋值。
shutil.ignore_patterns(*patterns)

# （递归）拷贝整个src目录到目标目录dst，且目标目录dst必须是不存在的。该函数相当于 'cp -pr'；目录的权限和时间通过shutilcopystat()来拷贝，单个文件通过shutil.copy2()来拷贝
shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2, ignore_dangling_symlinks=False)

# 递归删除，相当于 rm -r
shutil.rmtree(path, ignore_errors=False, onerror=None)

# 递归移动并返回目标路径，相当于move命令；如果dst是一个已经存在的目录，则src将会被移动到该目录里面；如果dst已经存在，但不是目录，他将会被覆盖；copy_function是Python 3.5新加的关键字参数
shutil.move(src, dst, copy_function=copy2)

# 以一个命名tuple的形式返回磁盘使用信息(total, used, free)，单位为字节；Python 3.3新增方法
shutil.disk_usage(path)

# 更改指定路径的属主和属组，user可以是一个系统用户名或一个uid，group也是这样；这两个参数至少要提供一个；Python 3.3新增方法
shutil.chown(path, user=None, group=None)

# 返回命名cmd的文件路径，相当于which命令；Python 3.3新增方法
shutil.which(cmd, mode=os.F_OK|os.X_OK, path=None)
```

### 2. 归档操作

shutil模块的当当操作是创建和读取压缩文件的高级工具，同时提供文档归档功能。这些高级工具的实现是基于zipfile和tarfile模块实现的，其中与make_archive相关的函数是在Python 2.7版本新增的，而与unpack_archive相关的函数是在Python3.2版本新增的。

```python
# 创建一个归档文件（zip或tar）并返回它的名字；
# basename是要创建的文件名称，包含路径，但是不包含特定格式的扩展名；
# format是归档格式，可取值为'zip', 'tar', 'gztar', 'bztar'和 ‘xztar’ 
# root_dir表示归档文件的根目录，即在创建归档之前先切换到它指定的目录，
# base_dir表示要进行归档的目录，如果没有提供则对root_dir目录下的所有文件进行归档压缩（它可以是绝对路径，也可以是相对于root_dir的相对路径，它将是归档中所有文件和目录的公共前缀）
# root_dir和base_dir默认都是当前目录
# dry_run如果值为Ture表示不会创建归档，但是操作输出会被记录到logger中，可用于测试
# loggger必须是一个兼容PEP 282的对象，通常是logging.Logger的一个实例
# verbose该参数没有用处且已经被废弃
# Python 3.5新增对xztar格式的支持
shutil.make_archive(base_name, format, root_dir=None, base_dir=None, verbose=0,
                    dry_run=0, owner=None, group=None, logger=None)

# 解压归档文件
# filename是归档文件的全路径
# extract_dir时解压归档的目标目录名称，如果没有提供，则取当前工作目录
# format是归档格式：'zip', 'tar' 或 'gztar'中的一种。或者是通过register_unpack_format()注册时的其他格式，如果未提供则会根据归档文件的扩展名去查找相应的解压器，如果没找到则会引发ValueError。
shutil.unpack_archive(filename[, extract_dir[, format]])

# 返回支持的归档格式列表，且该列表中的每个元素是一个元组(name, description)
# shutil默认提供以下归档格式：
# gztar: gzip'ed tar-file
# bztar: bzip2'ed tar-file（如果bz2模块可用）
# xztar: xz'ed tar-file（如果lzma模块可用）
# tar: uncompressed tar file
# zip: ZIP file
# 我们可以通过register_archive_format()来注册新的归档格式或者为已存在的格式提供我们自己的归档器
shutil.get_archive_formats()

# 以列表形式返回所有已注册的解压格式，每个列表中的每个元素都是一个元组(name, extensions, description)
# shutil默认提供的解压格式与shutil.get_archive_formats()返回结果一直
# 我们可以通过register_unpack_format()来注册新的格式或为已存在的格式提供我们自己的解压器
shutil.get_unpack_formats()

# 注册一个新的归档格式对应的归档器
shutil.register_archive_fromat(name, function[, extra_args[, description]])

# 从支持的归档格式列表中移除指定的归档格式
shutil.unregister_archive_fromat(name)

# 注册一个新的解压格式对应的解压器
shutil.register_unpack_format(name, extensions, function[, extra_args[, description]])

# 从支持的解压格式列表中移除指定的挤压格式
shutil.unregister_unpack_format(name)
```

### 3. 实例

```python
shutil.copyfile('/tmp/myprog/hello.py', '/tmp/hello.py')
# 仅复制文件内容
# -rw-r--r-- 1 root root 46 Feb 21 16:22 /tmp/hello.py

shutil.copymode('/tmp/myprog/hello.py', '/tmp/hello.py')
# 仅复制文件权限位
# -rwxr-xr-x 1 root root 46 Feb 21 16:46 /tmp/hello.py

shutil.copystat('/tmp/myprog/hello.py', '/tmp/hello.py')
# 仅复制文件元数据(atime, mtime)
# -rwxr-xr-x 1 root root 46 Feb 18 17:32 /tmp/hello.py

shutil.copy('/tmp/myprog/hello.py', '/tmp/hello1.py')
# 复制文件内容和权限位
# -rwxr-xr-x 1 root root 46 Feb 21 16:54 /tmp/hello1.py

shutil.copy2('/tmp/myprog/hello.py', '/tmp/hello2.py')
# 同时复制文件内容、权限为和时间
# -rwxr-xr-x 1 root root 46 Feb 18 17:32 /tmp/hello2.py

shutil.copytree('/tmp/myprog', '/tmp/myprog1')
# 复制一个目录（包括子目录和文件）

shutil.move('/tmp/myprog1', '/tmp/myprog2')
# 移动文件或目录，也可以看做是“重命名”

shutil.rmtree('/tmp/myprog2')
# 删除一个目录（包括子目录和文件）

shutil.make_archive('/data/myprog', 'gztar', root_dir='/tmp/', base_dir='myprog')
# 切换到/tmp目录下，将myprog目录以gzip的格式进行归档压缩，压缩文件路径为/data/myprog.tar.gz
```