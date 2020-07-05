# -*- coding: utf-8 -*-
import threading
import time

from uitls.game_utils import KungFuWorldUltimateChallenge


# 功夫世界BOSS关卡-带有瓷砖刷金币
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

    # 真正刷金币开始的方法
    def game(self):
        # step4-1:重新挑战(图片1)
        self.tips.restart_fighting()
        # step4-2:等待重新挑战动画播放完成,暂停10s(这是时间不是很准，长一点总是好的)
        time.sleep(10)
        # step4-3:点击开始战斗(图片2)
        self.tips.start_fighting_one()
        # step4-4:等待开始战斗动画完成,暂停8s(这是时间不是很准，长一点总是好的)
        time.sleep(8)
        # step4-5:放置0号位置的植物到[1,2][2,2][3,2]][4,2]的位置上去
        self.tips.planting(0, 1, 2)
        self.tips.planting(0, 2, 2)
        self.tips.planting(0, 3, 2)
        self.tips.planting(0, 4, 2)
        # step4-6:放置1号位置的植物到[1,2][2,2][3,2]][4,2]的位置上去
        self.tips.planting(1, 1, 2)
        self.tips.planting(1, 2, 2)
        self.tips.planting(1, 3, 2)
        self.tips.planting(1, 4, 2)

        # step4-7:开始战斗
        self.tips.start_fighting_two()
        # step4-8:等待开始战斗动画完成
        time.sleep(3)
        #  收集能量豆(不需要了,有瓷砖一把最多10个大金币，已经超出了)
        # self.tips.collect_energy_beans()

        # step4-9:使用能量豆(使用能量豆是点击后,滑动到固定点的植物,在滑动过程中会收集金币)
        self.tips.using_Energy_Bean(4, 2)
        time.sleep(1)
        self.tips.using_Energy_Bean(4, 2)
        # step4-10:使用能量豆(使用能量豆是点击后,滑动到固定点的植物,在滑动过程中会收集金币)
        time.sleep(1)
        self.tips.using_Energy_Bean(4, 2)
        # step4-11:使用能量豆(使用能量豆是点击后,滑动到固定点的植物,在滑动过程中会收集金币)
        time.sleep(1)
        # self.tips.using_Energy_Bean(4, 2)
        # time.sleep(1.5)
        # 收集金币
        # step4-12:兜底操作,再收集一遍金币,放置遗落
        self.tips.click_on_gold_coins()
        # time.sleep(1)

    def start_game(self):
        for x in range(100000):
            flag = self.tips.check_devices()
            print("check_devices", flag)
            # step1:每一次循环之前，检测adb设备是否正常连接，如果没有正常连接，则一直检测，知道adb设备连接
            while not flag:
                self.tips.start_device()
                flag = self.tips.test_deivce()
                if flag:
                    time.sleep(5)

            # step2: 记录每次的开始时间
            start = time.time()
            # step3: 开始刷金币
            self.game()
            # step4: 记录每次的结束时间
            end = time.time()
            # step5: 打印本次所花费的时间总和
            print("total :", x, (end - start))
