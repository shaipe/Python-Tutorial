# -*- encoding: utf-8 -*-
import psutil
import time
import os
import logging
import logging.handlers
import platform
import configparser

"""
用于系统进程监控
author: shaipe
create: 2018-11-06
可以使用pyinstaller 将py文件打包为exe文件就可以到其他机器上运行
pyinstaller --onefile --nowindowed --icon=monitor.ico --clean monitor.py
"""

if platform.system() == 'Windows':
    from ctypes import windll, c_ulong


    def color_text_decorator(function):
        """
        给文本设置显示颜色
        :param function:
        :return:
        """
        def real_func(self, string):
            windll.Kernel32.GetStdHandle.restype = c_ulong
            h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))
            if function.__name__.upper() == 'ERROR':
                windll.Kernel32.SetConsoleTextAttribute(h, 12)
            elif function.__name__.upper() == 'WARN':
                windll.Kernel32.SetConsoleTextAttribute(h, 13)
            elif function.__name__.upper() == 'INFO':
                windll.Kernel32.SetConsoleTextAttribute(h, 14)
            elif function.__name__.upper() == 'DEBUG':
                windll.Kernel32.SetConsoleTextAttribute(h, 15)
            else:
                windll.Kernel32.SetConsoleTextAttribute(h, 15)
            function(self, string)
            windll.Kernel32.SetConsoleTextAttribute(h, 15)

        return real_func
else:
    def color_text_decorator(function):
        """
        给文本设置显示颜色
        :param function:
        :return:
        """
        def real_func(self, string):
            if function.__name__.upper() == 'ERROR':
                self.stream.write('\033[0;31;40m')
            elif function.__name__.upper() == 'WARN':
                self.stream.write('\033[0;35;40m')
            elif function.__name__.upper() == 'INFO':
                self.stream.write('\033[0;33;40m')
            elif function.__name__.upper() == 'DEBUG':
                self.stream.write('\033[0;37;40m')
            else:
                self.stream.write('\033[0;37;40m')
            function(self, string)
            self.stream.write('\033[0m')

        return real_func


class Logger(object):
    """
    日志对象
    """
    DEBUG_MODE = True   # 是否为调试模式

    LOG_LEVEL = 5   # 日志等级

    FORMAT = '%(asctime)s %(funcName)s[line:%(lineno)d] %(levelname)s %(message)s'
    # [%(asctime)s] [%(name)s] [%(levelname)s] %(message)s' # 日志输出格式

    ROTATING_MODE = 1   # 日志的切割模式; 1:表示文件大小进行分割,2:表示以时间周期进行分割

    def __init__(self, name):
        """
        构造方法
        :param name:
        """

        self.name = name

        current_path = os.path.join(os.getcwd(), 'logs')

        if not os.path.exists(current_path):
            os.makedirs(current_path)

        # base config
        logging.basicConfig()
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(logging.DEBUG if self.DEBUG_MODE else logging.INFO)
        formatter = logging.Formatter(self.FORMAT)

        if self.ROTATING_MODE == 2:
            # 按时间进行分割处理
            th_all = logging.handlers.TimedRotatingFileHandler(
                os.path.join(current_path, self.name + '_tr.log'), when='midnight', interval=1, backupCount=7)
            th_all.setFormatter(formatter)
            th_all.setLevel(logging.DEBUG)
            self.logger.addHandler(th_all)

        if self.ROTATING_MODE == 1:
            # 按大小进行分割处理
            rh_all = logging.handlers.RotatingFileHandler(
                os.path.join(current_path, self.name + '_fr.log'), mode='a', maxBytes=1024 * 1024 * 2, backupCount=5)
            rh_all.setFormatter(formatter)
            rh_all.setLevel(logging.DEBUG)
            self.logger.addHandler(rh_all)

        sh = logging.StreamHandler()
        sh.setFormatter(formatter)
        sh.setLevel(logging.DEBUG if self.DEBUG_MODE else logging.INFO)

        self.logger.addHandler(sh)
        self.stream = sh.stream

        # 防止在终端重复打印
        self.logger.propagate = 0

        """
        # output to user define file
        if file_path is None:
            file_path = os.path.join(os.path.dirname(
                os.path.abspath(__file__)), 'logs', 'log1.log')

            if not os.path.exists(file_path):
                os.makedirs(file_path)

            fh = logging.FileHandler()
            fh.setFormatter(formatter)
            fh.setLevel(logging.DEBUG if self.DEBUG_MODE else logging.INFO)

            self.logger.addHandler(fh)
            self.logger.propagate = 0  # 防止重复打印
        """

    @color_text_decorator
    def hint(self, string):
        """
        提示
        :param string:
        :return:
        """
        # 去除多余连续空格
        str_tmp = str(string)
        str_tmp = ' '.join(str_tmp.split())
        if self.LOG_LEVEL >= 5:
            return self.logger.debug(str_tmp)
        else:
            pass

    @color_text_decorator
    def debug(self, string):
        """
        输出调试信息
        :param string:
        :return:
        """
        # 去除多余连续空格
        str_tmp = str(string)
        str_tmp = ' '.join(str_tmp.split())
        if self.LOG_LEVEL >= 4:
            return self.logger.debug(str_tmp)
        else:
            pass

    @color_text_decorator
    def info(self, string):
        """
        直接以信息输出
        :param string:
        :return:
        """
        # 去除多余连续空格
        str_tmp = str(string)
        str_tmp = ' '.join(str_tmp.split())
        if self.LOG_LEVEL >= 3:
            return self.logger.info(str_tmp)
        else:
            pass

    @color_text_decorator
    def warn(self, string):
        """
        输出警告
        :param string:
        :return:
        """
        # 去除多余连续空格
        str_tmp = str(string)
        str_tmp = ' '.join(str_tmp.split())
        if self.LOG_LEVEL >= 2:
            return self.logger.warn(str_tmp)
        else:
            pass

    @color_text_decorator
    def error(self, string):
        """
        错误输出
        :param string:
        :return:
        """
        # print('str:', string)
        # 去除多余连续空格
        str_tmp = str(string)
        str_tmp = ' '.join(str_tmp.split())
        # print(self.LOG_LEVEL, string)
        if self.LOG_LEVEL >= 1:
            return self.logger.error(str_tmp)
        else:
            pass


def get_file_encoding(file_path, def_encoding='utf-8'):

    """
    获取文件编码方式
    :param file_path: 文件路径
    :param def_encoding: 默认编码方式
    :return:
    """

    import os

    if os.path.exists(file_path):
        with open(file_path, 'rb+') as f:
            import chardet
            encode = chardet.detect(f.read())
            # print(encode)
            enc = encode.get('encoding', def_encoding)
            if enc.lower().startswith('utf-16'):
                enc = def_encoding

            return enc

    return def_encoding


class Monitor:

    def __init__(self):
        self.cpu_count = 0
        self.logger = Logger("monitor")
        pass

    def get_cpus(self):
        """
        获取cpu数量
        :return:
        """
        if self.cpu_count == 0:
            self.cpu_count = psutil.cpu_count()
            # print(self.cpu_count)
        return self.cpu_count

    def monitor(self, proc_conf):
        """
        开始监控
        :param proc_conf: 监控配置
        :return:
        """

        processs = [p for p in psutil.process_iter(attrs=['pid', 'name', 'username'])
                    if p.info['name'] in proc_conf.keys()]
        # print(processs)
        for proc in processs:
            proc_name = proc.name()
            try:
                # print(proc_name, proc_conf.keys(), proc_name in proc_conf.keys())
                if proc_name in proc_conf.keys():
                    percent = int(proc_conf[proc_name]["percent"])
                    execute = proc_conf[proc_name]["execute"]
                    cpu_percent = proc.cpu_percent(interval=2) / self.get_cpus()
                    # print(":::::", cpu_percent, percent, execute)
                    if cpu_percent >= percent:
                        if execute == "":
                            proc.kill()
                        else:
                            if os.path.exists(execute):
                                # print(execute)
                                import subprocess
                                subprocess.call(execute)

                        self.logger.info('Process Name %s, CPU Use Percent %s UserName %s' %
                                     (proc_name, cpu_percent, proc.info["username"]))

                pass
            except psutil.NoSuchProcess:
                pass
        pass

    def get_config(self):
        """
        获取配置信息
        :return:
        """
        try:
            cf = configparser.ConfigParser()
            conf_path = os.path.join(os.getcwd(), 'monitor.ini')
            # print(conf_path)
            if os.path.exists(conf_path):
                encode = get_file_encoding(conf_path)
                cf.read(conf_path, encoding=encode)  # 读取配置文件 encoding用于中文读取
            else:
                with open(conf_path, 'w') as f:
                    f.write("# [config]节点下配置监控时间间隔(秒),interval: 2\n")
                    f.write("# 多节点需添加[process1...]\n# 添加监控进程信息\n#    process: 进程名\n"
                            "#    percent: cpu使用率\n#    execute: cpu问个问题率超过后执行的文件\n\n")
                    cf.add_section("config")
                    cf.set("config", "interval", "2")

                    # 增加section
                    cf.add_section('process1')  # 配合write使用
                    # 修改字段
                    cf.set("process1", "process", "w3wp.exe")
                    cf.set("process1", "percent", "60")
                    cf.set("process1", "execute", "")
                    cf.write(f)

            sections = cf.sections()
            result = dict()
            result["process"] = dict()
            for section in sections:
                if section == "config":
                    result["interval"] = cf.get("config", "interval")
                else:
                    name = cf.get(section, "process").lower()
                    data = {
                        "percent": cf.get(section, "percent"),
                        "execute": cf.get(section, "execute")
                    }
                    result["process"][name] = data
            return result
        except Exception as ex:
            raise ex
            self.logger.error(ex)

    def start(self):
        """
        采用循环的模式间隔5s检测一次
        :return:
        """
        conf = self.get_config()
        # print(conf)
        interval = int(conf.get("interval", 2))

        self.logger.info("Monitor CPU usage Start")

        while True:
            time.sleep(interval)
            self.monitor(conf["process"])
        pass


if __name__ == "__main__":

    Monitor().start()
