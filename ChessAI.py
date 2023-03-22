import copy


# 找到棋子周围所有空位
def get_charge_pos(board):
    # 八邻域
    direction = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    moves = []
    for x in range(15):
        for y in range(15):
            # 当前位置不为空
            if board[x][y] != 0:
                # 搜索八邻域
                for d in direction:
                    position = (x + d[0], y + d[1])
                    # 该位置出界
                    if position[0] not in range(15) or position[1] not in range(15):
                        continue
                    # 该位置为空且未记录
                    if (board[position[0]][position[1]] == 0) and (position not in moves):
                        moves.append(position)

    return moves


# 根据棋型统计得分
def get_line_score(line):
    # 连五 ： 100000   活四 ：5000   双冲四，冲四活三 ： 10000, 双活三 ： 10000, 活三眠三 ： 1000
    # 活三 ： 200, 双活二 ： 100, 眠三 ： 50, 活二眠二 ： 10, 活二 ： 5
    # 眠二 ：3, 死四 ： -5, 死三 ： -5, 死二 ： -5
    # find函数未找到返回-1
    score = 0

    # 连五
    for i in line:
        if i.find('22222') != -1:
            score += 100000
            break

    # 活四
    for i in line:
        if i.find('022220') != -1:
            score += 50000
            break

    # 双冲四
    count = 0
    for i in line:
        for mold in ['022221', '122220', '20222', '22202', '22022']:
            if i.find(mold) != -1:
                count += 1
                break

        if count == 2:
            score += 10000
            break

    # 冲四活三
    CFOUR_THREE = [0, 0]
    for i in line:
        if not CFOUR_THREE[0]:
            for mold in ['022221', '122220', '20222', '22202', '22022']:
                if i.find(mold) != -1:
                    CFOUR_THREE[0] = 1
                    break

        if not CFOUR_THREE[1]:
            for mold in ['02220', '2022', '2202']:
                if i.find(mold) != -1:
                    CFOUR_THREE[1] = 1
                    break

        if CFOUR_THREE[0] and CFOUR_THREE[1]:
            score += 10000
            break

    # 双活三
    count = 0
    for i in line:
        for mold in ['02220', '2022', '2202']:
            if i.find(mold) != -1:
                count += 1
                break

        if count == 2:
            score += 10000
            break

    # 活三眠三
    THREE_STHREE = [0, 0]
    for i in line:
        if not THREE_STHREE[0]:
            for mold in ['02220', '2022', '2202']:
                if i.find(mold) != -1:
                    THREE_STHREE[0] = 1
                    break

        if not THREE_STHREE[1]:
            for mold in ['002221', '122200', '020221', '122020', '022021', '120220', '20022', '22002', '20202',
                         '1022201']:
                if i.find(mold) != -1:
                    THREE_STHREE[1] = 1
                break

        if THREE_STHREE[0] and THREE_STHREE[1]:
            score += 1000
            break

    # 活三
    count = 0
    for i in line:
        for mold in ['02220', '2022', '2202']:
            if i.find(mold) != -1:
                count += 1
                break
    score += count * 200

    # 双活二
    count = 0
    for i in line:
        for mold in ['002200', '02020', '2002']:
            if i.find(mold) != -1:
                count += 1
                break
        if count == 2:
            score += 100
            break

    # 眠三
    count = 0
    for i in line:
        for mold in ['002221', '122200', '020221', '122020', '022021', '120220', '20022', '22002', '20202',
                     '1022201']:
            if i.find(mold) != -1:
                count += 1
                break
    score += count * 50

    # 活二眠二
    TWO_STWO = [0, 0]
    for i in line:
        if not TWO_STWO[0]:
            for mold in ['002200', '02020', '2002']:
                if i.find(mold) != -1:
                    TWO_STWO[0] = 1
                    break

        if not TWO_STWO[1]:
            for mold in ['000221', '122000', '002021', '120200', '020021', '120020', '20002']:
                if i.find(mold) != -1:
                    TWO_STWO[1] = 1
                    break

        if TWO_STWO[0] and TWO_STWO[1]:
            score += 10
            break

    # 活二
    count = 0
    for i in line:
        for mold in ['002200', '02020', '2002']:
            if i.find(mold) != -1:
                count += 1
                break
    score += count * 5

    # 眠二
    count = 0
    for i in line:
        for mold in ['000221', '122000', '002021', '120200', '020021', '120020', '20002']:
            if i.find(mold) != -1:
                count += 1
                break
    score += count * 3

    # 死四，死三，死二
    count = 0
    for i in line:
        if i.find('122221') != -1:
            count += 1
        if i.find('12221') != -1:
            count += 1
        if i.find('1221') != -1:
            count += 1
    score += count * -5

    return score


# 落子后获取四个方向上的棋型字符串
def get_score(position, board):
    # 获取棋盘副本，在当前位置落子
    new = copy.deepcopy(board)
    x, y = position[0], position[1]
    new[x][y] = 2

    # 横，竖
    h = str(new[x])[1:-1].replace(',', '').replace(' ', '')
    s = str([new[i][y] for i in range(15)])[1:-1].replace(',', '').replace(' ', '')

    # 左斜
    lx = str(
        [new[i][i - x + y] for i in range(15) if (i - x + y) in range(15)])[1:-1].replace(',', '').replace(' ', '')

    # 右斜
    rx = str(
        [new[i][x + y - i] for i in range(15) if (x + y - i) in range(15)])[1:-1].replace(',', '').replace(' ', '')

    return get_line_score([h, s, lx, rx])


# 反转棋盘  由于棋线上对于棋型是单向查找的，所以对于不对称的棋型要反转棋型再次查找
def opp_board(board):
    o_board = [[0] * 15 for i in range(15)]

    for i in range(15):
        for j in range(15):
            if board[i][j] != 0:
                o_board[i][j] = 1 if board[i][j] == 2 else 2

    return o_board


# 求得在所有空位置落子后的最大分数   对每个可下位置进行两次评分得到最终分数后，返回分数最高的位置
def get_pos(board):
    moves = get_charge_pos(board)

    best_move = (-1, -1)
    max_score = -float("inf")

    for position in moves:
        o_board = opp_board(board)
        score = get_score(position, board) + get_score(position, o_board)
        if score > max_score:
            best_move = position
            max_score = score

    return best_move[0], best_move[1]
