xiaoming_dict = {"name": "小明",
                 "age": 18}

# 1. 统计键值对数量
print(len(xiaoming_dict))

# 2. 合并字典
temp_dict = {"height": 1.75,
             "age": 20}
# 注意：如果被合并的字典中含有已存在的键值对，合并后会覆盖原有键值对
xiaoming_dict.update(temp_dict)

# 3. 清空字典
xiaoming_dict.clear()

print(xiaoming_dict)