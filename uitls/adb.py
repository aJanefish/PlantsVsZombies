# -*- coding: utf-8 -*-
import os
import subprocess
import platform

#  adb 触屏函数
#  参看 https://github.com/wangshub/wechat_jump_game
import time


class auto_adb():
    def __init__(self):
        try:
            adb_path = 'adb'
            subprocess.Popen([adb_path], stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
            self.adb_path = adb_path
        except OSError:
            if platform.system() == 'Windows':
                adb_path = os.path.join('Tools', "adb", 'adb.exe')
                try:
                    subprocess.Popen(
                        [adb_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    self.adb_path = adb_path
                except OSError:
                    pass
            else:
                try:
                    subprocess.Popen(
                        [adb_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                except OSError:
                    pass
            print('请安装 ADB 及驱动并配置环境变量')
            print('具体链接: https://github.com/wangshub/wechat_jump_game/wiki')
            exit(1)

    def get_screen(self):
        process = os.popen(self.adb_path + ' shell wm size')
        output = process.read()
        return output

    def run(self, x1, y1, x2, y2, duration):
        # 坐标原点（右上角） 50 50
        #  1080 2160
        cmd = 'shell input swipe {} {} {} {} {}'.format(
            x1,
            y1,
            x2,
            y2,
            duration
        )
        # print(cmd)
        self.__run(cmd)

    def __run(self, raw_command):
        command = '{} {}'.format(self.adb_path, raw_command)
        process = os.popen(command)
        output = process.read()
        return output

    def test_device(self):
        print('检查设备是否连接...')
        print("adb_path:", self.adb_path)
        command_list = [self.adb_path, 'devices']
        print(command_list)
        process = subprocess.Popen(command_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = process.communicate()
        # print("output", len(output))
        # print(type(output[0]), output[0])
        # print(output[0].decode('utf8'))
        # if output[0].decode('utf8') == 'List of devices attached\n\n':
        #     print('未找到设备')
        #     print('adb 输出:')
        #     for each in output:
        #         print(each.decode('utf8'))
        #     return False
        #     #   exit(1)
        # print('设备已连接')
        # print('adb 输出:', )
        flag = False
        file = open("myLog.txt", "a")
        for each in output:
            print(type(each), type(each.decode('utf8')), each.decode('utf8'))
            file.write(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) + "  :  " + each.decode('utf8'))
            if ('\tdevice' in each.decode('utf8')):
                flag = True
        file.close()
        return flag

    def check_devices(self):
        command_list = [self.adb_path, 'devices']
        process = subprocess.Popen(command_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = process.communicate()
        flag = False
        for each in output:
            if ('\tdevice' in each.decode('utf8')):
                flag = True
        return flag

    def start_device(self):
        command_list = [self.adb_path, 'kill-server']
        print('重启adb服务...')
        print(command_list)
        subprocess.Popen(command_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def test_density(self):
        # adb shell wm density
        process = os.popen(self.adb_path + ' shell wm density')
        output = process.read()
        return output

    def test_device_detail(self):
        process = os.popen(self.adb_path + ' shell getprop ro.product.device')
        output = process.read()
        return output

    def test_device_os(self):
        process = os.popen(self.adb_path + ' shell getprop ro.build.version.release')
        output = process.read()
        return output

    def adb_path(self):
        return self.adb_path
