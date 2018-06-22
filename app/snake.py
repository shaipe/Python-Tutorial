# --*-- coding: utf-8 --*--

from tkinter import *
import random

APPLICATION_TITLE = '贪吃蛇游戏'


class Conf:
    """
    贪吃蛇游戏基础配置
    """
    PLACE_WIDTH = 300   # 场地宽度
    PLACE_HEIGHT = 300  # 场地高度
    BLOCK_SIZE = 10     # 食物方块大小
    START_LENGTH = 5    # 初始化时蛇的长度
    DIRECTION = 0       # 移动方向方向0-横向, 1-竖向
    COLOR = 'red'       # 蛇与食物颜色
    MOVE_SPEED = 200    # 移动速度单位毫秒


class Game:
    """
    主窗体
    """

    def __init__(self, root):
        """
        初始化界面
        :param root:
        """
        self.window = root

        # 创建菜单
        self.create_menu()

        # 创建场地
        self.place = Canvas(root,
                   width=Conf.PLACE_WIDTH,
                   height=Conf.PLACE_HEIGHT,
                   bg='#ffffff')
        self.place.pack()

        # 创建蛇
        snake = Snake(self.place)

        # 游戏开始
        snake.start()

        # 食物投递
        Food(self.place).get_food()

        # 绑定游戏
        root.bind('<Key>', self.key_press)

    def create_menu(self):
        """
        创建窗体菜单
        :return:
        """
        menubar = Menu(self.window, bg="red")
        self.window.config(menu=menubar)

        menus = {"游戏": {
                            "开始": self.start_click,
                            "配置": self.conf_click,
                            "关于": self.about_click}
                 }

        for m in menus:
            tool = Menu(menubar, tearoff=1)
            menubar.add_cascade(label=m, menu=tool)
            for sm in menus[m]:
                tool.add_command(label=sm, command=menus[m][sm])

    def start_click(self):
        """
        开始游戏
        :return:
        """
        from tkinter import messagebox
        messagebox.showinfo(title=APPLICATION_TITLE, message="想要联系作者吗？")

    def conf_click(self):
        """
        关于
        :return:
        """
        from tkinter import messagebox
        messagebox.showinfo(title=APPLICATION_TITLE, message="想要联系作者吗？")

    def about_click(self):
        """
        关于
        :return:
        """
        from tkinter import messagebox
        messagebox.showinfo(title=APPLICATION_TITLE, message="一个贪吃蛇游戏,系统当前版本1.0")

    def key_press(self, event):
        print('key:', event.keysym)


class Snake:
    """
    贪吃蛇
    """
    def __init__(self, place):
        """
        初始化贪吃蛇
        :param place: 运动场地
        """
        self.place = place
        if Conf.DIRECTION == 0:
            w = Conf.BLOCK_SIZE * Conf.START_LENGTH
            h = Conf.BLOCK_SIZE
        else:
            w = Conf.BLOCK_SIZE
            h = Conf.BLOCK_SIZE * Conf.START_LENGTH

        self.place.create_rectangle(0, 0, w, h, fill=Conf.COLOR)

    def eat(self):
        pass

    def start(self):
        pass


class Food:
    """
    食物类
    """
    def __init__(self, place):
        """
        初始始化食物类
        :param place: 给定放食物的场地
        """
        self.color = 'red'
        self.place = place
        pass

    def get_food(self):
        """
        获取一个食物得到随机开始位置
        :return:
        """
        x = round(random.random() * (Conf.PLACE_WIDTH / Conf.BLOCK_SIZE))
        y = round(random.random() * (Conf.PLACE_HEIGHT / Conf.BLOCK_SIZE))

        x = x * Conf.BLOCK_SIZE     # 获取方块大小整数倍的随机数
        y = y * Conf.BLOCK_SIZE

        # 判断是否超出场地
        if x >= Conf.PLACE_WIDTH:
            x = x - Conf.BLOCK_SIZE

        if y >= Conf.PLACE_HEIGHT:
            y = y - Conf.BLOCK_SIZE

        print(x, y, x + Conf.BLOCK_SIZE, y + Conf.BLOCK_SIZE)

        # 需要验证排队蛇当前的位置

        self.place.create_rectangle(x, y,
                                    x + Conf.BLOCK_SIZE, y + Conf.BLOCK_SIZE, fill=Conf.COLOR)


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
        pos = str(Conf.PLACE_WIDTH) + 'x' + str(Conf.PLACE_HEIGHT) + '+400+400'
        self.geometry(pos)  # 窗口呈现位置
        # self.wm_attributes('-topmost', 1)  #窗口置顶
        self.protocol('WM_DELETE_WINDOW', self.close_window)  # 重写关闭按钮事件

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

    def set_position_center(self, rt):
        """
        使用窗口居中
        :param rt:
        :return:
        """
        rt.update()
        cur_width = rt.winfo_reqwidth()  # get current width
        cur_height = rt.winfo_height()  # get current height
        scn_width, scn_height = rt.maxsize()  # get screen width and height
        # now generate configuration information
        tmpcnf = '%dx%d+%d+%d' % (cur_width, cur_height, (scn_width - cur_width) / 2, (scn_height - cur_height) / 2)
        rt.geometry(tmpcnf)


# 程序的入口
if __name__ == '__main__':
    Application().mainloop()