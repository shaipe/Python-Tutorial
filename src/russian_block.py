# --*-- coding: utf-8 --*--

from tkinter import *
import random

APPLICATION_TITLE = '俄罗斯方块'


class Conf:
    """
    基础配置
    """
    PLACE_WIDTH = 400   # 场地宽度
    PLACE_HEIGHT = 600  # 场地高度
    BLOCK_SIZE = 10     # 食物方块大小
    SNAKE_LENGTH = 5    # 初始化时蛇的长度
    DIRECTION = 4       # 移动方向方向1-上, 2-下, 3-左, 4-右
    COLOR = 'red'       # 蛇与食物颜色
    MOVE_SPEED = 200    # 移动速度单位毫秒

    SNAKE_POS = []
    SNAKE_POINT = []


class Game:

    def __init__(self, root):
        self.window = root
        pass


class Application(Tk):
    """
    主应用管理
    """
    def __init__(self):
        """
        主应用初始化
        """
        Tk.__init__(self)
        self.title(APPLICATION_TITLE)
        # 给定窗口的起始位置
        # pos = str(Conf.PLACE_WIDTH) + 'x' + str(Conf.PLACE_HEIGHT) + '+500+200'
        pos = self.get_center_pos(Conf.PLACE_WIDTH, Conf.PLACE_HEIGHT)
        self.geometry(pos)  # 窗口呈现位置
        # self.wm_attributes('-topmost', 1)  #窗口置顶
        self.protocol('WM_DELETE_WINDOW', self.close_window)  # 重写关闭按钮事件
        self['background'] = 'black'
        # 创建游戏
        g = Game(self)

    def close_window(self):
        """
        关闭窗口
        :return:
        """
        from tkinter.messagebox import askyesno
        ans = askyesno(title="warning", message="close the window?")
        if ans:
            self.destroy()
        else:
            return

    def get_center_pos(self, cur_width, cur_height):
        """
        获取窗口居中的位置
        :param cur_width: 窗口的宽度
        :param cur_height: 窗口的高度
        :return:
        """
        # rt.update()
        # cur_width = rt.winfo_reqwidth()  # get current width
        # cur_height = rt.winfo_height()  # get current height
        scn_width, scn_height = self.maxsize()  # get screen width and height
        print(scn_height, scn_width)
        # now generate configuration information
        return '%dx%d+%d+%d' % (cur_width, cur_height, (scn_width - cur_width) / 2, (scn_height - cur_height) / 2)


# 程序的入口
if __name__ == '__main__':
    Application().mainloop()
