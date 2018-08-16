name_list = ["zhangsan", "lisi", "wangwu"]

# 1. 取值和取索引
# list index out of range - 列表索引超出范围
print(name_list[2])

# 已知数据内容，查找该数据在列表中的位置
print(name_list.index("lisi"))

# 2. 修改
name_list[1] = "李四"
# list assignment index out of range - 列表指定的索引超出范围
# name_list[3] = "小明"

# 3. 增加
# append 方法可以向列表末尾追加数据
name_list.append("小强")
# insert 方法可以在列表的指定索引位置增加数据
name_list.insert(1,"小红")
# extend 方法可以把其他列表中完整的内容 追加到当前列表的末尾
temp_list = ["孙悟空", "猪二哥", "沙师弟"]
name_list.extend(temp_list)

# 4. 删除
# remove 方法可以从列表中删除指定数据
name_list.remove("小强")
# pop 方法默认情况下可以删除当前列表中最后一个数据
name_list.pop()
# pop 方法可以删除指定索引位置的数据
name_list.pop(1)
# clear 方法可以清空列表
name_list.clear()

print(name_list)
