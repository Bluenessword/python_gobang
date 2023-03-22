# -*- coding=utf-8 -*-
import pygame
from 五子棋.checkState import GoBang
import easygui as g
from 五子棋.ChessAI import get_pos

pygame.init()  # 初始化py_game

chess = []
flag = 1  # 1是黑棋 2是白棋
game_state = 0  # 0为游戏正常进行 1为黑棋胜利 2为白棋胜利

space = 60  # 四周留下的边距
cell_size = 40  # 每个格子大小
cell_num = 15
grid_size = cell_size * (cell_num - 1) + space * 2  # 棋盘的大小
title = pygame.display.set_caption('五子棋')
screen = pygame.display.set_mode((grid_size, grid_size))  # 设置窗口长宽

icon = "icon.jpg"
icon = pygame.image.load(icon).convert_alpha()
pygame.display.set_icon(icon)  # 设置显示窗口的图标
a = GoBang()
white_x, white_y = 0, 0

while True:
    for event in pygame.event.get():  # 从队列中获取事件
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # 监听鼠标的位置 落子
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            x = round((x - space) / cell_size)
            y = round((y - space) / cell_size)
            if 0 <= x < cell_num and 0 <= y < cell_num and (x, y, 1) not in chess and (x, y, 2) not in chess:
                chess.append((x, y, flag))
                if flag == 1:
                    flag = 2
                else:
                    flag = 1

        # AI落子
        if flag == 2:
            for x, y, z in chess:
                if z == 1:
                    a.map[x][y] = 1
                else:
                    a.map[x][y] = 2

            x, y = get_pos(a.map)
            white_x, white_y = x, y
            chess.append((x, y, flag))
            flag = 1

    screen.fill((238, 154, 73))  # 设置界面颜色 红 绿 蓝

    # 绘制棋盘
    # 画竖线
    for x in range(0, cell_size * cell_num, cell_size):
        if (x == 0) | (x == cell_size * (cell_num - 1)):
            pygame.draw.line(screen, (0, 0, 0), (x + space, 0 + space),
                             (x + space, cell_size * (cell_num - 1) + space), 3)
            continue
        pygame.draw.line(screen, (0, 0, 0), (x + space, 0 + space),
                         (x + space, cell_size * (cell_num - 1) + space), 1)
    # 画横线
    for y in range(0, cell_size * cell_num, cell_size):
        if (y == 0) | (y == cell_size * (cell_num - 1)):
            pygame.draw.line(screen, (0, 0, 0), (0 + space, y + space),
                             (cell_size * (cell_num - 1) + space, y + space), 3)
            continue
        pygame.draw.line(screen, (0, 0, 0), (0 + space, y + space),
                         (cell_size * (cell_num - 1) + space, y + space), 1)

    # 绘制天元 星
    for x, y in [(7, 7), (3, 11), (11, 3), (3, 3), (11, 11)]:
        pygame.draw.circle(screen, (0, 0, 0), (x * cell_size + space, y * cell_size + space), 6, 0)

    # 绘制落子显示
    x, y = pygame.mouse.get_pos()
    x = round((x - space) / cell_size)
    y = round((y - space) / cell_size)
    if 0 <= x < cell_num and 0 <= y < cell_num:
        pygame.draw.rect(screen, [0, 229, 238], [x * cell_size + space - 22, y * cell_size + space - 22, 44, 44], 1)

    # 绘制AI落子定位
    if white_x:
        pygame.draw.rect(screen, [0, 229, 238],
                         [white_x * cell_size + space - 22, white_y * cell_size + space - 22, 44, 44], 1)

    # 绘制棋子
    for x, y, z in chess:
        if z == 1:
            color = (0, 0, 0)
            a.map[x][y] = 1
        else:
            color = (255, 251, 240)
            a.map[x][y] = 2
        pygame.draw.circle(screen, color, (x * cell_size + space, y * cell_size + space), 16, 0)

    # 判断当前状态
    game_state = a.game_result()
    pygame.display.update()
    # 游戏结束
    game = False
    if game_state != 0:
        if game_state == 1:
            game = g.ccbox('黑棋获胜', '游戏结束', ["新的开局", "退出"])
        elif game_state == 2:
            game = g.ccbox('白棋获胜', '游戏结束', ["新的开局", "退出"])
        elif game_state == 3:
            game = g.ccbox('和棋', '游戏结束', ["新的开局", "退出"])
        if game:
            a = GoBang()
            chess = []
            flag = 1
            white_x, white_y = 0, 0
        else:
            pygame.quit()
            exit()

    pygame.display.update()  # 必须调用update才能看到绘图显示
