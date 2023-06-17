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

# 던전 진입 준비
def dunjeon_cla_play_su(cla, dun_where, dun_step):
    import os
    import numpy as np
    import cv2
    from myfunction import imgs_set_
    from action import now_hunting
    try:
        print("던전 준비")

        com_gg = False

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

        # 던전인지 아닌지 파악 후 아닐 경우 던전 진입하기
        # 던전일 경우 물약 파악하기
        if in_dun_ == True:
            print("던전에 들어와있다")
            now_hunting(dun_where, cla)
            data = "테스트"
            myPotion_check(dun_where, cla)
        else:
            print("던고 실행하러 간다")
            com_gg = dun_go(cla, dun_where, dun_step)








        return com_gg
    except Exception as e:
        print(e)
        return 0


def dun_go(cla, dun_where, dun_step):
    from myfunction import menuOpen, click_pos_2, imgs_set_, imgs_set, click_pos_reg
    from action import go_alrim_yes
    import cv2
    import numpy as np
    from function import drag_pos
    try:
        print("던전 진입")
        print("클라:", cla)
        print("어디:", dun_where)
        print("몇층:", dun_step)

        comp_g = False

        # 메뉴 오픈
        menuOpen(cla)
        # 던전 클릭
        click_pos_2(740, 370, cla)

        # 던전 글자 이미지 인식

        dun_img = False
        dun_img_count = 0
        while dun_img is False:
            dun_img_count += 1
            if dun_img_count > 5:
                dun_img = True

            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\dunjeon\\dungeon_title_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(25, 35, 100, 80, cla, img, 0.88)
            # 정예던전 클릭
            if imgs_ is not None and imgs_ != False:
                click_pos_2(230, 105, cla)
                time.sleep(1)
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\dunjeon\\dungeon_title_3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(420, 350, 490, 410, cla, img, 0.88)
                if imgs_ is not None and imgs_ != False:
                    dun_img = True

            time.sleep(1)

        # 공허 이미지 확인
        dun_img2 = False
        dun_img2_count = 0
        while dun_img2 is False:
            dun_img2_count += 1
            if dun_img2_count > 5:
                dun_img2 = True

            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\dunjeon\\dungeon_title_3.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(420, 350, 490, 410, cla, img, 0.88)
            # 드래그
            if imgs_ is not None and imgs_ != False:
                drag_pos(850, 500, 130, 500, cla)
                time.sleep(3)

                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\dunjeon\\dungeon_title_5.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(730, 360, 820, 400, cla, img, 0.88)
                if imgs_ is not None and imgs_ != False:
                    dun_img2 = True

            time.sleep(1)

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\dunjeon_lock.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        # 여기 던전마다 이미지 위치 달라져야 한다
        if dun_where == '공허':
            imgs_ = imgs_set(80, 440, 220, 580, cla, img)
        if dun_where == '난쟁이':
            imgs_ = imgs_set(390, 440, 530, 580, cla, img)
        if dun_where == '지하감옥':
            imgs_ = imgs_set(710, 440, 850, 580, cla, img)

        if imgs_ is None:
            print("rock 없고, 0초 인지 파악하자")

            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\zero.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            if dun_where == "공허":
                imgs_ = imgs_set_(100, 645, 200, 685, cla, img, 0.88)
            if dun_where == "난쟁이":
                imgs_ = imgs_set_(410, 645, 510, 685, cla, img, 0.88)
            if dun_where == "지하감옥":
                imgs_ = imgs_set_(730, 645, 830, 685, cla, img, 0.88)
            # 0초 남음 여부 확인 후 공허, 난쟁이, 지하감옥 클릭
            if imgs_ is None:
                print("던전진입ㄱ")
                # 여기 던전마다 클릭 위치 달라져야 한다.
                if dun_where == '공허':
                    click_pos_2(160, 520, cla)
                if dun_where == '난쟁이':
                    click_pos_2(460, 520, cla)
                if dun_where == '지하감옥':
                    click_pos_2(760, 520, cla)

                dun_img3 = False
                dun_img3_count = 0
                while dun_img3 is False:
                    dun_img3_count += 1
                    if dun_img3_count > 5:
                        dun_img3 = True

                    # 정예던전 이미지 확인
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\dunjeon\\dungeon_title_6.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(48, 41, 128, 70, cla, img, 0.88)
                    if imgs_ is not None and imgs_ != False:
                        dun_img3 = True

                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\dunjeon\\dungeon_clear_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(660, 960, 740, 1000, cla, img)
                        if imgs_ is not None and imgs_ != False:
                            comp_g = True

                        else:
                            in_dunjeon_list_su(cla, dun_where, dun_step)
                            click_pos_2(840, 990, cla)
                            click_pos_2(840, 990, cla)

                            result_ = go_alrim_yes(cla)
                            if result_[0] == True:
                                click_pos_reg(result_[1], result_[2], cla)
                            else:
                                click_pos_2(550, 610, cla)

                            # 던전 진입 후 순간이동서 클릭
                            dun_in_sungan(cla)




            else:
                print("0초 남음 스케줄 완료")
                comp_g = True
        else:
            print("던전락이니 스케줄 완료")
            comp_g = True


        return comp_g
    except Exception as e:
        print(e)
        return 0


def in_dunjeon_list_su(cla, dun_where, dunjeon_level):
    try:
        from myfunction import random_int, click_pos_2
        from schedule import myQuest_play_check

        step = 'none'

        dunjeon_level = int(dunjeon_level)

        y_ = 170

        if dun_where == '공허':
            if dunjeon_level == 6:
                y_ = 400
                click_pos_2(160, 400, cla)
                time.sleep(1)
                step = '광기의 균열'
            elif dunjeon_level == 5:
                y_ = 345
                click_pos_2(160, 345, cla)
                time.sleep(1)
                step = '분쟁의 신전'
            elif dunjeon_level == 4:
                y_ = 285
                click_pos_2(160, 285, cla)
                time.sleep(1)
                step = '공포의 내리막'
            elif dunjeon_level == 3:
                y_ = 230
                click_pos_2(160, 230, cla)
                time.sleep(1)
                step = '혼돈의 동굴'
            elif dunjeon_level == 2:
                y_ = 170
                click_pos_2(160, 170, cla)
                time.sleep(1)
                step = '악취 나는 통로'
            else:
                click_pos_2(160, 115, cla)
                time.sleep(1)
                step = '균열의 입구'

        elif dun_where == '난쟁이':
            if dunjeon_level == 6:
                y_ = 400
                click_pos_2(160, 400, cla)
                time.sleep(1)
                step = '불타버린 길'
            elif dunjeon_level == 5:
                y_ = 345
                click_pos_2(160, 345, cla)
                time.sleep(1)
                step = '울부짖는 길'
            elif dunjeon_level == 4:
                y_ = 285
                click_pos_2(160, 285, cla)
                time.sleep(1)
                step = '상처입은 길'
            elif dunjeon_level == 3:
                y_ = 230
                click_pos_2(160, 230, cla)
                time.sleep(1)
                step = '얼어붙은 길'
            elif dunjeon_level == 2:
                y_ = 170
                click_pos_2(160, 170, cla)
                time.sleep(1)
                step = '속삭이는 길'
            else:
                click_pos_2(160, 115, cla)
                time.sleep(1)
                step = '저주받은 길'

        elif dun_where == '지하감옥':
            if dunjeon_level == 6:
                y_ = 400
                click_pos_2(160, 400, cla)
                time.sleep(1)
                step = '식탐의 방'
            elif dunjeon_level == 5:
                y_ = 345
                click_pos_2(160, 345, cla)
                time.sleep(1)
                step = '음욕의 나락'
            elif dunjeon_level == 4:
                y_ = 285
                click_pos_2(160, 285, cla)
                time.sleep(1)
                step = '분노의 처형터'
            elif dunjeon_level == 3:
                y_ = 230
                click_pos_2(160, 230, cla)
                time.sleep(1)
                step = '질투의 고문소'
            elif dunjeon_level == 2:
                y_ = 170
                click_pos_2(160, 170, cla)
                time.sleep(1)
                step = '탐욕의 묘지'
            else:
                click_pos_2(160, 115, cla)
                time.sleep(1)
                step = '교만의 감옥'

        return step, y_
    except Exception as e:
        print(e)
        return 0


# 포션 체크
def myPotion_check(data, cla):
    try:
        from myfunction import menuOpenCheck, click_pos_2, go_auto, get_region, image_processing, change_number, potion_count_grow, potion_count, go_to_home, imgs_set, text_check_get, int_put_, isNumber_,dead_die
        from action import go_potion_off
        from clean import clean_screen
        import numpy as np
        import cv2
        import pyautogui
        import pytesseract

        print("def myPotion_check(data, cla): start")
        print("자동물약중, 어디에서 왔니?", data)
        print("넌 몇클라?", cla)

        if cla == 'one':
            cla_ing = v_.one_cla_ing
            isPotion_ = v_.mypotion_1
        if cla == 'two':
            cla_ing = v_.two_cla_ing
            isPotion_ = v_.mypotion_2

        ispotion__ = False
        ispotionOff = False
        isAnboyuCount = 0
        while ispotionOff is False:
            isAnboyuCount += 1
            if isAnboyuCount >= 5:
                ispotionOff = True

            result = go_potion_off(cla)
            if result == False:

                result___ = menuOpenCheck(cla, "myPotion_check_start")
                if result___ == True:
                    click_pos_2(920, 55, cla)
                    time.sleep(1)
                else:

                    result____ = go_auto(cla, '5')
                    if result____ == True:
                        click_pos_2(800, 840, cla)
                        time.sleep(1)
                    else:
                        print("화면 초기화")
                        clean_screen(cla, "myPotion_check")


            else:
                ispotionOff = True

                img = pyautogui.screenshot(region=(get_region(865, 825, 945, 850, cla)))
                white_img = image_processing(img, (148, 148, 148), (255, 255, 255))
                potion_count_ = pytesseract.image_to_string(white_img, lang=None)
                # print("good", potion_count_)

                # potion_count_ = text_check_get_3(855, 825, 935, 850, 3, cla)
                print("potion_count_", potion_count_)
                if '/' in potion_count_ and potion_count_ != 0:
                    print('/가 있당')
                    potion_count1 = potion_count_.split("/")
                    print("potion_count1", potion_count1)
                    potion_ = change_number(potion_count1[0])
                    potion_bloon = potion_.isdigit()
                    if potion_bloon == True:
                        potion = int(potion_)
                        print("potion", potion)
                        ispotion__ = True
                        if potion > 0:
                            click_pos_2(700, 840, cla)
                            time.sleep(1)
                        # click_pos_2(700, 840, cla) 이건 최초 1회만 하자
                    else:
                        print("포션 파악 불가")
                        print("포션 파악 불가인 것은 물약이 최대 소지 갯수 초과했기 때문임.")
                else:
                    print('/가 없당')
                    print("potion_count_99999", potion_count_)
                    print("/가 없는 것은 물약이 최대 소지 갯수 초과했기 때문임.")

        if ispotion__ == True:
            if potion < 150:
                result_po = potion_count(cla)
                time.sleep(0.5)
                click_pos_2(920, 55, cla)
                if cla == 'one':
                    v_.mypotion_1 = result_po
                if cla == 'two':
                    v_.mypotion_2 = result_po
                print('result_po', result_po)
                if result_po < 150:
                    go_to_home(data, cla)
                else:
                    print("휴...안가도 된다")
            else:
                print("물약 많지렁")
        else:
            print("물약 많아서 당장 파악 불가능")
            if isPotion_ < 150:
                result_po = potion_count(cla)
                time.sleep(0.5)
                click_pos_2(920, 55, cla)
                if cla == 'one':
                    v_.mypotion_1 = result_po
                if cla == 'two':
                    v_.mypotion_2 = result_po
                print('result_po', result_po)
                if result_po < 200:
                    go_to_home('start', cla)

        dead_die(cla, "myPotion_check")

        print("def myPotion_check(data, cla): end")
        return data
    except Exception as e:
        print(e)
        return 0

def dun_in_sungan(cla):
    from myfunction import imgs_set_, go_auto, click_pos_2, click_pos_reg
    from stop_18 import is_stop
    from massenger import line_to_me
    from action import go_alrim_yes
    import numpy as np
    import cv2
    try:
        print("순간이동 클릭 후 사냥하러 가자")

        in_dun = False
        in_dun_count = 0
        while in_dun is False:
            in_dun_count += 1
            if in_dun_count > 50:
                in_dun = True
                line_to_me(cla, "던전 진입중 오류...")

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
                        print("던전 재진입 완료")
                        time.sleep(0.5)

                        # x 같은 이벤트
                        is_stop(cla)

                        click_pos_2(900, 890, cla)
                    time.sleep(0.5)
            time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0