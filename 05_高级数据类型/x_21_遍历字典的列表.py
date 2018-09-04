students = [
    {"name": "阿土"},
    {"name": "小美"}
]

# 在学员列表中搜索指定的姓名
find_name = "张三"

for stu_dict in students:

    print(stu_dict)

    if stu_dict["name"] == find_name:

        print("找到了 %s" % find_name)

        # 如果找到，应该退出循环，不再继续遍历后续元素
        break
# 如果没有找到目标元素，输出未找到的提示
else:
    print("抱歉 没有找到 %s" % find_name)

print("循环结束")