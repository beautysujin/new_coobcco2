# import numpy as np
# import cv2
import time

import sys
sys.path.append('C:/my_games/coobcco2/data_od/mymodule')

import variable as v_

quest_checked_count = 0

def go_test(cla):
    print('hi test! event_get', cla)


def tuto_grow(cla):
    from action import go_juljun
    from myfunction import imgs_set, click_pos_2, drag_pos
    import numpy as np
    import cv2

    print("튜토리얼")

    # juljun
    print("Grow_juljun")
    go_juljun(cla, 'tuto_grow')

    # tuto_attack
    print("Grow_tuto_attack...")
    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_attack_1a.png"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set(600, 930, 820, 1010, cla, img)
    if imgs_ is None or imgs_ == False:
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_attack_2.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(410, 830, 840, 920, cla, img)
        if imgs_ is None or imgs_ == False:
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_attack_3.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(520, 910, 850, 1030, cla, img)
            if imgs_ is None or imgs_ == False:
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_attack_4.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(500, 900, 900, 1030, cla, img)
                if imgs_ is not None:
                    print("tuto_attack_4", imgs_)
                    click_pos_2(900, 975, cla)
            else:
                print("tuto_attack_3", imgs_)
                click_pos_2(900, 975, cla)
        else:
            print("tuto_attack_2", imgs_)
            click_pos_2(535, 990, cla)
            click_pos_2(670, 990, cla)
    else:
        print("tuto_attack_1", imgs_)
        click_pos_2(900, 975, cla)

    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_attack_22.png"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set(410, 830, 840, 920, cla, img)
    if imgs_ is not None:
        print("tuto_attack_22", imgs_)
        click_pos_2(535, 990, cla)
        click_pos_2(670, 990, cla)

    # tuto_drag
    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_drag_1.png"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set(220, 930, 800, 1030, cla, img)
    if imgs_ is not None:
        print("tuto_drag_1", imgs_)
        drag_pos(535, 970, 535, 1020, cla)
        drag_pos(670, 970, 670, 1020, cla)

    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\drag_.png"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set(220, 930, 800, 1030, cla, img)
    if imgs_ is not None:
        print("drag_", imgs_)
        drag_pos(535, 970, 535, 1020, cla)
        drag_pos(670, 970, 670, 1020, cla)

    # tuto_targeting
    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_targeting_1.png"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set(360, 680, 750, 760, cla, img)
    if imgs_ is not None:
        print("tuto_targeting_1", imgs_)
        click_pos_2(565, 575, cla)


def potion_nida(cla):
    from myfunction import go_auto, click_pos_2, drag_pos, imgs_set, click_pos_reg, imgs_set_, go_to_home
    from where import go_worldmap
    from massenger import line_to_me
    import pyautogui
    from clean import clean_screen
    import numpy as np
    import cv2

    yotoon_potion_line = 0

    if cla == 'one':
        mylevel = v_.mylevel_1
    if cla == 'two':
        mylevel = v_.mylevel_2

    # 요툰 대형 물약 사는 곳
    isBigPotion_1 = False
    while isBigPotion_1 is False:
        result_go_auto = go_auto(cla, '2')
        if result_go_auto == True:
            isBigPotion_2 = False
            while isBigPotion_2 is False:
                result_go_world = go_worldmap(cla, 'world')  # 월드보기
                time.sleep(1)
                if result_go_world == False:
                    click_pos_2(130, 220, cla)
                    time.sleep(1)
                else:
                    pyautogui.scroll(-1000)
                    time.sleep(1)
                    isBigPotion_2 = True
                    # click_pos_2(30, 105, cla)
                    # time.sleep(1)
            print("hi")
            isBigPotion_3 = False
            while isBigPotion_3 is False:
                result_go_world_yotoon = go_worldmap(cla, 'world_yotoon')  # 월드 하단 요툰하임 보기
                if result_go_world_yotoon == False:
                    click_pos_2(80, 960, cla)
                    time.sleep(1)
                    click_pos_2(280, 440, cla)
                    time.sleep(1)
                    click_pos_2(540, 990, cla)
                    time.sleep(3)
                    pyautogui.scroll(-1000)
                    time.sleep(1)
                else:
                    isBigPotion_3 = True
                    click_pos_2(30, 105, cla)
                    time.sleep(1)
            print("hi")
            isBigPotion_4 = False
            while isBigPotion_4 is False:
                result_go_world_moglog = go_worldmap(cla, 'world_moglog')  # 월드목록보기
                if result_go_world_moglog == False:
                    click_pos_2(30, 105, cla)
                    time.sleep(1)
                else:
                    isBigPotion_4 = True

                    click_pos_2(130, 500, cla)
                    time.sleep(1)
                    click_pos_2(890, 1005, cla)
                    time.sleep(1)
                    click_pos_2(540, 610, cla)
                    isBigPotion_1 = True
                    time.sleep(7)
            print("hi")
    print("hello")
    # 다시 월드맵 진입
    while isBigPotion_1 is True:
        result_go_auto = go_auto(cla, '3')
        if result_go_auto == True:
            isBigPotion_2 = False
            while isBigPotion_2 is False:
                result_go_world = go_worldmap(cla, 'world')  # 월드보기
                time.sleep(1)
                if result_go_world == False:
                    click_pos_2(130, 220, cla)
                    time.sleep(1)
                else:
                    pyautogui.scroll(-1000)
                    time.sleep(1)
                    isBigPotion_2 = True
                    # click_pos_2(30, 105, cla)
                    # time.sleep(1)
            print("hi2")
            isBigPotion_3 = False
            while isBigPotion_3 is False:
                result_go_world_yotoon = go_worldmap(cla, 'world_yotoon')  # 하단 요툰하임
                if result_go_world_yotoon == False:
                    click_pos_2(80, 960, cla)
                    time.sleep(1)
                    click_pos_2(280, 440, cla)
                    time.sleep(1)
                    click_pos_2(540, 990, cla)
                    time.sleep(3)
                    pyautogui.scroll(-1000)
                    time.sleep(1)
                else:
                    if yotoon_potion_line == 0:
                        line_to_me(cla, "요툰물약 사러 가는 중")
                        yotoon_potion_line += 1
                    isBigPotion_3 = True
                    pyautogui.scroll(-1000)
                    time.sleep(1)
                    pyautogui.scroll(-1000)
                    time.sleep(1)
                    print("drag")
                    drag_pos(300, 600, 800, 600, cla)
                    time.sleep(1)

                    click_pos_2(437, 590, cla)
                    time.sleep(1)


                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\yotoon_big_potion_1.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(250, 500, 800, 800, cla, img)
                    if imgs_ is not None:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(1)
                        click_pos_2(30, 55, cla)
                        time.sleep(1)

                        isBigPotion_3 = False
                        while isBigPotion_3 is False:
                            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\yotoon_big_potion_2.png"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set(750, 840, 890, 960, cla, img)
                            if imgs_ is not None:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(3)
                                isBigPotion_3 = True
                            else:
                                yotoon_potion_line += 1
                                print("요툰물약 사러 가는 중")
                                time.sleep(1)
                                if yotoon_potion_line == 300:
                                    line_to_me(cla, "물약 제대로 못사고 있당ㅠㅠ")
                        print("hi")
                        isBigPotion_4 = False
                        while isBigPotion_4 is False:
                            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\yotoon_big_potion_3.png"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set(30, 30, 160, 80, cla, img)
                            if imgs_ is not None:
                                click_pos_2(160, 160, cla)
                                time.sleep(1)
                                isBigPotion_4 = True
                            else:
                                print("소모품 상점 가는 중")
                        print("hi")
                        isBigPotion_5 = False
                        while isBigPotion_5 is False:
                            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\yotoon_big_potion_4.png"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(430, 610, 520, 670, cla, img, 0.85)
                            if imgs_ is not None:
                                click_pos_2(580, 590, cla)
                                time.sleep(1.5)
                                click_pos_2(550, 690, cla)
                                time.sleep(1.5)
                                isBigPotion_1 = False
                                isBigPotion_5 = True
                                click_pos_2(920, 65, cla)
                                time.sleep(1)
                            else:
                                click_pos_2(160, 160, cla)
                                time.sleep(1.5)
                                print("물약 사는중")
                        if mylevel > 12:
                            go_to_home('grow', cla)
                        print("니다 육성 물약사기 끝")



        else:
            clean_screen(cla, "potion_grow_end")


def potion_grow(cla, data):
    from myfunction import imgs_set, go_auto, click_pos_2, text_check_get_3, int_put_, random_int, potion_count_grow, go_to_home
    from clean import clean_screen
    from action import go_potion_off
    import numpy as np
    import cv2


    if cla == 'one':
        mylevel = v_.mylevel_1
    if cla == 'two':
        mylevel = v_.mylevel_2

    # juljun
    print("Grow_juljun")
    # go_juljun(cla, 'potion_grow')
    clean_screen(cla, "potion_grow")

    # menu
    print("Grow_menu")
    ismenu = False
    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\menu_1.png"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set(850, 30, 950, 80, cla, img)
    if imgs_ is None or imgs_ == False:
        ismenu = True
    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\menu_2.png"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set(850, 30, 950, 80, cla, img)
    if imgs_ is None or imgs_ == False:
        ismenu = True
    if ismenu == True:
        clean_screen(cla, "potion_grow_start")

    # potion
    print("Grow_potion")
    result____ = go_auto(cla, '1')
    if result____ == True:

        result = go_potion_off(cla)
        if result == False:
            click_pos_2(800, 840, cla)
            time.sleep(1)
        result = go_potion_off(cla)
        if result == True:
            potion_count_ = text_check_get_3(855, 825, 935, 850, 3, cla)
            print("potion_count_", potion_count_)
            if '/' in potion_count_ and potion_count_ != 0:
                print('/가 있당')
                potion_count1 = potion_count_.split("/")
                print("potion_count1", potion_count1)
                potion_ = int_put_(potion_count1[0])
                potion_bloon = potion_.isdigit()
                if potion_bloon == True:
                    potion = int(potion_)
                    print("_grow : potion", potion)

                    if potion > 0:
                        click_pos_2(700, 840, cla)
                        time.sleep(random_int())
                    if potion < 200:
                        # 정확하게 체크하기
                        print("potion < 200: 다시 체크하기 ", potion)
                        if data == '요툰육성':
                            result_po = potion_count_grow(cla)
                            time.sleep(0.5)
                            click_pos_2(920, 65, cla)
                            if result_po < 150:
                                print("요툰육성 물약 사러가기 150개 이하 : 레벨 판단")
                                if mylevel > 12:
                                    go_to_home('grow', cla)
                        elif data == '니다육성':
                            result_po = potion_count_grow(cla)
                            time.sleep(0.5)
                            click_pos_2(920, 65, cla)
                            if result_po < 200:
                                print("니다육성 물약 사러가기 : 200개 이하")
                                # 요툰 대형 물약 사는 곳
                                potion_nida(cla)


def common_grow(cla):
    global quest_checked_count
    from myfunction import imgs_set, click_pos_2, drag_pos, imgs_set_, click_pos_reg
    from login_start import go_tuto_grow_menu
    import pyautogui
    from action import go_alrim_confirm
    import numpy as np
    import cv2

    # skip
    print("Grow_skip")
    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\skip_1.png"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set(850, 35, 950, 80, cla, img)
    if imgs_ is None or imgs_ == False:
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\skip_2.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(850, 35, 950, 80, cla, img)
        if imgs_ is None or imgs_ == False:
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\skip_3.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(850, 35, 950, 80, cla, img)
            if imgs_ is not None:
                print("skip_3", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                click_pos_2(635, 275, cla)
        else:
            print("skip_2", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            click_pos_2(635, 275, cla)
    else:
        print("skip_1", imgs_)
        click_pos_reg(imgs_.x, imgs_.y, cla)
        click_pos_2(635, 275, cla)

    # main_ing
    print("Grow_main_ing")
    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\main_ing_1.png"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set(660, 100, 710, 150, cla, img)
    if imgs_ is None or imgs_ == False:
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\main_ing_2.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(660, 100, 710, 150, cla, img)
        if imgs_ is None or imgs_ == False:
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\main_ing_3.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(660, 100, 710, 150, cla, img)
            if imgs_ is not None:
                print("main_ing_3", imgs_)
                click_pos_2(780, 130, cla)
                time.sleep(1)
                result_me_ = go_tuto_grow_menu(cla)
                if result_me_ == True:
                    click_pos_2(895, 120, cla)
                click_pos_2(815, 980, cla)
                time.sleep(1)

                pyautogui.moveTo(imgs_.x, imgs_.y + 300)
                # free_move
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\free_move_1.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(465, 570, 600, 640, cla, img)
                if imgs_ is not None:
                    click_pos_2(550, 610, cla)
        else:
            print("main_ing_2", imgs_)
            click_pos_2(780, 130, cla)
            time.sleep(1)
            result_me_ = go_tuto_grow_menu(cla)
            if result_me_ == True:
                click_pos_2(895, 120, cla)
            click_pos_2(815, 980, cla)
            time.sleep(1)
            pyautogui.moveTo(imgs_.x, imgs_.y + 300)
            # free_move
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\free_move_1.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(465, 570, 600, 640, cla, img)
            if imgs_ is not None:
                click_pos_2(550, 610, cla)
    else:
        print("main_ing_1", imgs_)
        click_pos_2(780, 130, cla)
        time.sleep(1)
        result_me_ = go_tuto_grow_menu(cla)
        if result_me_ == True:
            click_pos_2(895, 120, cla)
        click_pos_2(815, 980, cla)
        time.sleep(1)
        pyautogui.moveTo(imgs_.x, imgs_.y + 300)
        # free_move
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\free_move_1.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(465, 570, 600, 640, cla, img)
        if imgs_ is not None:
            click_pos_2(550, 610, cla)

    # main_complete


    print("Grow_main_complete")
    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\main_complete_1.png"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set(660, 105, 710, 150, cla, img)
    if imgs_ is None or imgs_ == False:
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\main_complete_2.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(660, 100, 710, 150, cla, img)
        if imgs_ is None or imgs_ == False:
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\main_complete_3.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(660, 100, 710, 150, cla, img)
            if imgs_ is None or imgs_ == False:
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\main_complete_4.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(660, 100, 710, 150, cla, img)
                if imgs_ is None or imgs_ == False:
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\main_complete_5.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(700, 125, 830, 155, cla, img)
                    if imgs_ is None:
                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\main_complete_6.png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(700, 125, 830, 155, cla, img)
                        if imgs_ is not None:
                            print("main_complete_5", imgs_)
                            click_pos_2(780, 130, cla)
                        else:
                            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\auto.png"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set(870, 860, 930, 910, cla, img)
                            if imgs_ is None or imgs_ == False:
                                print("grow\\auto.png 안보여(grow\\auto.png)")
                                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\auto_2.png"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set(870, 860, 930, 910, cla, img)
                                if imgs_ is None or imgs_ == False:
                                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\auto_3.png"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set(870, 860, 930, 910, cla, img)
                                    if imgs_ is not None:
                                        print("grow\\auto_3.png 보여(grow\\auto_3.png)", imgs_)
                                        click_pos_2(780, 130, cla)
                                    else:
                                        drag_pos(330, 590, 630, 590, cla)
                                else:
                                    print("grow\\auto_2.png 보여(grow\\auto_2.png)", imgs_)
                                    click_pos_2(780, 130, cla)
                            else:
                                print("grow\\auto.png  보여(grow\\auto.png )", imgs_)
                                click_pos_2(780, 130, cla)

                    else:
                        print("main_complete_5", imgs_)
                        click_pos_2(780, 130, cla)
                else:
                    print("main_complete_4", imgs_)
                    click_pos_2(780, 130, cla)
            else:
                print("main_complete_3", imgs_)
                click_pos_2(780, 130, cla)
        else:
            print("main_complete_2", imgs_)
            click_pos_2(780, 130, cla)
    else:
        print("main_complete_1", imgs_)
        click_pos_2(780, 130, cla)

    quest_checked = True
    # full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\quest_checked_1.png"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(860, 90, 930, 150, cla, img, 0.6)
    # if imgs_ is not None and imgs_ != False:
    #     print("check1", imgs_)
    # else:
    #     print("안보여1")
    #     quest_checked = False

    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\quest_checked_1.png"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(860, 90, 930, 150, cla, img, 0.7)
    if imgs_ is not None and imgs_ != False:
        print("check2", imgs_)
        quest_checked_count = 0
    else:
        print("안보여2")

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\nidhog_4.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(650, 100, 720, 350, cla, img, 0.75)
        if imgs_ is not None and imgs_ != False:
            print("nidhog_4", imgs_)
            quest_checked_count = 0
        else:
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\nidhog_5.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(650, 100, 720, 350, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:
                print("nidhog_5", imgs_)
                quest_checked_count = 0
            else:
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\nidhog_6.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(650, 100, 720, 350, cla, img, 0.75)
                if imgs_ is not None and imgs_ != False:
                    print("nidhog_6", imgs_)
                    quest_checked_count = 0
                else:
                    print("oh my god")
                    quest_checked_count += 1
                    if quest_checked_count > 10:
                        quest_checked = False

    if quest_checked == False:
        click_pos_2(930, 130, cla)


    # main_bosang
    print("Grow_bosang")
    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\main_bosang_1.png"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set(620, 830, 770, 150, cla, img)
    if imgs_ is None or imgs_ == False:
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\main_bosang_2.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(400, 380, 550, 500, cla, img)
        if imgs_ is None or imgs_ == False:
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\main_bosang_3.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(380, 520, 570, 565, cla, img)
            if imgs_ is not None:
                print("main_bosang_3", imgs_)
                click_pos_2(705, 910, cla)
        else:
            print("main_bosang_1", imgs_)
            click_pos_2(705, 910, cla)
    else:
        print("main_bosang_1", imgs_)
        click_pos_2(705, 910, cla)

    # main_bosang
    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\main_quest_soolock_1.png"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set(400, 380, 550, 500, cla, img)
    if imgs_ is None or imgs_ == False:
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\main_quest_soolock_2.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(540, 910, 610, 960, cla, img)
        if imgs_ is not None:
            print("main_quest_soolock_2", imgs_)
            click_pos_2(580, 935, cla)
    else:
        print("main_quest_soolock_1", imgs_)
        click_pos_2(580, 935, cla)

    # tuto_story

    print("Grow_tuto_story")
    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_story_1.png"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set(860, 250, 950, 330, cla, img)
    if imgs_ is None or imgs_ == False:
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_story_2.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(860, 250, 950, 330, cla, img)
        if imgs_ is not None:
            print("tuto_story_2", imgs_)
            click_pos_2(635, 275, cla)
    else:
        print("tuto_story_1", imgs_)
        click_pos_2(635, 275, cla)

    # free_move
    print("Grow_free_move")
    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\free_move_1.png"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set(465, 570, 600, 640, cla, img)
    if imgs_ is not None:
        print("free_move_1", imgs_)
        click_pos_2(550, 610, cla)

    print("alrim_yes")
    go_alrim_confirm(cla, "grow")


def yotoon_grow(cla):
    import pyautogui
    from myfunction import imgs_set, click_pos_2, text_check_get, random_int, drag_pos, click_pos_reg, text_check_get_3, imgs_set_
    import numpy as np
    import cv2

    print("요툰 성장")

    # 맹독
    if cla =="one":
        pyautogui.moveTo(480, 480)
    if cla =="two":
        pyautogui.moveTo(960 + 480, 480)


    endmangdok = True
    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\mangdok_1.png"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(650, 90, 950, 170, cla, img, 0.85)
    if imgs_ is None or imgs_ == False:
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\mangdok_2.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(650, 90, 950, 170, cla, img, 0.85)
        if imgs_ is not None:
            endmangdok = False
    else:
        endmangdok = False
    if endmangdok == False:
        mangdok_auto_result = False
        while mangdok_auto_result is False:
            click_pos_2(780, 130, cla)
            mangdok_auto_ = text_check_get(350, 110, 580, 170, cla)
            mangdok_auto = mangdok_auto_.split("\n")
            print('mangdok_auto_', mangdok_auto_)
            print('mangdok_auto', mangdok_auto)
            if len(mangdok_auto) != 0:
                for list in mangdok_auto[0]:
                    try:
                        print('list', list)
                        if list == '활' or list == '성' or list == '화':
                            mangdok_auto_result = True
                    except:
                        pass
            print('mangdok_auto_result', mangdok_auto_result)
        while endmangdok is False:
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\mangdok_complete_1.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(200, 200, 800, 800, cla, img)
            if imgs_ is not None:
                endmangdok = True
            else:
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\mangdok_complete_2.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(700, 100, 870, 160, cla, img)
                if imgs_ is not None:
                    endmangdok = True
            time.sleep(1)

    # tuto_quest_moglog
    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_quest_moglog_1.png"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set(640, 180, 910, 260, cla, img)
    if imgs_ is not None:
        print("tuto_quest_moglog_1", imgs_)
        click_pos_2(780, 130, cla)

    # tuto_quest_moglog
    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_potion_click_1.png"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set(700, 690, 950, 780, cla, img)
    if imgs_ is not None:
        print("tuto_potion_click_1", imgs_)
        click_pos_2(840, 840, cla)
        time.sleep(random_int())
        click_pos_2(920, 65, cla)

    # tuto_gabang

    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\grow_gabang.png"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set(500, 40, 950, 300, cla, img)
    if imgs_ is not None:
        click_pos_2(860, 55, cla)

    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\grow_menu.png"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set(500, 40, 950, 300, cla, img)
    if imgs_ is not None:
        click_pos_2(920, 65, cla)

    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_gabang_1.png"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set(610, 120, 950, 200, cla, img)
    if imgs_ is None or imgs_ == False:
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_gabang_2.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(340, 130, 580, 210, cla, img)
        if imgs_ is None or imgs_ == False:
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_gabang_3.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(270, 130, 580, 210, cla, img)
            if imgs_ is None or imgs_ == False:
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_gabang_4.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(610, 100, 950, 180, cla, img)
                if imgs_ is not None:
                    print("tuto_gabang_4", imgs_)
                    click_pos_2(920, 65, cla)
            else:
                print("tuto_gabang_3", imgs_)
                click_pos_2(625, 170, cla)
        else:
            print("tuto_gabang_2", imgs_)
            click_pos_2(625, 170, cla)
    else:
        print("tuto_gabang_1", imgs_)
        click_pos_2(860, 50, cla)

    # somopoom : 일회성
    print("# somopoom : 일회성")
    issomopoom = False
    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\somopoom_1.png"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set(30, 30, 160, 90, cla, img)
    if imgs_ is not None:
        issomopoom = True
    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\somopoom_11.png"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set(30, 30, 160, 90, cla, img)
    if imgs_ is not None:
        issomopoom = True

    if issomopoom == True:
        print("somopoom_1", imgs_)
        click_pos_2(155, 155, cla)
        time.sleep(random_int())
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\somopoom_2.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(420, 610, 520, 660, cla, img)
        if imgs_ is not None:
            click_pos_2(580, 590, cla)
            time.sleep(random_int())
            click_pos_2(560, 690, cla)
            time.sleep(random_int())
            click_pos_2(560, 690, cla)
            time.sleep(random_int())
            click_pos_2(920, 65, cla)
        else:
            click_pos_2(560, 690, cla)
            time.sleep(random_int())
            click_pos_2(560, 690, cla)
            time.sleep(random_int())
            click_pos_2(920, 65, cla)

    # tuto_talgut 1~5
    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_talgut_1.png"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set(775, 120, 950, 175, cla, img)
    if imgs_ is None or imgs_ == False:
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_talgut_2.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(730, 30, 950, 70, cla, img)
        if imgs_ is None or imgs_ == False:
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_talgut_3.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(520, 75, 800, 130, cla, img)
            if imgs_ is None or imgs_ == False:
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_talgut_4.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(680, 900, 950, 940, cla, img)
                if imgs_ is None or imgs_ == False:
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_talgut_5.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(760, 110, 950, 180, cla, img)
                    if imgs_ is not None:
                        print("tuto_talgut_5", imgs_)
                        click_pos_2(920, 65, cla)
                else:
                    print("tuto_talgut_4", imgs_)
                    click_pos_2(880, 1010, cla)
            else:
                print("tuto_talgut_3", imgs_)
                click_pos_2(670, 200, cla)
        else:
            print("tuto_talgut_2", imgs_)
            click_pos_2(860, 145, cla)
    else:
        print("tuto_talgut_1", imgs_)
        click_pos_2(920, 65, cla)

    # tuto_talgut 6~10
    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_talgut_6.png"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set(775, 120, 950, 175, cla, img)
    if imgs_ is None or imgs_ == False:
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_talgut_7.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(730, 25, 950, 70, cla, img)
        if imgs_ is None or imgs_ == False:
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_talgut_8.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(675, 80, 890, 120, cla, img)
            if imgs_ is None or imgs_ == False:
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_talgut_9.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(760, 880, 950, 950, cla, img)
                if imgs_ is None or imgs_ == False:
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_talgut_10.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(760, 120, 950, 180, cla, img)
                    if imgs_ is not None:
                        print("tuto_talgut_10", imgs_)
                        click_pos_2(920, 65, cla)
                else:
                    print("tuto_talgut_9", imgs_)
                    click_pos_2(880, 1010, cla)
            else:
                print("tuto_talgut_8", imgs_)
                click_pos_2(800, 200, cla)
        else:
            print("tuto_talgut_7", imgs_)
            click_pos_2(860, 145, cla)
    else:
        print("tuto_talgut_6", imgs_)
        click_pos_2(920, 65, cla)

    # tuto_guihwan
    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_guihwan_1a.png"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set(70, 170, 400, 280, cla, img)
    if imgs_ is None or imgs_ == False:
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_guihwan_2.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(370, 480, 720, 560, cla, img)
        if imgs_ is None or imgs_ == False:
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\free_move_1.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(610, 100, 950, 180, cla, img)
            if imgs_ is not None:
                print("free_move_1", imgs_)
                click_pos_2(550, 610, cla)
        else:
            print("tuto_guihwan_2", imgs_)
            click_pos_2(550, 610, cla)
    else:
        print("tuto_guihwan_1", imgs_)
        click_pos_2(30, 220, cla)

    # tuto_skill
    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_skill_1.png"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set(770, 120, 950, 165, cla, img)
    if imgs_ is None or imgs_ == False:
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_skill_2.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(600, 80, 790, 130, cla, img)
        if imgs_ is None or imgs_ == False:
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_skill_3.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(300, 140, 900, 500, cla, img)
            if imgs_ is None or imgs_ == False:
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_skill_4.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(660, 110, 950, 150, cla, img)
                if imgs_ is None or imgs_ == False:
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_skill_5.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(610, 110, 950, 190, cla, img)
                    if imgs_ is None or imgs_ == False:
                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_skill_6.png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(635, 200, 850, 250, cla, img)
                        if imgs_ is None or imgs_ == False:
                            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_skill_7.png"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set(640, 870, 950, 950, cla, img)
                            if imgs_ is None or imgs_ == False:
                                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_skill_8.png"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set(630, 80, 900, 160, cla, img)
                                if imgs_ is None or imgs_ == False:
                                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_skill_9.png"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set(380, 220, 680, 300, cla, img)
                                    if imgs_ is None or imgs_ == False:
                                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_skill_10.png"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set(740, 110, 950, 160, cla, img)
                                        if imgs_ is None or imgs_ == False:
                                            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_skill_11.png"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set(410, 840, 950, 930, cla, img)
                                            if imgs_ is not None:
                                                print("tuto_skill_11", imgs_)
                                                drag_pos(605, 965, 605, 1005, cla)
                                                drag_pos(740, 965, 740, 1005, cla)

                                        else:
                                            print("tuto_skill_10", imgs_)
                                            click_pos_2(920, 65, cla)
                                    else:
                                        print("tuto_skill_9", imgs_)
                                        click_pos_2(530, 370, cla)
                                else:
                                    print("tuto_skill_8", imgs_)
                                    click_pos_2(685, 240, cla)
                            else:
                                print("tuto_skill_7", imgs_)
                                click_pos_2(900, 1005, cla)
                        else:
                            print("tuto_skill_6", imgs_)
                            click_pos_2(740, 140, cla)
                    else:
                        print("tuto_skill_5", imgs_)
                        click_pos_2(920, 65, cla)
                else:
                    print("tuto_skill_4", imgs_)
                    click_pos_2(920, 65, cla)
            else:
                print("tuto_skill_3", imgs_)
                click_pos_2(630, 160, cla)
                time.sleep(random_int())
                click_pos_2(630, 160, cla)
        else:
            print("tuto_skill_2", imgs_)
            click_pos_2(840, 100, cla)
    else:
        print("tuto_skill_1", imgs_)
        click_pos_2(860, 55, cla)

    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_skill_3_a.png"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set(500, 100, 950, 600, cla, img)
    if imgs_ is not None:
        click_pos_reg(imgs_.x, imgs_.y, cla)
    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_skill_3_b.png"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set(500, 100, 950, 600, cla, img)
    if imgs_ is not None:
        click_pos_reg(imgs_.x, imgs_.y, cla)

    # tuto_skillbook
    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_skillbook_1.png"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set(315, 100, 730, 190, cla, img)
    if imgs_ is None or imgs_ == False:
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_skillbook_2.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(340, 380, 610, 440, cla, img)
        if imgs_ is not None:
            print("tuto_skillbook_2", imgs_)
            click_pos_2(555, 690, cla)
            time.sleep(random_int())
            click_pos_2(920, 65, cla)
    else:
        print("tuto_skillbook_1", imgs_)
        click_pos_2(150, 150, cla)

    # tuto_gongjoong
    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_gongjoong_1.png"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set(450, 150, 950, 240, cla, img)
    if imgs_ is None or imgs_ == False:
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_gongjoong_2.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(320, 650, 760, 730, cla, img)
        if imgs_ is not None:
            print("tuto_gongjoong_2", imgs_)
            click_pos_2(560, 610, cla)
    else:
        print("tuto_gongjoong_1", imgs_)
        click_pos_2(900, 110, cla)

    # tuto_abata
    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_abata_11.png"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set(200, 510, 360, 600, cla, img)
    if imgs_ is not None and imgs_ != False:
        print("tuto_abata_11", imgs_)
        click_pos_2(300, 680, cla)

    result_sna = text_check_get_3(235, 525, 350, 570, 3, cla)
    if '스나' in result_sna:
        print("result_sna", result_sna)
        click_pos_2(300, 680, cla)

    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_abata_1.png"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set(200, 510, 360, 600, cla, img)
    if imgs_ is None or imgs_ == False:
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_abata_2.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(730, 140, 880, 200, cla, img)
        if imgs_ is None or imgs_ == False:
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_abata_3.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(380, 950, 560, 1010, cla, img)
            if imgs_ is None or imgs_ == False:
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_abata_4.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(730, 110, 950, 170, cla, img)
                if imgs_ is None or imgs_ == False:
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_abata_5.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(700, 210, 890, 270, cla, img)
                    if imgs_ is None or imgs_ == False:
                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_abata_6.png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(510, 260, 770, 350, cla, img)
                        if imgs_ is None or imgs_ == False:
                            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_abata_7.png"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set(760, 870, 950, 960, cla, img)
                            if imgs_ is None or imgs_ == False:
                                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_abata_8.png"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set(690, 100, 950, 180, cla, img)
                                if imgs_ is not None:
                                    print("tuto_abata_8", imgs_)
                                    click_pos_2(920, 65, cla)

                            else:
                                print("tuto_abata_7", imgs_)
                                click_pos_2(900, 1010, cla)
                        else:
                            print("tuto_abata_6", imgs_)
                            click_pos_2(650, 200, cla)
                    else:
                        print("tuto_abata_5", imgs_)
                        click_pos_2(800, 130, cla)
                else:
                    print("tuto_abata_4", imgs_)
                    click_pos_2(920, 65, cla)
            else:
                print("tuto_abata_3", imgs_)
                click_pos_2(480, 980, cla)
        else:
            print("tuto_abata_2", imgs_)
            click_pos_2(800, 1000, cla)
    else:
        print("tuto_abata_1", imgs_)
        click_pos_2(300, 680, cla)

    # tuto_boonhae
    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_boonhae_1.png"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set(740, 120, 950, 170, cla, img)
    if imgs_ is None or imgs_ == False:
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_boonhae_2.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(750, 120, 950, 190, cla, img)
        if imgs_ is None or imgs_ == False:
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_boonhae_3.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(200, 120, 590, 200, cla, img)
            if imgs_ is None or imgs_ == False:
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_boonhae_4.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(0, 670, 240, 710, cla, img)
                if imgs_ is None or imgs_ == False:
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_boonhae_5.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(630, 620, 940, 700, cla, img)
                    if imgs_ is None or imgs_ == False:
                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_boonhae_6.png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(510, 910, 580, 960, cla, img)
                        if imgs_ is not None:
                            print("tuto_boonhae_6", imgs_)
                            click_pos_2(550, 940, cla)

                    else:
                        print("tuto_boonhae_5", imgs_)
                        click_pos_2(550, 660, cla)
                else:
                    print("tuto_boonhae_4", imgs_)
                    click_pos_2(120, 770, cla)
            else:
                print("tuto_boonhae_3", imgs_)
                click_pos_2(625, 160, cla)
        else:
            print("tuto_boonhae_2", imgs_)
            click_pos_2(860, 50, cla)
    else:
        print("tuto_boonhae_1", imgs_)
        click_pos_2(920, 65, cla)

    # tuto_jejak
    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_jejak_1.png"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set(800, 110, 950, 170, cla, img)
    if imgs_ is None or imgs_ == False:
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_jejak_2.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(650, 280, 815, 330, cla, img)
        if imgs_ is None or imgs_ == False:
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_jejak_3.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(170, 370, 450, 420, cla, img)
            if imgs_ is None or imgs_ == False:
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_jejak_4.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(430, 200, 710, 250, cla, img)
                if imgs_ is None or imgs_ == False:
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_jejak_5.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(620, 850, 950, 930, cla, img)
                    if imgs_ is None or imgs_ == False:
                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_jejak_6.png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(500, 950, 575, 1000, cla, img)
                        if imgs_ is not None:
                            print("tuto_jejak_6", imgs_)
                            click_pos_2(550, 975, cla)

                    else:
                        print("tuto_jejak_5", imgs_)
                        click_pos_2(840, 1000, cla)
                else:
                    print("tuto_jejak_4", imgs_)
                    click_pos_2(290, 220, cla)
            else:
                print("tuto_jejak_3", imgs_)
                click_pos_2(80, 385, cla)
        else:
            print("tuto_jejak_2", imgs_)
            click_pos_2(740, 215, cla)
    else:
        print("tuto_jejak_1", imgs_)
        click_pos_2(920, 65, cla)

    # tuto_ganghwa
    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_ganghwa_1.png"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set(690, 120, 950, 230, cla, img)
    if imgs_ is None or imgs_ == False:
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_ganghwa_2.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(180, 130, 580, 210, cla, img)
        if imgs_ is None or imgs_ == False:
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_ganghwa_3.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(200, 670, 380, 720, cla, img)
            if imgs_ is None or imgs_ == False:
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_ganghwa_4.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(480, 840, 770, 910, cla, img)
                if imgs_ is None or imgs_ == False:
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_ganghwa_5.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(50, 870, 530, 950, cla, img)
                    if imgs_ is None or imgs_ == False:
                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\tuto_ganghwa_6.png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(690, 110, 950, 190, cla, img)
                        if imgs_ is not None:
                            print("tuto_ganghwa_6", imgs_)
                            click_pos_2(920, 65, cla)

                    else:
                        print("tuto_ganghwa_5", imgs_)
                        click_pos_2(290, 1000, cla)
                else:
                    print("tuto_ganghwa_4", imgs_)
                    click_pos_2(630, 980, cla)
            else:
                print("tuto_ganghwa_3", imgs_)
                click_pos_2(300, 775, cla)
        else:
            print("tuto_ganghwa_2", imgs_)
            click_pos_2(630, 170, cla)
    else:
        print("tuto_ganghwa_1", imgs_)
        click_pos_2(860, 50, cla)


def nida_grow(cla):
    print("니다 성장")
    from action import go_quest_ing
    from myfunction import click_pos_2, imgs_set_

    import numpy as np
    import cv2

    # 니드호그
    nidhog_ = False
    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\nidhog_1.png"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(700, 120, 910, 160, cla, img, 0.75)
    if imgs_ is not None and imgs_ != False:
        nidhog_ = True
        print("nidhog_1 보여", imgs_)
    else:
        print("nidhog_1 안보여")
    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\nidhog_2.png"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(700, 120, 910, 160, cla, img, 0.75)
    if imgs_ is not None and imgs_ != False:
        nidhog_ = True
        print("nidhog_2 보여", imgs_)
    else:
        print("nidhog_2 안보여")
    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\nidhog_3.png"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(700, 120, 910, 160, cla, img, 0.75)
    if imgs_ is not None and imgs_ != False:
        nidhog_ = True
        print("nidhog_3 보여", imgs_)
    else:
        print("nidhog_3 안보여")

    if nidhog_ == True:
        result = go_quest_ing(cla)
        if result == True:
            click_pos_2(900, 890, cla)
            time.sleep(1)
            click_pos_2(900, 890, cla)
            time.sleep(2)

            quest_count = 0
            result_ = False
            while result_ is False:
                click_pos_2(650, 500, cla)
                time.sleep(6)
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\nidhog_1.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(700, 120, 910, 160, cla, img, 0.75)
                if imgs_ is not None and imgs_ != False:
                    quest_count = 0
                else:
                    quest_count += 1
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\nidhog_2.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(700, 120, 910, 160, cla, img, 0.75)
                if imgs_ is not None and imgs_ != False:
                    quest_count = 0
                else:
                    quest_count += 1
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\nidhog_3.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(700, 120, 910, 160, cla, img, 0.75)
                if imgs_ is not None and imgs_ != False:
                    quest_count = 0
                else:
                    quest_count += 1

                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\nidhog_7.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(700, 120, 910, 160, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    quest_count += 1

                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\quest\\complete_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(700, 120, 910, 160, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    quest_count += 1

                if quest_count > 5:
                    result_ = True


def yotoon_grow_end(cla):
    try:
        from myfunction import imgs_set
        import numpy as np
        import cv2



        yotoon_end = False
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\yotoon_end_1.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(60, 110, 180, 160, cla, img)
        if imgs_ is None or imgs_ == False:
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\yotoon_end_2.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(60, 110, 180, 160, cla, img)
            if imgs_ is None or imgs_ == False:
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\yotoon_end_3.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(60, 110, 180, 160, cla, img)
                if imgs_ is None or imgs_ == False:
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\yotoon_end_4.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(60, 110, 180, 160, cla, img)
                    if imgs_ is None or imgs_ == False:
                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\yotoon_end_11.png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(60, 110, 180, 160, cla, img)
                        if imgs_ is None or imgs_ == False:
                            print("요툰 성장 계속 진행")
                        else:
                            print('yotoon_end_11', imgs_)
                            yotoon_end = True
                    else:
                        print('yotoon_end_4', imgs_)
                        yotoon_end = True
                else:
                    print('yotoon_end_3', imgs_)
                    yotoon_end = True
            else:
                print('yotoon_end_2', imgs_)
                yotoon_end = True
        else:
            print('yotoon_end_1', imgs_)
            yotoon_end = True

        if yotoon_end == False:
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\yotoon_end_22.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(60, 110, 180, 160, cla, img)
            if imgs_ is not None and imgs_ == False:
                print('yotoon_end_22', imgs_)
                yotoon_end = True
            else:
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\yotoon_end_33.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(60, 110, 180, 160, cla, img)
                if imgs_ is not None and imgs_ == False:
                    print('yotoon_end_33', imgs_)
                    yotoon_end = True
        return yotoon_end
    except Exception as e:
        print(e)
        return 0

###
def nida_grow_end(cla):
    try:
        import pyautogui
        from myfunction import imgs_set, click_pos_2, imgs_set_
        import numpy as np
        import cv2

        nida_end = False

        if cla == "one":
            pyautogui.moveTo(480, 480)
        if cla == "two":
            pyautogui.moveTo(960 + 480, 480)

        endmangdok = True
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\dongool.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(40, 100, 210, 160, cla, img)
        if imgs_ is not None:
            nida_end = True
            click_pos_2(30, 220, cla)
            time.sleep(1)
            click_pos_2(550, 610, cla)
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\nida_end_0.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(40, 100, 210, 160, cla, img, 0.8)
        if imgs_ is not None:
            print('nida_end_0', imgs_)
            nida_end = True
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\nida_end_1.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(40, 100, 210, 160, cla, img, 0.8)
        if imgs_ is None or imgs_ == False:
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\nida_end_2.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(40, 100, 210, 160, cla, img, 0.8)
            if imgs_ is None or imgs_ == False:
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\nida_end_3.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(40, 100, 210, 160, cla, img, 0.8)
                if imgs_ is None or imgs_ == False:
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\nida_end_4.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(40, 100, 210, 160, cla, img, 0.8)
                    if imgs_ is None or imgs_ == False:
                        print("니다 성장 계속 진행")
                    else:
                        print('nida_end_4', imgs_)
                        nida_end = True
                else:
                    print('nida_end_3', imgs_)
                    nida_end = True
            else:
                print('nida_end_2', imgs_)
                nida_end = True
        else:
            print('nida_end_1', imgs_)
            nida_end = True
        return nida_end
    except Exception as e:
        print(e)
        return 0


