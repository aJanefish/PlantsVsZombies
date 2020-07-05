# -*- coding: utf-8 -*-

import sys

from uitls.adb import AutoAdb
from uitls.game_utils import KungFuWorldUltimateChallenge
from uitls.plantUtils import PlantPosition


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
    tips = KungFuWorldUltimateChallenge(1080, 2160)
    # tips.using_Enerhy_Bean()
    tips.restart_fighting()


if __name__ == '__main__':
    main()
    # test()
    pass
