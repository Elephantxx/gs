def sum_2_num(num1,num2):
    """对两个数字的求和"""

    result = num1 + num2

    # 可以使用返回值，告诉调用函数一方计算的结果
    return result
    # return 表示返回，下方的代码将不会被执行


# 使用变量 接受函数执行的返回结果
sum_result = sum_2_num(10,20)

print("计算结果：%d" % sum_result)


