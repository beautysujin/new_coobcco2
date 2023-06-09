# import numpy as np
# import cv2
# import os.path
import time
# import random

import sys
sys.path.append('C:/my_games/coobcco2/data_od/mymodule')
# from myfunction import *
# from action import go_alrim_yes, now_hunting_is, now_hunting
# from where import go_worldmap

import variable as v_

def go_test(cla):
    print('hi test! dungeon', cla)



def go_jadong_in(world_, where, force_required, drag, moglog, select, delay, cla):
    try:
        from myfunction import imgs_set, random_int, click_pos_2, drag_pos, go_auto
        from where import go_worldmap
        from clean import clean_screen
        from action import now_hunting_is
        from massenger import line_to_me
        from stop_18 import is_stop
        import numpy as np
        import cv2

        go_ = False

        delay = int(delay)

        # 스케쥴 초기화 관련t ttttttttttttttttttttttttttttttttttttt
        # if os.path.isfile(file_path) == True:
        #     # 파일 읽기
        #     with open(file_path, "r", encoding='utf-8-sig') as file:
        #         lines_ = file.read().splitlines()
        #         lines = ' '.join(lines_).split()

        # go_jadong_in(where, 14500, drag, 550, 875, cla)
        # go_jadong_in(마을, 장소, 요구전투력, 드래그여부, 목록, 선택, 딜레이, cla)
        if cla == 'one':
            jadong_power = int(v_.mypower_1)
        if cla == 'two':
            jadong_power = int(v_.mypower_2)

        if jadong_power >= force_required:
            print("good my Power")
        # else:
        #     why = "요구 전투력 : " + str(force_required) + " / " + "내 전투력 : " + str(jadong_power)
        #     line_to_me(cla, why)
        # 파워 오류로 측정없이 무조건 보내기
        isJadong = False
        while isJadong is False:
            thisWorld = False
            print("자동장소", where)
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\worldmap_1.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(1, 30, 100, 80, cla, img)
            if imgs_ is None or imgs_ == False:
                print("월드맵 아니닷")

                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\worldmap_2.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(1, 30, 100, 80, cla, img)
                if imgs_ is None or imgs_ == False:
                    print("월드맵 아니닷2")
                else:
                    print("월드맵이닷2", imgs_)
                    thisWorld = True
            else:
                print("월드맵이닷", imgs_)
                thisWorld = True

            time.sleep(random_int())

            if thisWorld == True:
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\bbaln_move.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(400, 400, 540, 500, cla, img)
                if imgs_ is None or imgs_ == False:
                    print("빠른이동이 안보여")
                    # 시작
                    result_2 = go_worldmap(cla, "world_moglog")
                    time.sleep(0.5)
                    if result_2 == False:
                        print("아직 월드맵 목록이 아니여")
                        click_pos_2(130, 215, cla)  # 중복


                    time.sleep(random_int())  # 중복
                    if world_ == 'yotoon':
                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\jadong_yotoon.png"
                    if world_ == 'midgard':
                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\world_midgard.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(400, 965, 580, 1010, cla, img)
                    if imgs_ is None or imgs_ == False:
                        if world_ == 'yotoon':
                            print("요툰하임이 안보여")
                        if world_ == 'midgard':
                            print("미드가르드가 안보여")

                        click_pos_2(80, 956, cla)  # 중복
                        time.sleep(1)  # 중복
                        if world_ == 'yotoon':
                            click_pos_2(280, 450, cla)
                        if world_ == 'midgard':
                            click_pos_2(160, 515, cla)

                        time.sleep(1)  # 중복
                        click_pos_2(550, 994, cla)  # 중복
                        time.sleep(1)  # 중복
                    else:
                        if world_ == 'yotoon':
                            print("요툰하임이 보여")
                        if world_ == 'midgard':
                            print("미드가르드가 보여")

                        result_2 = go_worldmap(cla, "world_moglog")
                        time.sleep(2)
                        if result_2 == False:
                            print("아직 월드맵 목록이 아니여")
                            click_pos_2(30, 110, cla)  # 중복
                            time.sleep(1)  # 중복
                        else:
                            print("월드맵 목록이 맞당께")


                            if drag == True:
                                # 드래그
                                drag_pos(135, 745, 135, 210, cla)
                                time.sleep(1)
                                if where == "전사야영지":
                                    isClicked = False
                                    isClicked_count = 0
                                    while isClicked is False:
                                        isClicked_count += 1
                                        if isClicked_count > 5:
                                            isClicked = True
                                        full_path = "c:\\my_games\\coobcco2\\data_od\\jadong\\jadong\\songotnidan_bonguji.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set(85, 495, 200, 540, cla, img)
                                        if imgs_ is not None and imgs_ != False:
                                            print("송곳니단본거지 보여", imgs_)
                                            isClicked = True
                                        else:
                                            print("송곳니단본거지 안 보여")
                                            drag_pos(135, 745, 135, 210, cla)
                                        time.sleep(2)



                            # where로 정확한 장소 이동하게 만들기...

                            click_pos_2(135, moglog, cla)
                            time.sleep(2)  # 중복
                            click_pos_2(705, select, cla)
                            time.sleep(2)  # 중복
                            click_pos_2(892, 1004, cla)  # 중복
                            time.sleep(2)  # 중복
                else:
                    print("빠른이동이 보여")
                    isJadong = True
                    go_ = False


                    # 이후 도착했는지 파악하기
                    is8285 = False
                    while is8285 is False:
                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\bbaln_move.png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(400, 400, 540, 500, cla, img)
                        if imgs_ is None or imgs_ == False:
                            is8285 = True
                        else:
                            click_pos_2(545, 610, cla)  # 중복
                            time.sleep(random_int())

            else:
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\bbaln_move.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(400, 400, 540, 500, cla, img)
                if imgs_ is None or imgs_ == False:
                    print("빠른이동이 안보여")
                    time.sleep(1)
                    result_world = go_worldmap(cla, 'world')
                    if result_world == True:
                        click_pos_2(30, 110, cla)
                        time.sleep(1)
                    else:
                        # click_pos_2(920, 55, cla)
                        # time.sleep(random_int())
                        clean_screen(cla, "go_jadong_in")
                        click_pos_2(130, 215, cla)  # 중복
                        time.sleep(1)
                else:
                    print("빠른이동이 보여")
                    isJadong = True
                    go_ = False
                    is8285 = False
                    while is8285 is False:
                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\bbaln_move.png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(400, 400, 540, 500, cla, img)
                        if imgs_ is None or imgs_ == False:
                            # auto
                            isresultauto = False
                            while isresultauto is False:
                                resultauto = go_auto(cla, '10')
                                if resultauto == False:
                                    print("사냥터 미도착")
                                    time.sleep(random_int())
                                else:

                                    isresultauto = True
                                    print("사냥터 도착", delay)
                                    time.sleep(delay + random_int())

                                    # x 같은 이벤트
                                    is_stop(cla)

                                    click_pos_2(900, 890, cla)
                                    time.sleep(random_int())
                                    result_hunting = now_hunting_is(where, cla)
                                    is8285 = True
                                    time.sleep(random_int())
                        else:

                            click_pos_2(545, 610, cla)  # 중복
                            time.sleep(random_int())


        # else:
        #     print("요구투력 보다 낮아 자동 장소로 변경")
        #     # go_jadong_in(마을, 장소, 요구전투력, 드래그여부, 목록, 선택, 딜레이, cla)
        #     # jadong_cla_ready(cla, '바위해안')
        #     go_jadong_cla_mypower(cla)
        #     # go_jadong_in('yotoon', where, 0, False, 300, 850, cla)



        return go_
    except Exception as e:
        print(e)
        return 0


def start_ready_in_jadong(cla):
    try:
        from clean import clean_screen
        #def nowtestt
        print("start_ready_in_jadong")
        print("1")
        clean_screen(cla, "start_ready_in_jadong")

        # jadong_cla_ready(cla, '바위해안')
        go_jadong_cla_mypower(cla)
        #auto



    except Exception as e:
        print(e)
        return 0


def jadong_cla_play(cla, where):
    try:
        from myfunction import imgs_set, random_int, click_pos_2, drag_pos, myPotion_check
        from clean import clean_screen
        from action import now_hunting

        nowPlay = 'jadong'


        result = False
        if result == True:
            print("xxxxxxxxxxxx")
        else:
            print("zzzzzzzzzzzz")


        clean_screen(cla, "jadong_cla_play")
        result_ = now_hunting(nowPlay, cla)  # False는 현재 노사냥, True는 현재 사냥중
        print("result_ = now_hunting(nowPlay, cla)", result_)
        print("jadong_cla_play : ", where)

        if result_ == False:
            jadong_cla_ready(cla, where)  # False는 자동사냥 진행, True는 자동사냥 노진행
            print("자동사냥 시작")
            time.sleep(10 + random_int())
            # click_pos_2(900, 888, cla)
            # time.sleep(1 + random_int())
            myPotion_check(nowPlay, cla)
            if cla == 'one':
                v_.one_cla_ing = nowPlay
            if cla == 'two':
                v_.two_cla_ing = nowPlay
            time.sleep(5 + random_int())
            print("자동사냥 체크 끝")



            # 여기에 초기화 시간 넣어서 코딩하기(시간함수)
            # 시간
        else:
            complete_1(cla)
            myPotion_check(nowPlay, cla)
        time.sleep(1 + random_int())
        jadong_0_check = False

    except Exception as e:
        print(e)
        return 0

def complete_1(cla):
    try:
        print("complete_1")
        # 수령 다 받을때까지 WHILE  반복

        a = False
        aa = 0
        while a is False:
            aa += 1
            if aa >= 10:
                a = True

            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\quest\\complete_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(770, 170, 840, 320, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                # 퀘스트 의뢰 완료 수령 클릭
                print("complete_1", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)

                # # 카드 있는지 파악 후 있다면 카드 클릭
                # for i in range(5):
                #     full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\quest\\card.PNG"
                #     img_array = np.fromfile(full_path, np.uint8)
                #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #     imgs_ = imgs_set_(300, 550, 680, 680, cla, img, 0.85)
                #     if imgs_ is not None and imgs_ != False:
                #         print("card", imgs_)
                #         click_pos_2(540, 620, cla)
                #         break
                #     else:
                #         print("카드 없다...")
                #     time.sleep(1)

                # 카드 있는지 파악 후 있다면 카드 클릭_2
                card_search_ = False
                card_search_count = 0
                while card_search_ is False:
                    card_search_count += 1
                    if card_search_count > 10:
                        card_search_ = True

                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\quest\\card.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(300, 550, 680, 680, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("card", imgs_)
                        click_pos_2(540, 620, cla)
                        card_search_ = True

                        # 카드 수령 마무리 단계
                        card_search_2 = False
                        card_search_count2 = 0
                        while card_search_2 is False:
                            card_search_count2 += 1
                            if card_search_count2 > 10:
                                card_search_2 = True

                            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\quest\\card.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(300, 550, 680, 680, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("카드 아직 있다.")
                            else:
                                card_search_2 = True
                                # 절대값 REG, 1,2클라 적용 POS_2
                                click_pos_2(550, 930, cla)
                                print("카드 없다...")
                            time.sleep(1)

                    else:
                        print("카드 없다...")
                    time.sleep(1)

            else:
                print("complete_1 없")
                a = True
            time.sleep(3)
    except Exception as e:
        print(e)
        return 0

def dunjeon_cla_ready(cla, dunjeon):
    try:
        from myfunction import imgs_set, random_int, click_pos_2, drag_pos, menuOpenCheck, menuOpen
        from clean import clean_screen
        import numpy as np
        import cv2
        from massenger import line_to_me
        # test
        dunjeon_list_ready = False
        isdungeon_ing = False
        isdungeon_ing_count = 0
        while isdungeon_ing is False:
            isdungeon_ing_count += 1
            if isdungeon_ing_count > 10:
                isdungeon_ing = True
                line_to_me(cla, "오딘 던전 진입 실패...oT,.To...")

            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\dunjeon\\dungeon_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(30, 30, 110, 80, cla, img)
            if imgs_ is not None and imgs_ != False:
                print("진입함")

                click_pos_2(240, 105, cla)
                drag_pos(800, 522, 200, 522, cla)
                time.sleep(1)

                if dunjeon == 'gonghu':
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\gonghu.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(70, 350, 220, 410, cla, img)
                    if imgs_ is not None and imgs_ != False:
                        print("imgs", imgs_)
                        print('공허던전 진입 전')
                        dunjeon_list_ready = True
                        isdungeon_ing = True
                if dunjeon == 'nanjang':
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\nanjang.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(370, 350, 550, 410, cla, img)
                    if imgs_ is not None and imgs_ != False:
                        print("imgs", imgs_)
                        print('난쟁던전 진입 전')
                        dunjeon_list_ready = True
                        isdungeon_ing = True
                if dunjeon == 'underprison':
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\underprison.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(710, 350, 830, 410, cla, img)
                    if imgs_ is not None and imgs_ != False:
                        print("imgs", imgs_)
                        print('지감던전 진입 전')
                        dunjeon_list_ready = True
                        isdungeon_ing = True

            else:
                menuOpen(cla)
                click_pos_2(740, 375, cla)
            time.sleep(0.5)



        return dunjeon_list_ready
    except Exception as e:
        print(e)
        return 0


def in_dunjeon_list(cla, dunjeon):
    try:
        from myfunction import random_int, click_pos_2
        from schedule import myQuest_play_check

        datas = 'check'
        start_ready = myQuest_play_check(cla, datas)

        if '_' in start_ready[0][2]:
            print("_", "hello '_'")
            dunjeon_spl_ = start_ready[0][2].split("_")
            print("dunjeon_spl_[0]", dunjeon_spl_[0])
            print("dunjeon_spl_[1]", dunjeon_spl_[1])
            dunjeon_level = int(dunjeon_spl_[1])

        step = 'none'

        y_ = 170

        if cla == 'one':
            level_ = v_.mylevel_1
            power_ = v_.mypower_1
        if cla == 'two':
            level_ = v_.mylevel_2
            power_ = v_.mypower_2
        if dunjeon == 'gonghu':
            # 전투력 및 레벨 체크 후 클릭
            # if level_ >= 70 and power_ >= 30000:
            #     y_ = 400
            #     click_pos_2(160, 400, cla)
            #     time.sleep(1 + random_int())
            #     step = '광기의 균열'
            # elif level_ >= 64 and power_ >= 26000:
            #     y_ = 345
            #     click_pos_2(160, 345, cla)
            #     time.sleep(1 + random_int())
            #     step = '분쟁의 신전'
            # elif power_ >= 23000 and level_ >= 56:
            #     y_ = 285
            #     click_pos_2(160, 285, cla)
            #     time.sleep(1 + random_int())
            #     step = '공포의 내리막'
            # elif power_ >= 17000 and level_ >= 48:
            #     y_ = 230
            #     click_pos_2(160, 230, cla)
            #     time.sleep(1 + random_int())
            #     step = '혼돈의 동굴'
            # elif power_ >= 14000 and level_ >= 35:
            #     y_ = 170
            #     click_pos_2(160, 170, cla)
            #     time.sleep(1 + random_int())
            #     step = '악취 나는 통로'
            # else:
            #     click_pos_2(160, 115, cla)
            #     time.sleep(1 + random_int())
            #     step = '균열의 입구'
            if dunjeon_level == 6:
                y_ = 400
                click_pos_2(160, 400, cla)
                time.sleep(1 + random_int())
                step = '광기의 균열'
            elif dunjeon_level == 5:
                y_ = 345
                click_pos_2(160, 345, cla)
                time.sleep(1 + random_int())
                step = '분쟁의 신전'
            elif dunjeon_level == 4:
                y_ = 285
                click_pos_2(160, 285, cla)
                time.sleep(1 + random_int())
                step = '공포의 내리막'
            elif dunjeon_level == 3:
                y_ = 230
                click_pos_2(160, 230, cla)
                time.sleep(1 + random_int())
                step = '혼돈의 동굴'
            elif dunjeon_level == 2:
                y_ = 170
                click_pos_2(160, 170, cla)
                time.sleep(1 + random_int())
                step = '악취 나는 통로'
            else:
                click_pos_2(160, 115, cla)
                time.sleep(1 + random_int())
                step = '균열의 입구'
        elif dunjeon == 'nanjang':
            # 전투력 및 레벨 체크 후 클릭
            # if level_ >= 71 and power_ >= 30000:
            #     y_ = 400
            #     click_pos_2(160, 400, cla)
            #     time.sleep(1 + random_int())
            #     step = '불타버린 길'
            # elif level_ >= 65 and power_ >= 26000:
            #     y_ = 345
            #     click_pos_2(160, 345, cla)
            #     time.sleep(1 + random_int())
            #     step = '울부짖는 길'
            # elif power_ >= 23000 and level_ >= 57:
            #     y_ = 285
            #     click_pos_2(160, 285, cla)
            #     time.sleep(1 + random_int())
            #     step = '상처입은 길'
            # elif power_ >= 17000 and level_ >= 49:
            #     y_ = 230
            #     click_pos_2(160, 230, cla)
            #     time.sleep(1 + random_int())
            #     step = '얼어붙은 길'
            # elif power_ >= 14000 and level_ >= 36:
            #     y_ = 170
            #     click_pos_2(160, 170, cla)
            #     time.sleep(1 + random_int())
            #     step = '속삭이는 길'
            # else:
            #     click_pos_2(160, 115, cla)
            #     time.sleep(1 + random_int())
            #     step = '저주받은 길'
            if dunjeon_level == 6:
                y_ = 400
                click_pos_2(160, 400, cla)
                time.sleep(1 + random_int())
                step = '불타버린 길'
            elif dunjeon_level == 5:
                y_ = 345
                click_pos_2(160, 345, cla)
                time.sleep(1 + random_int())
                step = '울부짖는 길'
            elif dunjeon_level == 4:
                y_ = 285
                click_pos_2(160, 285, cla)
                time.sleep(1 + random_int())
                step = '상처입은 길'
            elif dunjeon_level == 3:
                y_ = 230
                click_pos_2(160, 230, cla)
                time.sleep(1 + random_int())
                step = '얼어붙은 길'
            elif dunjeon_level == 2:
                y_ = 170
                click_pos_2(160, 170, cla)
                time.sleep(1 + random_int())
                step = '속삭이는 길'
            else:
                click_pos_2(160, 115, cla)
                time.sleep(1 + random_int())
                step = '저주받은 길'
        elif dunjeon == 'underprison':
            # 전투력 및 레벨 체크 후 클릭
            # if power_ >= 60000:
            #     y_ = 575
            #     click_pos_2(160, 575, cla)
            #     time.sleep(1 + random_int())
            #     step = '혼돈의 전당'
            # elif power_ >= 50000:
            #     y_ = 520
            #     click_pos_2(160, 520, cla)
            #     time.sleep(1 + random_int())
            #     step = '최악의 심연'
            # elif power_ >= 40000:
            #     y_ = 460
            #     click_pos_2(160, 460, cla)
            #     time.sleep(1 + random_int())
            #     step = '나태의 지옥'
            # elif power_ >= 30000:
            #     y_ = 400
            #     click_pos_2(160, 400, cla)
            #     time.sleep(1 + random_int())
            #     step = '식탐의 방'
            # elif power_ >= 25000:
            #     y_ = 345
            #     click_pos_2(160, 345, cla)
            #     time.sleep(1 + random_int())
            #     step = '음욕의 나락'
            # elif power_ >= 20000:
            #     y_ = 285
            #     click_pos_2(160, 285, cla)
            #     time.sleep(1 + random_int())
            #     step = '분노의 처형터'
            # elif power_ >= 17000:
            #     y_ = 230
            #     click_pos_2(160, 230, cla)
            #     time.sleep(1 + random_int())
            #     step = '질투의 고문소'
            # elif power_ >= 14000:
            #     y_ = 170
            #     click_pos_2(160, 170, cla)
            #     time.sleep(1 + random_int())
            #     step = '탐욕의 묘지'
            # else:
            #     click_pos_2(160, 115, cla)
            #     time.sleep(1 + random_int())
            #     step = '교만의 감옥'
            # 지하감옥은 자체로 6층 까지만 열어두자
            # if dunjeon_level == 9:
            #     y_ = 575
            #     click_pos_2(160, 575, cla)
            #     time.sleep(1 + random_int())
            #     step = '혼돈의 전당'
            # elif dunjeon_level == 8:
            #     y_ = 520
            #     click_pos_2(160, 520, cla)
            #     time.sleep(1 + random_int())
            #     step = '최악의 심연'
            # elif dunjeon_level == 7:
            #     y_ = 460
            #     click_pos_2(160, 460, cla)
            #     time.sleep(1 + random_int())
            #     step = '나태의 지옥'
            if dunjeon_level == 6:
                y_ = 400
                click_pos_2(160, 400, cla)
                time.sleep(1 + random_int())
                step = '식탐의 방'
            elif dunjeon_level == 5:
                y_ = 345
                click_pos_2(160, 345, cla)
                time.sleep(1 + random_int())
                step = '음욕의 나락'
            elif dunjeon_level == 4:
                y_ = 285
                click_pos_2(160, 285, cla)
                time.sleep(1 + random_int())
                step = '분노의 처형터'
            elif dunjeon_level == 3:
                y_ = 230
                click_pos_2(160, 230, cla)
                time.sleep(1 + random_int())
                step = '질투의 고문소'
            elif dunjeon_level == 2:
                y_ = 170
                click_pos_2(160, 170, cla)
                time.sleep(1 + random_int())
                step = '탐욕의 묘지'
            else:
                click_pos_2(160, 115, cla)
                time.sleep(1 + random_int())
                step = '교만의 감옥'

        return step, y_
    except Exception as e:
        print(e)
        return 0

def dunjeon_in_cla_ready(cla, dunjeon):
    try:
        from myfunction import imgs_set, random_int, click_pos_2, click_pos_reg, go_auto, imgs_set_
        from action import go_alrim_yes
        from clean import clean_screen
        from schedule import myQuest_play_check, myQuest_play_add
        from massenger import line_to_me
        from stop_18 import is_stop
        import numpy as np
        import cv2
        import os

        print("던전준비", cla)
        print("던전준비", dunjeon)
        step = "none"
        isdungeon_ing = True

        isdunjeonclaready = False
        dunjeon_0_check = True
        isdunjeonclaready_count = 0
        while isdunjeonclaready is False:
            isdunjeonclaready_count += 1
            if isdunjeonclaready_count > 10:
                isdunjeonclaready = True
                line_to_me(cla, "던전 진입중 문제 발생")

            # select_stair = False
            print("점검--28----------------------던전화면으로 이동")
            result_d = dunjeon_cla_ready(cla, dunjeon)

            if result_d == True:
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\dunjeon_lock.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

                # 여기 던전마다 이미지 위치 달라져야 한다
                if dunjeon == 'gonghu':
                    imgs_ = imgs_set(80, 440, 220, 580, cla, img)
                if dunjeon == 'nanjang':
                    imgs_ = imgs_set(390, 440, 530, 580, cla, img)
                if dunjeon == 'underprison':
                    imgs_ = imgs_set(710, 440, 850, 580, cla, img)

                if imgs_ is None or imgs_ == False:
                    print("rock 없고, 0초 인지 파악하자")
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\zero.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

                    # 여기 던전마다 이미지 위치 달라져야 한다
                    if dunjeon == 'gonghu':
                        imgs_ = imgs_set_(100, 645, 200, 685, cla, img, 0.8)
                    if dunjeon == 'nanjang':
                        imgs_ = imgs_set_(410, 645, 510, 685, cla, img, 0.8)
                    if dunjeon == 'underprison':
                        imgs_ = imgs_set_(730, 645, 830, 685, cla, img, 0.8)



                    if imgs_ is None:
                        print("없..")
                        # 여기 던전마다 클릭 위치 달라져야 한다.
                        if dunjeon == 'gonghu':
                            click_pos_2(160, 520, cla)
                        if dunjeon == 'nanjang':
                            click_pos_2(460, 520, cla)
                        if dunjeon == 'underprison':
                            click_pos_2(760, 520, cla)
                        time.sleep(3 + random_int())

                        # 여기서 화면 넘어갔는지 확인인
                        in_jungye = False
                        in_jungye_count = 0
                        while in_jungye is False:
                            in_jungye_count += 1
                            if in_jungye_count > 10:
                                in_jungye = True
                            print("ho")
                            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\jungye.png"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set(30, 30, 140, 80, cla, img)
                            if imgs_ is None or imgs_ == False:
                                print("정예던전이 없다. 클릭")
                                # 여기 던전마다 클릭 위치 달라져야 한다.
                                if dunjeon == 'gonghu':
                                    click_pos_2(160, 520, cla)
                                if dunjeon == 'nanjang':
                                    click_pos_2(460, 520, cla)
                                if dunjeon == 'underprison':
                                    click_pos_2(760, 520, cla)
                                time.sleep(3 + random_int())
                            else:
                                print("정예던전이 있다. 진행..")
                                in_jungye = True
                                # 실수로 들어왔을 경우 한번더 체크(끝난 던전인지.../////////////////////////////////////////////////////////////////////////////////////////////////)
                                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\dunjeon\\dungeon_clear_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set(660, 960, 740, 1000, cla, img)
                                if imgs_ is not None and imgs_ != False:
                                    print("dungeon_clear_1", imgs_)
                                    isdunjeonclaready = True
                                    print("imgs", imgs_)
                                    print("여기 " + str(dunjeon) + " 이미 끝나 있음.")
                                    dunjeon_0_check = False
                                    isdungeon_ing = False
                                else:
                                    print("dungeon_clear_1 없")


                                    #
                                    in_dun = False
                                    in_dun_count = 0
                                    while in_dun is False:
                                        in_dun_count += 1
                                        if in_dun_count > 30:
                                            in_dun = True
                                            line_to_me(cla, "던전 진입중 오류...")

                                        in_dun_pic = False

                                        dir_path = "C:\\my_games\\coobcco2\\data_od"
                                        file_path = dir_path + "\\imgs\\dunjeon\\in_dun.txt"

                                        with open(file_path, "r", encoding='utf-8-sig') as file:
                                            read_indun = file.read().splitlines()
                                            print("던전?", read_indun)

                                        for i in range(len(read_indun)):
                                            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\dunjeon\\in_dun\\" + read_indun[
                                                i] + ".PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(40, 100, 240, 340, cla, img, 0.85)
                                            if imgs_ is not None and imgs_ != False:
                                                print(read_indun[i], "던전 내 표시 있다~!")
                                                in_dun_pic = True

                                        if in_dun_pic == True:
                                            result_auto = go_auto(cla, 999)
                                            if result_auto == True:
                                                in_dun = True
                                                print("던전 진입 완료")
                                                time.sleep(0.5)
                                                click_pos_2(585, 985, cla)
                                                time.sleep(0.1)
                                                click_pos_2(585, 985, cla)
                                                time.sleep(1)
                                                in_dun2 = False
                                                in_dun_count2 = 0
                                                while in_dun2 is False:
                                                    in_dun_count2 += 1
                                                    if in_dun_count2 > 30:
                                                        in_dun2 = True
                                                        line_to_me(cla, "던전 진입중 오류...222")

                                                    result_auto = go_auto(cla, 999)
                                                    if result_auto == True:
                                                        in_dun2 = True
                                                        isdunjeonclaready = True
                                                        print("던전 재진입 완료")
                                                        time.sleep(0.5)

                                                        # x 같은 이벤트
                                                        is_stop(cla)

                                                        click_pos_2(900, 890, cla)
                                                    time.sleep(0.5)
                                        else:
                                            if in_dun_count == 2 or in_dun_count == 22:
                                                print("진입중")
                                                # 여긴 던전마다 다른 포인트...
                                                in_dunjeon_list(cla, dunjeon)
                                                time.sleep(0.2)
                                                step = in_dunjeon_list(cla, dunjeon)
                                                print('step', step)
                                                time.sleep(0.5)

                                                click_pos_2(840, 992, cla)
                                                time.sleep(0.2)
                                                click_pos_2(840, 992, cla)
                                                time.sleep(0.5)

                                                result_ = go_alrim_yes(cla)
                                                if result_[0] == True:
                                                    click_pos_reg(result_[1], result_[2], cla)
                                                else:
                                                    click_pos_2(550, 610, cla)
                                        time.sleep(0.5)


                            time.sleep(0.3)
                    else:
                        isdunjeonclaready = True
                        # while 끝
                        print("zero....이미 끝", imgs_)
                        print("여기 " + str(dunjeon) + " 던전 끝")
                        dunjeon_0_check = False
                        isdungeon_ing = False

                else:
                    isdunjeonclaready = True
                    # while 끝
                    print("던전 안 열림", imgs_)
                    print("여기 " + str(dunjeon) + " 던전 열리지 않았음. 던전 완료로 간주.")
                    dunjeon_0_check = False
                    isdungeon_ing = False
            else:

                clean_screen(cla, "dunjeon_in_cla_ready")
                # dunjeon_cla_ready(cla, dunjeon)

            if dunjeon_0_check == False:
                print(dunjeon + " 끝???남...")
                click_pos_2(930, 60, cla)
        # isdungeon_ing => False는 완료
        return step[0], isdungeon_ing
    except Exception as e:
        print(e)
        return 0




def jadong_low_power(cla):
    try:
        from myfunction import imgs_set, random_int, click_pos_2
        print('들소황무지')
        click_pos_2(130, 215, cla)
        time.sleep(3 + random_int())
        click_pos_2(80, 956, cla)
        time.sleep(3 + random_int())

        click_pos_2(280, 450, cla)
        time.sleep(3 + random_int())
        click_pos_2(550, 994, cla)
        time.sleep(5 + random_int())
        click_pos_2(28, 106, cla)
        time.sleep(3 + random_int())
        click_pos_2(135, 300, cla)
        time.sleep(3 + random_int())

        click_pos_2(700, 850, cla)
        time.sleep(3 + random_int())
        click_pos_2(892, 1004, cla)
        time.sleep(3 + random_int())
        click_pos_2(545, 610, cla)
        time.sleep(20 + random_int())
        time.sleep(25 + random_int())
    except Exception as e:
        print(e)
        return 0
def go_jadong_cla_mypower(cla):
    try:
        import os.path
        import random

        hunt_where = "none"
        jadong_power = 0
        if cla == 'one':
            jadong_power = v_.mypower_1
            jadong_now = v_.jadong_1
        if cla == 'two':
            jadong_power = v_.mypower_2
            jadong_now = v_.jadong_2


        dir_path = "C:\\my_games\\coobcco2\\data_od"
        file_path12 = dir_path + "\\jadong\\jadong_random.txt"

        if os.path.isfile(file_path12) == True:
            # 파일 읽기
            with open(file_path12, "r", encoding='utf-8-sig') as file:
                lines_ = file.read().splitlines()
                lines = ' '.join(lines_).split()

        # print("random list_1", random.choice(lines))
        # print("random list_2", random.choice(lines))

        for i in range(len(lines)):
            result_hunt = lines[i].split(":")

            if int(jadong_power) >= int(result_hunt[0]):
                print("내 전투력 " + str(result_hunt[0]) + " 이상")
                hunt_where = random.choice(result_hunt[1].split("/"))
                break

        print("당첨된 장소 : ", hunt_where)
        if hunt_where != "none":
            jadong_cla_ready(cla, str(hunt_where))
        else:
            jadong_cla_ready(cla, '바위해안')




    except Exception as e:
        print(e)
        return 0
def jadong_cla_ready(cla, where):
    try:
        import os.path

        if cla == 'one':
            jadong_power = v_.mypower_1
            jadong_now = v_.jadong_1
        if cla == 'two':
            jadong_power = v_.mypower_2
            jadong_now = v_.jadong_2

        none_where = True

        print("자동사냥 준비(내 전투력 : )", jadong_power)
        print("자동사냥 준비(장소 : )", where)

        # go_jadong_in(마을, where, 14500, drag, 550, 875, cla)
        # go_jadong_in(마을 ,장소, 요구전투력, 드래그여부, 목록, 선택, 딜레이, cla)
        dir_path = "C:\\my_games\\coobcco2\\data_od"
        file_path = dir_path + "\\jadong\\jadong_in.txt"

        if os.path.isfile(file_path) == True:
            # 파일 읽기
            with open(file_path, "r", encoding='utf-8-sig') as file:
                lines_ = file.read().splitlines()
                lines = ' '.join(lines_).split()
                print('lines', lines)
                print('lines[0]', lines[0])
                # result_ = []
                for i in range(len(lines)):
                    result_file = lines[i].split(':')
                    # print('lines', lines[i])
                    # print('result_file[0]', result_file[0]) # 마을
                    # print('result_file[1]', result_file[1]) # 장소
                    # print('result_file[2]', result_file[2]) # 요구전투력
                    # print('result_file[3]', result_file[3]) # 드래그
                    # print('result_file[4]', result_file[4]) # 목록
                    # print('result_file[5]', result_file[5]) # 선택
                    # print('result_file[6]', result_file[6]) # 딜레이
                    if result_file[1] == where:
                        result_ = result_file
                        none_where = False
                if none_where == False:
                    print("result_", result_)
                    if result_[3] == 'true':
                        re_ = True
                    else:
                        re_ = False
                    result = go_jadong_in(result_[0], result_[1], int(result_[2]), re_, int(result_[4]), int(result_[5]), int(result_[6]), cla)
                    print("go_jadong_result", result)
                else:
                    # jadong_cla_ready(cla, '바위해안')
                    go_jadong_cla_mypower(cla)


        return jadong_now
    except Exception as e:
        print(e)
        return 0





def dunjeon_cla_play(cla, data, dunjeon):
    try:
        from clean import clean_screen
        from myfunction import random_int, click_pos_2, imgs_set, myPotion_check, imgs_set_, drag_pos
        from action import now_hunting, now_hunting_is
        import os
        import numpy as np
        import cv2
        print("현재 던전 : " + str(dunjeon) + " 진행중")
        print(str(dunjeon) + " 진행중? " + str(data))
        print("data!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", data)

        questcomplete = False
        in_dun_ = False

        dir_path = "C:\\my_games\\coobcco2\\data_od"
        file_path = dir_path + "\\imgs\\dunjeon\\in_dun.txt"

        with open(file_path, "r", encoding='utf-8-sig') as file:
            indun = file.read().splitlines()
            print("&&&&&&", indun)

        for i in range(len(indun)):
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\dunjeon\\in_dun\\" + indun[i] + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(40, 100, 240, 340, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print(indun[i], "///////////////////있다/////////////////////")
                in_dun_ = True

        print("in_dun_////////////////////////////", in_dun_)

        if in_dun_ == False:
            # 던전 입장하기

            result = dunjeon_in_cla_ready(cla, dunjeon)
            print("던전체크", result)
            # [0] 현재 돌고 있는 곳, [1] False 면 완료

            if result[1] == False:
                questcomplete = True


        else:
            myPotion_check(data, cla)
            result_ = now_hunting_is(data, cla)
            if result_ == False:
                drag_pos(250, 650, 350, 650, cla)
                time.sleep(0.2)

            print("던전 중")


        return questcomplete
    except Exception as e:
        print(e)
        return 0


def dunjeonCheck(cla, data, same):
    try:
        from myfunction import random_int, click_pos_2, myPotion_check, imgs_set
        from where import go_worldmap
        from clean import clean_screen, game_event_popup
        from action import now_hunting_is, go_potion_off
        import pyautogui
        import numpy as np
        import cv2

        print("def dunjeonCheck(cla, data, same): start", same)
        # data = gonghu, nanjang, underprison
        isdunjeonCheck = False
        dungeon_decision = False
        # data는 해당던전 종류(공허, 난쟁, 지하감옥)

        # 던전내에서 순간이동, 자동사냥, 지도 클릭 => 진행중일땐 최초 1회만...
        isIndungeon = False
        while isdunjeonCheck is False:
            if same == False:
                while isIndungeon is False:

                    result = mydungeon_check(cla, 'in_check')
                    if result == False:
                        print("def dunjeonCheck(cla, data, same): False => 던전 진입 전")
                        click_pos_2(120, 210, cla)
                        time.sleep(5)
                        result_world = go_worldmap(cla, 'world') #월드보기
                        if result_world == True:
                            isIndungeon = True
                            if cla == 'one':
                                v_.one_cla_ing = 'check'
                            if cla == 'two':
                                v_.two_cla_ing = 'check'
                            clean_screen(cla, "dunjeonCheck")
                    else:
                        time.sleep(random_int())
                        game_event_popup(cla)
                        click_pos_2(585, 985, cla)
                        # 여기서 가방화면 나오면 곤란...

                        isIndungeon = True
                        isSoongan = False
                        while isSoongan is False:
                            result_ = mydungeon_check(cla, 'in_check')
                            if result_ == False:
                                print("def dunjeonCheck(cla, data, same): 던전 진입 중, 순간이동 하는 중")
                                # 만약 현재 월드맵일 경우 다시 던전에 재진입 해야함.
                                thisWorld = False
                                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\worldmap_1.png"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set(1, 30, 100, 80, cla, img)
                                if imgs_ is None or imgs_ == False:
                                    print("월드맵 아니닷, clean_screen")

                                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\worldmap_2.png"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set(1, 30, 100, 80, cla, img)
                                    if imgs_ is None or imgs_ == False:
                                        print("월드맵 아니닷2, clean_screen")
                                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\worldmap_3.png"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set(1, 30, 100, 80, cla, img)
                                        if imgs_ is None or imgs_ == False:
                                            print("월드맵 아니닷3, clean_screen")
                                            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\worldmap_4.png"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set(1, 30, 100, 80, cla, img)
                                            if imgs_ is None or imgs_ == False:
                                                print("월드맵 아니닷4, clean_screen")
                                                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\worldmap_5.png"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set(1, 30, 100, 80, cla, img)
                                                if imgs_ is None or imgs_ == False:
                                                    print("월드맵 아니닷5, clean_screen")
                                                else:
                                                    print("월드맵이닷5, clean_screen", imgs_)
                                                    thisWorld = True
                                            else:
                                                print("월드맵이닷4, clean_screen", imgs_)
                                                thisWorld = True
                                        else:
                                            print("월드맵이닷3, clean_screen", imgs_)
                                            thisWorld = True
                                    else:
                                        print("월드맵이닷2, clean_screen", imgs_)
                                        thisWorld = True
                                else:
                                    print("월드맵이닷, clean_screen", imgs_)
                                    thisWorld = True

                                if thisWorld == True:
                                    isSoongan = True
                                    click_pos_2(920, 55, cla)
                                time.sleep(random_int())
                            else:
                                isSoongan = True
                                click_pos_2(900, 890, cla)
                                result = now_hunting_is(data, cla)
                                time.sleep(random_int())
                                # if result == False:
                                #     click_pos_2(585, 985, cla)
                                #     time.sleep(random_int())
                                #     now_hunting_is(data, cla)


                                result__ = mydungeon_check(cla, 'ing_check')
                                if result__ == False:
                                    # 던전 아닐 가능성 높음.
                                    click_pos_2(125, 215, cla)
                                    time.sleep(random_int())

                                result___ = go_potion_off(cla)
                                if result___ == False:
                                    click_pos_2(800, 840, cla)
                                    time.sleep(random_int())
                                    click_pos_2(700, 840, cla)
                                    time.sleep(random_int())
                                    # click_pos_2(570, 50, cla)
                                    pyautogui.moveTo(490, 550, 0.2)



            game_event_popup(cla)
            result = mydungeon_check(cla, 'ing_check')
            print("던전 진행중인지 mydungeon_check로 확인중", result)
            if result == True:
                isdunjeonCheck = True
                dungeon_decision = True
                myPotion_check(data, cla)
                print("mydungeoncheck로 확인하니 현재 던전 진행 중.")
                if cla == 'one':
                    v_.one_cla_ing = data
                if cla == 'two':
                    v_.two_cla_ing = data
                print("good", str(cla) + " 클라_ing :" + str(data))
            else:
                isdunjeonCheck = True
                print("mydungeoncheck로 확인하니 던전 진행중이지 않음")

        print("def dunjeonCheck(cla, data, same): end", same)
        return dungeon_decision
    except Exception as e:
        print(e)
        return 0

def mydungeon_check(cla, data):
    try:
        from myfunction import drag_pos, click_pos_2, imgs_set
        import numpy as np
        import cv2

        go_ = False

        if data == 'ing_check':
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\dunjeon\\namum_2.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(100, 280, 200, 330, cla, img)
            if imgs_ is not None:
                go_ = True
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\dunjeon\\namum_3.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(100, 280, 200, 330, cla, img)
            if imgs_ is not None:
                go_ = True

            isMap = False
            while isMap is False:
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\dun_x.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(630, 320, 700, 365, cla, img)
                if imgs_ is None:
                    print("던전 X 안보여")
                    click_pos_2(125, 215, cla)
                    time.sleep(1)
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\namum.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(100, 280, 200, 330, cla, img)
                    if imgs_ is None:
                        print("던전 남음 안보여")
                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\dangye.png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(360, 320, 600, 365, cla, img)
                        if imgs_ is None:
                            print("던전 단계 안보여")
                            isMap = True
                            go_ = False
                            click_pos_2(920, 55, cla)
                        else:
                            print("던전 단계 보여", imgs_)
                            isMap = True
                            go_ = True
                    else:
                        print("던전 남음 보여", imgs_)
                        isMap = True
                        go_ = True
                else:
                    print("던전 X 보여", imgs_)
                    isMap = True
                    go_ = True

            if go_ == False:
                drag_pos(545, 725, 600, 725, cla)
                time.sleep(1)
                click_pos_2(125, 215, cla)
                time.sleep(1)

                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\dunjeon\\namum_2.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(100, 280, 200, 330, cla, img)
                if imgs_ is not None:
                    go_ = True
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\dunjeon\\namum_3.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(100, 280, 200, 330, cla, img)
                if imgs_ is not None:
                    go_ = True

                isMap = False
                while isMap is False:
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\dun_x.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(630, 320, 700, 365, cla, img)
                    if imgs_ is None:
                        print("던전 X 안보여")
                        click_pos_2(125, 215, cla)
                        time.sleep(1)
                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\namum.png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(100, 280, 200, 330, cla, img)
                        if imgs_ is None:
                            print("던전 남음 안보여")
                            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\dangye.png"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set(360, 320, 600, 365, cla, img)
                            if imgs_ is None:
                                print("던전 단계 안보여")
                                isMap = True
                                go_ = False
                                click_pos_2(920, 55, cla)
                            else:
                                print("던전 단계 보여", imgs_)
                                isMap = True
                                go_ = True
                        else:
                            print("던전 남음 보여", imgs_)
                            isMap = True
                            go_ = True
                    else:
                        print("던전 X 보여", imgs_)
                        isMap = True
                        go_ = True

        # 던전 사진들 비교하기기 x 545 y 725 x 600
        if data =='in_check':
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\dunjeon\\namum_2.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(100, 280, 200, 330, cla, img)
            if imgs_ is not None:
                go_ = True
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\dunjeon\\namum_3.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(100, 280, 200, 330, cla, img)
            if imgs_ is not None:
                go_ = True
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\namum.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(100, 280, 200, 330, cla, img)
            if imgs_ is None or imgs_ == False:
                print("던전 남음 안보여(in_check)")
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\dangye.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(360, 320, 600, 365, cla, img)
                if imgs_ is not None:
                    print("던전 단계 보여(in_check)", imgs_)
                    go_ = True
                else:
                    print("던전 단계 안보여(in_check)")
                    click_pos_2(120, 210, cla)
                    time.sleep(1)
                    drag_pos(545, 725, 600, 725, cla)
                    time.sleep(1)
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\dangye.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(360, 320, 600, 365, cla, img)
                    full_path2 = "c:\\my_games\\coobcco2\\data_od\\imgs\\jiha.png"
                    img_array2 = np.fromfile(full_path2, np.uint8)
                    img2 = cv2.imdecode(img_array2, cv2.IMREAD_COLOR)
                    imgs_2 = imgs_set(360, 320, 600, 365, cla, img2)
                    if imgs_ is not None:
                        print("던전 단계 보여2(in_check)", imgs_)
                        go_ = True
                    else:
                        print("던전 단계 안보여2(in_check)")
                    if imgs_2 is not None:
                        print("던전 지하 보여2(in_check)", imgs_2)
                        go_ = True
                    else:
                        print("던전 지하 안보여2(in_check)")

            else:
                print("던전 남음 보여(in_check)", imgs_)
                go_ = True



        if data == 'soongan_ready':
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\dangye.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(360, 320, 600, 365, cla, img)
            if imgs_ is None:
                print("던전 단계 안보여")
            else:
                print("던전 단계 보여", imgs_)
                go_ = True

        return go_
    except Exception as e:
        print(e)
        return 0




