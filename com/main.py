# -*- coding: utf-8 -*-

#  程序主函数
from com.utils.game_utils import KungFuWorldUltimateChallenge
import time


def game():
    tips.restart_fighting()
    # 等待动画播放完成
    time.sleep(10)
    # 点击开始战斗
    tips.start_fighting_one()
    # 等待动画完成
    time.sleep(8)
    # 放置植物
    tips.planting_peas()
    tips.planting_sunflowers_one()
    tips.planting_sunflowers_two()
    tips.planting_sunflowers_three()
    tips.planting_sunflowers_four()

    # 开始战斗
    tips.start_fighting_two()
    # 等待动画完成
    time.sleep(3)
    #  收集能量豆
    tips.click_on_gold_coins()

    # 使用能量豆
    tips.using_peas_one()
    tips.click_on_gold_coins()
    tips.using_peas_two()
    tips.click_on_gold_coins()
    tips.using_peas_three()
    tips.click_on_gold_coins()
    tips.using_peas_four()
    tips.click_on_gold_coins()
    time.sleep(1)


def main():
    for x in range(1000):
        start = time.time()
        game()
        end = time.time()
        print("total :", x, (end - start))


if __name__ == '__main__':
    tips = KungFuWorldUltimateChallenge()
    main()
