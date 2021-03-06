class Tool(object):

    # 使用赋值语句，定义类属性，记录创建工具对象的总数
    count = 0

    def __init__(self, name):
        self.name = name

        # 针对类属性做一个计数 +1
        Tool.count += 1


# 1.创建工具对象 
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("铁锹")

# 2.输出工具对象的总数
tool3.count = 99
print("工具对象总数 %d" % tool1.count)
print("===> %d" % Tool.count)