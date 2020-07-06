# -*- coding: utf-8 -*-

# 植物位置信息工具类
# 计算各个植物位置的point
# 以 1080*2016 为标准(我的是1080*2016)


class PZPoint:
    def __init__(self, x, y, ratio_w, ratio_h):
        self.x = int(float(x) * ratio_w)
        self.y = int(float(y) * ratio_h)
        # print(self.x, self.y)


class PlantPosition:
    def __init__(self, width, high):
        # 基准参数
        self._defWidth = 1080
        self._defHigh = 2160
        # 实际参数
        self._width = width
        self._high = high

        # 比例
        self._ratioW = float(self._width) / float(self._defWidth)
        self._ratioH = float(self._high) / float(self._defHigh)

        # 植物存放列表的坐标,[1,9]
        self._plantListX1 = 10
        self._plantListY1 = 120
        self._plantListX2 = 180
        self._plantListY2 = 970
        self._plantList = []
        mid_x = (self._plantListX1 + self._plantListX2) / 2
        average_y = (self._plantListY2 - self._plantListY1) / 8
        for x in range(8):
            y = self._plantListY1 + average_y * x + average_y / 2
            self._plantList.append(PZPoint(mid_x, y, self._ratioW, self._ratioH))

        # 植物战斗二维数组的坐标,[9,5]
        self._battlefieldSpace = {}
        self._battlefieldSpaceX1 = 850
        self._battlefieldSpaceX2 = 2120
        self._battlefieldSpaceY1 = 150
        self._battlefieldSpaceY2 = 950

        average_x = (self._battlefieldSpaceX2 - self._battlefieldSpaceX1) / 9
        average_y = (self._battlefieldSpaceY2 - self._battlefieldSpaceY1) / 5
        # 计算每一个框的点击位置
        for x in range(9):
            for y in range(5):
                point_x = 850 + average_x * x + average_x / 2
                point_y = 150 + average_y * y + average_y / 2
                self._battlefieldSpace.update(
                    {str(x) + "" + str(y): PZPoint(point_x, point_y, self._ratioW, self._ratioH)})

        # 能量豆位置
        self._energy_bean = PZPoint(950, 1000, self._ratioW, self._ratioH)
        # 右下角的开始战斗
        self._start_game_right_bottom = PZPoint(2100, 1000, self._ratioW, self._ratioH)
        # 右上角的开始战斗
        self._start_game_right_top = PZPoint(1900, 200, self._ratioW, self._ratioH)
        # 暂停point
        self._pause_point = PZPoint(2100, 50, self._ratioW, self._ratioH)
        # 重新开始按钮point
        self._restart_game = PZPoint(1100, 800, self._ratioW, self._ratioH)
        # 新版本广告推荐弹窗-删除按钮坐标point
        self._recommend_dialog_point = PZPoint(1680, 160, self._ratioW, self._ratioH)

    def get_plant_list_by(self, index):
        return self._plantList[index]

    def get_battlefield_space(self, x, y):
        return self._battlefieldSpace[str(x) + "" + str(y)]

    def get_restart_game_point(self):
        return self._restart_game

    def get_pause_point(self):
        return self._pause_point

    # 获取右下角的开始战斗point
    def start_game_right_bottom(self):
        return self._start_game_right_bottom

    # 获取右下角的开始战斗point
    def start_game_right_top(self):
        return self._start_game_right_top

    # 获取能量豆位置
    def get_energy_bean(self):
        return self._energy_bean

    # 新版本广告推荐弹窗-删除按钮坐标point
    def get_recommend_dialog_point(self):
        return self._recommend_dialog_point