# import numpy as np
# import cv2
# import os.path
import time

import sys
sys.path.append('C:/my_games/coobcco2/data_od/mymodule')
# from myfunction import *
# from action import go_skip

def go_test(cla):
    print('hi test! event_get', cla)

def go_get_open(cla):
    try:
        from action import go_bag
        from myfunction import drag_pos, click_pos_2

        go_bag(cla, "go_get_open")
        go_item_open(cla)
        time.sleep(1)
        go_ticket_open(cla)
        drag_pos(800, 900, 800, 200, cla)
        time.sleep(1)
        go_ticket_open(cla)
        # drag_pos(800, 300, 800, 900, cla)
        #time.sleep(1)
        go_item_open(cla)
        drag_pos(800, 900, 800, 200, cla)
        time.sleep(1)
        go_item_open(cla)
        time.sleep(1)
        click_pos_2(920, 55, cla)

    except Exception as e:
        print(e)
        return 0

def go_item_open(cla):
    try:
        from myfunction import click_pos_2, imgs_set_, click_pos_reg, imgs_set
        from action import go_alrim_, go_alrim_yes
        import numpy as np
        import cv2
        import os.path

        dir_path = "C:\\my_games\\coobcco2\\data_od"
        file_path7 = dir_path + "\\item\\event_get_item_open.txt"

        if os.path.isfile(file_path7) == True:
            # 파일 읽기
            with open(file_path7, "r", encoding='utf-8-sig') as file:
                lines = file.read().splitlines()
                file.close()
            print("lines", lines)

        for i in range(len(lines)):
            full_path = "c:\\my_games\\coobcco2\\data_od\\item\\item_open\\" + lines[i] + ".png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(560, 100, 950, 960, cla, img, 0.9)
            if imgs_ is None or imgs_ == False:
                print(lines[i] + "(in_이)가 없다...")
            else:
                print(lines[i], imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(1)
                full_path = "c:\\my_games\\coobcco2\\data_od\\item\\item_open\\sayong.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(330, 750, 420, 800, cla, img, 0.9)
                if imgs_ is None or imgs_ == False:
                    print("sayong(이)가 없다...")
                    click_pos_2(380, 780, cla)
                    time.sleep(1)
                    result_alrim = go_alrim_(cla)
                    if result_alrim == True:
                        click_pos_2(580, 620, cla)
                        time.sleep(1)
                        result_yes = go_alrim_yes(cla)
                        if result_yes[0] == True:
                            click_pos_reg(result_yes[1], result_yes[2], cla)
                            time.sleep(1)
                else:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(1)
                    result_alrim = go_alrim_(cla)
                    if result_alrim == True:
                        click_pos_2(580, 620, cla)
                        time.sleep(1)
                        result_yes = go_alrim_yes(cla)
                        if result_yes[0] == True:
                            click_pos_reg(result_yes[1], result_yes[2], cla)
                            time.sleep(1)
                time.sleep(2)
                click_pos_2(200, 900, cla)
                time.sleep(1)
                click_pos_2(200, 900, cla)

    except Exception as e:
        print(e)
        return 0

def go_ticket_open(cla):
    try:
        from myfunction import click_pos_2, imgs_set_, click_pos_reg, imgs_set
        from action import go_alrim_, go_alrim_yes, go_skip
        import numpy as np
        import cv2
        import os.path

        dir_path = "C:\\my_games\\coobcco2\\data_od"
        file_path8 = dir_path + "\\item\\event_get_ticket_open.txt"
        file_path8_random = dir_path + "\\item\\event_get_ticket_open_random.txt"

        if os.path.isfile(file_path8) == True:
            # 파일 읽기
            with open(file_path8_random, "r", encoding='utf-8-sig') as file:
                lines = file.read().splitlines()
                file.close()
            print("lines", lines)

        print("랜덤부터 까자")

        for i in range(len(lines)):
            full_path = "c:\\my_games\\coobcco2\\data_od\\item\\ticket_open\\" + lines[i] + ".png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(560, 100, 950, 960, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.2)
                full_path = "c:\\my_games\\coobcco2\\data_od\\item\\ticket_open\\sayong.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(330, 750, 420, 800, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                # 랜덤권...
                for z in range(10):
                    full_path = "c:\\my_games\\coobcco2\\data_od\\item\\ticket_open\\select_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(520, 390, 600, 440, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(510, 530, cla)
                        time.sleep(0.2)
                        click_pos_2(550, 650, cla)
                        for x in range(5):
                            click_pos_2(330, 330, cla)
                            time.sleep(0.3)
                        break



                    full_path = "c:\\my_games\\coobcco2\\data_od\\item\\ticket_open\\full_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(530, 580, 640, 640, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)

                        full_path = "c:\\my_games\\coobcco2\\data_od\\item\\ticket_open\\confirm_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(510, 660, 580, 700, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.2)

        time.sleep(1)

        if os.path.isfile(file_path8) == True:
            # 파일 읽기
            with open(file_path8, "r", encoding='utf-8-sig') as file:
                lines = file.read().splitlines()
                file.close()
            print("lines", lines)


        for i in range(len(lines)):
            full_path = "c:\\my_games\\coobcco2\\data_od\\item\\ticket_open\\" + lines[i] + ".png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(560, 100, 950, 960, cla, img, 0.9)
            if imgs_ is None or imgs_ == False:
                print(lines[i] + "(in_이)가 없다...")
            else:
                print(lines[i], imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(1)
                full_path = "c:\\my_games\\coobcco2\\data_od\\item\\ticket_open\\sayong.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(330, 750, 420, 800, cla, img, 0.9)
                if imgs_ is None or imgs_ == False:
                    print("sayong(이)가 없다...")
                    click_pos_2(380, 780, cla)
                    time.sleep(1)
                    result_alrim = go_alrim_(cla)
                    if result_alrim == True:
                        click_pos_2(580, 620, cla)
                        time.sleep(1)
                        result_yes = go_alrim_yes(cla)
                        if result_yes[0] == True:
                            click_pos_reg(result_yes[1], result_yes[2], cla)
                            time.sleep(1)
                else:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(1)
                    go_skip(cla)
                    result_alrim = go_alrim_(cla)
                    if result_alrim == True:
                        click_pos_2(580, 620, cla)
                        time.sleep(1)
                        result_yes = go_alrim_yes(cla)
                        if result_yes[0] == True:
                            click_pos_reg(result_yes[1], result_yes[2], cla)
                            time.sleep(1)
                            go_skip(cla)

                isticketing = False
                while isticketing is False:
                    full_path = "c:\\my_games\\coobcco2\\data_od\\item\\ticket_open\\x.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(370, 300, 440, 360, cla, img)
                    if imgs_ is not None:
                        isticketing = True
                        click_pos_2(415, 340, cla)
                        time.sleep(1)
                    else:
                        isconfirm = False
                        full_path = "c:\\my_games\\coobcco2\\data_od\\item\\ticket_open\\confirm_1.png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(290, 940, 480, 1030, cla, img)
                        if imgs_ is not None:
                            isconfirm = True
                        full_path = "c:\\my_games\\coobcco2\\data_od\\item\\ticket_open\\confirm_2.png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(290, 940, 480, 1030, cla, img)
                        if imgs_ is not None:
                            isconfirm = True

                        if isconfirm == False:
                            full_path = "c:\\my_games\\coobcco2\\data_od\\item\\ticket_open\\balobogi.png"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set(200, 900, 800, 1030, cla, img)
                            if imgs_ is not None:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(1)
                            else:
                                click_pos_2(480, 370, cla)
                                time.sleep(1)
                                full_path = "c:\\my_games\\coobcco2\\data_od\\item\\ticket_open\\balobogi_2.png"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set(200, 900, 800, 1030, cla, img)
                                if imgs_ is not None:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(1)
                                else:
                                    click_pos_2(480, 975, cla)
                                    time.sleep(1)
                                    full_path = "c:\\my_games\\coobcco2\\data_od\\item\\ticket_open\\balobogi_1.png"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set(200, 900, 800, 1030, cla, img)
                                    if imgs_ is not None:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(1)
                                    else:
                                        click_pos_2(480, 980, cla)
                                        time.sleep(1)

                        else:

                            isticketing = True

                            time.sleep(1)
                            click_pos_2(390, 980, cla)
                            time.sleep(3)
                            full_path = "c:\\my_games\\coobcco2\\data_od\\item\\ticket_open\\x.png"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set(770, 270, 850, 350, cla, img)
                            if imgs_ is not None:
                                click_pos_2(815, 310, cla)
                                time.sleep(1)

                time.sleep(1)
    except Exception as e:
        print(e)
        return 0

def special_guild(cla):
    try:
        print("special_guild")
    except Exception as e:
        print(e)
        return 0

def game_event_search(cla, data, y_):
    try:
        import pyautogui
        from myfunction import click_pos_reg, imgs_set, imgs_set_, click_pos_2, random_int, menuOpenCheck, text_check_get, int_put_, drag_pos
        from clean import clean_screen
        import numpy as np
        import cv2


        isGet = False
        if cla == 'one':
            plus = 0
        if cla == 'two':
            plus = 960

        ###########

        item_1 = 95 + plus
        item_2 = 190 + plus
        item_3 = 285 + plus
        item_4 = 380 + plus
        item_5 = 475 + plus
        item_6 = 570 + plus
        item_7 = 665 + plus

        y_1 = 620
        y_2 = 720

        if data == 'seven':
            y_1 = 720

        if data == 'fourteen':
            y_1 = 620
            y_2 = 720
        ##########

        if data != 'seven_four':

            if data == 'fivetofive':
                print("5x5 뽑기")
                isZero = False
                while isZero is False:
                    full_path = "c:\\my_games\\coobcco2\\data_od\\item\\55\\zero.png"  # zero 파악
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(230, 380, 275, 435, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        isZero = True
                        isGet = True
                        print("받을 포인트 부족 : 모두 받음")
                    else:
                        print("받기 시작")
                        click_pos_2(840, y_, cla)
                        time.sleep(0.3)
                        full_path = "c:\\my_games\\coobcco2\\data_od\\item\\seven_four\\eventandbosang.png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(380, 270, 550, 330, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(480, 320, cla)
                            full_path = "c:\\my_games\\coobcco2\\data_od\\item\\55\\open_ready.png"  # 오픈대기 파악
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set(35, 400, 400, 770, cla, img)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(2)
                                isGet = False
                                while isGet is False:
                                    full_path = "c:\\my_games\\coobcco2\\data_od\\item\\seven_four\\eventandbosang.png"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(380, 270, 550, 330, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        isGet = True
                                        print("5x5 받기 완료", imgs_)
                                        time.sleep(0.3)
                                    else:
                                        print("5x5 스킵하기")
                                        click_pos_2(840, y_, cla)
                                        time.sleep(0.3)
                        # else:
                        #     isEventCheck = False
                        #     while isEventCheck is False:
                        #         time.sleep(random_int())
                        #         full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\event1.png"
                        #         img_array = np.fromfile(full_path, np.uint8)
                        #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        #         imgs_ = imgs_set(600, 30, 800, 90, cla, img)
                        #         if imgs_ is not None:
                        #             print("event1 보여")
                        #             isEventCheck = True
                        #             click_pos_2(680, 60, cla)
                        #             time.sleep(random_int())
                        #         else:
                        #             print("event1 안보여", imgs_)
                        #             click_pos_2(920, 55, cla)
                        #             time.sleep(random_int())
                        #             result = menuOpenCheck(cla, "game_event_get_ready")
                        #             if result == True:
                        #                 print("event1 보여어")
                        #                 isEventCheck = True
                        #                 click_pos_2(680, 60, cla)
                        #                 time.sleep(random_int())
                        #             else:
                        #                 clean_screen(cla, "game_event_get_ready_middle")
                    time.sleep(0.3)
            elif data == "black_six":
                isGet = True
                print("black_six")
                full_path = "c:\\my_games\\coobcco2\\data_od\\item\\six\\black_six_check.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(250, 570, 320, 600, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("black_six_check1", imgs_)
                    full_path = "c:\\my_games\\coobcco2\\data_od\\item\\six\\complete_1.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(300, 530, 380, 600, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("black_six_check complete_1", imgs_)
                    else:
                        print("black_six_check complete_1 없")
                        click_pos_2(355, 570, cla)
                        time.sleep(1)
                        click_pos_2(820, 310, cla)
                else:
                    print("black_six_check1 없")

                time.sleep(1)

                full_path = "c:\\my_games\\coobcco2\\data_od\\item\\six\\black_six_check.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(600, 570, 665, 600, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("black_six_check2", imgs_)
                    full_path = "c:\\my_games\\coobcco2\\data_od\\item\\six\\complete_1.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(660, 540, 720, 600, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("black_six_check complete_2", imgs_)
                    else:
                        print("black_six_check complete_2 없")
                        click_pos_2(690, 575, cla)
                        time.sleep(1)
                        click_pos_2(820, 310, cla)
                else:
                    print("black_six_check2 없")

            elif data == "yellow_six":
                isGet = True
                print("yellow_six")
                full_path = "c:\\my_games\\coobcco2\\data_od\\item\\six\\yellow_six_check.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(250, 570, 320, 600, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("yellow_six_check1", imgs_)
                    full_path = "c:\\my_games\\coobcco2\\data_od\\item\\six\\complete_1.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(300, 530, 380, 600, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("yellow_six_check complete_1", imgs_)
                    else:
                        print("yellow_six_check complete_1 없")
                        click_pos_2(355, 570, cla)
                        time.sleep(1)
                        click_pos_2(820, 310, cla)
                else:
                    print("yellow_six_check1 없")

                time.sleep(1)

                full_path = "c:\\my_games\\coobcco2\\data_od\\item\\six\\yellow_six_check.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(600, 570, 665, 600, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("yellow_six_check2", imgs_)
                    full_path = "c:\\my_games\\coobcco2\\data_od\\item\\six\\complete_1.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(660, 540, 720, 600, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("yellow_six_check2 complete_2", imgs_)
                    else:
                        print("yellow_six_check2 complete_2 없")
                        click_pos_2(690, 575, cla)
                        time.sleep(1)
                        click_pos_2(820, 310, cla)
                else:
                    print("yellow_six_check2 없")

            elif data == "change":
                print("event : change")
                bom_wind = text_check_get(670, 397, 715, 415, cla)
                print("bom_wind", bom_wind)
                bom_wind = int_put_(bom_wind)
                if int(bom_wind) > 300:
                    click_pos_2(385, 725, cla)

                    time.sleep(1)

                    full_path = "c:\\my_games\\coobcco2\\data_od\\item\\six\\sold_out.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(380, 560, 460, 640, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("sold_out", imgs_)
                        full_path = "c:\\my_games\\coobcco2\\data_od\\item\\six\\sold_out.png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(530, 560, 610, 640, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("sold_out", imgs_)

                            drag_pos(640, 600, 140, 600, cla)
                            time.sleep(0.3)
                            click_pos_2(630, 600, cla)
                            time.sleep(1)
                            click_pos_2(590, 590, cla)
                            time.sleep(0.2)
                            full_path = "c:\\my_games\\coobcco2\\data_od\\item\\change\\change.png"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(500, 670, 600, 710, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("change", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                click_pos_2(600, 710, cla)
                            isGet = True

                        else:
                            print("sold_out 없")
                            click_pos_2(565, 600, cla)
                            time.sleep(1)
                            click_pos_2(590, 690, cla)
                            time.sleep(1)
                            click_pos_2(820, 310, cla)
                            isGet = True
                    else:
                        print("sold_out 없")
                        click_pos_2(420, 600, cla)
                        time.sleep(1)
                        click_pos_2(590, 690, cla)
                        time.sleep(1)
                        click_pos_2(820, 310, cla)
                        isGet = True

                    full_path = "c:\\my_games\\coobcco2\\data_od\\item\\change\\change.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(500, 670, 600, 710, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("change", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)


                else:
                    isGet = True
                    print("포인트 부족", int(bom_wind))

            else:

                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\event_complete.png"  # '완료' 그림 갯수 파악
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                last_x = 0
                last_y = 0
                for list in pyautogui.locateAllOnScreen(img, region=(15 + plus, 300, 800, 600), confidence=0.8):
                    last_x = list.left
                    last_y = list.top
                    print("list", list)
                    print("last_x", last_x)
                    print("last_y", last_y)

                if last_x == 0:
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\event_complete_2.png"  # '완료' 그림 갯수 파악
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    for list in pyautogui.locateAllOnScreen(img, region=(15 + plus, 300, 800, 600), confidence=0.8):
                        last_x = list.left
                        last_y = list.top
                        print("list", list)
                        print("last_x", last_x)
                        print("last_y", last_y)

                if last_x != 0:
                    if item_7 - 40 < last_x < item_7 + 40:
                        if last_y < y_1:
                            if cla == 'one':
                                click_pos_reg(95 + plus, y_2, cla)
                                print("click_pos_reg(95, y_2, cla)")
                            if cla == 'two':
                                click_pos_reg(95 + plus, y_2, cla)
                                print("click_pos_reg(95 + 960, y_2, cla)")
                        else:
                            isGet = True
                            print("다 받았으니 패스")
                    else:
                        click_pos_reg(last_x + 115, last_y + 30, cla)
                        print("click_pos_reg(last_x + 115, last_y + 30, cla)")
                else:
                    print("last_x", last_x)
                    print("last_y", last_y)
                    print("이벤트 보상을 안 받았다.")
                    click_pos_reg(95 + plus, y_1, cla)
                    print("click_pos_reg(95, y_1, cla)")
        else:
            # 여긴 seven_four
            print("seven_four")
            isGetSevenFour = False
            while isGetSevenFour is False:
                full_path = "c:\\my_games\\coobcco2\\data_od\\item\\seven_four\\get_new.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(30, 480, 730, 550, cla, img)
                time.sleep(0.2)
                if imgs_ is None or imgs_ == False:
                    isGetSevenFour = True
                    isGet = True
                    print("seven_four 받기 끝")
                else:
                    print("새로운 seven_four 있다", imgs_)
                    click_pos_reg(imgs_.x - 40, imgs_.y + 10, cla)
                    time.sleep(0.5)
                    # 실질적인 받기
                    full_path = "c:\\my_games\\coobcco2\\data_od\\item\\seven_four\\get_complete.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(320, 540, 380, 600, cla, img)
                    if imgs_ is None or imgs_ == False:
                        full_path = "c:\\my_games\\coobcco2\\data_od\\item\\seven_four\\get_complete_2.png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(220, 570, 330, 600, cla, img, 0.9)
                        if imgs_ is None or imgs_ == False:
                            print("미완료 _ 1")
                        else:
                            print("완료하여 받기 _ 1", imgs_)
                            click_pos_2(350, 570, cla)
                            time.sleep(0.3)
                            isGet = False
                            while isGet is False:
                                full_path = "c:\\my_games\\coobcco2\\data_od\\item\\seven_four\\eventandbosang.png"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(380, 270, 550, 330, cla, img, 0.8)
                                if imgs_ is None or imgs_ == False:
                                    print("완료하여 받기 _ 1 => skip")
                                    click_pos_2(350, 700, cla)
                                    time.sleep(0.3)
                                else:
                                    isGet = True
                                    print("완료 _ 1", imgs_)
                                    time.sleep(0.3)
                    else:
                        print("이미 받음 _ 1", imgs_)

                    full_path = "c:\\my_games\\coobcco2\\data_od\\item\\seven_four\\get_complete.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(660, 540, 720, 600, cla, img)
                    if imgs_ is None or imgs_ == False:
                        full_path = "c:\\my_games\\coobcco2\\data_od\\item\\seven_four\\get_complete_2.png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(570, 570, 660, 600, cla, img, 0.9)
                        if imgs_ is None or imgs_ == False:
                            print("미완료 _ 2")
                        else:
                            print("완료하여 받기 _ 2", imgs_)
                            click_pos_2(700, 570, cla)
                            time.sleep(0.3)
                            isGet = False
                            while isGet is False:
                                full_path = "c:\\my_games\\coobcco2\\data_od\\item\\seven_four\\eventandbosang.png"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(380, 270, 550, 330, cla, img, 0.8)
                                if imgs_ is None or imgs_ == False:
                                    print("완료하여 받기 _ 1 => skip")
                                    click_pos_2(350, 700, cla)
                                    time.sleep(0.3)
                                else:
                                    isGet = True
                                    print("완료 _ 1", imgs_)
                                    time.sleep(0.3)
                    else:
                        print("이미 받음 _ 2", imgs_)

                    full_path = "c:\\my_games\\coobcco2\\data_od\\item\\seven_four\\get_complete.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(320, 600, 380, 660, cla, img)
                    if imgs_ is None or imgs_ == False:
                        full_path = "c:\\my_games\\coobcco2\\data_od\\item\\seven_four\\get_complete_2.png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(220, 630, 330, 660, cla, img, 0.9)
                        if imgs_ is None or imgs_ == False:
                            print("미완료 _ 3")
                        else:
                            print("완료하여 받기 _ 3", imgs_)
                            click_pos_2(350, 630, cla)
                            time.sleep(0.3)
                            isGet = False
                            while isGet is False:
                                full_path = "c:\\my_games\\coobcco2\\data_od\\item\\seven_four\\eventandbosang.png"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(380, 270, 550, 330, cla, img, 0.8)
                                if imgs_ is None or imgs_ == False:
                                    print("완료하여 받기 _ 1 => skip")
                                    click_pos_2(350, 700, cla)
                                    time.sleep(0.3)
                                else:
                                    isGet = True
                                    print("완료 _ 1", imgs_)
                                    time.sleep(0.3)
                    else:
                        print("이미 받음 _ 3", imgs_)

                    full_path = "c:\\my_games\\coobcco2\\data_od\\item\\seven_four\\get_complete.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(660, 600, 720, 660, cla, img)
                    if imgs_ is None or imgs_ == False:
                        full_path = "c:\\my_games\\coobcco2\\data_od\\item\\seven_four\\get_complete_2.png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(570, 630, 660, 660, cla, img, 0.9)
                        if imgs_ is None or imgs_ == False:
                            print("미완료 _ 4")
                        else:
                            print("완료하여 받기 _ 4", imgs_)
                            click_pos_2(700, 630, cla)
                            time.sleep(0.3)
                            isGet = False
                            while isGet is False:
                                full_path = "c:\\my_games\\coobcco2\\data_od\\item\\seven_four\\eventandbosang.png"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(380, 270, 550, 330, cla, img, 0.8)
                                if imgs_ is None or imgs_ == False:
                                    print("완료하여 받기 _ 1 => skip")
                                    click_pos_2(350, 700, cla)
                                    time.sleep(0.3)
                                else:
                                    isGet = True
                                    print("완료 _ 1", imgs_)
                                    time.sleep(0.3)
                    else:
                        print("이미 받음 _ 4", imgs_)


        return isGet
    except Exception as e:
        print(e)
        return 0
def game_event_item_get(cla):
    try:
        from myfunction import imgs_set, click_pos_2, random_int
        import numpy as np
        import cv2

        getBloon = False
        isitemGet_1 = False
        isitemGet_2 = False
        _count = 0

        dir_path = "C:\\my_games\\coobcco2\\data_od"
        file_path = dir_path + "\\item\\event_not_get_item.txt"
        with open(file_path, "r", encoding='utf-8-sig') as file:
            data = file.read()
            datas = data.split(":")
            print('datas', datas)

        while isitemGet_1 is False:
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\event_get.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(400, 460, 550, 515, cla, img)
            if imgs_ is not None:
                isitemGet_1 = True
                print("'일차'가 보여", imgs_)
                while isitemGet_2 is False:
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\event_get.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(400, 460, 550, 515, cla, img)
                    if imgs_ is not None:
                        print("'일차'가 아직 보여", imgs_)
                        click_pos_2(680, 310, cla)
                        time.sleep(1)
                    else:
                        # getBloon 은 실제 보상 받았는지 여부...
                        getBloon = True
                        isitemGet_1 = True
                        isitemGet_2 = True
                        print("'일차'가 이제 안보여")
                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\event_x.png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(590, 300, 675, 365, cla, img)
                        if imgs_ is not None:
                            print("이미 보상 받은거다2")
                            click_pos_2(640, 340, cla)
                            time.sleep(1)
                        else:
                            for i in range(len(datas)):
                                full_path = "c:\\my_games\\coobcco2\\data_od\\item\\not_get_item\\" + str(datas[i]) + ".png"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set(30, 300, 950, 850, cla, img)
                                if imgs_ is not None:
                                    print("이미 보상 받은거다3")
                                    click_pos_2(640, 340, cla)
                                    time.sleep(1)
            else:
                print("'일차'가 안보여")
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\event_x.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(590, 300, 675, 365, cla, img)
                if imgs_ is not None:
                    # getBloon 은 실제 보상 받았는지 여부...
                    getBloon = True
                    isitemGet_1 = True
                    print("이미 보상 받은거다1")
                    click_pos_2(640, 340, cla)
                    time.sleep(1)
                else:
                    for i in range(len(datas)):
                        full_path = "c:\\my_games\\coobcco2\\data_od\\item\\not_get_item\\" + str(datas[i]) + ".png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(100, 600, 880, 820, cla, img)
                        if imgs_ is not None:
                            getBloon = True
                            isitemGet_1 = True
                            print("이미 보상 받은거다3")
                            click_pos_2(640, 340, cla)
                            time.sleep(1)

                    else:
                        print("이벤트 화면 그대로 보상 못 받았거나 이미 받은 상태...")
                        _count += 1
                        if _count > 3:
                            isitemGet_1 = True
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\event_x.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(590, 300, 675, 365, cla, img)
        if imgs_ is not None:
            click_pos_2(640, 340, cla)
            time.sleep(1)
        else:
            for i in range(len(datas)):
                full_path = "c:\\my_games\\coobcco2\\data_od\\item\\not_get_item\\" + str(datas[i]) + ".png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(100, 600, 880, 820, cla, img)
                if imgs_ is not None:
                    print("이미 보상 받은거다3")
                    click_pos_2(640, 340, cla)
                    time.sleep(1)
        return getBloon
    except Exception as e:
        print(e)
        return 0

def game_event_get(cla):
    try:
        from myfunction import click_pos_2, random_int, drag_pos, imgs_set, imgs_set_, click_pos_reg
        import numpy as np
        import cv2

        # 이벤트 받기 시작 (14일짜리 7일로 나눠서 있는 이벤트)
        # 총 횟수 / 840(370, 425, ...) / seven or fourteen
        dir_path = "C:\\my_games\\coobcco2\\data_od"
        file_path = dir_path + "\\item\\event_get_item.txt"
        with open(file_path, "r", encoding='utf-8-sig') as file:
            datas = file.read().splitlines()
            file.close()
            # data = '370/fourteen:540/fourteen:600/fourteen'
            # datas = data.split(":")
            print("이벤트 대기중 => ", len(datas))
            for i in range(len(datas)):
                if datas[i] != 'drag':
                    item_list = datas[i].split("/")
                    isEventGet = False
                    isEventGetCount = 0
                    while isEventGet is False:
                        isEventGetCount += 1
                        time.sleep(1)
                        click_pos_2(840, int(item_list[0]), cla)
                        time.sleep(1)
                        result = game_event_search(cla, str(item_list[1]), int(item_list[0]))
                        time.sleep(random_int())
                        if result == False:
                            result_ = game_event_item_get(cla)
                            if result_ == True or isEventGetCount > 2:
                                isEventGet = True
                        else:
                            isEventGet = True
                else:
                    drag_pos(840, 660, 840, 360, cla)
                    time.sleep(1)


        isEventEnd = False
        while isEventEnd is False:
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\eventandbosang.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(400, 280, 600, 330, cla, img)
            if imgs_ is None or imgs_ == False:
                isEventEnd = True
                print("이벤트 & 보상이 안보여, 이벤트 보상받기 끝~!")
                time.sleep(1)
                # 가방 정리 전 특별패키지 있는지 파악하기
                special_package(cla)
                # 가방 열어 정리하기
                go_get_open(cla)
            else:
                print("이벤트 & 보상이 보여")
                click_pos_2(915, 310, cla)
                time.sleep(1)
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\special_package\\x.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(870, 270, 950, 350, cla, img, 0.8)
                if imgs_ is not None:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(1)





    except Exception as e:
        print(e)
        return 0

def game_event_get_ready(cla):
    try:
        from myfunction import click_pos_2, random_int, imgs_set, menuOpenCheck
        from clean import clean_screen
        import numpy as np
        import cv2

        # 이벤트 받기 시작
        clean_screen(cla, "game_event_get_ready_start")
        print("def game_event_get_ready(cla): ", cla)
        isEventCheck = False
        while isEventCheck is False:
            time.sleep(random_int())
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\event1.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(600, 30, 800, 90, cla, img)
            if imgs_ is not None:
                print("event1 보여")
                isEventCheck = True
                click_pos_2(680, 60, cla)
                time.sleep(random_int())
            else:
                print("event1 안보여", imgs_)
                click_pos_2(920, 55, cla)
                time.sleep(random_int())
                result = menuOpenCheck(cla, "game_event_get_ready")
                if result == True:
                    print("event1 보여어")
                    isEventCheck = True
                    click_pos_2(680, 60, cla)
                    time.sleep(random_int())

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\eventandbosang.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(400, 280, 600, 330, cla, img)
        if imgs_ is not None:
            print("이벤트 & 보상이 보여")
            print("game_event_get(cla)")
            game_event_get(cla)
        else:
            print("이벤트 & 보상이 안보여")
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\eventandbosang.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(400, 280, 600, 330, cla, img)
            if imgs_ is not None:
                print("이벤트 & 보상이 보여...")
                print("game_event_get(cla)...")
                game_event_get(cla)
            else:
                print("이벤트 & 보상이 안보여...ㅠㅠ???")
                click_pos_2(680, 60, cla)
                time.sleep(random_int())
                game_event_get(cla)

    except Exception as e:
        print(e)
        return 0



def achieve_get_(cla):
    try:
        from myfunction import imgs_set, click_pos_2, menuOpenCheck
        import numpy as np
        import cv2

        print("achieve_get_")
        isachieve_ = False
        while isachieve_ is False:
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\achieve\\upjuk.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(30, 30, 200, 150, cla, img)
            if imgs_ is not None and imgs_ != False:
                time.sleep(0.5)
                click_pos_2(880, 1010, cla)
                time.sleep(1)
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\achieve\\upjuk.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(30, 30, 200, 150, cla, img)
                if imgs_ is not None and imgs_ != False:
                    print("업적 받기 끝")
                    isachieve_ = True
                    click_pos_2(920, 55, cla)
                    time.sleep(1)
                else:
                    time.sleep(0.5)
                    click_pos_2(880, 1010, cla)
                    time.sleep(1)
            else:
                time.sleep(0.5)
                click_pos_2(920, 55, cla)
                time.sleep(1)
                isMenu = False
                while isMenu is False:
                    result_menu = menuOpenCheck(cla, "achieve_get_1")
                    if result_menu == True:
                        isMenu = True
                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\achieve\\point.png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(910, 180, 950, 220, cla, img)
                        if imgs_ is not None:
                            print("point", imgs_)
                            click_pos_2(920, 220, cla)
                            time.sleep(2)
                        else:
                            isachieve_ = True
                            time.sleep(0.5)
                            click_pos_2(920, 55, cla)
                            time.sleep(1)
                    else:
                        time.sleep(0.5)
                        click_pos_2(920, 55, cla)
                        time.sleep(1)

                        # result_menu = menuOpenCheck(cla, "achieve_get_2")
                        # if result_menu == True:
                        #     isMenu = True
                        #     isguild_ = False
                        #     print("업적 비활성화 상태")
                        #     time.sleep(0.5)
                        #     click_pos_2(920, 55, cla)
                        #     time.sleep(1)

        # while isachieve_ is False:
        #     full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\achieve\\upjuk.png"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set(30, 30, 200, 150, cla, img)
        #     if imgs_ is not None and imgs_ != False:
        #         print("achieve_get_ 보상", imgs_)
        #         # 좌측 7개 메뉴 모두 돌리기 110 / 220, 265, 310, 355, 400, 445, 490
        #         datas = [220, 265, 310, 355, 400, 445, 490]
        #         for i in range(len(datas)):
        #             print(datas[i])
        #             time.sleep(0.5)
        #             click_pos_2(110, datas[i], cla)
        #             time.sleep(0.5)
        #             # 1번 업적 획득하기
        #             isachieve_complete_1 = False
        #             while isachieve_complete_1 is False:
        #                 time.sleep(0.2)
        #                 full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\achieve\\achieve_complete_1.png"
        #                 img_array = np.fromfile(full_path, np.uint8)
        #                 img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #                 imgs_ = imgs_set_(800, 100, 950, 180, cla, img, 0.9)
        #                 time.sleep(0.2)
        #                 if imgs_ is not None and imgs_ != False:
        #                     print("achieve_complete_1 보상", imgs_)
        #                     click_x = imgs_.x + 40
        #                     click_y = imgs_.y
        #                     click_pos_reg(click_x, click_y, cla)
        #                     time.sleep(0.2)
        #
        #                     isGet = False
        #                     while isGet is False:
        #                         full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\achieve\\upjuk.png"
        #                         img_array = np.fromfile(full_path, np.uint8)
        #                         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #                         imgs_ = imgs_set(30, 30, 200, 150, cla, img)
        #                         if imgs_ is not None and imgs_ != False:
        #                             isGet = True
        #                             print("achieve_complete_1 획득")
        #                             time.sleep(0.1)
        #                         else:
        #                             click_pos_reg(click_x, click_y, cla)
        #                             time.sleep(0.3)
        #                 else:
        #                     isachieve_complete_1 = True
        #             # 2번 업적 획득하기
        #             isachieve_complete_2 = False
        #             while isachieve_complete_2 is False:
        #                 time.sleep(0.2)
        #                 full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\achieve\\achieve_complete_2.png"
        #                 img_array = np.fromfile(full_path, np.uint8)
        #                 img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #                 imgs_ = imgs_set(800, 200, 950, 260, cla, img)
        #                 time.sleep(0.2)
        #                 if imgs_ is not None and imgs_ != False:
        #                     print("achieve_complete_2 보상", imgs_)
        #                     click_x = imgs_.x + 40
        #                     click_y = imgs_.y
        #                     click_pos_reg(click_x, click_y, cla)
        #                     time.sleep(0.2)
        #
        #                     isGet_1 = False
        #                     while isGet_1 is False:
        #                         time.sleep(0.1)
        #                         full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\achieve\\achieve_complete_ing.png"
        #                         img_array = np.fromfile(full_path, np.uint8)
        #                         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #                         imgs_ = imgs_set(800, 280, 950, 340, cla, img)
        #                         time.sleep(0.1)
        #                         if imgs_ is not None and imgs_ != False:
        #                             isGet_1 = True
        #                             time.sleep(0.1)
        #                         else:
        #                             print("achieve_complete_1 빠른획득")
        #                             click_pos_reg(click_x, click_y, cla)
        #                             time.sleep(0.3)
        #
        #                     isGet_2 = False
        #                     while isGet_2 is False:
        #                         time.sleep(0.1)
        #                         full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\achieve\\upjuk.png"
        #                         img_array = np.fromfile(full_path, np.uint8)
        #                         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #                         imgs_ = imgs_set(30, 30, 200, 150, cla, img)
        #                         time.sleep(0.1)
        #                         if imgs_ is not None and imgs_ != False:
        #                             isGet_2 = True
        #                             print("achieve_complete_1 느린 획득")
        #                             time.sleep(0.1)
        #                         else:
        #                             click_pos_reg(click_x, click_y, cla)
        #                             time.sleep(0.3)
        #
        #                 else:
        #                     isachieve_complete_2 = True
        #             if i == len(datas) - 1:
        #                 isachieve_ = True
        #                 print("업적 획득 끝")
        #                 time.sleep(0.3)
        #                 click_pos_2(920, 55, cla)
        #                 time.sleep(1)
        #
        #
        #     else:
        #         time.sleep(0.5)
        #         click_pos_2(920, 55, cla)
        #         time.sleep(1)
        #         isMenu = False
        #         while isMenu is False:
        #             result_menu = menuOpenCheck(cla, "achieve_get_1")
        #             if result_menu == True:
        #                 isMenu = True
        #                 time.sleep(0.5)
        #                 click_pos_2(920, 220, cla)
        #                 time.sleep(2)
        #                 result_menu = menuOpenCheck(cla, "achieve_get_2")
        #                 if result_menu == True:
        #                     isMenu = True
        #                     isguild_ = False
        #                     print("업적 비활성화 상태")
        #                     time.sleep(0.5)
        #                     click_pos_2(920, 55, cla)
        #                     time.sleep(1)
        #             else:
        #                 time.sleep(0.5)
        #                 click_pos_2(920, 55, cla)
        #                 time.sleep(1)
    except Exception as e:
        print(e)
        return 0


def special_package(cla):
    try:
        from myfunction import menuOpenCheck, imgs_set_, click_pos_reg, click_pos_2
        from clean import clean_screen
        import numpy as np
        import cv2
        print("스폐샬 팩키지 얻기 시작")

        # clean_screen(cla, "special_package")
        #
        # isSP_ = False
        #
        # isSpecial_Package = False
        # while isSpecial_Package is False:
        #     ismenu_ = menuOpenCheck(cla, "special_package")
        #     time.sleep(0.5)
        #     if ismenu_ == False:
        #         click_pos_2(920, 55, cla)
        #     else:
        #         isSpecial_Package = True
        #         full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\special_package\\point_1.png"
        #         img_array = np.fromfile(full_path, np.uint8)
        #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #         imgs_ = imgs_set_(730, 25, 780, 60, cla, img, 0.8)
        #         if imgs_ is None or imgs_ == False:
        #             print("(point_1)가 없다...")
        #             full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\special_package\\point_2.png"
        #             img_array = np.fromfile(full_path, np.uint8)
        #             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #             imgs_ = imgs_set_(730, 25, 780, 60, cla, img, 0.8)
        #             if imgs_ is None or imgs_ == False:
        #                 print("(point_2)가 없다...")
        #                 full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\special_package\\point_3.png"
        #                 img_array = np.fromfile(full_path, np.uint8)
        #                 img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #                 imgs_ = imgs_set_(730, 25, 780, 60, cla, img, 0.8)
        #                 if imgs_ is None or imgs_ == False:
        #                     print("(point_3)가 없다...")
        #                     isSP_ = True
        #                 else:
        #                     print("(point_3)가 있다...", imgs_)
        #                     click_pos_reg(imgs_.x, imgs_.y, cla)
        #                     time.sleep(0.5)
        #             else:
        #                 print("(point_2)가 있다...", imgs_)
        #                 click_pos_reg(imgs_.x, imgs_.y, cla)
        #                 time.sleep(0.5)
        #         else:
        #             print("(point_1)가 있다...", imgs_)
        #             click_pos_reg(imgs_.x, imgs_.y, cla)
        #             time.sleep(0.5)
        #
        #
        # if isSP_ == False:
        #     time.sleep(1)
        #     full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\special_package\\special_package.png"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(400, 270, 540, 330, cla, img, 0.8)
        #     if imgs_ is not None:
        #         click_pos_2(840, 370, cla)
        #         time.sleep(0.5)
        #         time.sleep(0.5)
        #         click_pos_2(270, 750, cla)
        #         time.sleep(1)
        #         isClick = False
        #         while isClick is False:
        #             full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\special_package\\special_package.png"
        #             img_array = np.fromfile(full_path, np.uint8)
        #             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #             imgs_ = imgs_set_(400, 270, 540, 330, cla, img, 0.8)
        #             if imgs_ is None:
        #                 print("받는 중")
        #                 click_pos_2(475, 315, cla)
        #                 time.sleep(1)
        #             else:
        #                 isClick = True
        #                 click_pos_2(475, 315, cla)
        #                 time.sleep(1)
        #     else:
        #         print("이미 특별패키지를 받은 상태")
        #
        #
        #
        #     full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\special_package\\special_package.png"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(400, 270, 540, 330, cla, img, 0.8)
        #     if imgs_ is not None:
        #         print("받기 완료")
        #         click_pos_2(915, 310, cla)
        #         time.sleep(1)
        #     else:
        #         print("특별패키지 받는 중")
        #         click_pos_2(475, 315, cla)
        #         time.sleep(0.3)
        #
        #
        # full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\special_package\\x.png"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(870, 270, 950, 350, cla, img, 0.8)
        # if imgs_ is not None:
        #     click_pos_reg(imgs_.x, imgs_.y, cla)
        #     time.sleep(1)
        # ismenu_ = menuOpenCheck(cla, "special_package 받기 완료")
        # if ismenu_ == True:
        #     click_pos_2(920, 55, cla)

    except Exception as e:
        print(e)
        return 0
