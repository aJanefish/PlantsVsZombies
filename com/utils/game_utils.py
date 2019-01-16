# -*- coding: utf-8 -*-

#  植物大战僵尸 辅助函数
#  功夫世界 终极挑战  刷金币
from com.utils.adb import auto_adb
import time


class KungFuWorldUltimateChallenge:
    def __init__(self):
            self.adb = auto_adb()
            self.adb.test_device()

    # 开始战斗 点击一下
    def start_fighting_one(self):
        self.adb.run(2100, 1000, 2100, 1000, 50)

        # 开始战斗 点击一下
    def start_fighting_two(self):
        self.adb.run(1800, 200, 1800, 200, 50)

    # 重新开始 点击两下
    def restart_fighting(self):
        self.adb.run(2100, 50, 2100, 50, 50)
        self.adb.run(1000, 800, 1000, 800, 50)

    # 种植豌豆到八卦 点击两下
    def planting_peas(self):
        self.adb.run(100, 900, 100, 900, 50)
        self.adb.run(1000, 600, 1000, 600, 50)

    #  种植太阳花1   到1
    def planting_sunflowers_one(self):
        self.adb.run(100, 800, 100, 800, 50)
        self.adb.run(1100, 600, 1100, 600, 50)

    #  种植太阳花2   到2
    def planting_sunflowers_two(self):
        self.adb.run(100, 800, 100, 800, 50)
        self.adb.run(1200, 600, 1200, 600, 50)

    #  种植太阳花3   到3
    def planting_sunflowers_three(self):
        self.adb.run(100, 800, 100, 800, 50)
        self.adb.run(1350, 600, 1350, 600, 50)

        #  种植太阳花3   到4
    def planting_sunflowers_four(self):
        self.adb.run(100, 800, 100, 800, 50)
        self.adb.run(1500, 600, 1500, 600, 50)

    # 使用豌豆 到太阳花1  点击两次
    def using_peas_one(self):
        self.adb.run(950, 1000, 950, 1000, 50)
        self.adb.run(1100, 600, 1100, 600, 50)

    # 使用豌豆 到太阳花2
    def using_peas_two(self):
        self.adb.run(950, 1000, 950, 1000, 50)
        self.adb.run(1200, 600, 1200, 600, 50)

    # 使用豌豆 到太阳花3
    def using_peas_three(self):
        self.adb.run(950, 1000, 950, 1000, 50)
        self.adb.run(1350, 600, 1350, 600, 50)

        # 使用豌豆 到太阳花4
    def using_peas_four(self):
        self.adb.run(950, 1000, 950, 1000, 50)
        self.adb.run(1500, 600, 1500, 600, 50)

    # 模拟点击金币 否则会影响到使用能量豆
    def click_on_gold_coins(self):
        self.adb.run(850, 650, 1550, 650, 200)
        self.adb.run(950, 600, 1550, 600, 200)
        self.adb.run(950, 550, 1550, 550, 200)

