# 需求1：定义一个print_line函数，能够打印 * 组成的一条分隔线
def print_line1():
    print("*" * 50)

print_line1()

# 需求2：定义一个函数，能够打印 任意字符 组成的一条分隔线
def print_line2(char):
    print(char * 50)

print_line2("-")

# 需求3：定义一个函数，能够打印 任意重复次数 的一条分隔线
def print_line3(char, times):
    print(char * times)

print_line3("+", 30)

# 需求4：定义一个函数，能够打印 5行 分隔线，要求符合需求3

