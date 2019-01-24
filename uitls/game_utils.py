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
        self._duration = 10
        self._plantPosition = PlantPosition(width, high)

    def test_deivce(self):
        return self._adb.test_device()

    def check_devices(self):
        return self._adb.check_devices()

    def start_device(self):
        self._adb.start_device()

    def _click_plant(self, index):
        point = self._plantPosition.get_plant_list_by(index)
        self._adb.run(point.x, point.y, point.x, point.y, self._duration)

    def _click_space(self, index, x, y):
        self._click_plant(index)
        point_space = self._plantPosition.get_battlefield_space(x, y)
        self._adb.run(point_space.x, point_space.y, point_space.x, point_space.y, self._duration)

    # 开始战斗 点击一下
    def start_fighting_one(self):
        point = self._plantPosition.start_fighting_one()
        self._adb.run(point.x, point.y, point.x, point.y, self._duration)

    # 开始战斗 点击一下
    def start_fighting_two(self):
        point = self._plantPosition.start_fighting_two()
        self._adb.run(point.x, point.y, point.x, point.y, self._duration)

    # 重新开始
    def restart_fighting(self):
        point = self._plantPosition.get_restart_game_point()
        self._adb.run(point.x, point.y, point.x, point.y, self._duration)
        point_time_out = self._plantPosition.get_time_out()
        self._adb.run(point_time_out.x, point_time_out.y, point_time_out.x, point_time_out.y, self._duration)

        self._adb.run(point.x, point.y, point.x, point.y, self._duration)

    # 种植豌豆到八卦位置 点击两下
    def planting_peas(self):
        self._click_space(1, 0, 2)

    #  种植太阳花
    def planting_sunflowers(self):
        self._click_space(0, 1, 2)
        self._click_space(0, 2, 2)
        self._click_space(0, 3, 2)
        self._click_space(0, 4, 2)

    # 点击能量豆
    def _click_energy(self, x, y):
        point_energy = self._plantPosition.get_Energy_Bean()
        point = self._plantPosition.get_battlefield_space(x, y)
        self._adb.run(point_energy.x, point_energy.y, point.x+20, point.y+20, 200)

    # 使用能量豆
    def using_Energy_Bean(self):
        self._click_energy(1, 2)
        self._click_energy(2, 2)
        self._click_energy(3, 2)
        self._click_energy(4, 2)

        self.click_on_gold_coins()

    # 收集能量豆
    def collect_energy_beans(self):
        duration = 50
        point1 = self._plantPosition.get_battlefield_space(0, 2)
        self._adb.run(point1.x - 100, point1.y + 50, point1.x + 100, point1.y + 50, duration)
        self._adb.run(point1.x - 100, point1.y + 100, point1.x + 100, point1.y + 100, duration)

    # 模拟点击金币 否则会影响到使用能量豆
    def click_on_gold_coins(self):
        duration = 100
        point1 = self._plantPosition.get_battlefield_space(0, 2)
        point2 = self._plantPosition.get_battlefield_space(4, 2)
        self._adb.run(point1.x - 100, point1.y + 50, point2.x + 100, point2.y + 50, duration)
        self._adb.run(point1.x - 100, point1.y, point2.x + 100, point2.y, duration)
        self._adb.run(point1.x - 100, point1.y + 50, point2.x + 100, point2.y - 50, duration)
        self._adb.run(point1.x - 100, point1.y - 50, point2.x + 100, point2.y + 50, duration)
