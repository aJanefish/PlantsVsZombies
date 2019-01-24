# -*- coding: utf-8 -*-

# 植物位置信息工具类
# 计算各个植物位置的point
# 以 1080*2016 为标准(我的是1080*2016)


class PZPoint:
    def __init__(self, x, y, ratiow, ratioh):
        self.x = int(float(x) * ratiow)
        self.y = int(float(y) * ratioh)
        # print(self.x, self.y)


class PlantPosition:
    def __init__(self, width, high):
        # 基准参数
        self._defWidth = 1080
        self._defHigh = 2160
        # 实际参数
        self._width = width
        self._high = high

        self._ratioW = float(self._width) / float(self._defWidth)
        self._ratioH = float(self._high) / float(self._defHigh)

        self._plantListX1 = 10
        self._plantListY1 = 120
        self._plantListX2 = 180
        self._plantListY2 = 970
        self._plantList = []
        midx = (self._plantListX1 + self._plantListX2) / 2
        averagey = (self._plantListY2 - self._plantListY1) / 8
        for x in range(8):
            y = self._plantListY1 + averagey * x + averagey / 2
            self._plantList.append(PZPoint(midx, y, self._ratioW, self._ratioH))

        self._battlefieldSpace = {}
        self._battlefieldSpaceX1 = 850
        self._battlefieldSpaceX2 = 2120
        self._battlefieldSpaceY1 = 150
        self._battlefieldSpaceY2 = 950

        averagex = (self._battlefieldSpaceX2 - self._battlefieldSpaceX1) / 9
        averagey = (self._battlefieldSpaceY2 - self._battlefieldSpaceY1) / 5
        for x in range(9):
            for y in range(5):
                pointx = 850 + averagex * x + averagex / 2
                pointy = 150 + averagey * y + averagey / 2
                self._battlefieldSpace.update(
                    {str(x) + "" + str(y): PZPoint(pointx, pointy, self._ratioW, self._ratioH)})

        # 能量豆位置
        self._energy_bean = PZPoint(950, 1000, self._ratioW, self._ratioH)
        # 右下角的开始战斗
        self._start_game_one = PZPoint(2100, 1000, self._ratioW, self._ratioH)
        # 右上角的开始战斗
        self._start_game_two = PZPoint(1900, 200, self._ratioW, self._ratioH)
        # 暂停point
        self._time_out = PZPoint(2100, 50, self._ratioW, self._ratioH)
        # 重新开始按钮point
        self._restart_game = PZPoint(1100, 800, self._ratioW, self._ratioH)

    def get_plant_list_by(self, index):
        return self._plantList[index]

    def get_battlefield_space(self, x, y):
        return self._battlefieldSpace[str(x) + "" + str(y)]

    def get_restart_game_point(self):
        return self._restart_game

    def get_time_out(self):
        return self._time_out

    # 获取右下角的开始战斗point
    def start_fighting_one(self):
        return self._start_game_one

    # 获取右下角的开始战斗point
    def start_fighting_two(self):
        return self._start_game_two

    # 获取能量豆位置
    def get_Enerhy_Bean(self):
        return self._energy_bean
