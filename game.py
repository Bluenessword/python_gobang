# -*- coding=utf-8 -*-
class GoBang:
    def __init__(self):
        self.map = [[0 for x in range(15)] for y in range(15)]  # 棋盘大小
        self.step = 0  # 落子数

    def player_move(self):
        while 1:
            try:
                x = int(input("x:"))
                y = int(input("y:"))
                if 0 <= x <= 14 and 0 <= y <= 14:  # 判断是否能落子
                    if self.map[x][y] == 0:  # 判断是否有位置
                        self.map[x][y] = 1
                        self.step += 1
                        return
            except ValueError:  # 输入x，y时非数字
                continue

    def ai_move(self):
        for x in range(15):
            for y in range(15):
                if self.map[x][y] == 0:
                    self.map[x][y] = 2
                    self.step += 1
                    return

    def game_result(self):
        """判断获胜条件 0为游戏进行中 1为玩家获胜 2为ai获胜 3为和局"""
        # 1.横向五子
        for x in range(11):
            for y in range(15):
                if self.map[x + 4][y] == 1 and self.map[x + 3][y] == 1 \
                        and self.map[x + 2][y] == 1 and self.map[x + 1][y] == 1 \
                        and self.map[x][y] == 1:
                    return 1
                if self.map[x + 4][y] == 2 and self.map[x + 3][y] == 2 \
                        and self.map[x + 2][y] == 2 and self.map[x + 1][y] == 2 \
                        and self.map[x][y] == 2:
                    return 2

        # 2.纵向五子
        for x in range(15):
            for y in range(11):
                if self.map[x][y] == 1 and self.map[x][y + 1] == 1 \
                        and self.map[x][y + 2] == 1 and self.map[x][y + 3] == 1 \
                        and self.map[x][y + 4] == 1:
                    return 1
                if self.map[x][y] == 2 and self.map[x][y + 1] == 2 \
                        and self.map[x][y + 2] == 2 and self.map[x][y + 3] == 2 \
                        and self.map[x][y + 4] == 2:
                    return 2

        # 3.左上右下的五子
        for x in range(11):
            for y in range(11):
                if self.map[x + 4][y + 4] == 1 and self.map[x + 3][y + 3] == 1 \
                        and self.map[x + 2][y + 2] == 1 and self.map[x + 1][y + 1] == 1 \
                        and self.map[x][y] == 1:
                    return 1
                if self.map[x + 4][y + 4] == 2 and self.map[x + 3][y + 3] == 2 \
                        and self.map[x + 2][y + 2] == 2 and self.map[x + 1][y + 1] == 2 \
                        and self.map[x][y] == 2:
                    return 2

        # 4.右上左下的五子
        for x in range(11):
            for y in range(11):
                if self.map[x + 4][y] == 1 and self.map[x + 3][y + 1] == 1 \
                        and self.map[x + 2][y + 2] == 1 and self.map[x + 1][y + 3] == 1 \
                        and self.map[x][y + 4] == 1:
                    return 1
                if self.map[x + 4][y] == 2 and self.map[x + 3][y + 1] == 2 \
                        and self.map[x + 2][y + 2] == 2 and self.map[x + 1][y + 3] == 2 \
                        and self.map[x][y + 4] == 2:
                    return 2

        # 5.判断是否和局
        for x in range(15):
            for y in range(15):
                if self.map[x][y] == 0:
                    return 0
        return 3

    def show(self, res):  # 显示游戏内容
        for x in range(15):
            for y in range(15):
                if self.map[x][y] == 0:
                    print('  ', end='')
                elif self.map[x][y] == 1:
                    print('〇', end='')
                elif self.map[x][y] == 2:
                    print('×', end='')

                if x != 14:
                    print('-', end='')
            print('\n', end='')
            for z in range(15):
                print('|  ', end='')
            print('\n', end='')

        if res == 1:
            print('玩家获胜!')
        elif res == 2:
            print('电脑获胜!')
        elif res == 3:
            print('平局!')

    def play(self):
        while 1:
            self.player_move()
            res = self.game_result()
            if res != 0:
                self.show(res)
                return
            self.ai_move()
            res = self.game_result()
            if res != 0:
                self.show(res)
                return
            self.show(0)


if __name__ == '__main__':
    a = GoBang()
    a.play()
