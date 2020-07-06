# -*- coding: utf-8 -*-

#  植物大战僵尸 辅助函数
#  功夫世界 终极挑战  刷金币
import time

from uitls.adb import AutoAdb
from uitls.plantUtils import PlantPosition


class KongFuWorldUltimateChallenge:
    def __init__(self, width, high):
        self._adb = AutoAdb()
        # self.test_devices()
        # 点击的时间间隔
        self._duration = 1
        self._plantPosition = PlantPosition(width, high)

    def test_devices(self):
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
    def start_game_right_bottom(self):
        point = self._plantPosition.start_game_right_bottom()
        self._adb.run(point.x, point.y, point.x, point.y, self._duration)

    # 开始战斗 点击一下
    def start_game_right_top(self):
        point = self._plantPosition.start_game_right_top()
        self._adb.run(point.x, point.y, point.x, point.y, self._duration)

    # 重新开始
    # 由于最新的版本中点击暂停后会弹出广告推荐弹窗-需要广告推荐弹窗多一步点击取消的操作
    def restart_fighting(self):
        # 获取重新开始按钮的坐标
        restart_point = self._plantPosition.get_restart_game_point()
        # 点击重新开始按钮(为什么需要先点击一次重新开始呢？就是防止你已经在重新开始页面)
        self._adb.run(restart_point.x, restart_point.y, restart_point.x, restart_point.y, self._duration)
        # 获取暂停按钮的坐标
        point_pause_point = self._plantPosition.get_pause_point()
        self._adb.run(point_pause_point.x, point_pause_point.y, point_pause_point.x, point_pause_point.y,
                      self._duration)
        # 新版本—点击暂停过后会弹出广告推荐弹窗-过滤掉
        # 防止出现广告 - 暂停2s
        time.sleep(2)
        # 点击广告删除按钮
        recommend_dialog_point = self._plantPosition.get_recommend_dialog_point()
        self._adb.run(recommend_dialog_point.x, recommend_dialog_point.y, recommend_dialog_point.x,
                      recommend_dialog_point.y, self._duration)

        # 点击重新开始按钮
        self._adb.run(restart_point.x, restart_point.y, restart_point.x, restart_point.y, self._duration)

    # 种植豌豆到八卦位置 点击两下
    def planting(self, index, x, y):
        self._click_space(index, x, y)

    # #  种植太阳花
    # def planting_sunflowers(self):
    #     self._click_space(0, 1, 2)
    #     self._click_space(0, 2, 2)
    #     self._click_space(0, 3, 2)
    #     self._click_space(0, 4, 2)

    # 点击能量豆
    def _click_energy(self, x, y):
        point_energy = self._plantPosition.get_energy_bean()
        self._adb.run(point_energy.x, point_energy.y, point_energy.x, point_energy.y, self._duration)
        point02 = self._plantPosition.get_battlefield_space(0, 2)
        point = self._plantPosition.get_battlefield_space(x, y)
        self._adb.run(point02.x - 100, point02.y, point.x + 20, point.y, 200)

    # 使用能量豆
    def using_energy_bean(self, x, y):
        self._click_energy(x, y)

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
