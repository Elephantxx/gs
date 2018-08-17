
# 格式化字符串后面的 '()' 本质上就是元组
print("%s 的年龄是 %d 岁，身高是 %.2f 米" % ("zhangsan", 18, 1.75))

info_tuple = ("zhangsan", 18, 1.75)
print("%s 的年龄是 %d 岁，身高是 %.2f 米" % info_tuple)

info_str = "%s 的年龄是 %d 岁，身高是 %.2f 米" % info_tuple
print(info_str)
