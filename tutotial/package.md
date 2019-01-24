对python应用进行打包
---

## 一. Windows平台

### PyInstaller

#### 安装方法

```bash
pip install PyInstaller
```

#### 打包命令

```bash
# 打包Python文件成exe文件
pyinstaller -f -w xxx.py
```
#### 参数说明

参数|说明
--|--
-F|指定打包后只生成一个exe文件
-D|-onedir 创建一个目录,包含exe文件,但会依赖很多文件(默认选项)
-c| -console, -nowindowed 使用控制台, 不使用视窗(无界面-默认)
-w| -windowed, -noconsole 使用窗口, 无控制台
-p|添加搜索路径,让其找到对应的库
-i | 改变生成程序的icon图标

#### 用python程序进行打包
```python

from PyInstaller.__main__ import run

if __name__ == '__main__':
    print("start build updater ...")
    params = ['updater.py', '-F', '-c', '--icon=updater.ico']
    run(params)
    print("start build monitor ...")
    params = ["monitor.py", "-F", "-c", "--icon=monitor.ico"]
    run(params)

```

## 二. Mac系统

### py2app

####  安装

```bash
pip3 install py2app
```

#### 打包

```bash
# 1. 生成setup文件, run为程序启动文件
py2applet --make-setup run.py

# 2. 删除旧文件
rm -rf build dist
# 3. 打包app
python3 setup.py py2app

```

#### 添加图标

```python
# 修改创建的setup.py文件
# 在 OPTIONS 字典中添加 "iconfile": "youricon.icns" 即可：
from setuptools import setup

APP = ['run.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'app.icns'
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

```
