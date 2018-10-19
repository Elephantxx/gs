class MusicPlayer(object):

    # 记录第一个被创建对象的引用
    isinstance = None

    def __new__(cls, *args, **kwargs):

        # 1.判断类属性是否是空对象
        if cls.isinstance is None:
            # 2.调用父类方法，为第一个对象调用空间
            cls.isinstance = super().__new__(cls)

        # 3.返回类属性保存的对象引用
        return cls.isinstance

# 创建多个对象
player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)
