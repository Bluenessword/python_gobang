# -*- coding=utf-8 -*-
class GoBang:
    def __init__(self):
        self.map = [[0 for x in range(15)] for y in range(15)]  # 棋盘大小

    def game_result(self):
        """判断获胜条件 0为游戏进行中 1为黑棋获胜 2为白棋获胜 3为和局"""
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
