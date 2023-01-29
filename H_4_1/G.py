def can_eat(knight_pos, figure_pos):
    x1, y1 = knight_pos
    x2, y2 = figure_pos

    return abs(x1 - x2) == 2 and abs(y1 - y2) == 1 or abs(x1 - x2) == 1 and abs(y1 - y2) == 2
