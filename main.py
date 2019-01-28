# -*- coding: utf-8 -*-

#  程序主函数
#  有瓷砖
from gameThreadCeramicTile import GameCeramicTile

if __name__ == '__main__':
    print("main start")
    # 输入自己手机的分辨率 1080 2160
    w = 1080
    h = 2160
    if w == 0 or h == 0:
        print("请设置手机的分辨率")
        exit(1)
    print("手机分辨率为:", w, h)

    game = GameCeramicTile("有瓷砖的刷法", w, h)
    game.start()
    print()
    print("main end")
