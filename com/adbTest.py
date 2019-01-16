# -*- coding: utf-8 -*-

import sys

from com.utils.adb import auto_adb


def main():
    print("Python版本为", sys.version_info.major)
    adb = auto_adb()
    adb.test_device()

    # 获取屏幕分辨率
    # density_str = adb.test_density()
    # print(density_str[:-1] + "dp")
    #  1080 2160
    # 坐标原点
    # adb.run(50, 50, 50, 50, 50)
    # 右上角
    # adb.run(1030, 50, 1030, 50, 50)
    # 左下角
    # adb.run(50, 2110, 50, 2110, 50)
    # 右下角
    # adb.run(100, 800, 100, 800, 50)
    #adb.run(950, 1000, 950, 1000, 50)

    # 模拟点击金币
    adb.run(950, 550, 1550, 550, 500)
    adb.run(950, 600, 1550, 600, 500)
    adb.run(950, 650, 1550, 650, 500)


if __name__ == '__main__':
    main()
