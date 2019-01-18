# -*- coding: utf-8 -*-

#  程序主函数
from gameThread import Game

if __name__ == '__main__':
    print("main start")
    # 输入自己收的分辨率 1080 2160
    game = Game("zhangyu", 1080, 2160)
    game.start()
    print()
    print("main end")
