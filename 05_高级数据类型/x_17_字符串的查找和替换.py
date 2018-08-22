hello_str = "hello world"

# 1. 判断是否以指定字符串开始
print(hello_str.startswith("hello"))

# 2. 判断是否以指定字符串结束
print(hello_str.endswith("world"))

# 3. 查找指定字符串
# index同样可以查找指定字符串在大字符串中的位置
print(hello_str.find("llo"))
# index方法 如果指定字符串不存在，程序会报错
# find 方法 如果指定字符串不存在，程序会返回 -1
print(hello_str.find("abc"))

# 4. 替换字符串
# replace方法执行完成后，会返回一个新的字符串
# 不会修改原有字符串的内容
print(hello_str.replace("world", "python"))

print(hello_str)