# -*- coding: utf-8 -*-

# 植物位置信息工具类
# 计算各个植物位置的point
# 以 1080*2016 为标准(我的是1080*2016)


class PZPoint:
    def __init__(self, x, y, ratiow, ratioh):
        self.x = int(float(x) * ratiow)
        self.y = int(float(y) * ratioh)
        print(self.x, self.y)


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

        # 300阳关豌豆初始位置
        self._pea300_initial = PZPoint(100, 300, self._ratioW, self._ratioH)
        # 300阳关豌豆放置位置 放置位置在八卦图位置
        self._pea300_space = PZPoint(950, 550, self._ratioW, self._ratioH)

        # 原始太阳花初始位置
        self._primitive_sun_flower_initial = PZPoint(100, 200, self._ratioW, self._ratioH)
        # 原始太阳花放置位置
        self._primitive_sun_flower_space = PZPoint(1200, 550, self._ratioW, self._ratioH)
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

    def get_restart_game_point(self):
        return self._restart_game.x, \
               self._restart_game.y, \
               self._restart_game.x, \
               self._restart_game.y

    def get_time_out(self):
        return self._time_out.x, \
               self._time_out.y, \
               self._time_out.x, \
               self._time_out.y

    # 获取右下角的开始战斗point
    def start_fighting_one(self):
        return self._start_game_one.x, \
               self._start_game_one.y, \
               self._start_game_one.x, \
               self._start_game_one.y

    # 获取右下角的开始战斗point
    def start_fighting_two(self):
        return self._start_game_two.x, \
               self._start_game_two.y, \
               self._start_game_two.x, \
               self._start_game_two.y

    # 获取收取金币的路线点
    def collect_gold_coins_line_one(self):
        return self._pea300_space.x - 100, \
               self._pea300_space.y + 50, \
               self._primitive_sun_flower_space.x + 200, \
               self._primitive_sun_flower_space.y + 50

    # 获取收取金币的路线点
    def collect_gold_coins_line_two(self):
        return self._pea300_space.x - 100, \
               self._pea300_space.y, \
               self._primitive_sun_flower_space.x + 200, \
               self._primitive_sun_flower_space.y

    # 获取收取金币的路线点
    def collect_gold_coins_line_three(self):
        return self._pea300_space.x - 100, \
               self._pea300_space.y + 50, \
               self._primitive_sun_flower_space.x + 200, \
               self._primitive_sun_flower_space.y - 50

    # 获取收取金币的路线点
    def collect_gold_coins_line_four(self):
        return self._pea300_space.x - 100, \
               self._pea300_space.y - 50, \
               self._primitive_sun_flower_space.x + 200, \
               self._primitive_sun_flower_space.y + 50

    # 获取能量豆位置
    def get_Enerhy_Bean(self):
        return self._energy_bean.x, \
               self._energy_bean.y, \
               self._energy_bean.x, \
               self._energy_bean.y

    # 获取原始太阳花初始位置
    def get_Primitive_sun_flower_initial(self):
        return self._primitive_sun_flower_initial.x, \
               self._primitive_sun_flower_initial.y, \
               self._primitive_sun_flower_initial.x, \
               self._primitive_sun_flower_initial.y

    # 获取原始太阳花放置位置
    def get_Primitive_sun_flower_space(self):
        return self._primitive_sun_flower_space.x, \
               self._primitive_sun_flower_space.y, \
               self._primitive_sun_flower_space.x, \
               self._primitive_sun_flower_space.y

    #  获取豌豆300 初始位置
    def getPea300_initial(self):
        return self._pea300_initial.x, \
               self._pea300_initial.y, \
               self._pea300_initial.x, \
               self._pea300_initial.y

    #  获取豌豆300 放置位置
    def getPea300_space(self):
        return self._pea300_space.x, \
               self._pea300_space.y, \
               self._pea300_space.x, \
               self._pea300_space.y
