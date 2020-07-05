# -*- coding: utf-8 -*-
###
#  植树活动 获取碎片
###
import threading
import time

from treeplanting.worker import TreeWorker


class Tree(threading.Thread):
    def __init__(self, name, width, high):
        threading.Thread.__init__(self)
        self.name = name
        self._worker = TreeWorker(width, high)

    def run(self):
        for x in range(300):
            print(x)
            self.work()

    def work(self):
        # 浇水
        self._worker.watering()
        time.sleep(5)
        self._worker.watering()
        time.sleep(5)
        self._worker.watering()
        time.sleep(5)
        # 获取果实
        self._worker.fruit()
        self._worker.reward()
        self._worker.confirm()
