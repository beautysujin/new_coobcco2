# import numpy as np
# import cv2
import time
# import re


import sys
sys.path.append('C:/my_games/coobcco2/data_od/mymodule')

# from action import *
# from where import *
# from myfunction import *

def go_test(cla):
    print('hi test! chango', cla)

def go_chango(cla, data):
    try:
        from myfunction import imgs_set, imgs_set_, click_pos_reg, click_pos_2, drag_pos
        import numpy as np
        import cv2


        go_ = False
        if cla == 'one':
            plus = 0
        if cla == 'two':
            plus = 960

        if data == 'village':
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\chango_1.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(620, 950, 705, 1005, cla, img)

            if imgs_ is None or imgs_ == False:
                print("창고그림이 안보여1")
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\chango_1_1.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(620, 950, 705, 1005, cla, img)

                if imgs_ is None or imgs_ == False:
                    print("창고그림이 안보여2")
                else:
                    print("창고그림이 보여2")
                    go_ = True
            else:
                print("창고그림이 보여1")
                go_ = True
        if data == 'chango':
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\chango_2.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(25, 35, 100, 70, cla, img)

            if imgs_ is None or imgs_ == False:
                print("창고 글자가 안보여")
            else:
                print("창고 글자가 보여")
                go_ = True

        if data == 'in':

            drag_bool = go_chango_drag(cla)

            for i in range(5):
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\jangbi_out\\event_item_2.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(540, 70, 950, 980, cla, img, 0.6)

                if imgs_ is None or imgs_ == False:
                    print("evnet_item(out_이)가 없다...")
                else:
                    print("있나", imgs_)
                    click_pos_reg(imgs_.x - 20, imgs_.y, cla)
                    time.sleep(0.3)
                    click_pos_2(890, 1010, cla)
                    time.sleep(0.3)

            for z in range(3):

                item_list_ = my_jangbi_out()
                item_list = item_list_.split("\n")
                item_count = 0
                for i in range(len(item_list)):
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\jangbi_out\\" + item_list[i] + ".png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(540, 70, 950, 980, cla, img, 0.8)
                    if imgs_ is None or imgs_ == False:
                        print(item_list[i] + "(in_이)가 없다...")
                    else:
                        item_count += 1
                        print(item_list[i], imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
                if item_count > 0:
                    click_pos_2(890, 1010, cla)
                    click_pos_2(890, 1010, cla)
                    time.sleep(0.3)
            for z in range(1):
                item_list_ = my_auction_in()
                item_list = item_list_.split("\n")
                item_count = 0
                for i in range(len(item_list)):
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\auction_in\\" + item_list[i] + ".png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(540, 70, 950, 980, cla, img, 0.8)
                    # test
                    if imgs_ is None or imgs_ == False:
                        print(item_list[i] + "(in_이)가 없다...")
                    else:
                        item_count += 1
                        print(item_list[i] + "(in_이)가 있다...")
                        print(item_list[i], imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)
                if item_count > 0:
                    click_pos_2(890, 1010, cla)
                    time.sleep(0.3)

                item_list_ = my_jangbi_in()
                item_list = item_list_.split("\n")
                for i in range(len(item_list)):
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\jangbi_in\\" + item_list[i] + ".png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(540, 70, 950, 980, cla, img, 0.8)
                    # test
                    if imgs_ is None or imgs_ == False:
                        print(item_list[i] + "(in_이)가 없다...")
                    else:
                        print(item_list[i] + "(in_이)가 있다...")
                        print(item_list[i], imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)

                        if cla == "one":
                            cla_x = imgs_.x
                        if cla == "two":
                            cla_x = imgs_.x - 960

                        if imgs_.x > 810 + plus:
                            print("한번더 나누기")
                            if 810 + plus < imgs_.x < 860 + plus:
                                imgs_2 = imgs_set(cla_x + 20, imgs_.y - 30, cla_x + 100, imgs_.y + 45,
                                                  cla,
                                                  img)

                                if imgs_2 is None or imgs_2 == False:
                                    print(item_list[i] + "(in_이)가 없다...2")
                                else:
                                    print(item_list[i] + "(in_이)가 있다...2")
                                    click_pos_reg(imgs_.x + 70, imgs_.y, cla)
                                    time.sleep(0.5)
                                imgs_3 = imgs_set(cla_x - 240, imgs_.y + 20, cla_x - 160, imgs_.y + 120,
                                                  cla, img)
                                if imgs_3 is None or imgs_3 == False:
                                    print(item_list[i] + "(in_이)가 없다...3")
                                else:
                                    print(item_list[i] + "(in_이)가 있다...3")
                                    click_pos_reg(imgs_.x - 200, imgs_.y + 70, cla)
                                    time.sleep(0.5)
                            if 880 + plus < imgs_.x < 930 + plus:
                                imgs_4 = imgs_set(cla_x - 330, imgs_.y + 20, cla_x - 240, imgs_.y + 120,
                                                  cla, img)
                                if imgs_4 is None or imgs_4 == False:
                                    print(item_list[i] + "(in_이)가 없다...4")
                                else:
                                    print(item_list[i] + "(in_이)가 있다...4")
                                    click_pos_reg(imgs_.x - 285, imgs_.y + 70, cla)
                                    time.sleep(0.5)
                                imgs_5 = imgs_set(cla_x - 240, imgs_.y + 20, cla_x - 160, imgs_.y + 120,
                                                  cla, img)
                                if imgs_5 is None or imgs_5 == False:
                                    print(item_list[i] + "(in_이)가 없다...5")
                                else:
                                    print(item_list[i] + "(in_이)가 있다...5")
                                    click_pos_reg(imgs_.x - 200, imgs_.y + 70, cla)
                                    time.sleep(0.5)
                        else:
                            imgs_6 = imgs_set(cla_x + 40, imgs_.y - 40, cla_x + 100, imgs_.y + 45, cla,
                                              img)
                            if imgs_6 is None or imgs_6 == False:
                                print(item_list[i] + "(in_이)가 없다...6")
                                print("*", imgs_)
                            else:
                                print(item_list[i] + "(in_이)가 있다...6")
                                click_pos_reg(imgs_.x + 70, imgs_.y, cla)
                                time.sleep(0.5)

                            imgs_7 = imgs_set(cla_x + 100, imgs_.y - 40, cla_x + 180, imgs_.y + 45,
                                              cla, img)
                            if imgs_7 is None or imgs_7 == False:
                                print(item_list[i] + "(in_이)가 없다...7")
                            else:
                                print(item_list[i] + "(in_이)가 있다...7")
                                click_pos_reg(imgs_.x + 140, imgs_.y, cla)
                                time.sleep(0.5)
                        click_pos_2(900, 1005, cla)
                        time.sleep(0.5)
            if drag_bool == True:
                drag_pos(800, 900, 800, 200, cla)
                time.sleep(1)

                # for z in range(3):
                #
                #     item_list_ = my_jangbi_out()
                #     item_list = item_list_.split("\n")
                #     for i in range(len(item_list)):
                #         full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\jangbi_out\\" + item_list[i] + ".png"
                #         img_array = np.fromfile(full_path, np.uint8)
                #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #         imgs_ = imgs_set_(540, 70, 950, 980, cla, img, 0.8)
                #         if imgs_ is None or imgs_ == False:
                #             print(item_list[i] + "(in_이)가 없다...")
                #         else:
                #             print(item_list[i], imgs_)
                #             click_pos_reg(imgs_.x, imgs_.y, cla)
                #             time.sleep(0.2)
                #     click_pos_2(890, 1010, cla)
                #     time.sleep(0.3)
                for z in range(2):

                    item_list_ = my_jangbi_in()
                    item_list = item_list_.split("\n")
                    for i in range(len(item_list)):
                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\jangbi_in\\" + item_list[i] + ".png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(540, 70, 950, 980, cla, img, 0.85)
                        # test
                        if imgs_ is None or imgs_ == False:
                            print(item_list[i] + "(in_이)가 없다...")
                        else:
                            print(item_list[i] + "(in_이)가 있다...")
                            print(item_list[i], imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)

                            if cla == "one":
                                cla_x = imgs_.x
                            if cla == "two":
                                cla_x = imgs_.x - 960

                            if imgs_.x > 810 + plus:
                                print("한번더 나누기")
                                if 810 + plus < imgs_.x < 860 + plus:
                                    imgs_2 = imgs_set_(cla_x + 20, imgs_.y - 30, cla_x + 100, imgs_.y + 45,
                                                      cla, img, 0.85)

                                    if imgs_2 is None or imgs_2 == False:
                                        print(item_list[i] + "(in_이)가 없다...2")
                                    else:
                                        print(item_list[i] + "(in_이)가 있다...2")
                                        click_pos_reg(imgs_.x + 70, imgs_.y, cla)
                                        time.sleep(0.5)
                                    imgs_3 = imgs_set_(cla_x - 240, imgs_.y + 20, cla_x - 160, imgs_.y + 120,
                                                      cla, img,  0.85)
                                    if imgs_3 is None or imgs_3 == False:
                                        print(item_list[i] + "(in_이)가 없다...3")
                                    else:
                                        print(item_list[i] + "(in_이)가 있다...3")
                                        click_pos_reg(imgs_.x - 200, imgs_.y + 70, cla)
                                        time.sleep(0.5)
                                if 880 + plus < imgs_.x < 930 + plus:
                                    imgs_4 = imgs_set_(cla_x - 330, imgs_.y + 20, cla_x - 240, imgs_.y + 120,
                                                      cla, img, 0.85)
                                    if imgs_4 is None or imgs_4 == False:
                                        print(item_list[i] + "(in_이)가 없다...4")
                                    else:
                                        print(item_list[i] + "(in_이)가 있다...4")
                                        click_pos_reg(imgs_.x - 285, imgs_.y + 70, cla)
                                        time.sleep(0.5)
                                    imgs_5 = imgs_set_(cla_x - 240, imgs_.y + 20, cla_x - 160, imgs_.y + 120,
                                                      cla, img, 0.85)
                                    if imgs_5 is None or imgs_5 == False:
                                        print(item_list[i] + "(in_이)가 없다...5")
                                    else:
                                        print(item_list[i] + "(in_이)가 있다...5")
                                        click_pos_reg(imgs_.x - 200, imgs_.y + 70, cla)
                                        time.sleep(0.5)
                            else:
                                imgs_6 = imgs_set_(cla_x + 40, imgs_.y - 40, cla_x + 100, imgs_.y + 45, cla, img,
                                                  0.85)
                                if imgs_6 is None or imgs_6 == False:
                                    print(item_list[i] + "(in_이)가 없다...6")
                                    print("*", imgs_)
                                else:
                                    print(item_list[i] + "(in_이)가 있다...6")
                                    click_pos_reg(imgs_.x + 70, imgs_.y, cla)
                                    time.sleep(0.5)

                                imgs_7 = imgs_set_(cla_x + 100, imgs_.y - 40, cla_x + 180, imgs_.y + 45,
                                                  cla, img, 0.85)
                                if imgs_7 is None or imgs_7 == False:
                                    print(item_list[i] + "(in_이)가 없다...7")
                                else:
                                    print(item_list[i] + "(in_이)가 있다...7")
                                    click_pos_reg(imgs_.x + 140, imgs_.y, cla)
                                    time.sleep(0.5)
                            click_pos_2(900, 1005, cla)
                            time.sleep(0.5)
                            # drag_pos(800, 900, 800, 200, cla)
                            time.sleep(0.5)
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\jangbi_in\\gold.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(540, 70, 950, 980, cla, img, 0.9)
                # test
                if imgs_ is None or imgs_ == False:
                    print(item_list[i] + "(in_이)가 없다...")
                else:
                    print(item_list[i] + "(in_이)가 있다...")
                    print(item_list[i], imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.2)

                    if cla == "one":
                        cla_x = imgs_.x
                    if cla == "two":
                        cla_x = imgs_.x - 960

                    if imgs_.x > 810 + plus:
                        print("한번더 나누기")
                        if 810 + plus < imgs_.x < 860 + plus:
                            imgs_2 = imgs_set(cla_x + 20, imgs_.y - 30, cla_x + 100, imgs_.y + 45,
                                              cla,
                                              img)

                            if imgs_2 is None or imgs_2 == False:
                                print(item_list[i] + "(in_이)가 없다...2")
                            else:
                                print(item_list[i] + "(in_이)가 있다...2")
                                click_pos_reg(imgs_.x + 70, imgs_.y, cla)
                                time.sleep(0.5)
                            imgs_3 = imgs_set(cla_x - 240, imgs_.y + 20, cla_x - 160, imgs_.y + 120,
                                              cla, img)
                            if imgs_3 is None or imgs_3 == False:
                                print(item_list[i] + "(in_이)가 없다...3")
                            else:
                                print(item_list[i] + "(in_이)가 있다...3")
                                click_pos_reg(imgs_.x - 200, imgs_.y + 70, cla)
                                time.sleep(0.5)
                        if 880 + plus < imgs_.x < 930 + plus:
                            imgs_4 = imgs_set(cla_x - 330, imgs_.y + 20, cla_x - 240, imgs_.y + 120,
                                              cla, img)
                            if imgs_4 is None or imgs_4 == False:
                                print(item_list[i] + "(in_이)가 없다...4")
                            else:
                                print(item_list[i] + "(in_이)가 있다...4")
                                click_pos_reg(imgs_.x - 285, imgs_.y + 70, cla)
                                time.sleep(0.5)
                            imgs_5 = imgs_set(cla_x - 240, imgs_.y + 20, cla_x - 160, imgs_.y + 120,
                                              cla, img)
                            if imgs_5 is None or imgs_5 == False:
                                print(item_list[i] + "(in_이)가 없다...5")
                            else:
                                print(item_list[i] + "(in_이)가 있다...5")
                                click_pos_reg(imgs_.x - 200, imgs_.y + 70, cla)
                                time.sleep(0.5)
                    else:
                        imgs_6 = imgs_set(cla_x + 40, imgs_.y - 40, cla_x + 100, imgs_.y + 45, cla,
                                          img)
                        if imgs_6 is None or imgs_6 == False:
                            print(item_list[i] + "(in_이)가 없다...6")
                            print("*", imgs_)
                        else:
                            print(item_list[i] + "(in_이)가 있다...6")
                            click_pos_reg(imgs_.x + 70, imgs_.y, cla)
                            time.sleep(0.5)

                        imgs_7 = imgs_set(cla_x + 100, imgs_.y - 40, cla_x + 180, imgs_.y + 45,
                                          cla, img)
                        if imgs_7 is None or imgs_7 == False:
                            print(item_list[i] + "(in_이)가 없다...7")
                        else:
                            print(item_list[i] + "(in_이)가 있다...7")
                            click_pos_reg(imgs_.x + 140, imgs_.y, cla)
                            time.sleep(0.5)
                    click_pos_2(900, 1005, cla)
                    time.sleep(0.5)
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\jangbi_in\\silver.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(540, 70, 950, 980, cla, img, 0.9)
                # test
                if imgs_ is None or imgs_ == False:
                    print(item_list[i] + "(in_이)가 없다...")
                else:
                    print(item_list[i] + "(in_이)가 있다...")
                    print(item_list[i], imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.2)

                    if cla == "one":
                        cla_x = imgs_.x
                    if cla == "two":
                        cla_x = imgs_.x - 960

                    if imgs_.x > 810 + plus:
                        print("한번더 나누기")
                        if 810 + plus < imgs_.x < 860 + plus:
                            imgs_2 = imgs_set(cla_x + 20, imgs_.y - 30, cla_x + 100, imgs_.y + 45,
                                              cla,
                                              img)

                            if imgs_2 is None or imgs_2 == False:
                                print(item_list[i] + "(in_이)가 없다...2")
                            else:
                                print(item_list[i] + "(in_이)가 있다...2")
                                click_pos_reg(imgs_.x + 70, imgs_.y, cla)
                                time.sleep(0.5)
                            imgs_3 = imgs_set(cla_x - 240, imgs_.y + 20, cla_x - 160, imgs_.y + 120,
                                              cla, img)
                            if imgs_3 is None or imgs_3 == False:
                                print(item_list[i] + "(in_이)가 없다...3")
                            else:
                                print(item_list[i] + "(in_이)가 있다...3")
                                click_pos_reg(imgs_.x - 200, imgs_.y + 70, cla)
                                time.sleep(0.5)
                        if 880 + plus < imgs_.x < 930 + plus:
                            imgs_4 = imgs_set(cla_x - 330, imgs_.y + 20, cla_x - 240, imgs_.y + 120,
                                              cla, img)
                            if imgs_4 is None or imgs_4 == False:
                                print(item_list[i] + "(in_이)가 없다...4")
                            else:
                                print(item_list[i] + "(in_이)가 있다...4")
                                click_pos_reg(imgs_.x - 285, imgs_.y + 70, cla)
                                time.sleep(0.5)
                            imgs_5 = imgs_set(cla_x - 240, imgs_.y + 20, cla_x - 160, imgs_.y + 120,
                                              cla, img)
                            if imgs_5 is None or imgs_5 == False:
                                print(item_list[i] + "(in_이)가 없다...5")
                            else:
                                print(item_list[i] + "(in_이)가 있다...5")
                                click_pos_reg(imgs_.x - 200, imgs_.y + 70, cla)
                                time.sleep(0.5)
                    else:
                        imgs_6 = imgs_set(cla_x + 40, imgs_.y - 40, cla_x + 100, imgs_.y + 45, cla,
                                          img)
                        if imgs_6 is None or imgs_6 == False:
                            print(item_list[i] + "(in_이)가 없다...6")
                            print("*", imgs_)
                        else:
                            print(item_list[i] + "(in_이)가 있다...6")
                            click_pos_reg(imgs_.x + 70, imgs_.y, cla)
                            time.sleep(0.5)

                        imgs_7 = imgs_set(cla_x + 100, imgs_.y - 40, cla_x + 180, imgs_.y + 45,
                                          cla, img)
                        if imgs_7 is None or imgs_7 == False:
                            print(item_list[i] + "(in_이)가 없다...7")
                        else:
                            print(item_list[i] + "(in_이)가 있다...7")
                            click_pos_reg(imgs_.x + 140, imgs_.y, cla)
                            time.sleep(0.5)
                    click_pos_2(900, 1005, cla)
                    time.sleep(0.5)


        if data == 'out':

            for i in range(5):
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\jangbi_out\\event_item_2.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 195, 300, 980, cla, img, 0.6)

                if imgs_ is None or imgs_ == False:
                    print("evnet_item(out_이)가 없다...")
                else:
                    print("있나", imgs_)
                    click_pos_reg(imgs_.x - 20, imgs_.y, cla)
                    time.sleep(0.3)
                    click_pos_2(240, 1010, cla)
                    time.sleep(0.3)

            for z in range(3):

                item_list_ = my_jangbi_out()
                item_list = item_list_.split("\n")
                item_count = 0
                for i in range(len(item_list)):
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\jangbi_out\\" + item_list[i] + ".png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 195, 300, 980, cla, img, 0.8)

                    if imgs_ is None or imgs_ == False:
                        print(item_list[i] + "(out_이)가 없다...")
                    else:
                        item_count += 1
                        print(item_list[i], imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
                if item_count > 0:
                    click_pos_2(240, 1010, cla)
                    time.sleep(0.3)


        if data == 'auction':

            item_list_ = my_auction_in()
            item_list = item_list_.split("\n")
            item_count = 0
            for i in range(len(item_list)):
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\auction_in\\" + item_list[i] + ".png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 195, 300, 980, cla, img, 0.8)
                # test
                if imgs_ is None or imgs_ == False:
                    print(item_list[i] + "(in_이)가 없다...")
                else:
                    item_count += 1
                    print(item_list[i] + "(in_이)가 있다...")
                    print(item_list[i], imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.3)
            if item_count >0:
                click_pos_2(240, 1005, cla)
                time.sleep(0.5)

            item_list_ = my_auction_in_item()
            item_list = item_list_.split("\n")
            for i in range(len(item_list)):
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\jangbi_in\\" + item_list[i] + ".png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 195, 300, 980, cla, img, 0.8)
                # test
                if imgs_ is None or imgs_ == False:
                    print(item_list[i] + "(in_이)가 없다...")
                else:
                    print(item_list[i] + "(in_이)가 있다...")
                    print(item_list[i], imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.3)

                    if cla == "one":
                        cla_x = imgs_.x
                    if cla == "two":
                        cla_x = imgs_.x - 960

                    if imgs_.x > 160 + plus:
                        print("한번더 나누기")
                        if 160 + plus < imgs_.x < 210 + plus:
                            imgs_2 = imgs_set_(cla_x + 20, imgs_.y - 30, cla_x + 100, imgs_.y + 45,
                                              cla,
                                              img, 0.8)

                            if imgs_2 is None or imgs_2 == False:
                                print(item_list[i] + "(in_이)가 없다...2")
                            else:
                                print(item_list[i] + "(in_이)가 있다...2")
                                click_pos_reg(imgs_.x + 70, imgs_.y, cla)
                                time.sleep(0.2)
                            imgs_3 = imgs_set_(cla_x - 180, imgs_.y + 20, cla_x - 90, imgs_.y + 120,
                                              cla, img, 0.8)
                            if imgs_3 is None or imgs_3 == False:
                                print(item_list[i] + "(in_이)가 없다...3")
                            else:
                                print(item_list[i] + "(in_이)가 있다...3")
                                click_pos_reg(imgs_.x - 140, imgs_.y + 70, cla)
                                time.sleep(0.3)
                        if 230 + plus < imgs_.x < 280 + plus:
                            if imgs_.x - 250 > 0:
                                result_x = cla_x - 250
                            else:
                                result_x = 0
                            imgs_4 = imgs_set_(result_x, imgs_.y + 20, cla_x - 170, imgs_.y + 120,
                                              cla, img, 0.8)
                            if imgs_4 is None or imgs_4 == False:
                                print(item_list[i] + "(in_이)가 없다...4")
                            else:
                                print(item_list[i] + "(in_이)가 있다...4")
                                click_pos_reg(imgs_.x - 210, imgs_.y + 70, cla)
                                time.sleep(0.2)
                            imgs_5 = imgs_set_(cla_x - 180, imgs_.y + 20, cla_x - 90, imgs_.y + 120,
                                              cla, img, 0.8)
                            if imgs_5 is None or imgs_5 == False:
                                print(item_list[i] + "(in_이)가 없다...5")
                            else:
                                print(item_list[i] + "(in_이)가 있다...5")
                                click_pos_reg(imgs_.x - 140, imgs_.y + 70, cla)
                                time.sleep(0.3)
                    else:
                        imgs_6 = imgs_set_(cla_x + 40, imgs_.y - 40, cla_x + 100, imgs_.y + 45, cla,
                                          img, 0.8)
                        if imgs_6 is None or imgs_6 == False:
                            print(item_list[i] + "(in_이)가 없다...6")
                            print("*", imgs_)
                        else:
                            print(item_list[i] + "(in_이)가 있다...6")
                            click_pos_reg(imgs_.x + 70, imgs_.y, cla)
                            time.sleep(0.2)

                        imgs_7 = imgs_set_(cla_x + 100, imgs_.y - 40, cla_x + 180, imgs_.y + 45,
                                          cla, img, 0.8)
                        if imgs_7 is None or imgs_7 == False:
                            print(item_list[i] + "(in_이)가 없다...7")
                        else:
                            print(item_list[i] + "(in_이)가 있다...7")
                            click_pos_reg(imgs_.x + 140, imgs_.y, cla)
                            time.sleep(0.3)
                    click_pos_2(240, 1005, cla)
                    time.sleep(0.5)


            drag_pos(150, 900, 150, 300, cla)
            time.sleep(1)

            item_list_ = my_auction_in_item()
            item_list = item_list_.split("\n")
            for i in range(len(item_list)):
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\jangbi_in\\" + item_list[i] + ".png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 195, 300, 980, cla, img, 0.8)
                # test
                if imgs_ is None or imgs_ == False:
                    print(item_list[i] + "(in_이)가 없다...")
                else:
                    print(item_list[i] + "(in_이)가 있다...")
                    print(item_list[i], imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.3)

                    if cla == "one":
                        cla_x = imgs_.x
                    if cla == "two":
                        cla_x = imgs_.x - 960

                    if imgs_.x > 160 + plus:
                        print("한번더 나누기")
                        if 160 + plus < imgs_.x < 210 + plus:
                            imgs_2 = imgs_set_(cla_x + 20, imgs_.y - 30, cla_x + 100, imgs_.y + 45,
                                               cla,
                                               img, 0.8)

                            if imgs_2 is None or imgs_2 == False:
                                print(item_list[i] + "(in_이)가 없다...2")
                            else:
                                print(item_list[i] + "(in_이)가 있다...2")
                                click_pos_reg(imgs_.x + 70, imgs_.y, cla)
                                time.sleep(0.2)
                            imgs_3 = imgs_set_(cla_x - 180, imgs_.y + 20, cla_x - 90, imgs_.y + 120,
                                               cla, img, 0.8)
                            if imgs_3 is None or imgs_3 == False:
                                print(item_list[i] + "(in_이)가 없다...3")
                            else:
                                print(item_list[i] + "(in_이)가 있다...3")
                                click_pos_reg(imgs_.x - 140, imgs_.y + 70, cla)
                                time.sleep(0.3)
                        if 230 + plus < imgs_.x < 280 + plus:
                            if imgs_.x - 250 > 0:
                                result_x = cla_x - 250
                            else:
                                result_x = 0
                            imgs_4 = imgs_set_(result_x, imgs_.y + 20, cla_x - 170, imgs_.y + 120,
                                               cla, img, 0.8)
                            if imgs_4 is None or imgs_4 == False:
                                print(item_list[i] + "(in_이)가 없다...4")
                            else:
                                print(item_list[i] + "(in_이)가 있다...4")
                                click_pos_reg(imgs_.x - 210, imgs_.y + 70, cla)
                                time.sleep(0.2)
                            imgs_5 = imgs_set_(cla_x - 180, imgs_.y + 20, cla_x - 90, imgs_.y + 120,
                                               cla, img, 0.8)
                            if imgs_5 is None or imgs_5 == False:
                                print(item_list[i] + "(in_이)가 없다...5")
                            else:
                                print(item_list[i] + "(in_이)가 있다...5")
                                click_pos_reg(imgs_.x - 140, imgs_.y + 70, cla)
                                time.sleep(0.3)
                    else:
                        imgs_6 = imgs_set_(cla_x + 40, imgs_.y - 40, cla_x + 100, imgs_.y + 45, cla,
                                           img, 0.8)
                        if imgs_6 is None or imgs_6 == False:
                            print(item_list[i] + "(in_이)가 없다...6")
                            print("*", imgs_)
                        else:
                            print(item_list[i] + "(in_이)가 있다...6")
                            click_pos_reg(imgs_.x + 70, imgs_.y, cla)
                            time.sleep(0.2)

                        imgs_7 = imgs_set_(cla_x + 100, imgs_.y - 40, cla_x + 180, imgs_.y + 45,
                                           cla, img, 0.8)
                        if imgs_7 is None or imgs_7 == False:
                            print(item_list[i] + "(in_이)가 없다...7")
                        else:
                            print(item_list[i] + "(in_이)가 있다...7")
                            click_pos_reg(imgs_.x + 140, imgs_.y, cla)
                            time.sleep(0.3)
                    click_pos_2(240, 1005, cla)
                    time.sleep(0.5)

            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\jangbi_in\\gold.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 195, 300, 980, cla, img, 0.9)
            # test
            if imgs_ is None or imgs_ == False:
                print(item_list[i] + "(in_이)가 없다...")
            else:
                print(item_list[i] + "(in_이)가 있다...")
                print(item_list[i], imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.2)

                if cla == "one":
                    cla_x = imgs_.x
                if cla == "two":
                    cla_x = imgs_.x - 960

                if imgs_.x > 160 + plus:
                    print("한번더 나누기")
                    if 160 + plus < imgs_.x < 210 + plus:
                        imgs_2 = imgs_set_(cla_x + 20, imgs_.y - 30, cla_x + 100, imgs_.y + 45,
                                           cla,
                                           img, 0.85)

                        if imgs_2 is None or imgs_2 == False:
                            print(item_list[i] + "(in_이)가 없다...2")
                        else:
                            print(item_list[i] + "(in_이)가 있다...2")
                            click_pos_reg(imgs_.x + 70, imgs_.y, cla)
                            time.sleep(0.5)
                        imgs_3 = imgs_set_(cla_x - 180, imgs_.y + 20, cla_x - 90, imgs_.y + 120,
                                           cla, img, 0.85)
                        if imgs_3 is None or imgs_3 == False:
                            print(item_list[i] + "(in_이)가 없다...3")
                        else:
                            print(item_list[i] + "(in_이)가 있다...3")
                            click_pos_reg(imgs_.x - 140, imgs_.y + 70, cla)
                            time.sleep(0.5)
                    if 230 + plus < imgs_.x < 280 + plus:
                        if imgs_.x - 250 > 0:
                            result_x = cla_x - 250
                        else:
                            result_x = 0
                        imgs_4 = imgs_set_(result_x, imgs_.y + 20, cla_x - 170, imgs_.y + 120,
                                           cla, img, 0.85)
                        if imgs_4 is None or imgs_4 == False:
                            print(item_list[i] + "(in_이)가 없다...4")
                        else:
                            print(item_list[i] + "(in_이)가 있다...4")
                            click_pos_reg(imgs_.x - 210, imgs_.y + 70, cla)
                            time.sleep(0.2)
                        imgs_5 = imgs_set_(cla_x - 180, imgs_.y + 20, cla_x - 90, imgs_.y + 120,
                                           cla, img, 0.85)
                        if imgs_5 is None or imgs_5 == False:
                            print(item_list[i] + "(in_이)가 없다...5")
                        else:
                            print(item_list[i] + "(in_이)가 있다...5")
                            click_pos_reg(imgs_.x - 140, imgs_.y + 70, cla)
                            time.sleep(0.3)
                else:
                    imgs_6 = imgs_set_(cla_x + 40, imgs_.y - 40, cla_x + 100, imgs_.y + 45, cla,
                                       img, 0.85)
                    if imgs_6 is None or imgs_6 == False:
                        print(item_list[i] + "(in_이)가 없다...6")
                        print("*", imgs_)
                    else:
                        print(item_list[i] + "(in_이)가 있다...6")
                        click_pos_reg(imgs_.x + 70, imgs_.y, cla)
                        time.sleep(0.2)

                    imgs_7 = imgs_set_(cla_x + 100, imgs_.y - 40, cla_x + 180, imgs_.y + 45,
                                       cla, img, 0.85)
                    if imgs_7 is None or imgs_7 == False:
                        print(item_list[i] + "(in_이)가 없다...7")
                    else:
                        print(item_list[i] + "(in_이)가 있다...7")
                        click_pos_reg(imgs_.x + 140, imgs_.y, cla)
                        time.sleep(0.3)
                click_pos_2(240, 1010, cla)
                time.sleep(0.5)

            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\jangbi_in\\silver.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 195, 300, 980, cla, img, 0.9)
            # test
            if imgs_ is None or imgs_ == False:
                print(item_list[i] + "(in_이)가 없다...")
            else:
                print(item_list[i] + "(in_이)가 있다...")
                print(item_list[i], imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.2)

                if cla == "one":
                    cla_x = imgs_.x
                if cla == "two":
                    cla_x = imgs_.x - 960

                if imgs_.x > 160 + plus:
                    print("한번더 나누기")
                    if 160 + plus < imgs_.x < 210 + plus:
                        imgs_2 = imgs_set_(cla_x + 20, imgs_.y - 30, cla_x + 100, imgs_.y + 45,
                                           cla,
                                           img, 0.85)

                        if imgs_2 is None or imgs_2 == False:
                            print(item_list[i] + "(in_이)가 없다...2")
                        else:
                            print(item_list[i] + "(in_이)가 있다...2")
                            click_pos_reg(imgs_.x + 70, imgs_.y, cla)
                            time.sleep(0.5)
                        imgs_3 = imgs_set_(cla_x - 180, imgs_.y + 20, cla_x - 90, imgs_.y + 120,
                                           cla, img, 0.85)
                        if imgs_3 is None or imgs_3 == False:
                            print(item_list[i] + "(in_이)가 없다...3")
                        else:
                            print(item_list[i] + "(in_이)가 있다...3")
                            click_pos_reg(imgs_.x - 140, imgs_.y + 70, cla)
                            time.sleep(0.5)
                    if 230 + plus < imgs_.x < 280 + plus:
                        if imgs_.x - 250 > 0:
                            result_x = cla_x - 250
                        else:
                            result_x = 0
                        imgs_4 = imgs_set_(result_x, imgs_.y + 20, cla_x - 170, imgs_.y + 120,
                                           cla, img, 0.85)
                        if imgs_4 is None or imgs_4 == False:
                            print(item_list[i] + "(in_이)가 없다...4")
                        else:
                            print(item_list[i] + "(in_이)가 있다...4")
                            click_pos_reg(imgs_.x - 210, imgs_.y + 70, cla)
                            time.sleep(0.2)
                        imgs_5 = imgs_set_(cla_x - 180, imgs_.y + 20, cla_x - 90, imgs_.y + 120,
                                           cla, img, 0.85)
                        if imgs_5 is None or imgs_5 == False:
                            print(item_list[i] + "(in_이)가 없다...5")
                        else:
                            print(item_list[i] + "(in_이)가 있다...5")
                            click_pos_reg(imgs_.x - 140, imgs_.y + 70, cla)
                            time.sleep(0.3)
                else:
                    imgs_6 = imgs_set_(cla_x + 40, imgs_.y - 40, cla_x + 100, imgs_.y + 45, cla,
                                       img, 0.85)
                    if imgs_6 is None or imgs_6 == False:
                        print(item_list[i] + "(in_이)가 없다...6")
                        print("*", imgs_)
                    else:
                        print(item_list[i] + "(in_이)가 있다...6")
                        click_pos_reg(imgs_.x + 70, imgs_.y, cla)
                        time.sleep(0.2)

                    imgs_7 = imgs_set_(cla_x + 100, imgs_.y - 40, cla_x + 180, imgs_.y + 45,
                                       cla, img, 0.85)
                    if imgs_7 is None or imgs_7 == False:
                        print(item_list[i] + "(in_이)가 없다...7")
                    else:
                        print(item_list[i] + "(in_이)가 있다...7")
                        click_pos_reg(imgs_.x + 140, imgs_.y, cla)
                        time.sleep(0.3)
                click_pos_2(240, 1010, cla)
                time.sleep(0.5)

        if data == 'auction_after':
            drag_bool = go_chango_drag(cla)
            item_list_ = my_auction_in()
            item_list = item_list_.split("\n")
            item_count = 0
            for i in range(len(item_list)):
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\auction_in\\" + item_list[i] + ".png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(540, 70, 950, 980, cla, img, 0.85)
                # test
                if imgs_ is None or imgs_ == False:
                    print(item_list[i] + "(in_이)가 없다...")
                else:
                    item_count += 1
                    print(item_list[i] + "(in_이)가 있다...")
                    print(item_list[i], imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.3)
            if item_count > 0:
                click_pos_2(900, 1005, cla)
                time.sleep(0.5)

            item_list_ = my_jangbi_in()
            item_list = item_list_.split("\n")
            for i in range(len(item_list)):
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\jangbi_in\\" + item_list[i] + ".png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(540, 70, 950, 980, cla, img, 0.85)
                # test
                if imgs_ is None or imgs_ == False:
                    print(item_list[i] + "(in_이)가 없다...")
                else:
                    print(item_list[i] + "(in_이)가 있다...")
                    print(item_list[i], imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.3)

                    if cla == "one":
                        cla_x = imgs_.x
                    if cla == "two":
                        cla_x = imgs_.x - 960

                    if imgs_.x > 810 + plus:
                        print("한번더 나누기")
                        if 810 + plus < imgs_.x < 860 + plus:
                            imgs_2 = imgs_set_(cla_x + 20, imgs_.y - 30, cla_x + 100, imgs_.y + 45,
                                              cla,
                                              img, 0.85)

                            if imgs_2 is None or imgs_2 == False:
                                print(item_list[i] + "(in_이)가 없다...2")
                            else:
                                print(item_list[i] + "(in_이)가 있다...2")
                                click_pos_reg(imgs_.x + 70, imgs_.y, cla)
                                time.sleep(0.2)
                            imgs_3 = imgs_set_(cla_x - 240, imgs_.y + 20, cla_x - 160, imgs_.y + 120,
                                              cla, img, 0.85)
                            if imgs_3 is None or imgs_3 == False:
                                print(item_list[i] + "(in_이)가 없다...3")
                            else:
                                print(item_list[i] + "(in_이)가 있다...3")
                                click_pos_reg(imgs_.x - 200, imgs_.y + 70, cla)
                                time.sleep(0.3)
                        if 880 + plus < imgs_.x < 930 + plus:
                            imgs_4 = imgs_set_(cla_x - 330, imgs_.y + 20, cla_x - 240, imgs_.y + 120,
                                              cla, img, 0.85)
                            if imgs_4 is None or imgs_4 == False:
                                print(item_list[i] + "(in_이)가 없다...4")
                            else:
                                print(item_list[i] + "(in_이)가 있다...4")
                                click_pos_reg(imgs_.x - 285, imgs_.y + 70, cla)
                                time.sleep(0.2)
                            imgs_5 = imgs_set_(cla_x - 240, imgs_.y + 20, cla_x - 160, imgs_.y + 120,
                                              cla, img, 0.85)
                            if imgs_5 is None or imgs_5 == False:
                                print(item_list[i] + "(in_이)가 없다...5")
                            else:
                                print(item_list[i] + "(in_이)가 있다...5")
                                click_pos_reg(imgs_.x - 200, imgs_.y + 70, cla)
                                time.sleep(0.3)
                    else:
                        imgs_6 = imgs_set_(cla_x + 40, imgs_.y - 40, cla_x + 100, imgs_.y + 45, cla,
                                          img, 0.85)
                        if imgs_6 is None or imgs_6 == False:
                            print(item_list[i] + "(in_이)가 없다...6")
                            print("*", imgs_)
                        else:
                            print(item_list[i] + "(in_이)가 있다...6")
                            click_pos_reg(imgs_.x + 70, imgs_.y, cla)
                            time.sleep(0.2)
                        imgs_7 = imgs_set_(cla_x + 100, imgs_.y - 40, cla_x + 180, imgs_.y + 45,
                                          cla, img, 0.85)
                        if imgs_7 is None or imgs_7 == False:
                            print(item_list[i] + "(in_이)가 없다...7")
                        else:
                            print(item_list[i] + "(in_이)가 있다...7")
                            click_pos_reg(imgs_.x + 140, imgs_.y, cla)
                            time.sleep(0.3)
                    click_pos_2(900, 1005, cla)
                    time.sleep(0.5)
            if drag_bool == True:
                drag_pos(800, 900, 800, 200, cla)
                time.sleep(1)

                item_list_ = my_jangbi_out()
                item_list = item_list_.split("\n")
                item_count = 0
                for i in range(len(item_list)):
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\jangbi_out\\" + item_list[i] + ".png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(540, 70, 950, 980, cla, img, 0.85)
                    if imgs_ is None or imgs_ == False:
                        print(item_list[i] + "(in_이)가 없다...")
                    else:
                        item_count += 1
                        print(item_list[i], imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.3)
                if item_count > 0:
                    click_pos_2(890, 1010, cla)
                    time.sleep(0.3)

                item_list_ = my_jangbi_in()
                item_list = item_list_.split("\n")
                for i in range(len(item_list)):
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\jangbi_in\\" + item_list[i] + ".png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(540, 70, 950, 980, cla, img, 0.85)
                    # test
                    if imgs_ is None or imgs_ == False:
                        print(item_list[i] + "(in_이)가 없다...")
                    else:
                        print(item_list[i] + "(in_이)가 있다...")
                        print(item_list[i], imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)

                        if cla == "one":
                            cla_x = imgs_.x
                        if cla == "two":
                            cla_x = imgs_.x - 960

                        if imgs_.x > 810 + plus:
                            print("한번더 나누기")
                            if 810 + plus < imgs_.x < 860 + plus:
                                imgs_2 = imgs_set_(cla_x + 20, imgs_.y - 30, cla_x + 100, imgs_.y + 45,
                                                  cla,
                                                  img, 0.85)

                                if imgs_2 is None or imgs_2 == False:
                                    print(item_list[i] + "(in_이)가 없다...2")
                                else:
                                    print(item_list[i] + "(in_이)가 있다...2")
                                    click_pos_reg(imgs_.x + 70, imgs_.y, cla)
                                    time.sleep(0.2)
                                imgs_3 = imgs_set_(cla_x - 240, imgs_.y + 20, cla_x - 160, imgs_.y + 120,
                                                  cla, img, 0.85)
                                if imgs_3 is None or imgs_3 == False:
                                    print(item_list[i] + "(in_이)가 없다...3")
                                else:
                                    print(item_list[i] + "(in_이)가 있다...3")
                                    click_pos_reg(imgs_.x - 200, imgs_.y + 70, cla)
                                    time.sleep(0.3)
                            if 880 + plus < imgs_.x < 930 + plus:
                                imgs_4 = imgs_set_(cla_x - 330, imgs_.y + 20, cla_x - 240, imgs_.y + 120,
                                                  cla, img, 0.85)
                                if imgs_4 is None or imgs_4 == False:
                                    print(item_list[i] + "(in_이)가 없다...4")
                                else:
                                    print(item_list[i] + "(in_이)가 있다...4")
                                    click_pos_reg(imgs_.x - 285, imgs_.y + 70, cla)
                                    time.sleep(0.2)
                                imgs_5 = imgs_set_(cla_x - 240, imgs_.y + 20, cla_x - 160, imgs_.y + 120,
                                                  cla, img, 0.85)
                                if imgs_5 is None or imgs_5 == False:
                                    print(item_list[i] + "(in_이)가 없다...5")
                                else:
                                    print(item_list[i] + "(in_이)가 있다...5")
                                    click_pos_reg(imgs_.x - 200, imgs_.y + 70, cla)
                                    time.sleep(0.3)
                        else:
                            imgs_6 = imgs_set_(cla_x + 40, imgs_.y - 40, cla_x + 100, imgs_.y + 45, cla,
                                              img, 0.85)
                            if imgs_6 is None or imgs_6 == False:
                                print(item_list[i] + "(in_이)가 없다...6")
                                print("*", imgs_)
                            else:
                                print(item_list[i] + "(in_이)가 있다...6")
                                click_pos_reg(imgs_.x + 70, imgs_.y, cla)
                                time.sleep(0.2)

                            imgs_7 = imgs_set_(cla_x + 100, imgs_.y - 40, cla_x + 180, imgs_.y + 45,
                                              cla, img, 0.85)
                            if imgs_7 is None or imgs_7 == False:
                                print(item_list[i] + "(in_이)가 없다...7")
                            else:
                                print(item_list[i] + "(in_이)가 있다...7")
                                click_pos_reg(imgs_.x + 140, imgs_.y, cla)
                                time.sleep(0.3)
                        click_pos_2(900, 1005, cla)
                        time.sleep(0.5)
                        # drag_pos(800, 900, 800, 200, cla)
                        time.sleep(0.5)

        return go_
    except Exception as e:
        print(e)
        return 0


def go_chango_drag(cla):
    try:
        from myfunction import text_check_get_3, int_put_

        go_ = False
        drag_ready = text_check_get_3(720, 995, 790, 1020, 1, cla)
        print("drag_ready", drag_ready)
        drag_re_ = drag_ready.split('/')
        drag_r_ = int_put_(drag_re_[0])
        drag_r_bloon = drag_r_.isdigit()
        if drag_r_bloon == True:
            drag_ = int(drag_r_)
            if drag_ > 60:
                go_ = True
        return go_
    except Exception as e:
        print(e)
        return 0

def chango_(cla, data):
    try:
        from clean import clean_screen
        from myfunction import menuOpenCheck, click_pos_2, drag_pos, text_check_get, random_int, imgs_set, text_check_get_2, text_check_get_3
        from action import go_bag, go_power_bag, go_boonhae, go_jangchack, go_haeje, go_escape, go_soongan_f5
        import numpy as np
        import cv2

        print("chango_", data)
        #data는 캐릭 바뀌기 전인지 후인지...
        # 마을로 가기

        heajae_ready_ = False
        # 창고로 옮겨놓기 #
        if data == 'before':
            isSomopoomCount = 0
            while heajae_ready_ is False:

                ismaul_ = False
                while ismaul_ is False:
                    clean_screen(cla, "chango_ : data == 'before'")
                    maul_bool = in_village_go(cla)
                    time.sleep(1)
                    if maul_bool == "mana" or maul_bool == "yotoon" or maul_bool == "nida":
                        ismaul_ = True

                    if ismaul_ == True:
                        click_pos_2(860, 55, cla)
                        chango1 = go_bag(cla, "chango_ : data == 'before'")

                        if chango1 == True:
                            go_power_bag(cla)
                            time.sleep(1)
                            go_boonhae(cla, "chango_ : data == 'before'")
                            time.sleep(1)
                            print("분해하라!!!!!!!!!!!!!!!!!!!!!!!!!!")

                            # 장비 모두 해제 인지 파악 후 맞다면
                            click_pos_2(300, 150, cla)
                            chango2 = go_jangchack(cla)
                            chango3 = go_haeje(cla)
                            if chango3 == True:
                                click_pos_2(900, 1005, cla)
                                time.sleep(1)
                            elif chango2 == True:
                                # 자동장착이라서 두번 클릭해서 해제해야함.
                                click_pos_2(900, 1005, cla)
                                time.sleep(1)
                                click_pos_2(900, 1005, cla)
                                time.sleep(1)
                            click_pos_2(300, 150, cla)
                            chango2 = go_jangchack(cla)
                            jangchak_bloon = False
                            if chango2 == False:
                                click_pos_2(900, 1005, cla)
                                click_pos_2(900, 1005, cla)
                                for i in range(7):
                                    jangchak_ = text_check_get_3(385, 65, 950, 160, i, cla)
                                    jangchak = jangchak_.split("\n")
                                    jangchak = " ".join(jangchak).strip()
                                    print("jangchak3", jangchak)
                                    if len(jangchak) != 0:
                                        for j in range(len(jangchak)):
                                            try:
                                                if jangchak[j] == '장' or jangchak[j] == '비':
                                                    jangchak_bloon = True
                                            except:
                                                pass
                                print("bloon : ", jangchak_bloon)

                            if chango2 == True:
                                jangchak_bloon = True
                            if jangchak_bloon == True:
                                click_pos_2(930, 55, cla)
                                time.sleep(1)

                                # 창고에 맡기러 가는 중

                                print("창고에 맡기러 가는 중")
                                isChango_go = False
                                while isChango_go is False:
                                    chango5 = go_chango(cla, 'chango')  # 창고 글자
                                    if chango5 == True:
                                        print("진행")
                                        isChango_go = True
                                        go_chango(cla, 'in')
                                        time.sleep(1)
                                        heajae_ready_ = True
                                        click_pos_2(900, 1005, cla)
                                        time.sleep(1)
                                        click_pos_2(930, 55, cla)
                                        time.sleep(1)
                                    else:
                                        chango4 = go_chango(cla, 'village')  # 창고 그림
                                        if chango4 == True:
                                            result_vil_1 = in_village_ready(cla)

                                            print("창고로 가는중")
                                            isSomopoomCount += 1
                                            click_pos_2(675, 980, cla)
                                            print("창고로 가는중(click_pos_2(675, 980, cla))", cla)
                                            if result_vil_1 == 'yotoon':
                                                time.sleep(1)
                                                click_pos_2(810, 980, cla)
                                                time.sleep(1)
                                                click_pos_2(810, 980, cla)
                                            time.sleep(10 + random_int())
                                            if isSomopoomCount == 12 or isSomopoomCount == 24:
                                                isSomopoomCount = 0
                                                go_escape(cla)
                                        else:
                                            menu_ = menuOpenCheck(cla, "창고에서 맡기러 가는 중이었음")
                                            if menu_ == True:
                                                #창고 그림이 있었는데 파악이 안된 상황임.
                                                click_pos_2(920, 65, cla)
                                                time.sleep(1)
                                                drag_pos(200, 500, 700, 500, cla)
                                                chango4 = go_chango(cla, 'village')  # 창고 그림
                                                if chango4 == True:
                                                    click_pos_2(675, 980, cla)
                                                else:
                                                    clean_screen(cla, "창고그림 찾기_1")
                                            else:
                                                chango4 = go_chango(cla, 'village')  # 창고 그림
                                                if chango4 == True:
                                                    click_pos_2(675, 980, cla)
                                                else:
                                                    drag_pos(200, 500, 700, 500, cla)
                                                    chango4 = go_chango(cla, 'village')  # 창고 그림
                                                    if chango4 == True:
                                                        click_pos_2(675, 980, cla)
                                                    else:
                                                        clean_screen(cla, "창고그림 찾기_2")

                    else:
                        print("무언가 잘못 되었당...")

        # 창고에서 꺼내기기

        if data == 'after':

            ismaul_ = False
            while ismaul_ is False:
                clean_screen(cla, "chango_ : data == 'after'")
                maul_bool = in_village_go(cla)
                time.sleep(random_int())
                if maul_bool == "mana" or maul_bool == "yotoon" or maul_bool == "nida":
                    ismaul_ = True

                if ismaul_ == True:
                    isAfter_2 = False
                    isSomopoomCount = 0
                    while isAfter_2 is False:
                        print("창고 꺼내기 진행")

                        isChango_go = False
                        while isChango_go is False:
                            chango5 = go_chango(cla, 'chango')  # 창고 글자
                            if chango5 == True:
                                print("진행")
                                isChango_go = True

                                go_chango(cla, 'out')
                                time.sleep(1)
                                click_pos_2(240, 1005, cla)
                                time.sleep(1)
                                click_pos_2(930, 55, cla)
                                time.sleep(1)
                                chango4 = go_chango(cla, 'village')
                                if chango4 == True:
                                    isAfter_2 = True
                            else:
                                chango4 = go_chango(cla, 'village')  # 창고 그림
                                if chango4 == True:
                                    result_vil_1 = in_village_ready(cla)

                                    print("창고로 가는중")
                                    isSomopoomCount += 1
                                    click_pos_2(675, 980, cla)
                                    print("창고로 가는중(click_pos_2(675, 980, cla))", cla)
                                    if result_vil_1 == 'yotoon':
                                        time.sleep(1)
                                        click_pos_2(810, 980, cla)
                                        time.sleep(1)
                                        click_pos_2(810, 980, cla)
                                    time.sleep(10 + random_int())
                                    if isSomopoomCount == 12 or isSomopoomCount == 24:
                                        isSomopoomCount = 0
                                        go_escape(cla)
                                else:
                                    menu_ = menuOpenCheck(cla, "창고에서 꺼내러 가는 중이었음")
                                    if menu_ == True:
                                        # 창고 그림이 있었는데 파악이 안된 상황임.
                                        click_pos_2(920, 65, cla)
                                        time.sleep(1)
                                        drag_pos(200, 500, 700, 500, cla)
                                        chango4 = go_chango(cla, 'village')  # 창고 그림
                                        if chango4 == True:
                                            click_pos_2(675, 980, cla)
                                        else:
                                            clean_screen(cla, "창고그림 찾기_11")
                                    else:
                                        chango4 = go_chango(cla, 'village')  # 창고 그림
                                        if chango4 == True:
                                            click_pos_2(675, 980, cla)
                                        else:
                                            drag_pos(200, 500, 700, 500, cla)
                                            chango4 = go_chango(cla, 'village')  # 창고 그림
                                            if chango4 == True:
                                                click_pos_2(675, 980, cla)
                                            else:
                                                clean_screen(cla, "창고그림 찾기_22")

                        print("durl")
                        if isChango_go == True:
                            chango4 = go_chango(cla, 'village')
                            if chango4 == True:
                                click_pos_2(860, 55, cla)
                                time.sleep(random_int())
                                chango1 = go_bag(cla, "chango_ : data == 'after'")
                                if chango1 == False:
                                    print("가방이 안 열렸다.")
                                else:
                                    print("가방이 열렸다.")
                                    go_boonhae(cla, "chango_ : data == 'after'")
                                    go_soongan_f5(cla)
                                    # 자동 장착 인지 파악 후 맞다면
                                    click_pos_2(300, 150, cla)
                                    chango2 = go_jangchack(cla)
                                    chango3 = go_haeje(cla)

                                    # 이미 장비 장착중
                                    time.sleep(1)
                                    if chango3 == True:
                                        click_pos_2(900, 1005, cla)
                                        time.sleep(1)
                                        click_pos_2(900, 1005, cla)
                                        time.sleep(1)
                                    # 아마 자동장착 버튼일듯...
                                    elif chango2 == True:
                                        click_pos_2(900, 1005, cla)
                                        time.sleep(1)
                                    # 파워 저장
                                    go_power_bag(cla)
                                    time.sleep(1)
                                    click_pos_2(920, 65, cla)
                                    time.sleep(1)
                else:
                    print("무언가 잘못 되었당.")

            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\gabang.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(30, 40, 100, 75, cla, img)
            # imgs_ = pyautogui.locateCenterOnScreen(img, region=(30 + plus, 40, 100 + plus, 75),
            #                                        confidence=0.7)
            if imgs_ is None or imgs_ == False:
                print("가방표시 없다. 창고 꺼내기 끝")
            else:
                print("가방표시 있다. 창고 꺼내기 끝")
                click_pos_2(920, 65, cla)
                time.sleep(random_int())


    except Exception as e:
        print(e)
        return 0

def my_jangbi_in():
    try:
        import os.path

        dir_path = "C:\\my_games\\coobcco2\\data_od"
        file_path4 = dir_path + "\\item\\myjangbilist_in.txt"
        if os.path.isdir(dir_path) == True:
            print('디렉토리 존재')
        else:
            os.makedirs(dir_path)

        if os.path.isfile(file_path4) == True:
            # 파일 읽기
            with open(file_path4, "r", encoding='utf-8-sig') as file:
                lines = file.read()
                file.close()
            print("lines", lines)
        else:
            # \nweg\ngoodbell\nmoogi\nbangugoo\njangsingoo\numool\nsegongsuk\njungsoo\nsilver
            data = "weg\ngoodbell\nmoogi\nbangugoo\njangsingoo\numool\nsegongsuk\njungsoo\nsilver\ngagongsuk\ngwangsuk\namafool\nnamoo\ng_more\nyunmasuk"
            with open(file_path4, "w", encoding='utf-8-sig') as file:
                file.write(data)
                file.close()
                with open(file_path4, "r", encoding='utf-8-sig') as file:
                    lines = file.read()
                    file.close()
        return lines
    except Exception as e:
        print(e)
        return 0




def my_jangbi_out():
    try:
        import os.path

        dir_path = "C:\\my_games\\coobcco2\\data_od"
        file_path5 = dir_path + "\\item\\myjangbilist_out.txt"
        if os.path.isdir(dir_path) == True:
            print('디렉토리 존재')
        else:
            os.makedirs(dir_path)

        if os.path.isfile(file_path5) == True:
            # 파일 읽기
            with open(file_path5, "r", encoding='utf-8-sig') as file:
                lines = file.read()
                file.close()
            print("lines", lines)
        else:
            data = "horn\nmoonjang\nwanjang\ngyunjang\nboojug\npendant\nsul_hwal\ntoogoo\nmomtong\npal\ndari\nmangto\nneck\nearing\npaljji\nring\nbelt"
            with open(file_path5, "w", encoding='utf-8-sig') as file:
                file.write(data)
                file.close()
                with open(file_path5, "r", encoding='utf-8-sig') as file:
                    lines = file.read()
                    file.close()
        return lines
    except Exception as e:
        print(e)
        return 0


def my_auction_():
    try:
        import os.path

        dir_path = "C:\\my_games\\coobcco2\\data_od"
        file_path5 = dir_path + "\\item\\myauctionlist.txt"
        if os.path.isdir(dir_path) == True:
            print('디렉토리 존재')
        else:
            os.makedirs(dir_path)

        if os.path.isfile(file_path5) == True:
            # 파일 읽기
            with open(file_path5, "r", encoding='utf-8-sig') as file:
                lines = file.read()
                file.close()
            print("lines", lines)
        else:
            data = 'umoon:10\nweg:20\ngoodbell:10\nmoogi:20\nbangugoo:100\njangsingoo:10\numool:10\nsegongsuk:10\njungsoo:10\nsilver:50\ndun_item:1'
            with open(file_path5, "w", encoding='utf-8-sig') as file:
                file.write(data)
                file.close()
                with open(file_path5, "r", encoding='utf-8-sig') as file:
                    lines = file.read()
                    file.close()
        return lines
    except Exception as e:
        print(e)
        return 0

def my_auction_in():
    try:
        import os.path

        dir_path = "C:\\my_games\\coobcco2\\data_od"
        file_path5 = dir_path + "\\item\\myauctionlist_in.txt"
        if os.path.isdir(dir_path) == True:
            print('디렉토리 존재')
        else:
            os.makedirs(dir_path)

        if os.path.isfile(file_path5) == True:
            # 파일 읽기
            with open(file_path5, "r", encoding='utf-8-sig') as file:
                lines = file.read()
                file.close()
            print("lines", lines)
        else:
            data = 'suri_earing\nsongot_momtong\nhwangmooji_dangum\nhwangmooji_hwal\ngyuwoo_bangpae\nsongot_toogoo\nsongot_pal\ngyuwoo_dangum\nmangja_neck\nguin_pal\ndoljajoog_moonjang\ngyuwoo_bong\ngyuwoo_hwal\ngyuwoo_doggi\nyobimang'
            with open(file_path5, "w", encoding='utf-8-sig') as file:
                file.write(data)
                file.close()
                with open(file_path5, "r", encoding='utf-8-sig') as file:
                    lines = file.read()
                    file.close()
        return lines
    except Exception as e:
        print(e)
        return 0

def my_auction_in_item():
    try:
        import os.path

        dir_path = "C:\\my_games\\coobcco2\\data_od"
        file_path5 = dir_path + "\\item\\myauctionlist_in_item.txt"
        if os.path.isdir(dir_path) == True:
            print('디렉토리 존재')
        else:
            os.makedirs(dir_path)

        if os.path.isfile(file_path5) == True:
            # 파일 읽기
            with open(file_path5, "r", encoding='utf-8-sig') as file:
                lines = file.read()
                file.close()
            print("lines", lines)
        else:
            data = 'umoon\nweg\ngoodbell\nsegongsuk\njungsoo\nsilver\ngold\nmoogi\nbangugoo\njangsingoo\numool'
            with open(file_path5, "w", encoding='utf-8-sig') as file:
                file.write(data)
                file.close()
                with open(file_path5, "r", encoding='utf-8-sig') as file:
                    lines = file.read()
                    file.close()
        return lines
    except Exception as e:
        print(e)
        return 0

def auction(cla):
    try:
        from clean import clean_screen
        from myfunction import click_pos_2, random_int, text_check_get, imgs_set_, click_pos_reg, int_put_, menuOpenCheck, imgs_set
        from action import go_alrim_confirm
        import numpy as np
        import cv2
        import re

        auction_ready = False
        print("acution")
        # 마을로 가기
        # clean_screen(cla, "auction_start")
        # 거래소 열기
        isAuctionReady = False
        while isAuctionReady is False:
            counted_ = text_check_get(33, 39, 110, 70, cla)
            counted_ = counted_.split("\n")
            print("거래소? => ", counted_)
            if len(counted_) != 0:
                for list in counted_:
                    try:
                        for i in range(len(list)):
                            try:
                                if list[i] == '거' or list[i] == '래' or list[i] == '소':
                                    isAuctionReady = True
                                    auction_ready = True
                            except:
                                pass
                    except:
                        pass

            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\clean\\auction.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(30, 30, 160, 80, cla, img)
            if imgs_ is not None:
                print("거래소 그림 보여", imgs_)
                isAuctionReady = True
                auction_ready = True
            if auction_ready == False:
                ismenu_ = menuOpenCheck(cla, "auction_go_1")
                if ismenu_ == False:
                    click_pos_2(920, 65, cla)
                    time.sleep(random_int())
                    ismenu_ = menuOpenCheck(cla, "auction_go_2")
                    if ismenu_ == False:
                        clean_screen(cla, "auction_gogo")
                    else:
                        click_pos_2(680, 220, cla)
                        time.sleep(3 + random_int())
                else:
                    click_pos_2(680, 220, cla)
                    time.sleep(3 + random_int())
        print("거래소 도착")

        if auction_ready == True:
            click_pos_2(240, 105, cla)
            time.sleep(1 + random_int())
            click_pos_2(510, 1010, cla)
            time.sleep(1)

            auction_re = False
            while auction_re is False:
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\auction\\auction_re.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 100, 600, 800, cla, img, 0.8)
                if imgs_ is not None:
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                else:
                    auction_re = True
                go_alrim_confirm(cla, "auction_re")
                time.sleep(0.3)
            go_alrim_confirm(cla, "auction_re")


            data = my_auction_()
            # data = 'umoon:10\nweg:20\ngoodbell:10\nmoogi:20\nbangugoo:100\njangsingoo:10\numool:10\nsegongsuk:10\njungsoo:10\nsilver:50'
            datas = data.split("\n")
            for i in range(len(datas)):
                item_list = datas[i].split(":")
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\auction\\" + item_list[0] + ".png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(580, 160, 950, 420, cla, img, 0.8)
                if imgs_ is None or imgs_ == False:
                    print(item_list[0] + "(이)가 없다...")
                else:
                    print(item_list[0], imgs_)
                    print("item_list[0] : ", item_list[0])
                    print("item_list[1] : ", item_list[1])
                    thisitem_ = int_put_(item_list[1])
                    result = thisitem_.isdigit()
                    print("result : ", result)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                    sell_count = 0

                    isSell_1 = False
                    while isSell_1 is False:

                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\auction\\auction_x.png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(590, 315, 700, 400, cla, img, 0.8)
                        if imgs_ is not None:
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                        sell_count += 1

                        buy_1 = False
                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\auction\\auction_sell_register_1.png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(200, 300, 350, 400, cla, img, 0.8)
                        if imgs_ is not None:
                            buy_1 = True

                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\auction\\auction_sell_register_11.png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(200, 300, 350, 400, cla, img, 0.8)
                        if imgs_ is not None:
                            buy_1 = True
                        if buy_1 == True:
                            isSell_1 = True
                            click_pos_2(190, 495, cla)
                            time.sleep(0.2)
                            click_pos_2(190, 495, cla)
                            time.sleep(1)
                            click_pos_2(540, 715, cla)
                            isSell_2 = False
                            isSell_2_count = 0
                            while isSell_2 is False:

                                time.sleep(0.3)
                                isSell_2_count += 1
                                buy_2 = False
                                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\auction\\auction_sell_register_2.png"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 300, 550, 400, cla, img, 0.8)
                                if imgs_ is not None:
                                    buy_2 = True

                                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\auction\\auction_sell_register_22.png"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 300, 550, 400, cla, img, 0.8)
                                if imgs_ is not None:
                                    buy_2 = True

                                if buy_2 == True:
                                    isSell_2 = True
                                    click_pos_2(550, 700, cla)
                                    time.sleep(0.5)
                                else:
                                    print("판매중_2")
                                    time.sleep(0.1)
                                    if isSell_2_count > 5:
                                        isSell_2_count = 0
                                        isSell_2 =True
                            time.sleep(0.3)
                        else:
                            time.sleep(0.1)
                            if sell_count > 5:
                                isSell_1 = True



            time.sleep(0.5)
            click_pos_2(575, 375, cla)
            time.sleep(0.5)
            click_pos_2(930, 55, cla)
            time.sleep(1)
        else:
            click_pos_2(930, 55, cla)
            time.sleep(1)
            clean_screen(cla, "auction_end")

    except Exception as e:
        print(e)
        return 0

def auction_example(cla):
    try:
        from clean import clean_screen
        from myfunction import click_pos_2, random_int, text_check_get, imgs_set_, click_pos_reg, int_put_, menuOpenCheck, imgs_set
        import numpy as np
        import cv2
        import re

        auction_ready = False
        print("acution")
        # 마을로 가기
        # clean_screen(cla, "auction_start")
        # 거래소 열기
        isAuctionReady = False
        while isAuctionReady is False:
            counted_ = text_check_get(33, 39, 110, 70, cla)
            counted_ = counted_.split("\n")
            print("거래소? => ", counted_)
            if len(counted_) != 0:
                for list in counted_:
                    try:
                        for i in range(len(list)):
                            try:
                                if list[i] == '거' or list[i] == '래' or list[i] == '소':
                                    isAuctionReady = True
                                    auction_ready = True
                            except:
                                pass
                    except:
                        pass

            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\clean\\auction.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(30, 30, 160, 80, cla, img)
            if imgs_ is not None:
                print("거래소 그림 보여", imgs_)
                isAuctionReady = True
                auction_ready = True
            if auction_ready == False:
                ismenu_ = menuOpenCheck(cla, "auction_go_1")
                if ismenu_ == False:
                    click_pos_2(920, 65, cla)
                    time.sleep(random_int())
                    ismenu_ = menuOpenCheck(cla, "auction_go_2")
                    if ismenu_ == False:
                        clean_screen(cla, "auction_gogo")
                    else:
                        click_pos_2(680, 220, cla)
                        time.sleep(3 + random_int())
                else:
                    click_pos_2(680, 220, cla)
                    time.sleep(3 + random_int())
        print("거래소 도착")

        if auction_ready == True:
            click_pos_2(240, 105, cla)
            time.sleep(1 + random_int())
            click_pos_2(510, 1010, cla)
            time.sleep(1)
            data = my_auction_()
            # data = 'umoon:10\nweg:20\ngoodbell:10\nmoogi:20\nbangugoo:100\njangsingoo:10\numool:10\nsegongsuk:10\njungsoo:10\nsilver:50'
            datas = data.split("\n")
            for i in range(len(datas)):
                item_list = datas[i].split(":")
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\auction\\" + item_list[0] + ".png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(580, 160, 950, 420, cla, img, 0.8)
                if imgs_ is None or imgs_ == False:
                    print(item_list[0] + "(이)가 없다...")
                else:
                    print(item_list[0], imgs_)
                    print("item_list[0] : ", item_list[0])
                    print("item_list[1] : ", item_list[1])
                    thisitem_ = int_put_(item_list[1])
                    result = thisitem_.isdigit()
                    print("result : ", result)
                    if 1 == int(thisitem_):
                        print("맞나", imgs_)
                        print("한개 팔기 : ", item_list[0])
                        click_pos_reg(imgs_.x, imgs_.y, cla)

                        sell_count = 0
                        isSell_1 = False
                        while isSell_1 is False:
                            buy_1 = False
                            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\auction\\auction_sell_register_1.png"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(200, 300, 350, 400, cla, img, 0.8)
                            if imgs_ is not None:
                                buy_1 = True

                            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\auction\\auction_sell_register_11.png"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(200, 300, 350, 400, cla, img, 0.8)
                            if imgs_ is not None:
                                buy_1 = True
                            if buy_1 == True:
                                click_pos_2(190, 495, cla)
                                time.sleep(1)
                                click_pos_2(190, 495, cla)
                                time.sleep(1)
                                click_pos_2(540, 715, cla)
                                isSell_2 = False
                                while isSell_2 is False:
                                    time.sleep(1)
                                    buy_2 = False
                                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\auction\\auction_sell_register_2.png"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(400, 300, 550, 400, cla, img, 0.8)
                                    if imgs_ is None or imgs_ == False:
                                        buy_2 = True

                                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\auction\\auction_sell_register_22.png"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(400, 300, 550, 400, cla, img, 0.8)
                                    if imgs_ is None or imgs_ == False:
                                        buy_2 = True

                                    if buy_2 == True:
                                        isSell_1 = True
                                        isSell_2 = True
                                        click_pos_2(550, 700, cla)
                                        time.sleep(0.5)
                                    else:
                                        print("판매중_2")
                                        time.sleep(0.3)
                                time.sleep(0.3)

                                buy_3 = False
                                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\auction\\auction_sell_register_2.png"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 300, 550, 400, cla, img, 0.8)
                                if imgs_ is None or imgs_ == False:
                                    buy_3 = True

                                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\auction\\auction_sell_register_2.png"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 300, 550, 400, cla, img, 0.8)
                                if imgs_ is None or imgs_ == False:
                                    buy_3 = True

                                if buy_3 == True:
                                    isSell_1 = True
                                    print("재확인??")
                                    click_pos_2(550, 700, cla)
                                    time.sleep(0.5)
                                else:
                                    print("판매중_2??")
                                    time.sleep(0.3)
                            else:
                                print("판매중_1")
                                time.sleep(0.3)
                                if sell_count > 5:
                                    isSell_1 = True
                    else:
                        print("아니가")
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(random_int())
                        counted_ = text_check_get(240, 635, 272, 655, cla)
                        #
                        num = re.sub(r"[^0-9]", "", counted_)
                        num_bloon = int_put_(num).isdigit()
                        print("a")
                        print("num", num)
                        print(item_list[0], num_bloon)
                        print("a")
                        if num_bloon == True:

                            if int(num) >= int(item_list[1]):
                                time.sleep(random_int())
                                print("수량 충족 : ", int(item_list[1]))
                                click_pos_2(190, 495, cla)
                                time.sleep(1)
                                click_pos_2(190, 495, cla)
                                time.sleep(1)
                                click_pos_2(540, 715, cla)
                                time.sleep(random_int())
                                click_pos_2(540, 680, cla)
                                time.sleep(0.5)
                            else:
                                print("수량 모자름, 필요수량 : ", int(item_list[1]))
                                click_pos_2(575, 375, cla)
                                time.sleep(0.5)
                        else:
                            print("숫자인식 불능")
            time.sleep(0.5)
            click_pos_2(575, 375, cla)
            time.sleep(0.5)
            click_pos_2(930, 55, cla)
            time.sleep(1)
        else:
            click_pos_2(930, 55, cla)
            time.sleep(1)
            clean_screen(cla, "auction_end")

    except Exception as e:
        print(e)
        return 0

def auction_all_get(cla):
    try:
        from myfunction import imgs_set, imgs_set_, click_pos_reg, click_pos_2, drag_pos, random_int, menuOpenCheck
        from clean import clean_screen
        from action import go_escape


        # clean_screen(cla, "auction_all_get_1")
        # maul_bool = in_village_go(cla)
        # time.sleep(random_int())

        ismaul_ = False
        while ismaul_ is False:
            clean_screen(cla, "auction_all_get_1")
            maul_bool = in_village_go(cla)
            time.sleep(random_int())
            if maul_bool == "mana" or maul_bool == "yotoon" or maul_bool == "nida":
                ismaul_ = True

            if ismaul_ == True:
                isAfter_2 = False
                isSomopoomCount = 0
                while isAfter_2 is False:
                    print("창고 꺼내기 진행")

                    isChango_go = False
                    while isChango_go is False:
                        chango5 = go_chango(cla, 'chango')  # 창고 글자
                        if chango5 == True:
                            print("진행")
                            isChango_go = True

                            go_chango(cla, 'auction')
                            time.sleep(1)
                            click_pos_2(930, 55, cla)
                            time.sleep(1)
                            chango4 = go_chango(cla, 'village')
                            if chango4 == True:
                                isAfter_2 = True
                                auction(cla)
                                # 창고에 다시 남는 물품 넣기
                                print("창고에 맡기러 가는 중")
                                isSomopoomCount = 0
                                isChango_go = False
                                while isChango_go is False:
                                    chango5 = go_chango(cla, 'chango')  # 창고 글자
                                    if chango5 == True:
                                        print("진행")
                                        isChango_go = True
                                        go_chango(cla, 'auction_after')
                                        time.sleep(1)
                                        click_pos_2(900, 1005, cla)
                                        time.sleep(1)
                                        click_pos_2(930, 55, cla)
                                        time.sleep(1)
                                    else:
                                        chango4 = go_chango(cla, 'village')  # 창고 그림
                                        if chango4 == True:
                                            result_vil_1 = in_village_ready(cla)

                                            print("창고로 가는중")
                                            isSomopoomCount += 1
                                            click_pos_2(675, 980, cla)
                                            print("창고로 가는중(click_pos_2(675, 980, cla))", cla)
                                            if result_vil_1 == 'yotoon':
                                                time.sleep(1)
                                                click_pos_2(810, 980, cla)
                                                time.sleep(1)
                                                click_pos_2(810, 980, cla)
                                            time.sleep(10 + random_int())
                                            if isSomopoomCount == 12 or isSomopoomCount == 24:
                                                isSomopoomCount = 0
                                                go_escape(cla)
                                        else:
                                            menu_ = menuOpenCheck(cla, "창고에서 맡기러 가는 중이었음")
                                            if menu_ == True:
                                                # 창고 그림이 있었는데 파악이 안된 상황임.
                                                click_pos_2(920, 65, cla)
                                                time.sleep(1)
                                                drag_pos(200, 500, 700, 500, cla)
                                                chango4 = go_chango(cla, 'village')  # 창고 그림
                                                if chango4 == True:
                                                    click_pos_2(675, 980, cla)
                                                else:
                                                    clean_screen(cla, "창고그림 찾기_1")
                                            else:
                                                chango4 = go_chango(cla, 'village')  # 창고 그림
                                                if chango4 == True:
                                                    click_pos_2(675, 980, cla)
                                                else:
                                                    drag_pos(200, 500, 700, 500, cla)
                                                    chango4 = go_chango(cla, 'village')  # 창고 그림
                                                    if chango4 == True:
                                                        click_pos_2(675, 980, cla)
                                                    else:
                                                        clean_screen(cla, "창고그림 찾기_2")


                        else:
                            chango4 = go_chango(cla, 'village')  # 창고 그림
                            if chango4 == True:
                                result_vil_1 = in_village_ready(cla)

                                print("창고로 가는중")
                                isSomopoomCount += 1
                                click_pos_2(675, 980, cla)
                                print("창고로 가는중(click_pos_2(675, 980, cla))", cla)
                                if result_vil_1 == 'yotoon':
                                    time.sleep(1)
                                    click_pos_2(810, 980, cla)
                                    time.sleep(1)
                                    click_pos_2(810, 980, cla)
                                time.sleep(10 + random_int())
                                if isSomopoomCount == 12 or isSomopoomCount == 24:
                                    isSomopoomCount = 0
                                    go_escape(cla)
                            else:
                                menu_ = menuOpenCheck(cla, "창고에서 맡기러 가는 중이었음")
                                if menu_ == True:
                                    # 창고 그림이 있었는데 파악이 안된 상황임.
                                    click_pos_2(920, 65, cla)
                                    time.sleep(1)
                                    drag_pos(200, 500, 700, 500, cla)
                                    chango4 = go_chango(cla, 'village')  # 창고 그림
                                    if chango4 == True:
                                        click_pos_2(675, 980, cla)
                                    else:
                                        clean_screen(cla, "창고그림 찾기_1")
                                else:
                                    chango4 = go_chango(cla, 'village')  # 창고 그림
                                    if chango4 == True:
                                        click_pos_2(675, 980, cla)
                                    else:
                                        drag_pos(200, 500, 700, 500, cla)
                                        chango4 = go_chango(cla, 'village')  # 창고 그림
                                        if chango4 == True:
                                            click_pos_2(675, 980, cla)
                                        else:
                                            clean_screen(cla, "창고그림 찾기_2")


            else:
                print("무언가 잘못 되었다.ㅠ")

    except Exception as e:
        print(e)
        return 0

def in_village_ready(cla):
    try:
        from myfunction import imgs_set, click_pos_2
        import numpy as np
        import cv2

        print("def in_village_ready(cla): start")
        thisnida = False
        thisyotoon = False
        thismana = False
        data = 'none'

        if cla == 'one':
            plus = 0
        if cla == 'two':
            plus = 960

        # 니다인지 체크 test
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\nida.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(50, 110, 180, 150, cla, img)
        # imgs_ = pyautogui.locateCenterOnScreen(img, region=(50 + plus, 110, 180 + plus, 150),
        #                                        confidence=0.7)
        if imgs_ is None or imgs_ == False:
            print("니다 아님..")
        else:
            print("imgs", imgs_)
            print('니다 마을~!')
            thisnida = True

        # 요툰인지 체크

        full_path2 = "c:\\my_games\\coobcco2\\data_od\\imgs\\yotoon.png"
        img_array2 = np.fromfile(full_path2, np.uint8)
        img2 = cv2.imdecode(img_array2, cv2.IMREAD_COLOR)
        imgs_2 = imgs_set(50, 110, 180, 150, cla, img2)
        # imgs_2 = pyautogui.locateCenterOnScreen(img2, region=(50 + plus, 110, 180 + plus, 150),
        #                                        confidence=0.7)
        if imgs_2 is None or imgs_2 == False:
            print("요툰 아님..?")
            full_path3 = "c:\\my_games\\coobcco2\\data_od\\imgs\\yotoon2.png"
            img_array3 = np.fromfile(full_path3, np.uint8)
            img3 = cv2.imdecode(img_array3, cv2.IMREAD_COLOR)
            imgs_3 = imgs_set(50, 110, 180, 150, cla, img3)
            # imgs_3 = pyautogui.locateCenterOnScreen(img3, region=(50 + plus, 110, 180 + plus, 150),
            #                                        confidence=0.7)
            if imgs_3 is None or imgs_3 == False:
                print("요툰 아님..")
            else:
                print("imgs", imgs_3)
                print('요툰 마을~!!')
                thisyotoon = True
        else:
            print("imgs", imgs_2)
            print('요툰 마을~!')
            thisyotoon = True

        # 마나인지 체크 test
        full_path4 = "c:\\my_games\\coobcco2\\data_od\\imgs\\mana_1.png"
        img_array4 = np.fromfile(full_path4, np.uint8)
        img4 = cv2.imdecode(img_array4, cv2.IMREAD_COLOR)
        imgs_4 = imgs_set(50, 110, 180, 150, cla, img4)
        # imgs_4 = pyautogui.locateCenterOnScreen(img4, region=(50 + plus, 110, 180 + plus, 150),
        #                                        confidence=0.7)
        if imgs_4 is None or imgs_4 == False:
            print("마나하임 아님..")
        else:
            print("imgs", imgs_4)
            print('마나하임 마을~!')
            thismana = True


        if thisyotoon == True:
            data = 'yotoon'
        if thisnida == True:
            data = 'nida'
        if thismana == True:
            data = 'mana'
        print("def in_village_ready(cla): end")
        return data
    except Exception as e:
        print(e)
        return 0

def in_village_go_to(cla):
    try:
        from myfunction import click_pos_2, random_int, text_check_get, imgs_set, go_auto
        from where import go_worldmap
        from action import go_alrim_
        from clean import clean_screen
        import numpy as np
        import cv2

        print("def in_village_go_to(cla): start")
        inVillage = False
        isworldmap = False
        thisvil_ = 'none'

        click_pos_2(125, 210, cla)
        time.sleep(2 + random_int())

        click_pos_2(80, 955, cla)
        time.sleep(2 + random_int())

        worlded_ = text_check_get(50, 40, 114, 70, cla)
        world_ = worlded_.split("\n")
        if len(world_) != 0:
            for list in world_[0]:
                try:
                    if list == '월' or list == '드' or list == '맵' or list == '만':
                        isworldmap = True
                except:
                    pass

        time.sleep(1)
        if isworldmap == False:
            click_pos_2(930, 55, cla)
            time.sleep(1)
            click_pos_2(655, 450, cla)
            time.sleep(1)

        if isworldmap == True:

            # 니다벨리르가 미발견 지역인지 체크
            if cla == 'one':
                plus = 0
            if cla == 'two':
                plus = 960

            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\mibalgyun.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(305, 585, 415, 630, cla, img)
            # imgs_ = pyautogui.locateCenterOnScreen(img, region=(305 + plus, 585, 415 + plus, 630),
            #                                        confidence=0.7)

            print("nidacheck", imgs_)

            if imgs_ is None or imgs_ == False:
                # 니다벨리르가 발견된 지역일 때
                # 니다벨리르 마을 클릭
                thisvil_ = 'nida'
                click_pos_2(365, 565, cla)  # 니다 클릭
            else:
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\mibalgyun_2.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(230, 450, 330, 490, cla, img)
                if imgs_ is None or imgs_ == False:
                    # 니다벨리르가 발견된 지역일 때
                    # 요툰 마을 클릭
                    thisvil_ = 'yotoon'
                    click_pos_2(280, 440, cla)  # 요툰 클릭

                else:
                    thisvil_ = 'mana'
                    click_pos_2(160, 520, cla)  # 마나 클릭

            time.sleep(1 + random_int())

            click_pos_2(415, 990, cla)  # 마을 이동 클릭

            villaged_2 = text_check_get(360, 115, 590, 155, cla)
            village_2 = villaged_2.split("\n")
            if len(village_2) != 0:
                print("village2222", village_2[0])
                for list in village_2[0]:
                    try:
                        if list == '마' or list == '을' or list == '안' or list == '에' or list == '서' or list == '는' or list == '귀' or list == '환' or list == '할' or list == '수':
                            inVillage = True
                    except:
                        pass
            if len(village_2) == 0:
                click_pos_2(415, 990, cla)
                villaged_2 = text_check_get(360, 115, 590, 155, cla)
                village_2 = villaged_2.split("\n")
                print("village22222")
                if len(village_2) != 0:
                    for list in village_2[0]:
                        try:
                            if list == '마' or list == '을' or list == '안' or list == '에' or list == '서' or list == '는' or list == '귀' or list == '환' or list == '할' or list == '수':
                                inVillage = True
                        except:
                            pass
            if len(village_2) >= 1:
                if village_2[0] == "'":
                    click_pos_2(415, 990, cla)
                    villaged_2 = text_check_get(360, 115, 590, 155, cla)
                    village_2 = villaged_2.split("\n")
                    print("village222222", village_2[0])
                    if len(village_2) != 0:
                        for list in village_2[0]:
                            try:
                                if list == '마' or list == '을' or list == '안' or list == '에' or list == '서' or list == '는' or list == '귀' or list == '환' or list == '할' or list == '수':
                                    inVillage = True
                            except:
                                pass
            time.sleep(1 + random_int())
            time.sleep(2)
            rea_ = go_alrim_(cla)

            if inVillage == True and rea_ == False:
                click_pos_2(932, 55, cla)
                print("920, 65")
                time.sleep(2 + random_int())
            else:
                click_pos_2(550, 610, cla)
                print("550, 610")

                maul_bbaln__ = text_check_get(200, 110, 800, 520, cla)
                print("maul_bbaln__", maul_bbaln__)
                maul_bbaln_ = maul_bbaln__.split("\n")
                print("maul_bbaln_[0] ", maul_bbaln_[0])
                maul_bbaln = " ".join(maul_bbaln_[0]).strip()
                print("maul_bbaln def maul_mission_start", maul_bbaln)
                ismaul_bbaln = False
                if len(maul_bbaln) != 0:
                    for list in range(len(maul_bbaln)):
                        try:
                            if maul_bbaln[list] == "상" or maul_bbaln[list] == '태' or maul_bbaln[list] == '입' or \
                                    maul_bbaln[
                                        list] == '니' or maul_bbaln[list] == '다' or maul_bbaln[list] == '빠' or \
                                    maul_bbaln[
                                        list] == '른':
                                ismaul_bbaln = True
                                print("ismaul_bbaln ", maul_bbaln[list])
                        except:
                            pass
                time.sleep(random_int())
                if ismaul_bbaln == True:
                    click_pos_2(30, 55, cla)
                    time.sleep(1)
                    result_2 = go_worldmap(cla, "world_moglog")
                    time.sleep(1)
                    if result_2 == False:
                        print("월드맵 목록이 아니여, def in_village_go_to(cla):")
                        click_pos_2(30, 110, cla)  # 중복
                        time.sleep(random_int())  # 중복


                        click_pos_2(135, 300, cla)
                        time.sleep(3 + random_int())  # 중복
                        click_pos_2(800, 1004, cla)  # 중복
                        time.sleep(random_int())  # 중복
                        click_pos_2(932, 55, cla)
                        time.sleep(2 + random_int())
                        time.sleep(50 + random_int())  # 중복
                        in_village_go_to(cla)
                else:
                    click_pos_2(932, 55, cla)
                    time.sleep(2 + random_int())
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\swim.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(850, 920, 950, 1020, cla, img)

                    if imgs_ is None or imgs_ == False:
                        print("어떤 상태인지 파악 불가")

                        clean_screen(cla, "in_village_go_to : 마을로 가는 중")

                        resutl_village = in_village_ready(cla)
                        if resutl_village == 'none':
                            print("젠장 여긴 어디지???")
                            in_village_go_to(cla)
                        else:
                            print("얏호 마을이당", resutl_village)
                    else:
                        print("이새끼 수영한다.")
                        click_pos_2(30, 55, cla)
                        time.sleep(random_int())
                        result_2 = go_worldmap(cla, "world_moglog")
                        time.sleep(1 + random_int())
                        if result_2 == False:
                            print("월드맵 목록이 아니여, def in_village_go_to(cla):")
                            click_pos_2(30, 110, cla)  # 중복
                            time.sleep(random_int())  # 중복

                        click_pos_2(135, 300, cla)
                        time.sleep(3 + random_int())  # 중복
                        click_pos_2(800, 1004, cla)  # 중복
                        time.sleep(random_int())  # 중복
                        click_pos_2(932, 55, cla)
                        time.sleep(2 + random_int())
                        time.sleep(50 + random_int())  # 중복
                        in_village_go_to(cla)





        print("def in_village_go_to(cla): end")
        return thisvil_
    except Exception as e:
        print(e)
        return 0

def in_village_go(cla):
    try:
        from myfunction import click_pos_2, random_int, imgs_set, go_auto
        from massenger import line_to_me

        print("def in_village_go(cla): start")
        thisnida = False
        thisyotoon = False
        this_nida = False
        this_yotoon = False
        result_vil_data = 'none'
        result__ = 'none'
        inVillage = False
        data = 'none'

        isinmaul_ = 0
        isMenu = False
        while isMenu is False:
            result_auto = go_auto(cla, '6')
            isinmaul_ += 1
            if isinmaul_ == 300:
                line_to_me(cla, "마을에서 AUTO 안 보이는 에러 발생함")
            if result_auto == True:
                print("진행")
                isMenu = True
                isVillage_cou_ = 0
                isVillage_go_ = False
                while isVillage_go_ is False:
                    result_vil_1 = in_village_ready(cla)
                    result_vil_data = result_vil_1
                    if result_vil_data == 'none':



                        click_pos_2(30, 220, cla)  # 960차이
                        time.sleep(random_int())
                        click_pos_2(550, 610, cla)  # 960차이
                        time.sleep(5 + random_int())
                        isVillage_cou_ += 1
                        if isVillage_cou_ == 3:
                            isVillage_go_ = True
                            result__ = in_village_go_to(cla)
                            print('마을 도착~!')
                            time.sleep(random_int())
                    else:
                        isVillage_go_ = True
                        time.sleep(random_int())
                        print('마을 도착~!')


            else:
                click_pos_2(920, 65, cla)
                time.sleep(1)

        if result__ == 'nida' or result_vil_data == 'nida':
            data = 'nida'
        elif result__ == 'yotoon' or result_vil_data == 'yotoon':
            data = 'yotoon'
        elif result__ == 'mana' or result_vil_data == 'mana':
            data = 'mana'

        print("def in_village_go(cla): end")
        return data
    except Exception as e:
        print(e)
        return 0





