# 导入随机工具包
import random

# 从控制台输入要出的拳 —— 石头(1) / 剪刀(2) / 布(3)

def game(player):
    if (player != 1 and player != 2 and player != 3):
        print("您输入的数字不正确，请输入1-3 的数字")
        return

    # 电脑 随机 出拳 —— 先假定电脑只会出石头，完成整体代码
    computer = random.randint(1, 3)
    print("玩家出拳是 %d - 电脑出拳是 %d" % (player, computer))

    # 比较胜负：1.石头 胜 剪刀 / 2.剪刀 胜 布 / 3.布 胜 石头
    if ((player == 1 and computer == 2)
            or (player == 2 and computer == 3)
            or (player == 3 and computer == 1)):

        print("恭喜玩家胜利！")
    # 平局
    elif player == computer:
        print("真实心有灵犀啊，再来一局！")
    # 其他情况电脑获胜
    else:
        print("电脑获胜！")


inputStr=input("请输入您要出的拳 石头(1) / 剪刀(2) / 布(3):")

try:
    player=int(inputStr)
    game(player)
except ValueError as e:
    print(e)
    print("请输入正确的数字1-3")

