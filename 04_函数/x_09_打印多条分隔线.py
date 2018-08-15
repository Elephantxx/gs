# 需求4：定义一个函数，能够打印 5行 分隔线，要求符合需求3
def print_line(char, times):
    """打印单行分隔线

    :param char: 分隔字符
    :param times:重复次数
    """
    print(char * times)


def print_lines(char, times):
    """打印多行分隔线

    :param char:分隔线使用的字符
    :param times:分隔字符重复次数
    """
    row = 0

    while row < 5:

        print_line(char, times)

        row += 1


print_lines("+", 20)
