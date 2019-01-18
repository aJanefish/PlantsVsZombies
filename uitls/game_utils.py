# -*- coding: utf-8 -*-

#  植物大战僵尸 辅助函数
#  功夫世界 终极挑战  刷金币

from uitls.adb import auto_adb
from uitls.plantUtils import PlantPosition


class KungFuWorldUltimateChallenge:
    def __init__(self, width, high):
        self._adb = auto_adb()
        # self.test_deivce()
        # 点击的时间间隔
        self._duration = 5
        self._plantPosition = PlantPosition(width, high)

    def test_deivce(self):
        return self._adb.test_device()

    def check_devices(self):
        return self._adb.check_devices()

    def start_device(self):
        self._adb.start_device()

    # 开始战斗 点击一下
    def start_fighting_one(self):
        x1, y1, x2, y2 = self._plantPosition.start_fighting_one()
        self._adb.run(x1, y1, x2, y2, self._duration)

    # 开始战斗 点击一下
    def start_fighting_two(self):
        x1, y1, x2, y2 = self._plantPosition.start_fighting_two()
        self._adb.run(x1, y1, x2, y2, self._duration)

    # 重新开始
    def restart_fighting(self):
        x1, y1, x2, y2 = self._plantPosition.get_restart_game_point()
        self._adb.run(x1, y1, x2, y2, self._duration)
        x1, y1, x2, y2 = self._plantPosition.get_time_out()
        self._adb.run(x1, y1, x2, y2, self._duration)
        x1, y1, x2, y2 = self._plantPosition.get_restart_game_point()
        self._adb.run(x1, y1, x2, y2, self._duration)

    # 种植豌豆到八卦位置 点击两下
    def planting_peas(self):
        x1, y1, x2, y2 = self._plantPosition.getPea300_initial()
        self._adb.run(x1, y1, x2, y2, self._duration)
        x1, y1, x2, y2 = self._plantPosition.getPea300_space()
        self._adb.run(x1, y1, x2, y2, self._duration)

    #  种植太阳花
    def planting_sunflowers(self):
        x1, y1, x2, y2 = self._plantPosition.get_Primitive_sun_flower_initial()
        self._adb.run(x1, y1, x2, y2, self._duration)
        x1, y1, x2, y2 = self._plantPosition.get_Primitive_sun_flower_space()
        self._adb.run(x1, y1, x2, y2, self._duration)

    # 使用能量豆
    def using_Enerhy_Bean(self):
        x1, y1, x2, y2 = self._plantPosition.get_Enerhy_Bean()
        self._adb.run(x1, y1, x2, y2, self._duration)
        x1, y1, x2, y2 = self._plantPosition.get_Primitive_sun_flower_space()
        self._adb.run(x1, y1, x2, y2, self._duration)
        self.click_on_gold_coins()

    # 模拟点击金币 否则会影响到使用能量豆
    def click_on_gold_coins(self):
        duration = 100
        x1, y1, x2, y2 = self._plantPosition.collect_gold_coins_line_one()
        self._adb.run(x1, y1, x2, y2, duration)
        x1, y1, x2, y2 = self._plantPosition.collect_gold_coins_line_two()
        self._adb.run(x1, y1, x2, y2, duration)
        x1, y1, x2, y2 = self._plantPosition.collect_gold_coins_line_three()
        self._adb.run(x1, y1, x2, y2, duration)
        x1, y1, x2, y2 = self._plantPosition.collect_gold_coins_line_four()
        self._adb.run(x1, y1, x2, y2, duration)
