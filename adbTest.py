# -*- coding: utf-8 -*-

import sys

from uitls.adb import AutoAdb
from uitls.game_utils import KongFuWorldUltimateChallenge
from uitls.plantUtils import PZPoint


def main():
    print("Python版本为", sys.version_info.major)
    adb = AutoAdb()
    flag = adb.test_device()
    print("flag", flag)
    while not flag:
        adb.start_device()
        flag = adb.test_device()
        print("flag", flag)
    print("连接成功")

    # Battlefield space
    # 850 150
    # 2120 950
    # adb.run(2120, 950, 2120, 950, 5)
    # plantposition = PlantPosition(1080, 2160)
    # for x in range(9):
    #     for y in range(5):
    #        point = plantposition.get_battlefield_space(x, y)
    #        adb.run(point.x, point.y, point.x, point.y, 500)


def test():
    tips = KongFuWorldUltimateChallenge(1080, 2160)
    tips.restart_fighting()


def test_click():
    adb = AutoAdb()
    point = PZPoint(1780, 160, 1, 1)
    adb.run(point.x, point.y, point.x, point.y, 500)
    # 新版本弹窗广告删除按钮坐标
    point1 = PZPoint(1680, 160, 1, 1)
    adb.run(point1.x, point1.y, point1.x, point1.y, 500)
    pass


if __name__ == '__main__':
    # main()
    # test()
    test_click()
    pass
