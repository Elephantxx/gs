# 需求
#
# 在控制台连续输出 5 行 * ，每行 * 的个数依次递增
#
# 开发步骤
# 1> 完成 5 行内容的简单输出
# 2> 分析每行内部的 * 应如何处理
row = 1
while row <= 5:

    # 每行打印 * 的数量 与当前行数一致
    # 增加一个小循环，专门负责当前行中每列星星的显示
    # 1. 定义一个列计数器
    col = 1
    # 2.开始循环
    while col <= row:
        # print("%d" % col)
        print("*", end="")
        col += 1
    # print("第 %d 行" % row)
    print("")

    row += 1
