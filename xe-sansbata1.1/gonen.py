

def helph():
    print('''帮助:
    calc    计算器
    log     启动日志监测
    quit    退出''')

def help():
    print('''帮助:
    calc    计算器
    log     启动日志监测
    us      降权
    quit    退出''')


# 你要的函数：calac(a, b, c)
def calac(a, b, c):
    # a = 第一个数字
    # b = 第二个数字
    # c = 运算符（+ - * /）

    if c == "+":
        return a + b
    elif c == "-":
        return a - b
    elif c == "*":
        return a * b
    elif c == "/":
        if b == 0:
            return "不能除以0"
        return a / b
    else:
        return "错误符号"
