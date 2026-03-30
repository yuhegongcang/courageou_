# 计算机我需要有哪几个阶段
# 1.选择计算器分支。（以后整合）
# 计算器应有功能：加减乘除，开根，平方
# 加减乘除
def add(a, b):
    print("加法结果:", a + b)


def substract(a, b):
    print("减法结果:", a - b)


def multiply(a, b):
    print("乘法结果:", a * b)


def divde(a, b):
    if b == 0:
        print("除数不能为0!")
    else:
        print("除法结果:", a / b)


if __name__ == '__main__':
    