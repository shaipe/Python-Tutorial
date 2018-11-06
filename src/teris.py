from tkinter import *
from time import sleep
from random import *
from tkinter import messagebox


class Teris:
    """
    俄罗斯方块
    """
    def __init__(self):
        """

        """
        # 方块颜色列表
        self.color = ['red', 'orange', 'yellow', 'purple', 'blue', 'green', 'pink']
        # Set a core squre and any shape can be drawn by the relative location.
        # 字典 存储形状对应7种形状 元组存储坐标
        self.shapeDict = {1: [(0, 0), (0, -1), (0, -2), (0, 1)],  # shape I
                          2: [(0, 0), (0, -1), (1, -1), (1, 0)],  # shape O
                          3: [(0, 0), (-1, 0), (0, -1), (1, 0)],  # shape T T型
                          4: [(0, 0), (0, -1), (1, 0), (2, 0)],  # shape J 右长倒L盖子
                          5: [(0, 0), (0, -1), (-1, 0), (-2, 0)],  # shape L
                          6: [(0, 0), (0, -1), (-1, -1), (1, 0)],  # shape Z
                          7: [(0, 0), (-1, 0), (0, -1), (1, -1)]}  # shape S
        # 旋转坐标控制
        self.rotateDict = {(0, 0): (0, 0), (0, 1): (-1, 0), (0, 2): (-2, 0), (0, -1): (1, 0),
                           (0, -2): (2, 0), (1, 0): (0, 1), (2, 0): (0, 2), (-1, 0): (0, -1),
                           (-2, 0): (0, -2), (1, 1): (-1, 1), (-1, 1): (-1, -1),
                           (-1, -1): (1, -1), (1, -1): (1, 1)}

        # 初始高度，宽度 核心块位置
        self.coreLocation = [4, -2]
        self.height, self.width = 20, 10
        self.size = 32
        # Map can record the location of every square.i宽  j高
        self.map = {}
        # 全部置0
        for i in range(self.width):
            for j in range(-4, self.height):
                self.map[(i, j)] = 0
        # 添加边界
        for i in range(-4, self.width + 4):
            self.map[(i, self.height)] = 1
        for j in range(-4, self.height + 4):
            for i in range(-4, 0):
                self.map[(i, j)] = 1
        for j in range(-4, self.height + 4):
            for i in range(self.width, self.width + 4):
                self.map[(i, j)] = 1

        # 初始化分数0  默认不加快  按下时加快
        self.score = 0
        self.isFaster = False
        # 创建GUI界面
        self.root = Tk()
        self.root.title("Teris")
        self.root.geometry("500x645")
        self.area = Canvas(self.root, width=320, height=640, bg='white')
        self.area.grid(row=2)
        self.pauseBut = Button(self.root, text="Pause", height=2, width=13, font=(18), command=self.isPause)
        self.pauseBut.place(x=340, y=100)
        self.startBut = Button(self.root, text="Start", height=2, width=13, font=(18), command=self.play)
        self.startBut.place(x=340, y=20)
        self.restartBut = Button(self.root, text="Restart", height=2, width=13, font=(18), command=self.isRestart)
        self.restartBut.place(x=340, y=180)
        self.quitBut = Button(self.root, text="Quit", height=2, width=13, font=(18), command=self.isQuit)
        self.quitBut.place(x=340, y=260)
        self.scoreLabel1 = Label(self.root, text="Score:", font=(24))
        self.scoreLabel1.place(x=340, y=600)
        self.scoreLabel2 = Label(self.root, text="0", fg='red', font=(24))
        self.scoreLabel2.place(x=410, y=600)
        # 按键交互
        self.area.bind("<Up>", self.rotate)
        self.area.bind("<Left>", self.moveLeft)
        self.area.bind("<Right>", self.moveRight)
        self.area.bind("<Down>", self.moveFaster)
        self.area.bind("<Key-w>", self.rotate)
        self.area.bind("<Key-a>", self.moveLeft)
        self.area.bind("<Key-d>", self.moveRight)
        self.area.bind("<Key-s>", self.moveFaster)
        self.area.focus_set()

        # 菜单
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)
        self.startMenu = Menu(self.menu)
        self.menu.add_cascade(label='Start', menu=self.startMenu)
        self.startMenu.add_command(label='New Game', command=self.isRestart)
        self.startMenu.add_separator()
        self.startMenu.add_command(label='Continue', command=self.play)
        self.exitMenu = Menu(self.menu)
        self.menu.add_cascade(label='Exit', command=self.isQuit)
        self.helpMenu = Menu(self.root)
        self.menu.add_cascade(label='Help', menu=self.helpMenu)
        self.helpMenu.add_command(label='How to play', command=self.rule)
        self.helpMenu.add_separator()
        self.helpMenu.add_command(label='About...', command=self.about)

    def getLocation(self):
        """
        先将核心块的所在位置在map中的元素设为1，通过self.shapeDict获取其余方块位置，将map中对应元素设为1。
        :return:
        """
        map[(core[0], core[1])] = 1
        for i in range(4):
            map[((core[0] + getNew[i][0]),
                 (core[1] + getNew[i][1]))] = 1

    def canMove(self):
        """
        判断方块下移一格后对应位置map中的元素是否为一，是，则不可移动，返回False；否，可以移动，返回True。
        :return:
        """
        for i in range(4):
            if map[(core[0] + getNew[i][0]), (core[1] + 1 + getNew[i][1])] == 1:
                return False
        return True

    def drawNew(self):
        """
        # 先用randRange获取1～7中的随机整数，随机到某一整数，那么访问self.shapeDict,获取这种形状方块的核心块及其他方块的相对位置。
        # 访问颜色字典，获取此方块的颜色。建立循环，当方块可移动时(while self. canMove():)，且暂停键未被摁下（if isPause:)，
        # 核心块纵坐标加一，根据核心块及其他方块对于核心块的相对位置，画出四个方块。用self.getLocation()函数获取方块的位置。
        :return:
        """
        global next
        global getNew
        global core
        next = randrange(1, 8)
        # 形状
        self.getNew = self.shapeDict[next]
        getNew = self.getNew
        core = [4, -2]
        time = 0.2
        while self.canMove():
            if isPause:
                core[1] += 1
                self.drawSquare()
                if self.isFaster:
                    sleep(time - 0.15)
                else:
                    sleep(time + 0.22)
                self.isFaster = False
            else:
                self.drawSquare()
                sleep(time)
        self.getLocation()

    def drawSquare(self):
        """
        绘制当前方块
        :return:
        """
        self.area.delete("new")
        for i in range(4):
            self.area.create_rectangle((core[0] + self.getNew[i][0]) * self.size,
                                       (core[1] + self.getNew[i][1]) * self.size,
                                       (core[0] + self.getNew[i][0] + 1) * self.size,
                                       (core[1] + self.getNew[i][1] + 1) * self.size,
                                       fill=self.color[next - 1], tags="new")
        self.area.update()

    def drawBottom(self):
        """
        # 给底部每行中方块都加上标签：bottom + str(j), j代表该块所在行数，每次遍历map，建立对于range（self. height）的for循环，删去每一行，
        # 若map什么地方的元素为1，画出这一位置的方块，不断更新。这样可以画出底部方块。
        :return:
        """
        for j in range(self.height):
            self.area.delete('bottom' + str(j))
            for i in range(self.width):
                if map[(i, j)] == 1:
                    self.area.create_rectangle(self.size * i, self.size * j, self.size * (i + 1),
                                               self.size * (j + 1), fill='grey', tags='bottom' + str(j))
            self.area.update()

    def isFill(self):
        """
        # 判断填满遍历map每一行的各个元素，若所有元素为1，则标签中score值+10，将
        # 此行所有元素改为0，行数map（i,j)=map(i-1,j)（即所有之上的行下移）
        # ，那么后续画底部方块时，可实现消行。
        :return:
        """
        for j in range(self.height):
            t = 0
            for i in range(self.width):
                if map[(i, j)] == 1:
                    t = t + 1
            if t == self.width:
                self.getScore()
                self.deleteLine(j)

    def getScore(self):
        """
        加分
        :return:
        """
        scoreValue = eval(self.scoreLabel2['text'])
        scoreValue += 10
        self.scoreLabel2.config(text=str(scoreValue))

    def deleteLine(self, j):
        """
        消行
        """
        for t in range(j, 2, -1):
            for i in range(self.width):
                map[(i, t)] = map[(i, t - 1)]
        for i in range(self.width):
            map[(i, 0)] = 0
        self.drawBottom()

    def isOver(self):
        """
        # 遍历每一行，若从顶部到底部map每一行都有某一个元素或更多元素为1，
        # 那么说明方块以顶到最上端，游戏结束。此处不可以简单判定最上一行是否有元素为1就判定结束，
        # 若这样会产生顶部有新的方块产生，然后导致顶部有元素为1，误判为游戏结束。
        :return:
        """
        t = 0
        for j in range(self.height):
            for i in range(self.width):
                if self.map[(i, j)] == 1:
                    t += 1
                    break
        if t >= self.height:
            return False
        else:
            return True

    def canRotate(self):
        """
        # 先判断方块是否可以旋转（针对其靠近边界时）。先将其现在所在位置对应map中的元素改为0，判断其旋
        # 转后位置对应map中的元素是否有一，若有，说明其旋转后的位置已经被占，是不能旋转的，返回值为False
        # 。否则为可旋转，返回值True。若已判定可以旋转，那么访问self.rotateDict，得出旋转以后所有小块的位置
        # 变换，将变换以后的位置对应map的元素设为1，旋转便已完成。
        :return:
        """
        for i in range(4):
            map[((core[0] + getNew[i][0]),
                 (core[1] + getNew[i][1]))] = 0
        for i in range(4):
            if map[((core[0] + self.rotateDict[getNew[i]][0]),
                    (core[1] + self.rotateDict[getNew[i]][1]))] == 1:
                return False
        return True

    def rotate(self, event):
        """旋转"""
        if next != 2:
            if self.canRotate():
                for i in range(4):
                    getNew[i] = self.rotateDict[getNew[i]]
                self.drawSquare()
        if not self.canMove():
            for i in range(4):
                map[((core[0] + getNew[i][0]), (core[1] + getNew[i][1]))] = 1

    def canLeft(self):
        """
        # 先判断是否左移/右移，同样，将方块现在所处位置的map中元素设为0，看其移动后的位置上map的元素是否有1，
        # 若有，说明这一位置已被占据或已到边界，不可移动，返回False。若可移动，返回True。按下左键，若可
        # 以移动，核心块的横坐标减1，由于我们只讨论其他小块对于核心块的相对位置，所以其他小块的位置自动随
        # 核心块的位置移动而移动。将移动过后的位置对应map中的元素设为1。
        :return:
        """
        coreNow = core
        for i in range(4):
            map[((coreNow[0] + getNew[i][0]), (coreNow[1] + getNew[i][1]))] = 0
        for i in range(4):
            if map[((coreNow[0] + getNew[i][0] - 1), (coreNow[1] + getNew[i][1]))] == 1:
                return False
        return True

    def moveLeft(self, event):
        """左移"""
        if self.canLeft():
            core[0] -= 1
            self.drawSquare()
            self.drawBottom()
        if not self.canMove():
            for i in range(4):
                map[((core[0] + getNew[i][0]), (core[1] + getNew[i][1]))] = 1

    def canRight(self):
        """判断右移"""
        for i in range(4):
            map[((core[0] + getNew[i][0]), (core[1] + getNew[i][1]))] = 0
        for i in range(4):
            if map[((core[0] + getNew[i][0] + 1), (core[1] + getNew[i][1]))] == 1:
                return False
        return True

    def moveRight(self, event):
        """右移"""
        if self.canRight():
            core[0] += 1
            self.drawSquare()
            self.drawBottom()
        if not self.canMove():
            for i in range(4):
                map[((core[0] + getNew[i][0]), (core[1] + getNew[i][1]))] = 1

    # 初始化中有一self. isFaster 的变量被设为False，当其为False时，
    # 程序中的sleep(time)中time的值为0.35，而按下下键，self. isFaster变为True，
    # time变成0.05，通过调整sleep()中变量的大小可以调节方块运动的速度。
    # 此功能通过if语句实现。
    def moveFaster(self, event):
        self.isFaster = True
        if not self.canMove():
            for i in range(4):
                map[((core[0] + getNew[i][0]), (core[1] + getNew[i][1]))] = 1

    # run the programe
    def run(self):
        self.isFill()
        self.drawNew()
        self.drawBottom()

    # play the game
    def play(self):
        self.startBut.config(state=DISABLED)
        global isPause
        isPause = True
        global map
        map = self.map
        while True:
            if self.isOver():
                self.run()
            else:
                break
        self.over()

    def restart(self):
        """重新开始游戏"""
        self.core = [4, -2]
        self.map = {}
        for i in range(self.width):
            for j in range(-4, self.height):
                self.map[(i, j)] = 0
        for i in range(-1, self.width):
            self.map[(i, self.height)] = 1
        for j in range(-4, self.height + 1):
            self.map[(-1, j)] = 1
            self.map[(self.width, j)] = 1
        self.score = 0
        self.t = 0.07
        for j in range(self.height):
            self.area.delete('bottom' + str(j))
        self.play()

    def over(self):
        """
        结束后告诉用户失败
        :return:
        """
        feedback = messagebox.askquestion("You Lose!", "You Lose!\nDo you want to restart?")
        if feedback == 'yes':
            self.restart()
        else:
            self.root.destroy()

    def isQuit(self):
        """退出"""
        askQuit = messagebox.askquestion("Quit", "Are you sure to quit?")
        if askQuit == 'yes':
            self.root.destroy()
            exit()

    def isRestart(self):
        """
        判断是否按下restart
        :return:
        """
        askRestart = messagebox.askquestion("Restart", "Are you sure to restart?")
        if askRestart == 'yes':
            self.restart()
        else:
            return

    def isPause(self):
        """
        # 每次一按下暂停键，isPause = not isPause,当isPause = True时，由于之前提到过的if isPause:语句，
        # 方块可以移动，游戏运行。当按下暂停键以后，isPause值为False，方块将不可移动。同时，isPause值为False时
        # ，暂停键变为开始键，即标签由Pause 改为 Resume,当isPause值为True时，Resume改为Pause。这一功能由if语句实现。
        :return:
        """
        global isPause
        isPause = not isPause
        if not isPause:
            self.pauseBut["text"] = "Resume"
        else:
            self.pauseBut["text"] = "Pause"

    def rule(self):
        """帮助"""
        ruleTop = Toplevel()
        ruleTop.title('Help')
        ruleTop.geometry('800x400')
        rule = "Start: Press the start button or choose the option 'Continue' to start the game.\n%-s%-s%-s%-s%-s%-s%-s%-s%-s%-s%-s%-s%-s%-s" % (
        "Restart: Press the restart button or choose the option 'New Game' to resatrt the game.\n",
        "Enjoy the Teris game! Have fun!")
        ruleLabel = Label(ruleTop, text=rule, fg='blue', font=(18))
        ruleLabel.place(x=50, y=50)

    def about(self):
        """显示有关信息"""
        aboutTop = Toplevel()
        aboutTop.title('About')
        aboutTop.geometry('300x150')
        about = "Teris.py\n\
By Programmer Lee\n\
All Rights Reserved."
        aboutLabel = Label(aboutTop, font=('Curier', 20), fg='darkblue', text=about)
        aboutLabel.pack()

        # Get into mainloop

    def mainloop(self):
        self.root.mainloop()


def main():
    teris = Teris()
    teris.mainloop()


main()