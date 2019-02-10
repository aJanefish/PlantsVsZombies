# -*- coding: utf-8 -*-
import threading
import time

from uitls.game_utils import KungFuWorldUltimateChallenge


class GameCeramicTile(threading.Thread):
    def __init__(self, name, width, high):
        threading.Thread.__init__(self)
        self.name = name
        self.tips = KungFuWorldUltimateChallenge(width, high)

    def run(self):
        print("开始线程：" + self.name)
        print()
        self.start_game()
        print("退出线程：" + self.name)

    def game(self):
        self.tips.restart_fighting()
        # 等待动画播放完成
        time.sleep(10)
        # 点击开始战斗
        self.tips.start_fighting_one()
        # 等待动画完成
        time.sleep(8)
        # 放置植物
        # self.tips.planting(1, 0, 2)
        #
        self.tips.planting(0, 1, 2)
        self.tips.planting(0, 2, 2)
        self.tips.planting(0, 3, 2)
        self.tips.planting(0, 4, 2)
        # ss
        self.tips.planting(1, 1, 2)
        self.tips.planting(1, 2, 2)
        self.tips.planting(1, 3, 2)
        self.tips.planting(1, 4, 2)

        # 开始战斗
        self.tips.start_fighting_two()
        # 等待动画完成
        time.sleep(3)
        #  收集能量豆
        self.tips.collect_energy_beans()

        # 使用能量豆
        self.tips.using_Energy_Bean(4, 2)
        time.sleep(1.5)
        self.tips.using_Energy_Bean(4, 2)
        time.sleep(1.5)
        self.tips.using_Energy_Bean(4, 2)
        time.sleep(1.5)
        # self.tips.using_Energy_Bean(4, 2)
        # time.sleep(1.5)
        # 收集金币
        self.tips.click_on_gold_coins()
        time.sleep(1)

    def start_game(self):
        for x in range(100000):
            flag = self.tips.check_devices()
            print("check_devices", flag)
            while not flag:
                self.tips.start_device()
                flag = self.tips.test_deivce()
                if flag:
                    time.sleep(5)

            start = time.time()
            self.game()
            end = time.time()
            print("total :", x, (end - start))
