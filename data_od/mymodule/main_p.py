# * QTabWidget 탭에 다양한 위젯 추가
import numpy as np
from PyQt5.QtWidgets import *
# from PyQt5.QtGui import QIcon, QFont       #아이콘
from PyQt5.QtCore import Qt, QThread

import sys
sys.path.append('C:/my_games/coobcco2/data_od/mymodule')
import os
import time
from datetime import datetime
import random
import os.path
from datetime import date, timedelta
import re

import cv2
# print(cv2.__version__)
# import matplotlib.pyplot as plt
from PIL import Image




import numpy
# 패키지 다운 필요
import pytesseract
# from pytesseract import image_to_string #
import pyautogui
import clipboard
# import keyboard
# 패키지 다운 불필요
import tkinter
import webbrowser
import colorthief
import git

# 나의 모듈
# from schedule import go_test, go_character_select
from schedule import myQuest_number_check, go_character_select, myQuest_number_check_bool, myQuest_grow_check, myQuest_play_check, myQuest_play_add, go_test
from login_start import login_start_ready, get_cla_count, grow_chango_check, status_check_get, today_lotation, just_login, characterChange
from clean import lotation_change_ready, clean_screen, bangchi_mode
from action import go_alrim_confirm, now_hunting_is, go_collection_on, go_juljun, game_settings, mypost, go_level, go_quest_ing, go_mynumber_, go_potion_off, go_boonhae, go_bag, go_power_bag
from myfunction import imgs_set, imgs_set_, click_pos_2, random_int, background_myPotion_check, go_to_home, text_check_get_3, potion_count_grow, int_put_, text_check_get, click_with_image, drag_pos, image_processing, get_region, dead_die, go_auto, click_pos_reg
from chango import go_chango, chango_, auction, auction_all_get
from dungeon import jadong_cla_ready, go_jadong_cla_mypower, dunjeon_cla_play, jadong_cla_play
from event_get import game_event_get_ready, achieve_get_
from guild import guild_join_
from maul import maul_mission
from where import go_worldmap
from go_ import go_test
from grow import yotoon_grow, potion_grow, common_grow, nida_grow, nida_grow_end, tuto_grow, yotoon_grow_end
from stop_18 import is_stop
from dungeon_su import dunjeon_cla_play_su


from massenger import line_to_me, line_monitor

import variable as v_

sys.setrecursionlimit(10**7)
# pyqt5 관련##################################################
rowcount = 0
colcount = 0
rehi_ = 'none'
thisRow = 0
thisCol = 0
table_datas = ""
onCharacter = 0
onRefresh_time = 0
onDunjeon = "none"
onDunjeon_level = 0
onHunt = "none"
onMaul = "none"

isgloballoop = False

# 기존 오토모드 관련###############################################
one_cla_id = "none"
one_cla_pw = "none"
two_cla_id = "none"
two_cla_pw = "none"
# 1번
v_.mynumber_1 = 0
v_.mylevel_1 = 0
v_.mymoney_1 = 0
v_.mypower_1 = 0
v_.mypotion_1 = 0
v_.gonghu_1 = False
v_.nanjang_1 = False
v_.underprison_1 = False
v_.jadong_1 = False
v_.myId_1 = 0
v_.one_cla_count = 0
v_.one_cla_ing = 'check'
# 2번
v_.mynumber_2 = 0
v_.mylevel_2 = 0
v_.mymoney_2 = 0
v_.mypower_2 = 0
v_.mypotion_2 = 0
v_.gonghu_2 = False
v_.nanjang_2 = False
v_.underprison_2 = False
v_.jadong_2 = False
v_.myId_2 = 0
v_.two_cla_count = 0
v_.two_cla_ing = 'check'
# 현재실행중인 클라우드
v_.now_cla = 'none'
v_.one_cla_start = 0
v_.two_cla_start = 0
v_.global_howcla = 'none'
v_.change_ready_main = False
v_.change_ready_step = False

v_.one_now_growing_ = 'none'
v_.two_now_growing_ = 'none'

version = v_.version_

pyautogui.FAILSAFE = False
####################################################################################################################
# pytesseract.pytesseract.tesseract_cmd = R'E:\workspace\pythonProject\Tesseract-OCR\tesseract'
pytesseract.pytesseract.tesseract_cmd = R'C:\Program Files\Tesseract-OCR\tesseract'
####################################################################################################################
####################################################################################################################
####################################################################################################################
#######pyqt5 관련####################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################


class MyApp(QDialog):


    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMaximizeButtonHint | Qt.WindowMinimizeButtonHint)

        self.initUI()

    def initUI(self):
        tabs = QTabWidget()
        tabs.addTab(FirstTab(), '스케쥴')
        tabs.addTab(SecondTab(), '내 정보')
        tabs.addTab(ThirdTab(), '모니터링')

        # buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        # buttonbox.accepted.connect(self.accept)
        # buttonbox.rejected.connect(self.reject)




        vbox = QVBoxLayout()
        vbox.addWidget(tabs)
        # vbox.addWidget(buttonbox)

        self.setLayout(vbox)

        self.setWindowTitle('오딘(ver ' + str(version) + ')')
        # 업데이트 버젼
        # pyinstaller --hidden-import PyQt5 --hidden-import requests --hidden-import chardet -i="star_icon.ico" --add-data="star_icon.ico;./" --icon="star_icon.ico" --paths "C:\my_games\venv\lib\site-packages\cv2" main.py
        # 풀버젼
        # pyinstaller --hidden-import PyQt5 --hidden-import requests --hidden-import chardet --add-data="C:\\my_games\\coobcco2\\data_od;./data_od" -i="star_icon.ico" --add-data="star_icon.ico;./" --icon="star_icon.ico" --paths "C:\Users\1_S_3\AppData\Local\Programs\Python\Python311\Lib\site-packages\cv2" main.py

        self.setGeometry(50, 300, 830, 600)
        self.show()

        # self.pause = False

        # print("gdsgas")
        # for i in range(100):
        #     if self.pause:
        #         print("Paused")
        #         while self.pause: time.sleep(1)
        #     print("Number: " + str(i))
        #     time.sleep(1)
        # self.Test_check = Test_check()
        # self.Test_check.start()



    # def keyPressEvent(self, e):
    #     global isgloballoop
    #     if e.key() == Qt.Key_Escape:
    #         self.close()
    #     elif e.key() == Qt.Key_Q:
    #         print("e.key() == Qt.Key_Q:")
    #         self.Test_check.pause = False
    #
    #         # self.Test_check.stop_()
    #     elif e.key() == Qt.Key_W:
    #         print("e.key() == Qt.Key_W:")
    #         self.Test_check.pause = True
    #         self.Test_check.start()

class ThirdTab(QWidget):


    def __init__(self):
        super().__init__()
        self.initUI()
        # self.set_rand_int()

    def initUI(self):


        dir_path = "C:\\my_games"
        file_path = dir_path + "\\line\\line.txt"

        if os.path.isdir(dir_path) == False:
            os.makedirs(dir_path)
        isFile = False
        while isFile is False:
            if os.path.isfile(file_path) == True:
                isFile = True
                # 파일 읽기
                with open(file_path, "r", encoding='utf-8-sig') as file:
                    line = file.read()
                    line_ = line.split(":")
                    print('line', line)
            else:
                print('line 파일 없당')
                with open(file_path, "w", encoding='utf-8-sig') as file:
                    file.write("ccocco:메에롱")

        self.monitor = QGroupBox('My Cla Monitor')

        self.own = QLabel("       현재 소유자 : " + line_[0] + "\n\n")
        self.computer = QLabel("       현재 컴퓨터 : " + line_[1] + " 컴퓨터\n\n")

        self.own_in = QLineEdit(self)
        self.own_in.setText(line_[0])
        self.computer_in = QLineEdit(self)
        self.computer_in.setText(line_[1])
        self.line_save = QPushButton("저장하기")
        self.line_save.clicked.connect(self.button_line_save)

        self.monitoring_1 = QPushButton("one 모니터링")
        self.monitoring_1.clicked.connect(self.button_monitoring_one)
        self.monitoring_2 = QPushButton("all 모니터링")
        self.monitoring_2.clicked.connect(self.button_monitoring_all)

        mo1_1 = QHBoxLayout()
        mo1_1.addWidget(self.own)


        mo1_2 = QHBoxLayout()
        mo1_2.addWidget(self.computer)


        mo1_3 = QHBoxLayout()
        mo1_3.addStretch(1)
        mo1_3.addWidget(self.own_in)
        mo1_3.addWidget(self.computer_in)
        mo1_3.addStretch(1)
        mo1_3.addWidget(self.line_save)
        mo1_3.addStretch(18)

        mo1_4 = QHBoxLayout()
        mo1_4.addWidget(self.monitoring_1)
        mo1_4.addWidget(self.monitoring_2)

        Mobox1 = QVBoxLayout()
        Mobox1.addStretch(1)
        Mobox1.addLayout(mo1_1)
        Mobox1.addLayout(mo1_2)
        Mobox1.addLayout(mo1_3)
        Mobox1.addStretch(3)
        Mobox1.addLayout(mo1_4)
        Mobox1.addStretch(3)

        self.monitor.setLayout(Mobox1)

        hbox_ = QHBoxLayout()
        hbox_.addWidget(self.monitor)

        Vbox_ = QVBoxLayout()
        Vbox_.addLayout(hbox_)

        self.setLayout(Vbox_)

        # hbox__ = QHBoxLayout()
        # hbox__.addWidget(self.monitor)
        #
        # ###
        # vbox = QVBoxLayout()
        # vbox.addLayout(hbox__)

    def button_line_save(self):
        own_ = self.own_in.text()  # line_edit text 값 가져오기
        computer_ = self.computer_in.text()
        print(own_)
        print(computer_)

        self.own.setText("       현재 소유자 : " + own_ + "\n\n")
        self.computer.setText("       현재 컴퓨터 : " + computer_ + " 컴퓨터\n\n")
        write_ = own_ + ":" + computer_
        dir_path = "C:\\my_games"
        file_path = dir_path + "\\line\\line.txt"

        with open(file_path, "w", encoding='utf-8-sig') as file:
            file.write(write_)

    def button_monitoring_one(self):
        v_.global_howcla = 'onecla'
        m_ = Monitoring(self)
        m_.start()
    def button_monitoring_all(self):
        v_.global_howcla = 'onetwocla'
        m_ = Monitoring(self)
        m_.start()

class SecondTab(QWidget):


    def __init__(self):
        super().__init__()
        self.initUI()
        # self.set_rand_int()

    def initUI(self):


        dir_path = "C:\\my_games\\coobcco2"
        file_path_one = dir_path + "\\odin_schedule\\onecla.txt"
        file_path_two = dir_path + "\\odin_schedule\\twocla.txt"
        if os.path.isfile(file_path_one) == True:
            # 파일 읽기
            with open(file_path_one, "r", encoding='utf-8-sig') as file:
                lines_one = file.read().splitlines()
                print('lines_one', lines_one)
                thismyid_one = lines_one[0]
                thismypw_one = lines_one[1]
                thismyps_one = lines_one[2]
        else:
            print('one 파일 없당')
            thismyid_one = 'none'
            thismyps_one = 'none'

        if os.path.isfile(file_path_two) == True:
            # 파일 읽기
            with open(file_path_two, "r", encoding='utf-8-sig') as file:
                lines_two = file.read().splitlines()
                print('lines_two', lines_two)
                thismyid_two = lines_two[0]
                thismypw_two = lines_two[1]
                thismyps_two = lines_two[2]
        else:
            print('two 파일 없당')
            thismyid_two = 'none'
            thismyps_two = 'none'

        # 111

        self.com_group1 = QGroupBox('One Cla')
        self.one_cla_id = QLabel("       ID          ")
        self.one_cla_pw = QLabel("       PW        ")
        self.one_cla_ps = QLabel("       참고사항 ")

        self.one_cla_id_now = QLabel("       현재 내 아이디 : " + thismyid_one + "\n\n")
        self.one_cla_ps_now = QLabel("       무슨 참고 사항을 적었나요? " + thismyps_one)

        self.pushButton_login1 = QPushButton("로그인하기")
        self.pushButton_login1.clicked.connect(self.let_is_login_1)

        self.pushButton_left = QPushButton("좌로 정렬")
        self.pushButton_left.clicked.connect(self.win_left)

        # self.one_cla_id_in = QLineEdit()
        self.one_cla_id_in = QLineEdit(self)
        self.one_cla_id_in.setText(thismyid_one)
        self.one_cla_pw_in = QLineEdit(self)
        self.one_cla_pw_in.setText(thismypw_one)
        self.one_cla_ps_in = QLineEdit(self)
        self.one_cla_ps_in.setText(thismyps_one)
        self.pushButton_one = QPushButton("저장하기")
        self.pushButton_one.clicked.connect(self.button_event1)

        vbox1_1 = QHBoxLayout()
        vbox1_1.addWidget(self.one_cla_id_now)

        vbox1_2 = QHBoxLayout()
        vbox1_2.addWidget(self.one_cla_ps_now)

        vbox1_log = QHBoxLayout()
        vbox1_log.addStretch(5)
        vbox1_log.addWidget(self.pushButton_login1)
        vbox1_log.addStretch(5)

        vbox1_left = QHBoxLayout()
        vbox1_left.addStretch(15)
        vbox1_left.addWidget(self.pushButton_left)
        vbox1_left.addStretch(1)

        vbox1_3 = QHBoxLayout()
        vbox1_3.addWidget(self.one_cla_id)
        vbox1_3.addWidget(self.one_cla_id_in)

        vbox1_4 = QHBoxLayout()
        vbox1_4.addWidget(self.one_cla_pw)
        vbox1_4.addWidget(self.one_cla_pw_in)

        vbox1_5 = QHBoxLayout()
        vbox1_5.addWidget(self.one_cla_ps)
        vbox1_5.addWidget(self.one_cla_ps_in)

        vbox1_6 = QHBoxLayout()
        vbox1_6.addStretch(5)
        vbox1_6.addWidget(self.pushButton_one)

        Vbox1 = QVBoxLayout()
        Vbox1.addStretch(1)
        Vbox1.addLayout(vbox1_1)
        Vbox1.addLayout(vbox1_2)
        Vbox1.addStretch(1)
        Vbox1.addLayout(vbox1_log)
        Vbox1.addStretch(5)
        Vbox1.addLayout(vbox1_left)
        Vbox1.addStretch(3)
        Vbox1.addLayout(vbox1_3)
        Vbox1.addLayout(vbox1_4)
        Vbox1.addLayout(vbox1_5)
        Vbox1.addLayout(vbox1_6)
        Vbox1.addStretch(2)
        # maul_add = QPushButton('마을 의뢰 추가')
        # maul_add.clicked.connect(self.onActivated_maul_add)
        # vbox6.addWidget(maul_add)
        self.com_group1.setLayout(Vbox1)

        #222
        self.com_group2 = QGroupBox('Two Cla')
        self.two_cla_id = QLabel("       ID          ")
        self.two_cla_pw = QLabel("       PW        ")
        self.two_cla_ps = QLabel("       참고사항 ")

        self.two_cla_id_now = QLabel("       현재 내 아이디 : " + thismyid_two + "\n\n")
        self.two_cla_ps_now = QLabel("       무슨 참고 사항을 적었나요? " + thismyps_two)

        self.pushButton_login2 = QPushButton("로그인하기")
        self.pushButton_login2.clicked.connect(self.let_is_login_2)

        self.pushButton_right = QPushButton("우로 정렬")
        self.pushButton_right.clicked.connect(self.win_right)

        self.two_cla_id_in = QLineEdit(self)
        self.two_cla_id_in.setText(thismyid_two)
        self.two_cla_pw_in = QLineEdit(self)
        self.two_cla_pw_in.setText(thismypw_two)
        self.two_cla_ps_in = QLineEdit(self)
        self.two_cla_ps_in.setText(thismyps_two)
        self.pushButton_two = QPushButton("저장하기")
        self.pushButton_two.clicked.connect(self.button_event2)

        vbox2_1 = QHBoxLayout()
        vbox2_1.addWidget(self.two_cla_id_now)

        vbox2_2 = QHBoxLayout()
        vbox2_2.addWidget(self.two_cla_ps_now)

        vbox2_log = QHBoxLayout()
        vbox2_log.addStretch(5)
        vbox2_log.addWidget(self.pushButton_login2)
        vbox2_log.addStretch(5)

        vbox2_right = QHBoxLayout()
        vbox2_right.addStretch(1)
        vbox2_right.addWidget(self.pushButton_right)
        vbox2_right.addStretch(15)

        vbox2_3 = QHBoxLayout()
        vbox2_3.addWidget(self.two_cla_id)
        vbox2_3.addWidget(self.two_cla_id_in)

        vbox2_4 = QHBoxLayout()
        vbox2_4.addWidget(self.two_cla_pw)
        vbox2_4.addWidget(self.two_cla_pw_in)

        vbox2_5 = QHBoxLayout()
        vbox2_5.addWidget(self.two_cla_ps)
        vbox2_5.addWidget(self.two_cla_ps_in)

        vbox2_6 = QHBoxLayout()
        vbox2_6.addStretch(5)
        vbox2_6.addWidget(self.pushButton_two)

        Vbox2 = QVBoxLayout()
        Vbox2.addStretch(1)
        Vbox2.addLayout(vbox2_1)
        Vbox2.addLayout(vbox2_2)
        Vbox2.addStretch(1)
        Vbox2.addLayout(vbox2_log)
        Vbox2.addStretch(5)
        Vbox2.addLayout(vbox2_right)
        Vbox2.addStretch(3)
        Vbox2.addLayout(vbox2_3)
        Vbox2.addLayout(vbox2_4)
        Vbox2.addLayout(vbox2_5)
        Vbox2.addLayout(vbox2_6)
        Vbox2.addStretch(2)
        # maul_add = QPushButton('마을 의뢰 추가')
        # maul_add.clicked.connect(self.onActivated_maul_add)
        # vbox6.addWidget(maul_add)
        self.com_group2.setLayout(Vbox2)


        ###
        hbox_ = QHBoxLayout()
        hbox_.addWidget(self.com_group2)

        Vbox_ = QVBoxLayout()
        Vbox_.addLayout(hbox_)

        ###
        hbox__ = QHBoxLayout()
        hbox__.addWidget(self.com_group1)
        hbox__.addLayout(Vbox_)

        ###
        vbox = QVBoxLayout()
        vbox.addLayout(hbox__)
        self.setLayout(vbox)

    def win_left(self):
        cla = "one"
        print("왼쪽으로 정렬 합니다.")
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\odin.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1080, cla, img, 0.8)
        # imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.7)
        time.sleep(0.5)
        if imgs_ is not None:
            print("왼쪽 odin 보여")
            click_pos_reg(imgs_.x + 100, imgs_.y, cla)
            pyautogui.keyDown('win')
            pyautogui.press('left')
            pyautogui.keyUp('win')
            time.sleep(0.3)
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\odin.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 0, 960, 1080, cla, img, 0.8)
            if imgs_ is not None:
                click_pos_reg(imgs_.x + 100, imgs_.y, cla)
    def win_right(self):
        cla = "two"
        print("오른쪽으로 정렬 합니다.")
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\odin.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1080, cla, img, 0.8)
        time.sleep(0.5)
        if imgs_ is not None:
            print("오른쪽 odin 보여")
            click_pos_reg(imgs_.x + 100, imgs_.y, cla)
            pyautogui.keyDown('win')
            pyautogui.press('right')
            pyautogui.keyUp('win')
            time.sleep(0.3)
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\odin.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 0, 960, 1080, cla, img, 0.8)
            if imgs_ is not None:
                click_pos_reg(imgs_.x + 100, imgs_.y, cla)
    def let_is_login_1(self):
        print("로그인1 버튼 입니다.")
        log_ = just_loginstart_one(self)
        log_.start()

    def let_is_login_2(self):
        print("로그인2 버튼 입니다.")
        log_ = just_loginstart_two(self)
        log_.start()

    def button_event1(self):
        one_cla_id_ = self.one_cla_id_in.text()  # line_edit text 값 가져오기
        one_cla_pw_ = self.one_cla_pw_in.text()
        one_cla_ps_ = self.one_cla_ps_in.text()
        print(one_cla_id_)
        print(one_cla_pw_)

        one_cla_id_result = "       현재 내 아이디 : " + one_cla_id_ + "\n\n"
        one_cla_ps_result = "       무슨 참고 사항을 적었나요? " + one_cla_ps_
        self.one_cla_id_now.setText(one_cla_id_result)
        self.one_cla_ps_now.setText(one_cla_ps_result)
        shcedule = one_cla_id_ + "\n" + one_cla_pw_ + "\n" + one_cla_ps_
        dir_path = "C:\\my_games\\coobcco2"
        file_path_one = dir_path + "\\odin_schedule\\onecla.txt"
        file_path_two = dir_path + "\\odin_schedule\\twocla.txt"
        with open(file_path_one, "w", encoding='utf-8-sig') as file:
            file.write(shcedule)

    def button_event2(self):
        two_cla_id_ = self.two_cla_id_in.text()  # line_edit text 값 가져오기
        two_cla_pw_ = self.two_cla_pw_in.text()
        two_cla_ps_ = self.two_cla_ps_in.text()
        print(two_cla_id_)
        print(two_cla_pw_)

        two_cla_id_result = "       현재 내 아이디 : " + two_cla_id_ + "\n\n"
        two_cla_ps_result = "       무슨 참고 사항을 적었나요? " + two_cla_ps_
        self.two_cla_id_now.setText(two_cla_id_result)
        self.two_cla_ps_now.setText(two_cla_ps_result)
        shcedule = two_cla_id_ + "\n" + two_cla_pw_ + "\n" + two_cla_ps_
        dir_path = "C:\\my_games\\coobcco2"
        file_path_one = dir_path + "\\odin_schedule\\onecla.txt"
        file_path_two = dir_path + "\\odin_schedule\\twocla.txt"
        with open(file_path_two, "w", encoding='utf-8-sig') as file:
            file.write(shcedule)


class FirstTab(QWidget):


    def __init__(self):
        super().__init__()
        self.initUI()
        self.set_rand_int()



    def initUI(self):
        global rowcount, colcount, rehi_, onCharacter, onDunjeon, onDunjeon_level, onMaul, onHunt, isgloballoop


        # print(rehi_)
        # if rehi_ == 'none':
        #     print("흑흑흑흑흑흑흑흑흑흑흑흑흑흑흑흑흑흑흑흑흑흑흑흑흑흑흑흑흑흑흑흑흑흑흑흑흑흑흑흑흑흑흑흑흑", rehi_)
        # else:
        #     print("헤헤헤헤헤!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", rehi_)
        # C:\\my_games\\coobcco2\\data_od\\odin_schedule\\
        # C:\\my_games\\coobcco2\\data_od\\imgs\\main.py
        # pyinstaller --hidden-import PyQt5 --add-data="C:\\my_games\\coobcco2\\data_od\\imgs;./imgs" --add-data="C:\\my_games\\coobcco2\\data_od\\jadong;./jadong" --add-data="C:\\my_games\\coobcco2\\data_od\\item;./item" main.py
        # pyinstaller --hidden-import PyQt5 --add-data="C:\\my_games\\coobcco2\\data_od\\odin_schedule\\;./odin_schedule" --add-data="C:\\my_games\\coobcco2\\data_od\\imgs;./imgs" --add-data="C:\\my_games\\coobcco2\\data_od\\jadong;./jadong" --add-data="C:\\my_games\\coobcco2\\data_od\\item;./item" main.py
        # dir_path = "C:\\odin_schedule"
        # file_path = dir_path + "\\schedule.txt"
        dir_path = "C:\\my_games\\coobcco2"
        file_path = dir_path + "\\odin_schedule\\schedule.txt"
        file_path3 = dir_path + "\\odin_schedule\\schedule2.txt"
        if os.path.isfile(file_path) == True:
            # 파일 읽기
            with open(file_path, "r", encoding='utf-8-sig') as file:
                lines = file.read().splitlines()
        else:
            print('파일 없당')
            if os.path.isdir(dir_path) == True:
                print('디렉토리 존재함')
                with open(file_path3, "r", encoding='utf-8-sig') as file:
                    shcedule = file.read().splitlines()
                    with open(file_path, "w", encoding='utf-8-sig') as file:
                        file.write(str(shcedule))
                        with open(file_path, "r", encoding='utf-8-sig') as file:
                            lines = file.read().splitlines()
            else:
                print('디렉토리 존재하지 않음')
                os.makedirs(dir_path)
                with open(file_path3, "r", encoding='utf-8-sig') as file:
                    shcedule = file.read().splitlines()
                    with open(file_path, "w", encoding='utf-8-sig') as file:
                        file.write(str(shcedule))
                        with open(file_path, "r", encoding='utf-8-sig') as file:
                            lines = file.read().splitlines()

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(lines))
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.verticalHeader().setVisible(False)  # 행번호 안나오게 하는 코드
        self.tableWidget.setHorizontalHeaderLabels(["클라", "ID", "던전", "현재상태", "클라", "ID", "던전", "현재상태"])


        self.label = QLabel('')

        #스케쥴 한칸 위로
        sche_up_modify = QPushButton('up')
        sche_up_modify.clicked.connect(self.sche_up_modify)
        #스케쥴 한칸 아래로
        sche_down_modify = QPushButton('down')
        sche_down_modify.clicked.connect(self.sche_down_modify)
        # 스케쥴 변경 확인.
        self.sche_add1 = QPushButton('one 대기중')
        self.sche_add1.clicked.connect(self.mySchedule_start1)
        self.sche_add2 = QPushButton('two 대기중')
        self.sche_add2.clicked.connect(self.mySchedule_start2)

        # 테스트 버튼
        self.mytestin = QPushButton('테스뚜')
        self.mytestin.clicked.connect(self.mytestin_)
        self.temporary_pause = QPushButton('일시정지')
        self.temporary_pause.clicked.connect(self.temporary_all_pause_game)
        self.again_restart = QPushButton('업데이트')
        self.again_restart.clicked.connect(self.again_restart_game)

        # 스케쥴 선택 삭제
        self.del_ = QPushButton('삭제')
        self.del_.clicked.connect(self.mySchedule_del)
        # 스케쥴 초기화
        self.clear = QPushButton('초기화')
        self.clear.clicked.connect(self.mySchedule_refresh)


        # self.setItems = QPushButton('Set Items')
        # self.setItems.clicked.connect(self.set_rand_int)


        #캐릭터 아이디
        self.com_group3 = QGroupBox('캐릭터 선택')
        cb3 = QComboBox()
        list3 = ['캐릭터 선택', '1', '2', '3', '4', '5']
        cb3.addItems(list3)
        vbox3 = QVBoxLayout()
        vbox3.addWidget(cb3)
        character_ = QPushButton('캐릭터 선택')
        character_.clicked.connect(self.onActivated_character)
        self.com_group3.setLayout(vbox3)

        # 초기화 시간 수정
        self.com_group33 = QGroupBox('초기화 시간 수정')
        cb33 = QComboBox()
        list33 = ['시간 선택', '4', '5', '6', '7', '8', '9', '10', '11']
        cb33.addItems(list33)
        vbox33 = QVBoxLayout()
        vbox33.addWidget(cb33)
        refresh_time_ = QPushButton('시간 수정')
        refresh_time_.clicked.connect(self.onActivated_re_time)

        vbox33.addWidget(refresh_time_)
        self.com_group33.setLayout(vbox33)

        # 초기화 시간
        dir_path = "C:\\my_games\\coobcco2"
        file_path2 = dir_path + "\\odin_schedule\\quest.txt"
        file_path13 = dir_path + "\\odin_schedule\\refresh_time.txt"

        isRefresh = False
        while isRefresh is False:
            if os.path.isfile(file_path13) == True:
                with open(file_path13, "r", encoding='utf-8-sig') as file:
                    isRefresh = True
                    refresh_time = file.read()
                    print("refresh_time", refresh_time)
            else:
                with open(file_path13, "w", encoding='utf-8-sig') as file:
                    file.write(str(6))

        if os.path.isfile(file_path2) == True:
            # 파일 읽기
            with open(file_path2, "r", encoding='utf-8-sig') as file:
                lines2 = file.read().splitlines()
                day_ = lines2[0].split(":")
                re_time_ = str(day_[0]) + " => " + str(day_[1] + "시")
                print("최근 초기화 시간 : ", re_time_)
        else:
            re_time_ = "아직 모름..."



        self.com_group34 = QGroupBox('셋팅된 시간')
        # lbx = QBoxLayout(QBoxLayout.LeftToRight, parent=self)
        # self.com_group34.setLayout(lbx)
        self.my_refresh_time = QLabel("현재 초기화 시간 : " + str(refresh_time) + "\n\n" + "최근 초기화한 시간 : " + re_time_)
        # lbx.addWidget(self.my_refresh_time)



        self.pushButton_one = QPushButton("현재 내 상태 조회하기")
        self.pushButton_one.clicked.connect(self.mystatus_refresh)

        vbox34 = QHBoxLayout()
        vbox34.addWidget(self.my_refresh_time)

        Vbox3434 = QVBoxLayout()
        Vbox3434.addLayout(vbox34)
        Vbox3434.addWidget(self.pushButton_one)

        self.com_group34.setLayout(Vbox3434)

        # self.one_cla_id_now = QLabel("       현재 내 아이디 : " + thismyid_one + "\n\n")

        # 마을 의뢰
        self.com_group6 = QGroupBox('마을 의뢰, 육성, 각종템받기, 거래소등록하기')
        cb6 = QComboBox()
        list6 = ['스케쥴 선택', '캐릭터바꾸기', '미드가르드', '요툰하임', '요툰육성', '니다육성', '각종템받기', '거래소등록', '셋팅초기화']
        cb6.addItems(list6)
        vbox6 = QHBoxLayout()
        vbox6.addWidget(cb6)
        maul_add = QPushButton('의뢰 및 행동 추가')
        maul_add.clicked.connect(self.onActivated_maul_add)

        vbox6.addWidget(maul_add)
        self.com_group6.setLayout(vbox6)

        #던전 종류
        self.com_group4 = QGroupBox('던전 및 육성 선택')
        cb4 = QComboBox()
        list4 = ['던전 선택', '공허', '난쟁이', '지하감옥']
        cb4.addItems(list4)
        cb44 = QComboBox()
        list44 = ['층수 선택', '1', '2', '3', '4', '5', '6']
        cb44.addItems(list44)

        vbox4 = QHBoxLayout()
        vbox4.addWidget(cb4)
        vbox4.addWidget(cb44)

        dunjeon = QPushButton('던전 및 육성 추가')
        dunjeon.clicked.connect(self.onActivated_dunjeon_add)

        vbox4.addWidget(dunjeon)
        self.com_group4.setLayout(vbox4)

        # 사냥터
        self.com_group5 = QGroupBox('자동사냥 선택')
        cb5 = QComboBox()
        list5 = ['자동 사냥터 선택', '폐성터', '바위해안', '들소황무지', '거인처형지', '트롤의기원', '예티서식지', '바람의땅', '늑대고원', '울부짖는산', '전사야영지', '광기의고원', "고블린부패", "살얼음언덕"]
        cb5.addItems(list5)
        vbox5 = QHBoxLayout()
        vbox5.addWidget(cb5)
        jadong = QPushButton('사냥터 추가')
        jadong.clicked.connect(self.onActivated_hunt_add)

        vbox5.addWidget(jadong)
        self.com_group5.setLayout(vbox5)

        cb3.activated[str].connect(self.onActivated_character)  # 요건 함수
        cb33.activated[str].connect(self.onActivated_time)  # 요건 함수
        cb4.activated[str].connect(self.onActivated_dunjeon)  # 요건 함수
        cb44.activated[str].connect(self.onActivated_dunjeon_level)  # 요건 함수
        cb5.activated[str].connect(self.onActivated_hunt)  # 요건 함수
        cb6.activated[str].connect(self.onActivated_maul)  # 요건 함수

        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.cellClicked.connect(self.set_label)
        rowcount = self.tableWidget.rowCount()
        colcount = self.tableWidget.columnCount()

        #레이아웃
        hbox1 = QHBoxLayout()
        # hbox1.addWidget(self.setItems)
        hbox1.addWidget(self.mytestin)
        hbox1.addWidget(self.temporary_pause)
        hbox1.addWidget(self.again_restart)
        hbox1.addWidget(self.del_)
        hbox1.addWidget(self.clear)


        hbox7 = QHBoxLayout()
        hbox7.addWidget(sche_up_modify)
        hbox7.addWidget(sche_down_modify)
        hbox7.addStretch(4)
        hbox7.addWidget(self.sche_add1)
        hbox7.addWidget(self.sche_add2)
        hbox7.addStretch(8)
        hbox7.addLayout(hbox1)


        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.com_group4)

        hbox4 = QHBoxLayout()
        hbox4.addWidget(self.com_group5)

        hbox5 = QHBoxLayout()
        hbox5.addWidget(self.com_group6)

        hbox33 = QHBoxLayout()
        hbox33.addWidget(self.com_group33)

        Vbox33 = QVBoxLayout()
        Vbox33.addLayout(hbox33)

        Vbox2 = QVBoxLayout()
        Vbox2.addLayout(hbox5)
        Vbox2.addLayout(hbox3)
        Vbox2.addLayout(hbox4)

        hbox2 = QHBoxLayout()
        hbox2.addLayout(Vbox33)
        hbox2.addWidget(self.com_group34)
        hbox2.addWidget(self.com_group3)
        hbox2.addLayout(Vbox2)


        vbox = QVBoxLayout()

        # self.tableWidget.resizeColumnsToContents()
        vbox.addWidget(self.tableWidget)
        vbox.addWidget(self.label)
        vbox.addLayout(hbox7)
        vbox.addLayout(hbox2)
        self.setLayout(vbox)

    def temporary_all_pause_game(self):
        # change_ready_main = True
        # change_ready_step = True
        print("game_Playing(self): temporary_pause_game")
        # self.game.isCheck = False
        # self.game.quit()
        # self.game.wait(3000)
        # self.temporary_pause_background()
    def temporary_pause_background(self):

        print("game_Playing(self): temporary_pause_background")

    def temporary_pause_game(self):

        print("game_Playing(self): temporary_pause_game")
        # self.game.isCheck = False
        # self.game.quit()
        # self.game.wait(3000)
        time.sleep(5)


    def again_restart_game(self):
        # change_ready_main = False
        # change_ready_step = False

        print("업데이트 후 재시작")
        # git pull 실행 부분
        my_repo = git.Repo()
        my_repo.remotes.origin.pull()
        # 실행 후 재시작 부분
        os.execl(sys.executable, sys.executable, *sys.argv)

        # self.game.isCheck = True
        # self.game.start()
        # self.again_restart_background()
    def again_restart_background(self):


        print("game_Playing(self): again_restart_background")




    def onActivated_character(self, text):
        global onCharacter
        if text != 0 and text != '캐릭터 선택':
            onCharacter = text
            print('onCharacter', onCharacter)
        else:
            onCharacter = 0
            print("캐릭터를 선택해 주세요.")

    def onActivated_time(self, text):
        global onRefresh_time
        if text != 0 and text != '시간 선택':
            onRefresh_time = text
            print('onRefresh_time : ', onRefresh_time)
        else:
            onRefresh_time = 6
            print("시간을 선택해 주세요.")

    def onActivated_dunjeon(self, text):
        global onDunjeon
        if text != 0 and text != '던전 선택':
            onDunjeon = text
            print('onDunjeon', onDunjeon)
        else:
            onDunjeon = 'none'
            print("던전을 선택해 주세요.")

    def onActivated_dunjeon_level(self, text):
        global onDunjeon_level
        if text != 0 and text != '층수 선택':
            onDunjeon_level = text
            print('onDunjeon_level', onDunjeon_level)
        else:
            onDunjeon_level = 'none'
            print("던전 층수를 선택해 주세요.")

    def onActivated_hunt(self, text):
        global onHunt
        if text != 0 and text != '자동 사냥터 선택':
            onHunt = text
            print('onHunt', onHunt)
        else:
            onHunt = 'none'
            pyautogui.alert(button='넵', text='사냥터를 선택해 주시지예', title='뭐합니꺼')
            print("자동 사냥터를 선택해 주세요.")
    def onActivated_maul(self, text):
        global onMaul
        if text != 0 and text != '마을 의뢰 장소 선택':
            onMaul = text
            print('onMaul', onMaul)
        else:
            onMaul = 'none'
            pyautogui.alert(button='넵', text='마을 의뢰 장소를 선택해 주시지예', title='뭐합니꺼')
            print("마을 의뢰 장소를 선택해 주세요.")

    def onActivated_re_time(self):
        global onRefresh_time
        if onRefresh_time == '시간 선택' or onRefresh_time == 'none':
            # pyautogui.alert(button='넵', text='던전을 선택해 주시지예', title='아 진짜 뭐합니꺼')
            reply = QMessageBox.question(self, '던전을 선택해 주시지예', '아 진짜 뭐합니꺼?',
                                         QMessageBox.Yes, QMessageBox.NoButton)


        else:
            print('onRefresh_time', onRefresh_time)
            dir_path = "C:\\my_games\\coobcco2"
            file_path13 = dir_path + "\\odin_schedule\\refresh_time.txt"
            isRefresh = False
            while isRefresh is False:
                if os.path.isfile(file_path13) == True:
                    with open(file_path13, "w", encoding='utf-8-sig') as file:
                        file.write(onRefresh_time)
                    with open(file_path13, "r", encoding='utf-8-sig') as file:
                        isRefresh = True
                        refresh_time = file.read()
                        print("저장된 초기화 시간", onRefresh_time)
                else:
                    with open(file_path13, "w", encoding='utf-8-sig') as file:
                        file.write(onRefresh_time)

    def onActivated_dunjeon_add(self):
        global onCharacter, onDunjeon, onDunjeon_level
        char_ = onCharacter
        dun_ = str(onDunjeon) + "_" + str(onDunjeon_level)
        if onCharacter == 0:
            pyautogui.alert(button='넵', text='캐릭터를 선택해 주시지예', title='뭐합니꺼')
        elif onDunjeon == '던전 선택' or onDunjeon == 'none' or onDunjeon_level == 0 or onDunjeon_level == '층수 선택':
            pyautogui.alert(button='넵', text='던전 및 층수를 선택해 주시지예', title='아 진짜 뭐합니꺼')
        elif onCharacter != 0 and onDunjeon != '던전 선택':
            print('char_', char_)
            print('dun_', dun_)
            data = "One:" + char_ + ":" + dun_ + ":대기중:" + "Two:" + char_ + ":" + dun_ + ":대기중\n"
            print(data)
            self.onActivated_dunjeon_add2(data)
        #     result = self.mySchedule_add(data)
        # if result == True:
        #     # self.set_rand_int()
        #     self.__init__()

    def onActivated_dunjeon_add2(self, data):
        global onCharacter, onDunjeon, rowcount, colcount
        print("rowcount", rowcount)
        print("colcount", colcount)
        self.table_load()


        print("data", data)
        # self.tableWidget.removeRow(5)
        self.tableWidget.insertRow(self.tableWidget.rowCount())
        row_add = self.tableWidget.rowCount() - 1
        data_ = re.sub("\n", "", data)
        datas = data_.split(":")
        # datas = dataed.replace("\n", "")
        print("datas", datas)
        print("datas", datas[0])
        print(len(datas))
        print(range(colcount))
        for i in range(len(datas)):
            self.tableWidget.setItem(row_add, i, QTableWidgetItem(datas[i]))
        self.mySchedule_add(data)
        rowcount = self.tableWidget.rowCount()


    def onActivated_hunt_add(self):
        global onCharacter, onHunt
        char_ = onCharacter
        hun_ = onHunt
        if onCharacter == 0:
            pyautogui.alert(button='넵', text='캐릭터를 선택해 주시지예', title='뭐합니꺼')
        elif onHunt == '자동 사냥터 선택' or onHunt == 'none':
            pyautogui.alert(button='넵', text='던전을 선택해 주시지예', title='뭐합니꺼')
        elif onCharacter != 0 and onHunt != '던전 선택':
            print('char_', char_)
            print('dun_', hun_)
            data = "One:" + char_ + ":" + hun_ + ":대기중:" + "Two:" + char_ + ":" + hun_ + ":대기중\n"
            print(data)
            self.onActivated_hunt_add2(data)
        #     result = self.mySchedule_add(data)
        # if result == True:
        #     self.set_rand_int()


    def onActivated_hunt_add2(self, data):
        global onCharacter, onDunjeon, rowcount, colcount
        print("rowcount", rowcount)
        print("colcount", colcount)
        self.table_load()


        print("data", data)
        # self.tableWidget.removeRow(5)
        self.tableWidget.insertRow(self.tableWidget.rowCount())
        row_add = self.tableWidget.rowCount() - 1
        data_ = re.sub("\n", "", data)
        datas = data_.split(":")
        # datas = dataed.replace("\n", "")
        print("datas", datas)
        print("datas", datas[0])
        print(len(datas))
        print(range(colcount))
        for i in range(len(datas)):
            self.tableWidget.setItem(row_add, i, QTableWidgetItem(datas[i]))
            self.tableWidget.item(row_add, i).setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.mySchedule_add(data)
        rowcount = self.tableWidget.rowCount()

    def onActivated_maul_add(self):
        global onCharacter, onMaul
        char_ = onCharacter
        maul_ = onMaul
        if onCharacter == 0:
            pyautogui.alert(button='넵', text='캐릭터를 선택해 주시지예', title='뭐합니꺼')
        elif onMaul == '마을 의뢰 장소 선택' or onMaul == 'none':
            pyautogui.alert(button='넵', text='마을 의뢰 장소를 선택해 주시지예', title='아 진짜 뭐합니꺼')
        elif onCharacter != 0 and onMaul != '마을 의뢰 장소 선택':
            print('char_', char_)
            print('maul_', maul_)
            data = "One:" + char_ + ":" + maul_ + ":대기중:" + "Two:" + char_ + ":" + maul_ + ":대기중\n"
            print(data)
            self.onActivated_maul_add2(data)
        #     result = self.mySchedule_add(data)
        # if result == True:
        #     # self.set_rand_int()
        #     self.__init__()

    def onActivated_maul_add2(self, data):
        global onCharacter, onMaul, rowcount, colcount
        print("rowcount", rowcount)
        print("colcount", colcount)
        self.table_load()


        print("data", data)
        # self.tableWidget.removeRow(5)
        self.tableWidget.insertRow(self.tableWidget.rowCount())
        row_add = self.tableWidget.rowCount() - 1
        data_ = re.sub("\n", "", data)
        datas = data_.split(":")
        # datas = dataed.replace("\n", "")
        print("datas", datas)
        print("datas", datas[0])
        print(len(datas))
        print(range(colcount))
        for i in range(len(datas)):
            self.tableWidget.setItem(row_add, i, QTableWidgetItem(datas[i]))
        self.mySchedule_add(data)
        rowcount = self.tableWidget.rowCount()


    def mystatus_refresh(self):
        print("현재상태 초기화")
        # 초기화 시간
        dir_path = "C:\\my_games\\coobcco2"
        file_path2 = dir_path + "\\odin_schedule\\quest.txt"
        file_path13 = dir_path + "\\odin_schedule\\refresh_time.txt"

        isRefresh = False
        while isRefresh is False:
            if os.path.isfile(file_path13) == True:
                with open(file_path13, "r", encoding='utf-8-sig') as file:
                    isRefresh = True
                    refresh_time = file.read()
                    print("refresh_time", refresh_time)
            else:
                with open(file_path13, "w", encoding='utf-8-sig') as file:
                    file.write(str(6))

        if os.path.isfile(file_path2) == True:
            # 파일 읽기
            with open(file_path2, "r", encoding='utf-8-sig') as file:
                lines2 = file.read().splitlines()
                day_ = lines2[0].split(":")
                re_time_ = str(day_[0]) + " => " + str(day_[1] + "시")
                print("최근 초기화 시간 : ", re_time_)
        else:
            re_time_ = "아직 모름..."
        self.my_refresh_time.setText("현재 초기화 시간 : " + str(refresh_time) + "\n\n" + "최근 초기화한 시간 : " + re_time_)
        self.set_rand_int()


    def set_rand_int(self):
        try:
            dir_path = "C:\\my_games\\coobcco2"
            file_path = dir_path + "\\odin_schedule\\schedule.txt"
            file_path3 = dir_path + "\\odin_schedule\\schedule2.txt"
            if os.path.isfile(file_path) == True:
                # 파일 읽기
                with open(file_path, "r", encoding='utf-8-sig') as file:
                    lines = file.read().splitlines()
            else:
                print('파일 없당')
                if os.path.isdir(dir_path) == True:
                    print('디렉토리 존재함')
                    with open(file_path3, "r", encoding='utf-8-sig') as file:
                        shcedule = file.read().splitlines()
                        with open(file_path, "w", encoding='utf-8-sig') as file:
                            file.write(str(shcedule))
                            with open(file_path, "r", encoding='utf-8-sig') as file:
                                lines = file.read().splitlines()
                else:
                    print('디렉토리 존재하지 않음')
                    os.makedirs(dir_path)
                    with open(file_path3, "r", encoding='utf-8-sig') as file:
                        shcedule = file.read().splitlines()
                        with open(file_path, "w", encoding='utf-8-sig') as file:
                            file.write(shcedule)
                            with open(file_path, "r", encoding='utf-8-sig') as file:
                                lines = file.read().splitlines()

            # self.tableWidget.insertRow(self.tableWidget.rowCount(2))
            self.tableWidget.setColumnWidth(0, 50)
            self.tableWidget.setColumnWidth(1, 40)
            self.tableWidget.setColumnWidth(2, 200)
            self.tableWidget.setColumnWidth(3, 100)
            self.tableWidget.setColumnWidth(4, 50)
            self.tableWidget.setColumnWidth(5, 40)
            self.tableWidget.setColumnWidth(6, 200)
            self.tableWidget.setColumnWidth(7, 100)

            for i in range(len(lines)):
                result = str(lines[i]).split(":")
                for j in range(len(result)):
                    self.tableWidget.setItem(i, j, QTableWidgetItem())
                    self.tableWidget.item(i, j).setText(str(result[j].replace("\n", "")))
                    self.tableWidget.item(i, j).setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                    # self.tableWidget.resizeColumnsToContents()

        except Exception as e:
            print(e)
            return 0

    def set_rand_int_jinhang(self, cla):
        try:
            dir_path = "C:\\my_games\\coobcco2"
            file_path = dir_path + "\\odin_schedule\\schedule.txt"
            file_path3 = dir_path + "\\odin_schedule\\schedule2.txt"
            if os.path.isfile(file_path) == True:
                # 파일 읽기
                with open(file_path, "r", encoding='utf-8-sig') as file:
                    lines = file.read().splitlines()
                    print("lines", lines)
                    print("len(lines)", len(lines))
            else:
                print('파일 없당')
                if os.path.isdir(dir_path) == True:
                    print('디렉토리 존재함')
                    with open(file_path3, "r", encoding='utf-8-sig') as file:
                        shcedule = file.read().splitlines()
                        with open(file_path, "w", encoding='utf-8-sig') as file:
                            file.write(shcedule)
                            with open(file_path, "r", encoding='utf-8-sig') as file:
                                lines = file.read().splitlines()
                else:
                    print('디렉토리 존재하지 않음')
                    os.makedirs(dir_path)
                    with open(file_path3, "r", encoding='utf-8-sig') as file:
                        shcedule = file.read().splitlines()
                        with open(file_path, "w", encoding='utf-8-sig') as file:
                            file.write(shcedule)
                            with open(file_path, "r", encoding='utf-8-sig') as file:
                                lines = file.read().splitlines()

            ########################################
            cla_schedule = ""
            for i in range(len(lines)):
                complete_ = lines[i].split(":")
                for j in range(len(complete_)):
                    if cla == 'one':
                        if j < 3:
                            cla_schedule += complete_[j] + ":"
                        if j == 3:
                            cla_schedule += complete_[3] + "\n"
                    if cla == 'two':
                        if 3 < j < 7:
                            cla_schedule += complete_[j] + ":"
                        if j == 7:
                            cla_schedule += complete_[7] + "\n"
            # 시작 스케쥴 파악하기
            forBreak = False
            schedule_ = cla_schedule.split("\n")
            schedule_ = ' '.join(schedule_).split()
            print("schedule_", schedule_)
            for i in range(len(schedule_)):
                schedule_2 = schedule_[i].split(":")
                for j in range(len(schedule_2)):
                    if schedule_2[3] != "완료":
                        forBreak = True
                        print("대기중인 첫번째", i)
                        start_ = i
                        break
                if forBreak == True:
                    break
            print("진행중인 줄", start_)
            start = schedule_[start_].split(":")
            start = ' '.join(start).split()
            print("start[3]! 대기중을 진행중으로 보이게 하기", start[3])
            # start_ 줄(i), 진행중 (start[3])

            cla_schedule = ""
            for i in range(len(lines)):
                complete_ = lines[i].split(":")
                for j in range(len(complete_)):
                    if cla == 'one' and i == start_ and j == 3:
                        cla_schedule += complete_[j].replace("대기중", "진행중:")
                    elif cla == 'two' and i == start_ and j == 7:
                        cla_schedule += complete_[j].replace("대기중", "진행중\n")
                    else:
                        if j == 7:
                            cla_schedule += complete_[j] + "\n"
                        else:
                            cla_schedule += complete_[j] + ":"
            print("cla_schedule", cla_schedule)
            mycla_schedule = cla_schedule.split('\n')
            mycla_schedule = ' '.join(mycla_schedule).split()
            print("mycla_schedule", mycla_schedule)

            remove_ = self.tableWidget.rowCount()
            print("remove_", remove_)
            for i in range(remove_ - 1):
                self.tableWidget.removeRow(0)

            rowcount = self.tableWidget.rowCount()
            print("refresh_rowcount", self.tableWidget.rowCount())
            count_ = len(mycla_schedule) - rowcount
            for i in range(count_):
                self.tableWidget.insertRow(self.tableWidget.rowCount())
            print("refresh_rowcount2", self.tableWidget.rowCount())

            # self.tableWidget.clear

            # self.tableWidget.insertRow(self.tableWidget.rowCount(2))

            # self.tableWidget.setColumnWidth(0, 50)
            # self.tableWidget.setColumnWidth(1, 40)
            # self.tableWidget.setColumnWidth(2, 200)
            # self.tableWidget.setColumnWidth(3, 100)
            # self.tableWidget.setColumnWidth(4, 50)
            # self.tableWidget.setColumnWidth(5, 40)
            # self.tableWidget.setColumnWidth(6, 200)
            # self.tableWidget.setColumnWidth(7, 100)

            for i in range(len(mycla_schedule)):
                result = str(mycla_schedule[i]).split(":")
                for j in range(len(result)):
                    self.tableWidget.setItem(i, j, QTableWidgetItem())
                    self.tableWidget.item(i, j).setText(str(result[j]))
                    self.tableWidget.item(i, j).setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
            # time.sleep(0.2)
            self.tableWidget.clear


        except Exception as e:
            print(e)
            return 0

    def set_label(self, row, column):
        global thisRow, thisCol
        item = self.tableWidget.item(row, column)
        value = item.text()
        col = str(row + 1)
        col_ = int(col)
        col2 = str(column + 1)
        col_2 = int(col2)
        thisRow = col_
        thisCol = col_2
        print("0열 데이타", col_)   # good
        print("Row", str(row+1))
        print("Column", str(column+1))
        print("value", str(value))
        label_str = 'Row: ' + str(row+1) + ', Column: ' + str(column+1) + ', Value: ' + str(value)
        self.label.setText(label_str)


# 스케쥴 수정 및 추가
    def sche_load_(self):
        global table_datas
        try:
            rowcount = self.tableWidget.rowCount()
            print("schedule!!!")
            datas = ""
            if rowcount != 0:
                for i in range(0, rowcount):
                    for j in range(0, colcount):
                        data = self.tableWidget.item(i, j)
                        if data is not None:
                            if j + 1 == colcount:
                                datas += str(data.text()) + "\n"
                            else:
                                datas += str(data.text()) + ":"

                        else:
                            print("blank")
            # redata = ' '.join(datas).split()
            table_datas = datas
            return table_datas
        except Exception as e:
                print(e)
                return 0

    def table_load(self):
        global rowcount, colcount
        print("rowcount", rowcount)
        print("colcount", colcount)
        if rowcount != 0:
            for i in range(0, rowcount):
                for j in range(0, colcount):
                    data = self.tableWidget.item(i, j)
                    if data is not None:
                        if j + 1 == colcount:
                            item = QTableWidgetItem()
                            item.setText(str(data.text()))
                            # datas += str(data.text()) + "\n"
                            self.tableWidget.setItem(i, j, item)
                        else:
                            item = QTableWidgetItem()
                            item.setText(str(data.text()))
                            # datas += str(data.text()) + ":"
                            self.tableWidget.setItem(i, j, item)

                    else:
                        print("blank")



    def sche_up_modify(self):
        global thisRow, thisCol, rowcount
        try:
            rowcount = self.tableWidget.rowCount()
            last_1 = ""
            last_2 = ""
            last_result = ""
            modi_result = ""
            print("sche_up_modify", thisRow)
            result_ = self.sche_load_()
            modi_ready__ = result_.split("\n")
            modi_ready_ = " ".join(modi_ready__).split()
            if thisRow > 1:
                print("len(modi_ready_up)", len(modi_ready_))
                for i in range(len(modi_ready_)):

                    # if i + 1 == len(modi_ready_):
                    #     modi_result += modi_ready_[i]

                    if i == thisRow - 2:
                        modi_result += modi_ready_[i+1] + "\n"

                    elif i == thisRow - 1:
                        modi_result += modi_ready_[i-1] + "\n"

                    else:
                        modi_result += modi_ready_[i] + "\n"



                modi_result__ = modi_result.split("\n")
                print("modi_ready__!!!!!!!!!!!!!", modi_ready__)
                print("modi_result__!!!!!!!!!!!", modi_result__)

                modi_spl_1 = modi_ready_[thisRow - 2].split(":")  # 바뀌기전 5678 => 그대로
                modi_spl_2 = modi_ready_[thisRow - 1].split(":")  # 바뀌기전 5678 => 그대로

                modi_spl_3 = modi_result__[thisRow - 2].split(":")  # 바뀐 후 1234 => 바꾸기 b
                modi_spl_4 = modi_result__[thisRow - 1].split(":")  # 바뀐후 1234 => 바꾸기 a

                #      4번기준
                #      thisRow - 2
                #      modi_spl_3 + modi_spl_2
                #      thisRow - 1
                #      modi_spl_1 + modi_spl_4
                # else:
                #     thisRow - 2
                #     modi_spl_1 + modi_spl_4
                #     thisRow - 1
                #     modi_spl_3 + modi_spl_2##################나중에 마지막줄을 올릴때 잘못 처리되는거 수정하기

                if thisCol < 5:

                    last_1 = str(modi_spl_3[0]) + ":" + str(modi_spl_3[1]) + ":" + str(modi_spl_3[2]) + ":" + str(modi_spl_3[3]) + ":" + str(modi_spl_1[4]) + ":" + str(modi_spl_1[5]) + ":" + str(modi_spl_1[6]) + ":" + str(modi_spl_1[7])
                    last_2 = str(modi_spl_4[0]) + ":" + str(modi_spl_4[1]) + ":" + str(modi_spl_4[2]) + ":" + str(modi_spl_4[3]) + ":" + str(modi_spl_2[4]) + ":" + str(modi_spl_2[5]) + ":" + str(modi_spl_2[6]) + ":" + str(modi_spl_2[7])
                else:

                    last_1 = str(modi_spl_1[0]) + ":" + str(modi_spl_1[1]) + ":" + str(modi_spl_1[2]) + ":" + str(modi_spl_1[3]) + ":" + str(modi_spl_3[4]) + ":" + str(modi_spl_3[5]) + ":" + str(modi_spl_3[6]) + ":" + str(modi_spl_3[7])
                    last_2 = str(modi_spl_2[0]) + ":" + str(modi_spl_2[1]) + ":" + str(modi_spl_2[2]) + ":" + str(modi_spl_2[3]) + ":" + str(modi_spl_4[4]) + ":" + str(modi_spl_4[5]) + ":" + str(modi_spl_4[6]) + ":" + str(modi_spl_4[7])

                for i in range(len(modi_result__)):
                    print("last_result", modi_result__[i])
                    # if i == len(modi_result__) - 1:
                    #     last_result += str(modi_result__[i]) + 'a'
                    #     # last_result += str(i) + str(modi_result__[i])
                    #     print("i", i)
                    if thisRow - 1 == i:
                       last_result += last_2 + "\n"
                    elif thisRow - 2 == i:
                       last_result += last_1 + "\n"
                    elif i == len(modi_result__) - 1:
                        last_result += str(modi_result__[i]) + ''
                        # last_result += str(i) + str(modi_result__[i])
                        print("i", i)
                    else:
                       last_result += str(modi_result__[i]) + "\n"

                print("last_result_up", last_result)
                how_ = 'modify'
                modi_result_ = self.mySchedule_change(how_, last_result)

                if modi_result_ == True:
                    thisRow -= 1
                    self.set_rand_int()
                else:
                    print("수정 실패")


            else:
                pyautogui.alert(button='넵', text='수정할 행을 선택해 주세요', title='확인해주이소')
                print("수정할 행을 선택해 주세요. 추후 알러트로...")

        #      4번기준
        #      thisRow - 2
        #      modi_spl_3 + modi_spl_2
        #      thisRow - 1
        #      modi_spl_1 + modi_spl_4
        # else:
        #     thisRow - 2
        #     modi_spl_1 + modi_spl_4
        #     thisRow - 1
        #     modi_spl_3 + modi_spl_2

        except Exception as e:
                print(e)
                return 0

    def sche_down_modify(self):
        global thisRow, thisCol, rowcount
        try:
            rowcount = self.tableWidget.rowCount()
            last_1 = ""
            last_2 = ""
            last_result = ""
            modi_result = ""
            print("sche_down_modify", thisRow)
            result_ = self.sche_load_()
            modi_ready__ = result_.split("\n")
            modi_ready_ = " ".join(modi_ready__).split()
            if thisRow < len(modi_ready_) :
                print("len(modi_ready_down)", len(modi_ready_))
                for i in range(len(modi_ready_)):

                    # if i + 1 == len(modi_ready_):
                    #     modi_result += modi_ready_[i]
                    if thisRow == i:
                        modi_result += modi_ready_[i - 1] + "\n"
                    elif thisRow - 1 == i:
                        modi_result += modi_ready_[i + 1] + "\n"
                    else:
                        modi_result += modi_ready_[i] + "\n"

                modi_result__ = modi_result.split("\n")

                modi_spl_1 = modi_ready_[thisRow-1].split(":")  # 바뀌기전 1234 => 바꾸기
                modi_spl_2 = modi_ready_[thisRow].split(":")  # 바뀌기전 5678 => 그대로
                modi_spl_3 = modi_result__[thisRow - 1].split(":") # 바뀐 후 1234 => 바꾸기
                modi_spl_4 = modi_result__[thisRow].split(":") # 바뀐후 5678 => 그대로

                if thisCol < 5:

                    last_1 = str(modi_spl_3[0]) + ":" + str(modi_spl_3[1]) + ":" + str(modi_spl_3[2]) + ":" + str(modi_spl_3[3]) + ":" + str(modi_spl_1[4]) + ":" + str(modi_spl_1[5]) + ":" + str(modi_spl_1[6]) + ":" + str(modi_spl_1[7])
                    last_2 = str(modi_spl_4[0]) + ":" + str(modi_spl_4[1]) + ":" + str(modi_spl_4[2]) + ":" + str(modi_spl_4[3]) + ":" + str(modi_spl_2[4]) + ":" + str(modi_spl_2[5]) + ":" + str(modi_spl_2[6]) + ":" + str(modi_spl_2[7])
                else:

                    last_1 = str(modi_spl_1[0]) + ":" + str(modi_spl_1[1]) + ":" + str(modi_spl_1[2]) + ":" + str(modi_spl_1[3]) + ":" + str(modi_spl_3[4]) + ":" + str(modi_spl_3[5]) + ":" + str(modi_spl_3[6]) + ":" + str(modi_spl_3[7])
                    last_2 = str(modi_spl_2[0]) + ":" + str(modi_spl_2[1]) + ":" + str(modi_spl_2[2]) + ":" + str(modi_spl_2[3]) + ":" + str(modi_spl_4[4]) + ":" + str(modi_spl_4[5]) + ":" + str(modi_spl_4[6]) + ":" + str(modi_spl_4[7])

                for i in range(len(modi_result__)):

                    if i + 1 == len(modi_result__):
                        last_result += str(modi_result__[i])
                    elif thisRow - 1 == i:
                       last_result += last_1 + "\n"
                    elif thisRow == i:
                       last_result += last_2 + "\n"
                    else:
                       last_result += str(modi_result__[i]) + "\n"


                print("last_result_down", last_result)
                how_ = 'modify'
                modi_result_ = self.mySchedule_change(how_, last_result)
                if modi_result_ == True:
                    thisRow += 1
                    self.set_rand_int()
                else:
                    print("수정 실패")

            else:
                pyautogui.alert(button='넵', text='수정할 행을 선택해 주세요', title='확인해주이소')
                print("수정할 행을 선택해 주세요. 추후 알러트로...")

        except Exception as e:
            print(e)
            return 0


    def mySchedule_del(self):
        global rowcount, colcount
        try:
            self.table_load()
            rowcount = self.tableWidget.rowCount()
            print("rowcount", rowcount)
            self.tableWidget.removeRow(thisRow-1)
            rowcount = self.tableWidget.rowCount()
            print("rowcount", rowcount)
            print("del")
            result = self.sche_load_()
            print("result", result)
            how_ = "modify"
            self.mySchedule_change(how_, result)
            self.mystatus_refresh()

        except Exception as e:
            print(e)
            return 0


    def mySchedule_refresh(self):
        try:
            ##############다시 코딩

            v_.one_cla_count = 0
            v_.two_cla_count = 0
            v_.one_cla_ing = 'check'
            v_.two_cla_ing = 'check'
            v_.one_cla_get_event = True
            v_.two_cla_get_event = True

            myQuest_number_check('all', 'refresh')


            dir_path = "C:\\my_games\\coobcco2"
            file_path = dir_path + "\\odin_schedule\\schedule.txt"
            file_path2 = dir_path + "\\odin_schedule\\quest.txt"
            file_path3 = dir_path + "\\odin_schedule\\schedule2.txt"
            file_path13 = dir_path + "\\odin_schedule\\refresh_time.txt"

            if os.path.isdir(dir_path) == False:
                print('디렉토리 존재하지 않음')
                os.makedirs(dir_path)

            isRefresh = False
            while isRefresh is False:
                if os.path.isfile(file_path13) == True:
                    with open(file_path13, "r", encoding='utf-8-sig') as file:
                        isRefresh = True
                        refresh_time = file.read()
                        print("refresh_time", refresh_time)
                else:
                    with open(file_path13, "w", encoding='utf-8-sig') as file:
                        file.write(str(6))

            with open(file_path3, "r", encoding='utf-8-sig') as file:
                lines = file.read()
                # lines = file.read().splitlines()
                print('line_refresh', lines)
            with open(file_path, "w", encoding='utf-8-sig') as file:
                file.write(lines)

            nowDay_ = datetime.today().strftime("%Y%m%d")
            nowDay = int(nowDay_)
            nowTime = int(datetime.today().strftime("%H"))
            yesterday_ = date.today() - timedelta(1)
            yesterday = int(yesterday_.strftime('%Y%m%d'))

            if nowTime >= int(refresh_time):
                nowDay = str(nowDay)
            else:
                nowDay = yesterday
                nowDay = str(nowDay)
            with open(file_path2, "w", encoding='utf-8-sig') as file:
                file.write(str(nowDay) + ":" + str(refresh_time) + "\n")


            remove_ = self.tableWidget.rowCount()
            print("remove_", remove_)
            for i in range(remove_-1):
                self.tableWidget.removeRow(0)



            refresh_result = lines.split("\n")
            rowcount = self.tableWidget.rowCount()
            print("refresh_rowcount", self.tableWidget.rowCount())
            count_ = len(refresh_result) - rowcount - 1
            for i in range(count_):
                self.tableWidget.insertRow(self.tableWidget.rowCount())
            print("refresh_rowcount2", self.tableWidget.rowCount())
            self.set_rand_int()

        except Exception as e:
            print(e)
            return 0

    def mySchedule_is(self):
        try:
            ##############다시 코딩
            dir_path = "C:\\my_games\\coobcco2"
            file_path = dir_path + "\\odin_schedule\\schedule.txt"
            if os.path.isfile(file_path) == True:
                # 파일 읽기
                with open(file_path, "r", encoding='utf-8-sig') as file:
                    lines = file.read()



            remove_ = self.tableWidget.rowCount()
            print("remove_", remove_)
            for i in range(remove_-1):
                self.tableWidget.removeRow(0)



            refresh_result = lines.split("\n")
            rowcount = self.tableWidget.rowCount()
            print("refresh_rowcount", self.tableWidget.rowCount())
            count_ = len(refresh_result) - rowcount - 1
            for i in range(count_):
                self.tableWidget.insertRow(self.tableWidget.rowCount())
            print("refresh_rowcount2", self.tableWidget.rowCount())
            self.tableWidget.clear
            self.set_rand_int()
            self.tableWidget.clear
        except Exception as e:
            print(e)
            return 0

    def mySchedule_add(self, data):
        try:
            schedule_add = False
            how_ = 'add'
            datas = str(data)
            result = self.mySchedule_change(how_, datas)
            print("added_", result)
            if result == True:
                schedule_add = True
                self.mystatus_refresh()
                print('스케쥴 추가 됨')

            return schedule_add
        except Exception as e:
            print(e)
            return 0

    def mySchedule_change(self, how_, datas):
        try:
            ishow_ = False
            dir_path = "C:\\my_games\\coobcco2"
            file_path = dir_path + "\\odin_schedule\\schedule.txt"
            file_path3 = dir_path + "\\odin_schedule\\schedule2.txt"
            print(os.path.isfile(file_path))
            print(os.path.isdir(dir_path))

            if os.path.isdir(dir_path) == True:
                print('디렉토리 존재')
            else:
                os.makedirs(dir_path)

            print("how_", how_)
            if how_ == "add":
                with open(file_path, "a", encoding='utf-8-sig') as file:
                    file.write(datas)
                    ishow_ = True
                    reset_schedule_ = ""
                    with open(file_path, "r", encoding='utf-8-sig') as file:
                        lines = file.read().splitlines()
                        lines = ' '.join(lines).split()
                        print("lineslineslineslineslineslineslineslineslineslineslines", lines)
                        for i in range(len(lines)):
                            complete_ = lines[i].split(":")
                            for j in range(len(complete_)):
                                if j < 3:
                                    reset_schedule_ += complete_[j] + ":"
                                if j == 3:
                                    reset_schedule_ += '대기중:'
                                if 3 < j < 7:
                                    reset_schedule_ += complete_[j] + ":"
                                if j == 7:
                                    reset_schedule_ += "대기중\n"
                        print("reset_schedule_reset_schedule_reset_schedule_reset_schedule_reset_schedule_", reset_schedule_)
                        with open(file_path3, "w", encoding='utf-8-sig') as file:
                            file.write(reset_schedule_)
                    self.set_rand_int()

            elif how_ == "modify":

                with open(file_path, "w", encoding='utf-8-sig') as file:
                    file.write(datas)
                    ishow_ = True
                    reset_schedule_ = ""
                    lines = datas
                    lines = lines.split('\n')
                    lines = ' '.join(lines).split()
                    for i in range(len(lines)):
                        complete_ = lines[i].split(":")
                        for j in range(len(complete_)):
                            if j < 3:
                                reset_schedule_ += complete_[j] + ":"
                            if j == 3:
                                reset_schedule_ += '대기중:'
                            if 3 < j < 7:
                                reset_schedule_ += complete_[j] + ":"
                            if j == 7:
                                reset_schedule_ += "대기중\n"

                    with open(file_path3, "w", encoding='utf-8-sig') as file:
                        file.write(reset_schedule_)
                    self.set_rand_int()






            return ishow_
        except Exception as e:
            print(e)
            return 0




    def mySchedule_start1(self):
        try:
            v_.global_howcla = 'onecla'
            m_ = Monitoring(self)
            m_.start()

            self.sche_add1.setText("one 실행중")
            self.sche_add2.setText("two")
            self.sche_add1.setDisabled(True)
            self.sche_add2.setDisabled(True)

            time.sleep(0.3)
            start_onecla = game_Playing_onecla(self)
            start_onecla.start()

        except Exception as e:
            print(e)
            return 0
    def mySchedule_start2(self):
        try:
            v_.global_howcla = 'onecla'
            m_ = Monitoring(self)
            m_.start()

            self.sche_add1.setText("one")
            self.sche_add2.setText("two 실행중")
            self.sche_add1.setDisabled(True)
            self.sche_add2.setDisabled(True)

            time.sleep(0.3)
            start_twocla = game_Playing_twocla(self)
            start_twocla.start()

        except Exception as e:
            print(e)
            return 0

    def hello2(self):
        print("hello!!!!!!!!!!")

    def mytestin_(self):
        try:
            x = Test_check(self)
            x.start()
        except Exception as e:
            print(e)
            return 0



    # def keyPressEvent(self, e):
    #     if e.key() == Qt.Key_Escape:
    #         self.close()
    #     elif e.key() == Qt.Key_F:
    #         self.showFullScreen()
    #     elif e.key() == Qt.Key_N:
    #         self.showNormal()

###########BackGround(백그라운드) 관련############################nowtest



class BackGroundPotion(QThread):
    #parent = MainWidget을 상속 받음.
    def __init__(self):
        super().__init__()
        self.potion_back_ = True
    def run(self):
        # global change_ready_step, change_ready_main
        try:
            data = 'none'
            # 추후
            # print("BackGroundPotion(QThread): go")
            while self.potion_back_ is True:
                # if change_ready_step == False:
                #     print("(background)1", now_cla)
                #     time.sleep(3)
                #     print("(background)2", now_cla)
                #     time.sleep(3)
                #     print("(background)3", now_cla)
                #     time.sleep(3)
                #     print("(background)4", now_cla)
                #     time.sleep(3)

                if v_.change_ready_step == False:
                    if v_.now_cla != 'none' and v_.global_howcla == 'onetwocla':

                        if v_.now_cla == 'one':
                            data = 'two'
                            cla_ing_ = v_.two_cla_ing
                        if v_.now_cla == 'two':
                            data = 'one'
                            cla_ing_ = v_.one_cla_ing
                        cla = data



                        # 꺼졌을 경우 재 로그인
                        go_alrim_confirm(data, "BackGroundPotion")

                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\odin.png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(0, 0, 60, 30, data, img)
                        if imgs_ is not None and imgs_ != False:
                            print("오딘 백그라운드 " + str(data) + "클라 켜져있음  ^ㅅ^")



                            # 절전모드 해제


                            # 던전 일 경우
                            if cla_ing_ == 'gonghu' or cla_ing_ == 'nanjang' or cla_ing_ == 'underprison':
                                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<백그라운드 Potion 테스트중입니당>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", data)
                                lotation_change_ready(cla, 'BackGroundPotion')
                                result_ = now_hunting_is('백그라운드 바위해안', data)
                                # chango4 = go_chango(data, 'village')
                                if result_ == False:
                                    chango4 = go_chango(data, 'village')
                                    if chango4 == False:
                                        click_pos_2(586, 986, data)
                                        time.sleep(random_int())
                                        now_hunting_is('백그라운드 ', data)
                                    else:
                                        jadong_cla_ready(data, '바위해안')

                                # 가방 꽉 찼을 경우 분해하기
                                boonhae_ready = False
                                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\full_mybag_1.png"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set(820, 30, 885, 80, data, img)
                                if imgs_ is None or imgs_ == False:
                                    print("full_mybag_1 안보여")
                                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\full_mybag_2.png"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set(820, 30, 885, 80, data, img)
                                    if imgs_ is None:
                                        print("full_mybag_2 안보여")
                                    else:
                                        print("full_mybag_2 보여", imgs_)
                                        boonhae_ready = True
                                else:
                                    print("full_mybag_1 보여", imgs_)
                                    boonhae_ready = True

                                if boonhae_ready == True:
                                    go_boonhae(data, "BackGroundPotion")


                                # 물약 체크하기
                                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\gabang.png"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set(30, 40, 100, 75, data, img)
                                if imgs_ is None or imgs_ == False:
                                    background_myPotion_check(data)
                                else:
                                    click_pos_2(920, 55, data)
                                    time.sleep(random_int())
                                    background_myPotion_check(data)
                                # 줍줍
                                go_collection_on(data)
                            elif cla_ing_ == 'maul':
                                lotation_change_ready(cla, 'BackGroundPotion')
                                # 물약 체크하기
                                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\gabang.png"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set(30, 40, 100, 75, data, img)
                                if imgs_ is None or imgs_ == False:
                                    background_myPotion_check(data)
                                else:
                                    click_pos_2(920, 55, data)
                                    time.sleep(random_int())
                                    background_myPotion_check(data)
                                # 줍줍
                                go_collection_on(data)
                            elif cla_ing_ == 'jadong':
                                lotation_change_ready(cla, 'BackGroundPotion')
                                now_hunting_is('background', data)
                                dead_die(data, "BackGroundPotion => elif cla_ing_ == 'jadong':")
                                # 가방 꽉 찼을 경우 분해하기
                                boonhae_ready = False
                                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\full_mybag_1.png"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set(820, 30, 885, 80, data, img)
                                if imgs_ is None or imgs_ == False:
                                    print("full_mybag_1 안보여")
                                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\full_mybag_2.png"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set(820, 30, 885, 80, data, img)
                                    if imgs_ is None:
                                        print("full_mybag_2 안보여")
                                    else:
                                        print("full_mybag_2 보여", imgs_)
                                        boonhae_ready = True
                                else:
                                    print("full_mybag_1 보여", imgs_)
                                    boonhae_ready = True

                                if boonhae_ready == True:
                                    go_boonhae(data, "BackGroundPotion")
                                # 물약 체크하기
                                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\gabang.png"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set(30, 40, 100, 75, data, img)
                                if imgs_ is None or imgs_ == False:
                                    background_myPotion_check(data)
                                else:
                                    click_pos_2(920, 55, data)
                                    time.sleep(random_int())
                                    background_myPotion_check(data)
                                # 줍줍
                                go_collection_on(data)
                            elif cla_ing_ == 'grow':
                                lotation_change_ready(cla, 'BackGroundPotion')
                                # # 물약 체크하기
                                # full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\gabang.png"
                                # img_array = np.fromfile(full_path, np.uint8)
                                # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                # imgs_ = imgs_set(30, 40, 100, 75, data, img)
                                # if imgs_ is None or imgs_ == False:
                                #     full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\event1.png"
                                #     img_array = np.fromfile(full_path, np.uint8)
                                #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                #     imgs_ = imgs_set(600, 30, 800, 90, cla, img)
                                #     if imgs_ is not None:
                                #         background_myPotion_check(data)
                                # else:
                                #     click_pos_2(920, 55, data)
                                #     time.sleep(random_int())
                                #     full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\event1.png"
                                #     img_array = np.fromfile(full_path, np.uint8)
                                #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                #     imgs_ = imgs_set(600, 30, 800, 90, cla, img)
                                #     if imgs_ is not None:
                                #         background_myPotion_check(data)
                                # 줍줍
                                go_collection_on(data)
                                # 육성
                                if cla == "one":
                                    now_growing_ = v_.one_now_growing_
                                if cla == "two":
                                    now_growing_ = v_.two_now_growing_
                                if now_growing_ == "none":
                                    now_growing_ = "요툰육성"
                                if now_growing_ == "니다육성":
                                    # cla_grow = Grow_()
                                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\event1.png"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set(600, 30, 800, 90, cla, img)
                                    if imgs_ is not None:
                                        # cla_grow.potion_grow(cla, now_growing_)
                                        potion_grow(cla, now_growing_)
                                    else:
                                        clean_screen(cla, "니다육성")
                                    # cla_grow.common_grow(cla)
                                    # cla_grow.nida_grow(cla)
                                    common_grow(cla)
                                    nida_grow(cla)
                                elif now_growing_ == "요툰육성":
                                    # cla_grow = Grow_()
                                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\event1.png"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set(600, 30, 800, 90, cla, img)
                                    if imgs_ is not None:
                                        # cla_grow.potion_grow(cla, now_growing_)
                                        potion_grow(cla, now_growing_)
                                    else:
                                        clean_screen(cla, "요툰육성")
                                    # cla_grow.tuto_grow(cla)
                                    # cla_grow.common_grow(cla)
                                    # cla_grow.yotoon_grow(cla)
                                    tuto_grow(cla)
                                    common_grow(cla)
                                    nida_grow(cla)
                            else:
                                print("해당사항 없으니 쉬자")
                        else:
                            print("오딘 백그라운드 " + str(data) + "클라 꺼져있음  ㅠㅅㅠ")

                            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\odin.png"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set(0, 0, 960, 1030, data, img)
                            if imgs_ is not None and imgs_ != False:
                                print("어라?오딘 백그라운드 " + str(data) + "클라 켜져있음  ^ㅅ^", imgs_)
                                time.sleep(0.3)
                                click_pos_reg(imgs_.x + 100, imgs_.y, data)
                                pyautogui.keyDown('win')
                                if data == 'one':
                                    pyautogui.press('left')
                                elif data == 'two':
                                    pyautogui.press('right')
                                pyautogui.keyUp('win')
                                time.sleep(0.3)
                                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\odin.png"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set(0, 0, 60, 30, data, img)
                                if imgs_ is not None and imgs_ != False:
                                    print("정비 완료  ^ㅅ^", imgs_)
                                    time.sleep(1)
                                    click_pos_reg(imgs_.x + 100, imgs_.y, data)
                                    print("다시 ㄱㄱㄱㄱㄱㄱㄱㄱㄱㄱㄱㄱㄱㄱㄱ")

                            else:
                                print("힝..오딘 백그라운드 " + str(data) + "클라 꺼져있음  ㅠ,.ㅠ")
                                line_to_me(data, "꺼진 것 같다")
                            # 꺼져있을때 켜는거 나중에 다시 점검...
                            # if now_cla != 'none':
                            #     login_starting(data)
                            #     time.sleep(random_int())
                            #     get_cla_count(data)
                            #     time.sleep(random_int())
                            #     dead_die(data, "BackGroundPotion => if now_cla != 'none':")
                            #     go_bag(data, "BackGroundPotion")
                            #     time.sleep(random_int())
                            #     chango_(data, 'after')
                            #     jadong_cla_ready(data, '바위해안')


                print("백그라운드 포션 체크 클라 : ", data)

                if v_.change_ready_main == True:
                    v_.change_ready_main = False
                    print("(background)5", v_.now_cla)
                time.sleep(20)


        except Exception as e:
            print(e)
            return 0



class Test_check(QThread):



    #parent = MainWidget을 상속 받음.
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent



    def run(self):
        # self.parent.hello2()


        v_.now_cla = 'one'
        v_.global_howcla = 'onetwocla'

        cla = v_.now_cla
        if cla == 'one':
            plus = 0
        if cla == 'two':
            plus = 960
        # dunjeon_cla_ready(cla, 'nanjang')
        print("여긴 테스트 모드(ver " + str(version) + ")")


        go_test(cla)

        # self.parent.temporary_all_pause_game()
        # color change
        # potion__ = 0
        # img = pyautogui.screenshot(region=(get_region(105, 410, 165, 440, cla)))
        # white_img = image_processing(img, (148, 148, 148), (255, 255, 255))
        # result = pytesseract.image_to_string(white_img, lang=None)
        # digit_bloon = int_put_(result).isdigit()
        # if digit_bloon == True:
        #     num_ = int(int_put_(result))
        #     print("num_", num_)
        #     potion__ += num_
        # else:
        #     if result == '':
        #         print("비웠니랑..")
        #     else:
        #         print("보이질 않아", result)

        # go_alrim_confirm(cla, 'test')
        # go_power_bag(cla)

        # go_jadong_cla_mypower(cla)


        #line_to_me("one", "쿱꼬 초기화 갱신 안되었다.")

        # dir_path = "C:\\my_games\\coobcco2"
        # file_path = dir_path + "\\odin_schedule\\schedule.txt"
        # file_path2 = dir_path + "\\odin_schedule\\quest.txt"
        # file_path3 = dir_path + "\\odin_schedule\\schedule2.txt"
        # file_path13 = dir_path + "\\odin_schedule\\refresh_time.txt"
        #
        # if os.path.isfile(file_path) == True:
        #     with open(file_path, "r", encoding='utf-8-sig') as file:
        #         refresh_time = file.read()
        #     if refresh_time == "":
        #         print("empty")
        #     else:
        #         print("refresh_time", refresh_time)
        print(cv2.__file__)





        # full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\drag_.png"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set(220, 930, 800, 1030, cla, img)
        # if imgs_ is not None:
        #     print("drag_", imgs_)

        # auction_all_get(cla)
        # from event_get import special_package
        # special_package(cla)


        # print("5x5 뽑기")
        # isZero = False
        # while isZero is False:
        #     full_path = "c:\\my_games\\coobcco2\\data_od\\item\\55\\zero.png"  # zero 파악
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(220, 360, 275, 440, cla, img, 0.9)
        #     if imgs_ is not None and imgs_ != False:
        #         isZero = True
        #         print("받을 포인트 부족")
        #     else:
        #         print("받기 시작")
        #         full_path = "c:\\my_games\\coobcco2\\data_od\\item\\seven_four\\eventandbosang.png"
        #         img_array = np.fromfile(full_path, np.uint8)
        #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #         imgs_ = imgs_set_(380, 270, 550, 330, cla, img, 0.8)
        #         if imgs_ is not None and imgs_ != False:
        #             click_pos_2(480, 320, cla)
        #             full_path = "c:\\my_games\\coobcco2\\data_od\\item\\55\\open_ready.png"  # 오픈대기 파악
        #             img_array = np.fromfile(full_path, np.uint8)
        #             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #             imgs_ = imgs_set(35, 400, 400, 770, cla, img)
        #             if imgs_ is not None and imgs_ != False:
        #                 click_pos_reg(imgs_.x, imgs_.y, cla)
        #                 time.sleep(2)
        #                 isGet = False
        #                 while isGet is False:
        #                     full_path = "c:\\my_games\\coobcco2\\data_od\\item\\seven_four\\eventandbosang.png"
        #                     img_array = np.fromfile(full_path, np.uint8)
        #                     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #                     imgs_ = imgs_set_(380, 270, 550, 330, cla, img, 0.8)
        #                     if imgs_ is not None and imgs_ != False:
        #                         isGet = True
        #                         print("5x5 받기 완료", imgs_)
        #                         time.sleep(0.3)
        #                     else:
        #                         print("5x5 스킵하기")
        #                         click_pos_2(480, 320, cla)
        #                         time.sleep(0.3)


        #char_staus_.split('\n')

        # go_mynumber_(cla)
        # one_cla_ing = 'check'
        # go_chango_drag(cla)
        # go_boonhae_drag(cla)

        # go_soongan_f5(cla)
        # jadong_cla_ready(cla, '바위해안')

        # clean_screen(cla, "now_hunting_is")
        # go_bag(cla, 'test')
        # now_hunting_is("test", cla)

        # golded_ = text_check_get(815, 40, 891, 65, cla)
        # print("gold??", golded_)
        # gold_ = golded_.split("\n")
        # result_ = int_put_(gold_[0])
        # gold_bloon = isNumber_(result_)
        # if len(result_) >= 1 and gold_bloon == True:
        #     gold = int(result_)
        #     isGold = True
        #     print("gold", gold)
        # else:
        #     gold = 1000000
        #     print("noGold = True")
        # re_ = go_power_bag(cla)
        # print("dd",re_)

        #
        # result_cou_ = maul_cou_(cla)
        # # [0]수락 및 완료, [1]총갯수, [2]총갯수 - 수락 및 완료, [3]완료 글자 갯수, [4]수락함 글자 갯수, [5]완료 글자 + 수락함 글자 갯수
        # # [6] 진행중 의뢰 갯수, [7] 진행중 의뢰 총 갯수 [8] 진행중의뢰 총갯수 - 진행중 의뢰 갯수
        # print("[0]수락 및 완료, [1]총갯수, [2]총갯수 - 수락 및 완료, [3]완료 글자 갯수, [4]수락함 글자 갯수, [5]완료 글자 + 수락함 글자 갯수")
        # print("[6] 진행중 의뢰 갯수, [7] 진행중 의뢰 총 갯수 [8] 진행중의뢰 총갯수 - 진행중 의뢰 갯수")
        # print("result_cou", result_cou_)



        # full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\start_ready_in_jadong\\bawehaean.png"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set(45, 105, 200, 160, cla, img)
        #
        # if imgs_ is None or imgs_ == False:
        #     print('바위해안 아님')
        # else:
        #     print('바위해안 맞다')
        #     print("바위해안", imgs_)

        # print("test___________2")
        # print("================")
        # for i in range(4):
        #     print("i : ", i)
        #     mynick = text_check_get_3(10, 200, 165, 240, i, cla)
        #     print("mynick2", mynick)

        # for i in range(5):
        #     full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\jangbi_out\\event_item_2.png"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(540, 70, 950, 980, cla, img, 0.6)
        #
        #     if imgs_ is None or imgs_ == False:
        #         print("evnet_item(out_이)가 없다...")
        #     else:
        #         print("있나", imgs_)
        #         click_pos_reg(imgs_.x - 20, imgs_.y, cla)
        #         time.sleep(0.3)
        #         click_pos_reg(890, 1010, cla)
        #         time.sleep(0.3)
        # seven_four

        # go_level(cla)

        # full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\soongan.png"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set(560, 100, 950, 950, cla, img)
        # if imgs_ is None or imgs_ == False:
        #     full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\soongan_2.png"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set(560, 100, 950, 950, cla, img)
        #     if imgs_ is None or imgs_ == False:
        #         print("없")
        #     else:
        #         print("있2", imgs_)
        # else:
        #     print("있1", imgs_)
        # chango_(cla, 'after')


        # result = go_alrim_(cla)
        # print(result)
        # for i in range(4):
        #     print("i : ", i)
        #     # potion_count_ = text_check_get_3(850, 820, 935, 850, i, cla)
        #     potion_count_ = text_check_get_3(855, 825, 935, 850, i, cla)
        #     # potion_count_ = text_check_get_3(865, 830, 935, 850, i, cla)
        #     print("potion_count_", potion_count_)
        #     if '/' in potion_count_ and potion_count_ != 0:
        #         print('/가 있당')
        #         potion_count1 = potion_count_.split("/")
        #         print("potion_count1", potion_count1)
        #         potion_ = int_put_(potion_count1[0])
        #         potion_bloon = potion_.isdigit()
        #         if potion_bloon == True:
        #             potion = int(potion_)
        #             print("potion", potion)
        #             ispotion__ = True
        #             # click_pos_2(700, 840, cla) 이건 최초 1회만 하자
        #         else:
        #             print("포션 파악 불가")
        #             print("포션 파악 불가인 것은 물약이 최대 소지 갯수 초과했기 때문임.")
        #     else:
        #         print('/가 없당')
        #         print("potion_count_99999", potion_count_)
        #         print("/가 없는 것은 물약이 최대 소지 갯수 초과했기 때문임.")

        # myPotion_check('test', cla)
        # go_potion_off(cla)

        # self.xy = Grow_()
        # self.xy.potion_grow(cla, '니다육성')

        # get_cla_count_grow(cla)

        # x_ = game_Playing(self.parent)
        # x_.start()
        #
        # y_ = BackGroundPotion(self.parent)
        # y_.start()
        # myId_1 = 1
        # result_ = myQuest_play_check(cla, '요툰육성')
        # print('result_[2]', result_[2])
        # if result_[2] == True:
        #     self.parent.mySchedule_refresh()
        # else:
        #     cla_ing_ = result_
        #     self.parent.mySchedule_is()
        # myId_1 = 2
        # result_ = myQuest_play_add(cla, '요툰육성')
        # if result_ == 'check':
        #     cla_ing_ = result_
        #     self.parent.mySchedule_is()

        # go_chango(cla, 'out')
        # self.parent.set_rand_int()
        # result = quest_refresh()
        # if result == True:
        #     self.parent.mySchedule_refresh()


        # self.parent.temporary_all_pause_game()
        # self.parent.again_restart_game()



        # go_juljun(cla)

        # now_cla = 'one'
        # global_howcla = 'onetwocla'
        # self.parent.again_restart_game()
        # print("진행중으로 바꾸기 작업 시도")
        # self.parent.set_rand_int_jinhang(cla)
        # result = self.parent.sche_load_()
        # print(result)
        # how_ = 'modify'
        # result = self.parent.mySchedule_change(how_, result)
        # if result == True:
        #     self.parent.set_rand_int()
        # time.sleep(3)
        # self.parent.set_rand_int_jinhang('two')




    def hello(self):
        print("hi hello")
        # cla = 'one'
        # howcla= 'onecla'
        # game_play_test(howcla)

        # while self.one_ is True:
        #     print("self.one_ = True")
        #     time.sleep(3)
        #
        # while self.two_ is True:
        #     print("self.two_ = True")
        #     time.sleep(3)


        # print("test!~!~!~!", self.pause)
        # while self.pause:
        #     if self.pause == True:
        #         print("시작한다아")
        #         game_play_test(howcla)
        #     else:
        #         print("정지한다아")
        # num_ = 0
        # nono = 'none'
        # nono2= 'none'
        # while self.pause:
        #     num_ += 1
        #     print('...', num_)
        #     print('...', nono)
        #     print('...', nono2)
        #     if num_ == 2:
        #         nono = 'good'
        #     if num_ == 4:
        #         nono = 'gooddddddddd'
        #         nono2 = 'zzzzzzzzzzz'
        #     time.sleep(3)

    # def stop_(self):
    #
    #     print("stop!!!!!!!")
    #     self.pause = False
    #     self.quit()
    #     self.wait(3000)  # 3초 대기 (바로 안꺼질수도)
    #
    # def go_(self):
    #     print("start!!!!!!!")
    #     self.pause = True
    #     # self.Test_check = Test_check()
    #     # self.Test_check.start()


        # try:
        #
        #
        #     howcla = 'onetwocla'
        #     game_play_test(howcla)
        #
        #
        #
        #
        # except Exception as e:
        #     print(e)
        #     return



            # howcla = 'onetwocla'
            #
            # istest = isgloballoop
            # print('isgloballoop', isgloballoop)
            # while istest is False:
            #     print("tttttttttttttttttttttttt")
            #     # game_play_test(howcla)
            #     time.sleep(5)
            #
            # # game_play_test(howcla)




#############################################################################
def quest_refresh():
    refresh_ = True
    dir_path = "C:\\my_games\\coobcco2"
    file_path = dir_path + "\\odin_schedule\\schedule.txt"
    file_path3 = dir_path + "\\odin_schedule\\schedule2.txt"
    reset_schedule_ = ""
    with open(file_path, "r", encoding='utf-8-sig') as file:
        lines = file.read().splitlines()
        lines = ' '.join(lines).split()
        for i in range(len(lines)):
            complete_ = lines[i].split(":")
            for j in range(len(complete_)):
                if j < 3:
                    reset_schedule_ += complete_[j] + ":"
                if j == 3:
                    reset_schedule_ += '대기중:'
                if 3 < j < 7:
                    reset_schedule_ += complete_[j] + ":"
                if j == 7:
                    reset_schedule_ += "대기중\n"
        print('reset_schedule_', reset_schedule_)
        with open(file_path, "w", encoding='utf-8-sig') as file:
            file.write(reset_schedule_)
        with open(file_path3, "w", encoding='utf-8-sig') as file:

            file.write(reset_schedule_)
    return refresh_
def hello():
    global rehi_
    print("hello")
    rehi_ = "rehiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"

    MyApp()

####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
##기존 오토 부분####################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
# 공통 정의 ############################################################################

def thistest():
    try:
        result = True
        return result
    except Exception as e:
        print(e)



###############################################################################

# 실시간 체크 ###################################################################










##############################################################################





# 구상휘 캐릭 로테이션 부분 #############################################################



###############################################################################

# 구상휘 던전부분 #############################################################








# def start_ready_in_jadong_check(cla, nowing):
#     try:
#         # test
#         drag_pos(475, 580, 475, 150, cla)
#         time.sleep(1)
#         print("바위해안 체크?", nowing)
#
#         checked_ = False
#
#         full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\start_ready_in_jadong\\bawehaean.png"
#         img_array = np.fromfile(full_path, np.uint8)
#         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#         imgs_ = imgs_set(45, 105, 200, 160, cla, img)
#         # imgs_ = pyautogui.locateCenterOnScreen(img, region=(45 + plus, 105, 200 + plus, 160),
#         #                                        confidence=0.7)
#
#         if imgs_ is None or imgs_ == False:
#             print('바위해안 아님')
#         else:
#             print('바위해안 맞다')
#             print("바위해안", imgs_)
#             checked_ = True
#
#
#         return checked_
#     except Exception as e:
#         print(e)
#         return 0



###########시작 아이디 조회##########################################################







######################################################
##########################################
##############################################################
####################################################################
###################################################################




# 이미지 전반적 색상 배열 형태로 출력 R, G, B 값으로 출력됨
def image_get_palette(file_name, min_color, max_color):
    ct = colorthief.ColorThief(file_name)
    colors = ct.get_palette(color_count=3)
    return colors

# 1) 가방 연 후에 사용
# 2) 현재 버전 3자릿 수(0~999)까지만 읽을 수 있음
# 3) 아이템 전체크기 64 * 64
# 4) 숫자 1pixel 위인 64 * 46(!왼쪽 상단 기준) 아이템 이미지
# 5) 숫자는 자동으로 인식함
# return [아이템 유무, 숫자, 가운데 좌표]

def find_item_with_count(img_path: str):
    pos = pyautogui.locateOnScreen(img_path)
    center_pos = pyautogui.locateCenterOnScreen(img_path)
    print(pos)
    print(center_pos)
    if pos is None:
        return [False, 0, (0, 0)]
    else:
        # 30, 40
        img = pyautogui.screenshot(region=(pos[0] + 32, pos[1] + 46, 27, 14))
        # white_img = cv2.inRange(img_, (148, 148, 148), (255, 255, 255))
        white_img = image_processing(img, (148, 148, 148), (255, 255, 255))
        # adaptive threshold - 가우시안 방식
        # img__ = cv2.adaptiveThreshold(img_, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        #                               cv2.THRESH_BINARY, 15, 2)
        # blur = cv2.GaussianBlur(img_, (5, 5), 0)
        # img__ = cv2.adaptiveThreshold(img_, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 2)
        result = pytesseract.image_to_string(white_img, lang=None)
        try:
            num = int(re.sub(r"[^0-9]", "", result))
        except Exception as e:
            print('[ERROR!!] '+str(e))
            print('[ERROR!!] '+result)
            num = 1
        # print(result)
        return [True, num, (center_pos[0], center_pos[1])]

# 1) 가방 연 후에 사용
# return 돈

def get_gold(cla):
    # img = pyautogui.screenshot(region=(815, 44 + 46, 27, 14))
    # img = imgs_set(790, 40, 890, 70, cla, img)
    img = pyautogui.screenshot(region=(get_region(790, 40, 890, 70, cla)))
    white_img = image_processing(img, (148, 148, 148), (255, 255, 255))
    result = pytesseract.image_to_string(white_img, lang=None)
    try:
        num = int(re.sub(r"[^0-9]", "", result))
    except Exception as e:
        print('[ERROR!!] ' + str(e))
        print('[ERROR!!] ' + result)
        num = 1
    return num

def get_power(cla):
    img = pyautogui.screenshot(region=(get_region(48, 996, 140, 1020, cla)))
    # image color 모델 RGB to BGR로 변경 따라서 B-G-R 순으로 입력해야 동작함
    white_img = image_processing(img, (50, 126, 142), (89, 226, 255))
    result = pytesseract.image_to_string(white_img, lang=None)
    try:
        num = int(re.sub(r"[^0-9]", "", result))
    except Exception as e:
        print('[ERROR!!] ' + str(e))
        print('[ERROR!!] ' + result)
        num = 1
    return num

def get_dungeon_time(cla):
    file_name = 'get_colors.png'
    img = pyautogui.screenshot(file_name, region=(get_region(410, 655, 514, 693, cla)))
    images_color = image_get_palette(file_name, (117, 95, 20), (255, 206, 35))
    return images_color

# return [아이템 유무, 가운데 좌표]
def find_item(img_path: str):
    center_pos = pyautogui.locateCenterOnScreen(img_path, confidence=0.8)
    if center_pos is None:
        return [False, (0, 0)]
    else:
        return [True, (center_pos[0], center_pos[1])]

def image_string(img_path: str):
    result = pytesseract.image_to_string(img_path, lang=None)
    print(result)

def test(cla):
    img = pyautogui.screenshot(region=(get_region(6, 341, 63, 382, cla)))
    pyautogui.PAUSE = 3
    pyautogui.click(35, 346)
    pyautogui.PAUSE = 3
    pyautogui.click(464, 781)
    pyautogui.PAUSE = 3
    center_pos = pyautogui.locateCenterOnScreen(img, confidence=0.5)
    pyautogui.PAUSE = 3
    print(center_pos)



##########################################################
# Action(행동, 액션 부분)



#######################################################





def pause_ing(cla):
    try:
        print("pause")
        go_ = False
        if cla == 'one':
            if int(v_.myId_1) >= 0 and int(v_.mylevel_1) > 0 and int(v_.mypower_1) > 0 and int(v_.mymoney_1) > 0 and v_.one_cla_ing != 'none' and int(v_.one_cla_count) > 0:
                go_ = True
        if cla == 'two':
            if int(v_.myId_2) >= 0 and int(v_.mylevel_2) > 0 and int(v_.mypower_2) > 0 and int(v_.mymoney_2) > 0 and v_.two_cla_ing != 'none' and int(v_.two_cla_count) > 0:
                go_ = True
        return go_
    except Exception as e:
        print(e)
        return 0


class just_loginstart_one(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    def run(self):
        try:
            just_login('one')
        except Exception as e:
            print(e)
            return 0

class just_loginstart_two(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    def run(self):
        try:
            just_login('two')
        except Exception as e:
            print(e)
            return 0

class Monitoring(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    def run(self):
        try:
            print("monitoring start")
            line_monitor()
        except Exception as e:
            print(e)
            return 0


class game_Playing_onecla(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    def run(self):
        try:
            v_.now_cla = 'one'
            howcla = 'onecla'
            self.x_ = game_Playing()
            self.x_.start()
            # howcla = 'onecla'
            # result_ = login_start_ready(howcla)
            # if result_ == True:
            #     print("이제 시작 했다 다 죽었다!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", howcla)
            #
            #     v_.now_cla = 'one'
            #     v_.global_howcla = 'onecla'
            #
            #     # self.parent.again_restart_game()
            #     self.x_ = game_Playing()
            #     self.x_.start()
            #
            #     # self.y_ = BackGroundPotion()
            #     # self.y_.start()
        except Exception as e:
            print(e)
            return 0


class game_Playing_twocla(QThread):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent


    def run(self):
        try:

            v_.now_cla = 'two'
            howcla = 'onecla'
            self.x_ = game_Playing()
            self.x_.start()

            # howcla = 'onetwocla'
            # result_ = login_start_ready(howcla)
            # if result_ == True:
            #     print("이제 시작 했다 다 죽었다!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", howcla)
            #
            #     v_.now_cla = 'one'
            #     v_.global_howcla = 'onetwocla'
            #     self.x_ = game_Playing()
            #     self.x_.start()
            #
            #     self.y_ = BackGroundPotion()
            #     self.y_.start()
            # else:
            #     print("아직 2클라 덜 돌아갔다!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            # print('return!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!', result_)
        except Exception as e:
            print(e)
            return 0



# 실제 게임 플레이 부분 #################################################################
################################################

cla = v_.now_cla
cla_ing_ = 'none'
cla_gonghu = False
cla_nanjang = False
cla_underprison = False
myId_ = v_.myId_1
mypotion_ = 0
mylevel_ = 0
mypower_ = 0
mymoney_ = 0
a_ = 0
b_ = 0
v_.one_cla_get_event = True
v_.two_cla_get_event = True
################################################



class game_Playing(QThread):



    def __init__(self):
        super().__init__()
        # self.parent = parent



        self.isCheck = True

    def run(self):
        # global one_cla_id, one_cla_pw, mylevel_1, mypower_1, mypotion_1, mymoney_1, gonghu_1, nanjang_1, underprison_1, jadong_1, myId_1, one_cla_count, one_cla_ing, one_cla_start, \
        #     two_cla_id, two_cla_pw, mylevel_2, mypower_2, mypotion_2, mymoney_2, gonghu_2, nanjang_2, underprison_2, jadong_2, myId_2, two_cla_count, two_cla_ing, two_cla_start, \
        #     global_howcla, now_cla, a_, b_, change_ready_main, one_now_growing_, two_now_growing_, one_cla_get_event, two_cla_get_event, mynumber_1, mynumber_2 
        try:


            cla = v_.now_cla
            print("now_cla", v_.now_cla)
            print("global_howclaglobal ", v_.global_howcla)

            print('self.isCheck!!!!!!!!!!!!!', self.isCheck)

            print("여긴 실행 모드(ver " + str(version) + ")")
            while self.isCheck is True:

                is_stop(cla)

                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\check\\touching.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = pyautogui.locateCenterOnScreen(img, region=(0, 0, 1920, 1030),
                                                       confidence=0.7)
                if imgs_ is not None and imgs_ != False:
                    print("터칭 모드 중(ver " + str(version) + ")", imgs_)
                    time.sleep(5)
                else:

                    # %%%
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\odin.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(0, 0, 60, 30, cla, img)
                    if imgs_ is not None and imgs_ != False:
                        print("오딘 " + str(cla) + "클라 켜져있음  ^ㅅ^")

                        isready_ = False
                        isready_count = 0
                        while isready_ is False:
                            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\check\\odin_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                            if imgs_ is not None and imgs_ != False:
                                isready_count += 1
                                if isready_count < 4:
                                    print("오딘 매크로 내리면 시작")
                            else:
                                isready_ = True
                            time.sleep(5)





                        # 처음 로그인 화면 구분
                        # print("처음시작..get_cla_count(cla)")
                        #get_cla_count(cla)

                        # 빌어먹을 이벤트 창
                        is_stop(cla)

                        # 우선 방치모드 해제
                        bangchi_mode(cla)

                        # 스케쥴 체크
                        start_ready = myQuest_play_check(cla, "check")

                        print("진행중으로 바꾸기 작업 시도")
                        # self.parent.set_rand_int_jinhang(cla)

                        # start_ready[0] 진행중인 정보 [0][1] = id, [0][2] = 던전(공허, 난쟁이, 지하감옥, 자동사냥(들소황무지...), [0][3] = 완료 or 대기중, [3]진행되거나 진행중인 퀘스트
                        # 몇번째 인자에 정보가 담겨있는지 여부
                        print("checking", start_ready)
                        print("checking[0][1]", start_ready[0][1])
                        print("checking[0][2]", start_ready[0][2])
                        print("checking[0][3]", start_ready[0][3])
                        print("checking[3]", start_ready[3])

                        if start_ready[0][2] != "캐릭터바꾸기":
                            result_char_select = go_character_select(cla)
                            if result_char_select == True:
                                data = int(start_ready[0][1])
                                characterChange(data, cla)

                            else:
                                # 현재 진행중인 스케쥴 내 캐릭터 id와 기존 캐릭터 id 비교해서 다르면 캐릭터 바꾸기
                                dir_path = "C:\\my_games\\coobcco2"
                                if cla == 'one':
                                    file_path = dir_path + "\\odin_schedule\\one_now_id.txt"
                                if cla == 'two':
                                    file_path = dir_path + "\\odin_schedule\\two_now_id.txt"

                                if os.path.isfile(file_path) == True:

                                    with open(file_path, "r", encoding='utf-8-sig') as file:
                                        read_id = file.read()

                                    if str(start_ready[0][1]) != str(read_id):
                                        characterChange(start_ready[0][1], cla)
                                else:
                                    characterChange(start_ready[0][1], cla)


                        if start_ready[0][2] == "캐릭터바꾸기":
                            data = int(start_ready[0][1])
                            characterChange(data, cla)
                            myQuest_play_add(cla, "캐릭터바꾸기")

                        elif start_ready[0][2] == "각종템받기":
                            # if myQuest_grow_result[2] == '각종템받기':
                            print("우편, 이벤트, 업적 다 받아버리기")
                            # game_settings(cla, 'start')
                            game_event_get_ready(cla)
                            mypost(cla)
                            achieve_get_(cla)
                            chango_(cla, 'after')
                            guild_join_(cla)
                            myQuest_play_add(cla, start_ready[0][2])
                            datas = 'check'
                            start_ready = myQuest_play_check(cla, datas)

                        elif start_ready[0][2] == "거래소등록":
                            # if myQuest_grow_result[2] == '거래소등록':
                            print("창고에 꺼내서 팔아버리기")
                            # 먼저 창고에 가자
                            auction_all_get(cla)
                            myQuest_play_add(cla, start_ready[0][2])

                        elif '_' in start_ready[0][2]:

                            dir_path = "C:\\my_games\\coobcco2\\data_od"
                            file_path = dir_path + "\\imgs\\dunjeon\\in_dun.txt"

                            with open(file_path, "r", encoding='utf-8-sig') as file:
                                indun = file.read().splitlines()
                                print("&&&&&&", indun)
                            potion_go = False
                            for i in range(len(indun)):
                                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\dunjeon\\in_dun\\" + indun[i] + ".PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(40, 100, 240, 340, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print(indun[i], "있다")
                                    potion_go = True
                            if potion_go == False:
                                go_to_home('start', cla)

                            result_auto = go_auto(cla, 99)
                            if result_auto == True:
                                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\check\\full_bag_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(820, 0, 960, 100, cla, img, 0.9)
                                if imgs_ is not None and imgs_ != False:
                                    go_boonhae(cla, "full_bag")
                                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\gabang.png"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set(30, 40, 100, 75, cla, img)
                                    if imgs_ is None or imgs_ == False:
                                        click_pos_2(930, 55, cla)



                            dunjeon_spl_ = start_ready[0][2].split("_")
                            print("dunjeon_spl_[0]", dunjeon_spl_[0])
                            print("dunjeon_spl_[1]", dunjeon_spl_[1])
                            if dunjeon_spl_[0] == '공허':
                                print("game_gonghu", cla)
                                data = cla_ing_  # 최초 'check', 후에는 'gonghu', 'nanjang', 'underprison', 'jadong'

                                dunjeon = "gonghu"  # 보내고자 하는 던전


                                result = dunjeon_cla_play_su(cla, dunjeon_spl_[0], dunjeon_spl_[1])
                                if result == True:
                                    data_ = 'gonghu'
                                    result_ = myQuest_play_add(cla, data_)

                                # result = dunjeon_cla_play(cla, data, dunjeon)
                                #
                                # if result == True:
                                #     data_ = 'gonghu'
                                #     result_ = myQuest_play_add(cla, data_)



                            elif dunjeon_spl_[0] == '난쟁이':
                                print("game_nanjang", cla)
                                data = cla_ing_  # 최초 'check', 후에는 'gonghu', 'nanjang', 'underprison', 'jadong'
                                dunjeon = "nanjang"  # 보내고자 하는 던전

                                print("난쟁이 시작해볼까")

                                result = dunjeon_cla_play_su(cla, dunjeon_spl_[0], dunjeon_spl_[1])

                                if result == True:
                                    data_ = 'nanjang'
                                    result_ = myQuest_play_add(cla, data_)

                            elif dunjeon_spl_[0] == '지하감옥':
                                print("game_underprison", cla)
                                data = cla_ing_  # 최초 'check', 후에는 'gonghu', 'nanjang', 'underprison', 'jadong'

                                dunjeon = "underprison"  # 보내고자 하는 던전

                                result = dunjeon_cla_play_su(cla, dunjeon_spl_[0], dunjeon_spl_[1])

                                print("점검__8", cla, result)
                                if result == True:
                                    data_ = 'underprison'
                                    result_ = myQuest_play_add(cla, data_)
                                    print("점검__9", cla)
                        else:

                            if start_ready[0][2] == '미드가르드' or start_ready[0][2] == '요툰하임':
                                print("game_maul", cla)
                                # data = cla_ing_  # 최초 'check', 후에는 'gonghu', 'nanjang', 'underprison', 'jadong', 'maul'
                                print("마을 의뢰 시작해볼까")

                                result = maul_mission(cla, start_ready[0][2])

                                if result == True:
                                    data_ = start_ready[0][2]
                                    result_ = myQuest_play_add(cla, data_)


                            else:

                                if start_ready[0][2] == '요툰육성':
                                    yotoon_end = 0
                                    tuto_grow(cla)

                                    result = yotoon_grow_end(cla)

                                    if result == True:
                                        yotoon_end += 1

                                    # cla_grow.common_grow(cla)

                                    # result = cla_grow.yotoon_grow_end(cla)

                                    common_grow(cla)

                                    result = yotoon_grow_end(cla)

                                    if result == True:
                                        yotoon_end += 1

                                    # cla_grow.yotoon_grow(cla)

                                    yotoon_grow(cla)

                                    # result = cla_grow.yotoon_grow_end(cla)

                                    result = yotoon_grow_end(cla)

                                    if result == True:
                                        yotoon_end += 1

                                    time.sleep(1)

                                    if yotoon_end >= 1:

                                        print("요툰 육성 끝")

                                        result_ = myQuest_play_add(cla, start_ready[0][2])

                                    else:

                                        result_quest_ = go_quest_ing(cla)

                                elif start_ready[0][2] == '니다육성':
                                    nida_end = 0
                                    potion_grow(cla, start_ready[0][2])

                                    common_grow(cla)

                                    nida_grow(cla)

                                    result = nida_grow_end(cla)

                                    if result == True:
                                        nida_end += 1

                                    nida_grow(cla)

                                    result = nida_grow_end(cla)

                                    if result == True:
                                        nida_end += 1

                                    time.sleep(1)

                                    if nida_end >= 1:

                                        print("니다 육성 끝")

                                        result_ = myQuest_play_add(cla, start_ready[0][2])

                                    else:

                                        result_quest_ = go_quest_ing(cla)
                                else:
                                    # 자동 사냥
                                    #go_to_home('start', cla)

                                    result_auto = go_auto(cla, 99)
                                    if result_auto == True:
                                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\check\\full_bag_1.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(820, 0, 960, 100, cla, img, 0.9)
                                        if imgs_ is not None and imgs_ != False:
                                            go_boonhae(cla, "full_bag")
                                            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\gabang.png"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set(30, 40, 100, 75, cla, img)
                                            if imgs_ is None or imgs_ == False:
                                                click_pos_2(930, 55, cla)

                                    jadong_cla_play(cla, start_ready[0][2])



                        # 클라변경
                        print('global_howcla_change', v_.global_howcla)
                        if v_.global_howcla == 'onecla':
                            print("하나만 실행중")
                        else:
                            # self.isCheck = False
                            print("두개 실행중")

                            if v_.now_cla == 'one':
                                v_.now_cla = 'two'
                            else:
                                v_.now_cla = 'one'
                            print("end game!!!", v_.now_cla)
                            if cla == 'one':
                                cla = 'two'
                                # one_cla_ing = cla_ing_
                                nowTime = datetime.today().strftime("%Y/%m/%d %H:%M:%S")
                                print('one_two', cla)
                                print('claChange_1', nowTime)
                                time.sleep(10)
                            elif cla == 'two':
                                cla = 'one'
                                # two_cla_ing = cla_ing_
                                nowTime = datetime.today().strftime("%Y/%m/%d %H:%M:%S")
                                print('two_one', cla)
                                print('claChange_2', nowTime)
                                time.sleep(10)
                            v_.now_cla = cla
                            print('game_play_end', cla)

                            # if change_ready_main == False:
                            #     change_ready_main = True
                            #     print("end game", now_cla)
                            #     ############<<<pause>>>############
                            #     if self.isCheck == False:
                            #         paused_ = 0
                            #     while self.isCheck is False:
                            #         paused_ += 1
                            #         if paused_ == 1:
                            #             print("일시 정지 중입니다!!!!!!!!!")
                            #         time.sleep(2)
                            #     #####################################


                    else:
                        print("오딘 " + str(cla) + "클라 꺼져져있음? ㅠㅅㅠ")

                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\odin.png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(0, 0, 960, 1030, cla, img)
                        if imgs_ is not None and imgs_ != False:
                            print("어라?오딘 백그라운드 " + str(cla) + "클라 켜져있음  ^ㅅ^", imgs_)
                            time.sleep(0.3)
                            click_pos_reg(imgs_.x + 100, imgs_.y, cla)
                            pyautogui.keyDown('win')
                            if cla == 'one':
                                pyautogui.press('left')
                            elif cla == 'two':
                                pyautogui.press('right')
                            pyautogui.keyUp('win')
                            time.sleep(0.3)
                            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\odin.png"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set(0, 0, 60, 30, cla, img)
                            if imgs_ is not None and imgs_ != False:
                                print("정비 완료  ^ㅅ^", imgs_)
                                time.sleep(1)
                                click_pos_reg(imgs_.x + 100, imgs_.y, cla)
                                print("다시 ㄱㄱㄱㄱㄱㄱㄱㄱㄱㄱㄱㄱㄱㄱㄱ")

                        else:
                            print("힝..오딘 백그라운드 " + str(cla) + "클라 꺼져있음  ㅠ,.ㅠ")
                            line_to_me(cla, "꺼진 것 같다")


                            print('global_howcla_change', v_.global_howcla)
                            if v_.global_howcla == 'onecla':
                                print("하나만 실행중")

                                now_hunting_is(cla_ing_, cla)

                            else:
                                # self.isCheck = False
                                print("두개 실행중")

                                now_hunting_is(cla_ing_, cla)

                                if v_.now_cla == 'one':
                                    v_.now_cla = 'two'
                                else:
                                    v_.now_cla = 'one'
                                print("end game!!!", v_.now_cla)
                                if cla == 'one':
                                    cla = 'two'
                                    # one_cla_ing = cla_ing_
                                    nowTime = datetime.today().strftime("%Y/%m/%d %H:%M:%S")
                                    print('one_two', cla)
                                    print('claChange_1', nowTime)
                                    time.sleep(10)
                                elif cla == 'two':
                                    cla = 'one'
                                    # two_cla_ing = cla_ing_
                                    nowTime = datetime.today().strftime("%Y/%m/%d %H:%M:%S")
                                    print('two_one', cla)
                                    print('claChange_2', nowTime)
                                    time.sleep(10)
                                v_.now_cla = cla
                                print('game_play_end', cla)

                                if v_.change_ready_main == False:
                                    v_.change_ready_main = True
                                    print("end game", v_.now_cla)

                                    ############<<<pause>>>############
                                    paused_ = 0
                                    while v_.change_ready_main is True:
                                        paused_ += 1
                                        if paused_ == 1:
                                            print("일시 정지 중입니다!!!!!!!!!")
                                        time.sleep(2)
                        # %%%
                        #
                        #                 #
                        #                 #
                        #                 #
                                    #####################################


        except Exception as e:
            print(e)
            return 0




###############################################################################

# 안동환 로그인 부분 ##############################################################

def game_open(user_id, user_pw):
    webbrowser.open_new("https://odin.game.daum.net/odin/")
    click_with_image("img/game_start.png")
    click_with_image("img/yes.png")
    click_with_image("img/kakao_login.png")
    isClick = False
    while isClick is False:
        location = pyautogui.locateOnScreen("img/id_input.png")
        if location is not None:
            pyautogui.click(location)
            clipboard.copy(user_id)
            pyautogui.hotkey("ctrl", "v")
            isClick = True
    isClick = False
    while isClick is False:
        location = pyautogui.locateOnScreen("img/pw_input.png")
        if location is not None:
            pyautogui.click(location)
            clipboard.copy(user_pw)
            pyautogui.hotkey("ctrl", "v")
            isClick = True
    click_with_image("img/final_login.png")


############################################################

# 안동환 로그인 부분 ##########################################

def main():
    #
    # open window
    win = tkinter.Tk()
    win.title("오딘 실행 창")
    win.geometry("440x240")
    # frame setting
    frm = tkinter.Frame(win)
    frm.pack()
    id_label = tkinter.Label(frm, text="id")
    id_label.pack()
    id_txbox = tkinter.Entry(frm, width=40)
    id_txbox.pack()
    pw_label = tkinter.Label(frm, text="pw")
    pw_label.pack()
    pw_txbox = tkinter.Entry(frm, width=40)
    pw_txbox.pack()

    # debug 용 안동환 비번
    id_txbox.insert(0, one_cla_id)
    pw_txbox.insert(0, one_cla_pw)

    # id_txbox.insert(0, "adhashags@naver.com")
    # pw_txbox.insert(0, "dksehd!2044")

    def call_main_loop():
        # open window and login
        game_open(id_txbox.get(), pw_txbox.get())
        # 일단 로딩 화면 넘어가기
        # click_with_image()

        # text_check(805, 750, 1100, 820, ["화면을 터치해주세요", "화면올 터치해주세요", "화면올 퇴치해주세요"], click_pos, (950, 790))
        # #
        # text_check(328, 720, 475, 753, ["계정 보안 설정"], click_pos, (950, 790))
        # text_check(1494, 867, 1613, 939, ["게임하기"], click_pos, (1553, 892))
        # return my character


    button = tkinter.Button(frm, width=10, text="play!", command=call_main_loop)
    button.pack()
    # main loop setting
    # win.mainloop()
    win.mainloop()
    print("program exit")



####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    # sys.exit(1)
