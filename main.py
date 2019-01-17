# -*- coding: utf-8 -*-

#  程序主函数
from gameThread import Game

if __name__ == '__main__':
    print("main start")
    game = Game("zhangyu")
    game.start()
    print()
    print("main end")

