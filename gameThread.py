# -*- coding: utf-8 -*-
import threading
import time

from uitls.game_utils import KungFuWorldUltimateChallenge


class Game(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.tips = KungFuWorldUltimateChallenge()

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
        self.tips.planting_peas()
        # tips.planting_sunflowers_one()
        self.tips.planting_sunflowers_two()
        # tips.planting_sunflowers_three()
        # tips.planting_sunflowers_four()

        # 开始战斗
        self.tips.start_fighting_two()
        # 等待动画完成
        time.sleep(3)
        #  收集能量豆
        self.tips.click_on_gold_coins()

        # 使用能量豆
        self.tips.using_peas_two()
        self.tips.using_peas_two()
        self.tips.using_peas_two()
        self.tips.using_peas_two()
        # tips.using_peas_four()
        # tips.using_peas_two()
        # tips.using_peas_three()

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
