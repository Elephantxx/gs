i = 0

while i < 10:

    # continue 当某一条件满足时，不执行后续重复的代码
    # 假定条件 i == 3
    if i == 3:

        # 注意：在循环中，使用 continue 之前，需要确认循环计数器是否修改，否则会进入死循环
        i += 1

        continue

    print(i)

    i += 1
