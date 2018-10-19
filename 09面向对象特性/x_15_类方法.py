class Tool(object):

    # 使用赋值语句，定义类属性，记录创建工具对象的总数
    count = 0

    @classmethod
    def show_tool_count(cls):

        print("工具对象的数量 %d" % cls.count)

    def __init__(self, name):
        self.name = name

        # 针对类属性做一个计数 +1
        Tool.count += 1


# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")

# 调用类方法
Tool.show_tool_count()