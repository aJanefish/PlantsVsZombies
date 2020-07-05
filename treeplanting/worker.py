# -*- coding: utf-8 -*-
###
#  植树活动 获取碎片 works
###
from uitls.adb import AutoAdb
from uitls.plantUtils import PZPoint


class TreePosition:
    def __init__(self, width, high):
        # 基准参数
        self._defWidth = 1080
        self._defHigh = 2160
        # 实际参数
        self._width = width
        self._high = high
        # 对比
        self._ratioW = float(self._width) / float(self._defWidth)
        self._ratioH = float(self._high) / float(self._defHigh)

        self._watering = PZPoint(1000, 800, self._ratioW, self._ratioH)
        self._fruit = PZPoint(800, 600, self._ratioW, self._ratioH)
        # 收获
        self._reward = PZPoint(850, 820, self._ratioW, self._ratioH)
        # 确认
        self._confirm = PZPoint(1100, 830, self._ratioW, self._ratioH)

    def get_watering(self):
        return self._watering

    def get_fruit(self):
        return self._fruit

    def get_reward(self):
        return self._reward

    def get_confirm(self):
        return self._confirm


#  动作执行
class TreeWorker:

    def __init__(self, width, high):
        self._adb = AutoAdb()
        # 点击的时间间隔
        self._duration = 1
        self._treePosition = TreePosition(width, high)

    def watering(self):
        point = self._treePosition.get_watering()
        self._adb.run(point.x, point.y, point.x, point.y, self._duration)

    def fruit(self):
        point = self._treePosition.get_fruit()
        self._adb.run(point.x, point.y, point.x, point.y, self._duration)

    def reward(self):
        point = self._treePosition.get_reward()
        self._adb.run(point.x, point.y, point.x, point.y, self._duration)

    def confirm(self):
        point = self._treePosition.get_confirm()
        self._adb.run(point.x, point.y, point.x, point.y, self._duration)
