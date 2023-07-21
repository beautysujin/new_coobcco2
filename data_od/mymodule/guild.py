# import numpy as np
# import os
import time
# import random
# import os.path

# import cv2
# import pyautogui
# import clipboard

import sys
sys.path.append('C:/my_games/coobcco2/data_od/mymodule')
# from myfunction import *

def go_test(cla):
    print('hi test! guild', cla)



def guild_list_(cla):
    try:
        from myfunction import click_pos_2
        import os.path
        import clipboard
        import random
        import pyautogui

        dir_path = "C:\\my_games\\coobcco2\\data_od"
        file_path10 = dir_path + "\\item\\guild_list.txt"
        if os.path.isfile(file_path10) == True:
            # 파일 읽기
            with open(file_path10, "r", encoding='utf-8-sig') as file:
                lines = file.read().splitlines()
                file.close()
                print("all list", lines)
                print("random list_1", random.choice(lines))
                print("random list_2", random.choice(lines))
                click_pos_2(650, 105, cla)
                clipboard.copy(random.choice(lines))
                pyautogui.hotkey("ctrl", "v")
                time.sleep(0.3)
                click_pos_2(875, 105, cla)
                time.sleep(1)
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\guild\\not_join.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(30, 30, 200, 150, cla, img)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(880, 1010, cla)
                    time.sleep(0.2)
                    click_pos_2(880, 1010, cla)
                else:
                    click_pos_2(900, 200, cla)
                time.sleep(0.5)
    except Exception as e:
        print(e)
        return 0
def guild_join_(cla):
    try:
        from myfunction import imgs_set, imgs_set_, click_pos_2, menuOpenCheck
        import numpy as np
        import cv2

        print("guild_join_")
        isguild_ = False
        guild_count = 0
        isguild__count = 0
        while isguild_ is False:

            isguild__count += 1
            if isguild__count > 7:
                isguild_ = True
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\guild\\guild.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(30, 30, 200, 150, cla, img)
            if imgs_ is not None and imgs_ != False:
                print("guild_join_길드 보상", imgs_)
                time.sleep(0.5)
                guild_join_after = False
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\guild\\guild_lobby.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(20, 80, 330, 130, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    guild_join_after = True
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\guild\\guild_information.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(20, 80, 330, 130, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    guild_join_after = True
                if guild_join_after == True:
                    time.sleep(1)
                    click_pos_2(200, 105, cla)
                    time.sleep(1)
                    click_pos_2(200, 105, cla)

                    isbosang = False
                    isbosang_count = 0
                    while isbosang is False:

                        isbosang_count += 1
                        if isbosang_count > 7:
                            isbosang = True
                        time.sleep(0.5)
                        click_pos_2(320, 880, cla)
                        time.sleep(1)
                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\guild\\guild_bosang.png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(200, 300, 700, 700, cla, img)
                        if imgs_ is not None and imgs_ != False:
                            time.sleep(0.5)
                            click_pos_2(320, 880, cla)
                            time.sleep(0.5)
                        else:
                            isguild_ = True
                            isbosang = True
                            time.sleep(0.5)
                            click_pos_2(920, 65, cla)
            else:
                print("guild_join_길드가입")
                ########################길드가입#############################################
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\guild\\guild_join.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(30, 30, 160, 80, cla, img)
                if imgs_ is not None and imgs_ != False:
                    time.sleep(0.5)
                    guild_join_before = False
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\guild\\guild_moglog.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(20, 80, 330, 130, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        guild_join_before = True
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\guild\\guild_changsul.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(20, 80, 330, 130, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        guild_join_before = True

                    if guild_join_before == True:
                        guild_count += 1
                        time.sleep(1)
                        guild_list_(cla)
                        if guild_count > 3:
                            isguild_ = True
                            time.sleep(0.5)
                            click_pos_2(920, 65, cla)
                            time.sleep(1)
                else:
                    time.sleep(0.5)
                    click_pos_2(920, 65, cla)
                    time.sleep(1)
                    isMenu = False
                    isMenu_count = 0
                    while isMenu is False:

                        isMenu_count += 1
                        if isMenu_count > 7:
                            isMenu = True
                        result_menu = menuOpenCheck(cla, "guild_join_1")
                        if result_menu == True:
                            isMenu = True
                            time.sleep(0.5)
                            click_pos_2(680, 370, cla)
                            time.sleep(1)
                            click_pos_2(70, 105, cla)
                            time.sleep(1)
                            click_pos_2(70, 105, cla)
                            result_menu = menuOpenCheck(cla, "guild_join_2")
                            if result_menu == True:
                                isMenu = True
                                isguild_ = False
                                print("길드가입 비활성화 상태")
                                time.sleep(0.5)
                                click_pos_2(920, 65, cla)
                                time.sleep(1)
                        else:
                            time.sleep(0.5)
                            click_pos_2(920, 65, cla)
                            time.sleep(1)
                ########################길드가입#############################################
    except Exception as e:
        print(e)
        return 0

