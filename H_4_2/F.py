menu = {
    "Эспрессо": {"coffee": 1},
    "Капучино": {"coffee": 1, "milk": 3},
    "Макиато": {"coffee": 2, "milk": 1},
    "Кофе по-венски": {"coffee": 1, "cream": 2},
    "Латте Макиато": {"coffee": 1, "milk": 2, "cream": 1},
    "Кон Панна": {"coffee": 1, "cream": 1}
}
in_stock = {}


def order(*args):
    def check(rec: dict):
        flag = True
        for k in rec.keys():
            if in_stock[k] - rec[k] < 0:
                flag = False
        return flag

    for i in args:
        if check(menu[i]):
            for k in menu[i].keys():
                in_stock[k] -= menu[i][k]
            return i
    return 'К сожалению, не можем предложить Вам напиток'



