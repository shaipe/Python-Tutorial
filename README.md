Python教程
---

    Python是一种解释型、面向对象、动态数据类型的高级程序设计语言。

    Python由Guido van Rossum于1989年底发明，第一个公开发行版发行于1991年。

    像Perl语言一样, Python 源代码同样遵循 GPL(GNU General Public License)协议。


目录
===
- [Python环境安装](#环境安装)

## 环境安装

### Python in centos

```bash
#!/bin/bash
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
 
wget https://www.python.org/ftp/python/3.5.3/Python-3.5.3.tgz
 
mkdir /usr/local/python3 
tar -zxvf Python-3.5.3.tgz
cd Python-3.5.3

./configure --prefix=/usr/local/python3
make && make install
 
ln -s /usr/local/python3/bin/python3 /usr/bin/python3
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
pip3 -V
python3 -V
```

1. python 中pip更新
```bash
    python -m pip install --upgrade pip
```

主要两步操作，查看需要升级库，升级库。如下：
```bash
pip list # 列出安装的库
pip list --outdated # 列出有更新的库
pip install --upgrade library_name # 升级库library_name
```

2. python 中通过pip导出所有依赖

```bash
pip3 freeze > requirements.txt
```

3. pip 通过依赖文件安装

```bash
pip3 install --no-cache-dir -r requirements.txt
```

### Python 特点
- 1. 易于学习：Python有相对较少的关键字，结构简单，和一个明确定义的语法，学习起来更加简单。

- 2. 易于阅读：Python代码定义的更清晰。

- 3.易于维护：Python的成功在于它的源代码是相当容易维护的。

- 4.一个广泛的标准库：Python的最大的优势之一是丰富的库，跨平台的，在UNIX，Windows和Macintosh兼容很好。

- 5.互动模式：互动模式的支持，您可以从终端输入执行代码并获得结果的语言，互动的测试和调试代码片断。

- 6.可移植：基于其开放源代码的特性，Python已经被移植（也就是使其工作）到许多平台。

- 7.可扩展：如果你需要一段运行很快的关键代码，或者是想要编写一些不愿开放的算法，你可以使用C或C++完成那部分程序，然后从你的Python程序中调用。

- 8.数据库：Python提供所有主要的商业数据库的接口。

- 9.GUI编程：Python支持GUI可以创建和移植到许多系统调用。

- 10.可嵌入: 你可以将Python嵌入到C/C++程序，让你的程序的用户获得"脚本化"的能力。