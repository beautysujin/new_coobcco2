# import numpy as np
# import os
import sys
# import cv2
import time
# import re
# import pyautogui
sys.path.append('C:/my_games/coobcco2/data_od/mymodule')

# from chango import go_chango
# from myfunction import *
# from where import go_worldmap

import variable as v_

def go_test(cla):
    print('hi test! action', cla)

def go_haeje(cla):
    try:
        from myfunction import imgs_set
        import numpy as np
        import cv2

        go_ = False

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\haeje.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(825, 980, 950, 1030, cla, img)

        if imgs_ is None or imgs_ == False:
            print("장비모두해제가 안보여")
        else:
            go_ = True

        return go_
    except Exception as e:
        print(e)
        return 0

def go_bag(cla, story):
    try:
        import numpy as np
        import cv2
        from clean import clean_screen
        from myfunction import go_auto, imgs_set, random_int, text_check_get, int_put_, isNumber_, click_pos_2, menuOpenCheck
        from chango import go_chango

        get_story = str(story) + " => go_bag"
        print(get_story)

        go_ = False
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\gabang.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(30, 40, 100, 75, cla, img)
        # imgs_ = pyautogui.locateCenterOnScreen(img, region=(30 + plus, 40, 100 + plus, 75),
        #                                        confidence=0.7)
        if imgs_ is None or imgs_ == False:
            print("가방이 없다...")

            ismenu = False
            while ismenu is False:
                result_ = go_chango(cla, 'village')
                time.sleep(random_int())
                result_2 = go_auto(cla, '11')
                time.sleep(random_int())

                if result_ == True or result_2 == True:
                    ismenu = True
                    # hp 파악 ######
                    myhped_ = text_check_get(67, 37, 160, 73, cla)
                    print("myhp", myhped_)
                    if '/' in myhped_:
                        print("hp 파악 함")
                        myhp_ = myhped_.split("\n")
                        if len(myhp_) >= 1:
                            myhp = myhp_[0].split("/")
                            myhp1 = int(int_put_(myhp[0]))
                            myhp2 = int(int_put_(myhp[0]))
                            hpfloat_1 = isNumber_(myhp1)
                            hpfloat_2 = isNumber_(myhp2)
                            if hpfloat_1 == True and hpfloat_2 == True:
                                myhp_per = myhp1 / myhp2
                                print("myhp_per", myhp_per)
                    else:
                        print("hp 파악 못함")
                    time.sleep(random_int())
                    print("가방 클릭")
                    click_pos_2(860, 55, cla)
                    time.sleep(random_int())
                    go_ = True
                else:
                    clean_screen(cla, get_story) #찾았다 시팍
                    result_me_ = menuOpenCheck(cla, "go_bag")
                    if result_me_ == True:
                        click_pos_2(920, 55, cla)
        else:
            print("가방이 있다...")
            go_ = True

        print("def go_bag(cla): end", go_)

        return go_
    except Exception as e:
        print(e)
        return 0

def go_jangchack(cla):
    try:
        from myfunction import imgs_set
        import numpy as np
        import cv2

        go_ = False

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\jangchack.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(825, 980, 950, 1030, cla, img)

        if imgs_ is None or imgs_ == False:
            print("자동장착이 안보여")
        else:
            go_ = True

        return go_
    except Exception as e:
        print(e)
        return 0

def go_soongan_f5(cla):
    try:
        from myfunction import imgs_set, click_pos_2, random_int, drag_pos, go_to_home, click_pos_reg, imgs_set_
        import numpy as np
        import cv2

        print("go_soongan_f5")
        ready_ = go_bag(cla, "go_soongan_f5")
        if ready_ == True:
            result = go_quickslot(cla)
            if result == False:
                print("퀵슬롯 설정이 없다.")
            else:
                click_pos_2(770, 1005, cla)
                time.sleep(random_int())

                # full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\soongan_3.png"
                # img_array = np.fromfile(full_path, np.uint8)
                # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                # imgs_ = imgs_set(880, 880, 940, 940, cla, img)
                # if imgs_ is not None and imgs_ != False:
                #     print("장착된 상태다.")
                # else:
                isquick_ = False
                while isquick_ is False:
                    result_ = go_quickslot(cla)
                    if result_ == False:
                        time.sleep(1)
                        drag_pos(770, 200, 770, 900, cla)
                        time.sleep(1)
                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\soongan.png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(560, 100, 950, 860, cla, img, 0.85)
                        if imgs_ is None or imgs_ == False:
                            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\soongan_2.png"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(560, 100, 950, 860, cla, img, 0.85)
                            if imgs_ is None or imgs_ == False:
                                drag_pos(770, 900, 770, 200, cla)
                                time.sleep(1)
                                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\soongan.png"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(560, 100, 950, 860, cla, img, 0.85)
                                if imgs_ is None or imgs_ == False:
                                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\soongan_2.png"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(560, 100, 950, 860, cla, img, 0.85)
                                    if imgs_ is None or imgs_ == False:
                                        # isquick_ = True
                                        print("soongan(이)가 진짜 없다...")
                                        time.sleep(1)
                                        click_pos_2(905, 1005, cla)
                                        time.sleep(1)
                                        go_to_home('start', cla)
                                        click_pos_2(920, 55, cla)
                                        ready_ = go_bag(cla, "go_soongan_f5")
                                    else:
                                        isquick_ = True
                                        print("img4", imgs_)
                                        time.sleep(1)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(1)
                                        click_pos_2(905, 910, cla)
                                        time.sleep(1)
                                        click_pos_2(905, 1005, cla)
                                else:
                                    isquick_ = True
                                    print("img3", imgs_)
                                    time.sleep(1)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(1)
                                    click_pos_2(905, 910, cla)
                                    time.sleep(1)
                                    click_pos_2(905, 1005, cla)
                            else:
                                isquick_ = True
                                print("img2", imgs_)
                                time.sleep(1)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(1)
                                click_pos_2(905, 910, cla)
                                time.sleep(1)
                                click_pos_2(905, 1005, cla)
                        else:
                            isquick_ = True
                            print("img1", imgs_)
                            time.sleep(1)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(1)
                            click_pos_2(905, 910, cla)
                            time.sleep(1)
                            click_pos_2(905, 1005, cla)

                        time.sleep(1)
                    else:

                        click_pos_2(770, 1005, cla)
                        time.sleep(random_int())

    except Exception as e:
        print(e)
        return 0


def go_boonhae(cla, story):
    try:
        from myfunction import imgs_set_, click_pos_reg, click_pos_2, drag_pos, imgs_set, random_int, text_check_get, mouse_move_cpp
        import numpy as np
        import cv2
        import os.path

        get_story = str(story) + " => go_boonhae"
        print(get_story)

        go_bag(cla, get_story)


        dir_path = "C:\\my_games\\coobcco2\\data_od"
        file_path9 = dir_path + "\\item\\trash_list.txt"

        if os.path.isfile(file_path9) == True:
            # 파일 읽기
            with open(file_path9, "r", encoding='utf-8-sig') as file:
                lines = file.read().splitlines()
                file.close()
            print("lines", lines)\

            drag_bool = go_boonhae_drag(cla)

            # 분해전에 스킬 기술서 같은거 버리기
            for i in range(len(lines)):
                full_path = "c:\\my_games\\coobcco2\\data_od\\item\\trash\\" + lines[i] + ".png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(560, 100, 950, 960, cla, img, 0.94)
                if imgs_ is None or imgs_ == False:
                    print(lines[i] + "(in_이)가 없다...")
                else:
                    print(lines[i], imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(1)
                    click_pos_2(120, 770, cla)
                    time.sleep(1)
                    go_alrim_confirm(cla, get_story)
                    time.sleep(1)
            if drag_bool == True:
                drag_pos(800, 900, 800, 200, cla)
                time.sleep(1)
                for i in range(len(lines)):
                    full_path = "c:\\my_games\\coobcco2\\data_od\\item\\trash\\" + lines[i] + ".png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(560, 100, 950, 960, cla, img, 0.94)
                    if imgs_ is None or imgs_ == False:
                        print(lines[i] + "(in_이)가 없다...")
                    else:
                        print(lines[i], imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(1)
                        click_pos_2(120, 770, cla)
                        time.sleep(1)
                        go_alrim_confirm(cla, get_story)
                        time.sleep(1)

            isBoonhae = False
            is_count = 0
            while isBoonhae is False:
                is_count += 1
                if is_count > 5:
                    isBoonhae = True
                    print("분해하는데 오류 있다...")

                ready_ = go_bag(cla, get_story)
                if ready_ == True:

                    # 분해하기
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\ilgwalboonhae.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(560, 970, 720, 1030, cla, img)
                    if imgs_ is None or imgs_ == False:
                        print('일괄분해 안보여 다시..')
                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\boonhae_cancle.png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(740, 990, 830, 1030, cla, img)
                        if imgs_ is None or imgs_ == False:
                            print('분해캔슬 안보여 다시..')
                            click_pos_2(920, 55, cla)
                            time.sleep(random_int())
                        else:
                            print('분해캔슬 보여...')
                            click_pos_2(790, 1005, cla)
                            time.sleep(random_int())


                    else:
                        print('일괄분해 보여...진행')
                        click_pos_2(650, 1005, cla)
                        time.sleep(random_int())


                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\boonhae.png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(830, 970, 950, 1030, cla, img)

                        if imgs_ is None or imgs_ == False:
                            print('분해1 안보여 다시..')
                            click_pos_2(920, 55, cla)
                            time.sleep(random_int())
                        else:
                            print('분해1 보여...진행')

                            click_pos_2(895, 1005, cla)
                            boonhaed_ = text_check_get(382, 113, 565, 160, cla)
                            boonhae_ = boonhaed_.split("\n")
                            selected_item = False
                            if len(boonhae_) != 0:
                                for list in boonhae_[0]:
                                    try:
                                        if list == '선' or list == '택' or list == '된' or list == '아' or list == '이' or list == '템':
                                            selected_item = True
                                    except:
                                        pass

                            time.sleep(random_int())
                            if selected_item == True:
                                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\boonhae_cancle.png"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set(740, 990, 830, 1030, cla, img)
                                if imgs_ is None or imgs_ == False:
                                    print('selected_item == True : 분해캔슬 안보여 다시..')
                                    click_pos_2(920, 55, cla)
                                    time.sleep(1)
                                else:
                                    print('selected_item == True : 분해캔슬 보여...')
                                    click_pos_2(790, 1005, cla)
                                    time.sleep(1)

                            else:
                                print("selected_item == False:")
                                result = go_alrim_boonhae(cla)
                                if result == True:
                                    result_ = go_alrim_yes(cla)
                                    if result_[0] == True:
                                        click_pos_reg(result_[1], result_[2], cla)
                                    else:
                                        click_pos_2(550, 660, cla)

                                    isboon_ = False
                                    while isboon_ is False:
                                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\gabang.png"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set(30, 40, 100, 75, cla, img)
                                        # imgs_ = pyautogui.locateCenterOnScreen(img, region=(30 + plus, 40, 100 + plus, 75),
                                        #                                        confidence=0.7)
                                        if imgs_ is None or imgs_ == False:
                                            click_pos_2(305, 660, cla)
                                            print("가방 보일때 까지 갈겨갈겨")
                                            go_alrim_confirm(cla, "갈겨갈겨")
                                            time.sleep(0.3)
                                        else:
                                            isboon_ = True
                                            print("가방표시 있다. 분해 마무리단계")
                                            time.sleep(0.5)
                                    # time.sleep(10 + random_int())
                                    # click_pos_2(305, 660, cla)
                                    # time.sleep(random_int())
                            mouse_move_cpp(400, 500, cla)
                            time.sleep(2)
                            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\boonhae2.png"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set(600, 990, 680, 1025, cla, img)

                            if imgs_ is not None and imgs_ != False:
                                isBoonhae = True
                                print('분해12 보여...끝')
                                click_pos_2(305, 660, cla)
                                time.sleep(1)
                            else:
                                print('분해12 안보여 다시..')
                                click_pos_2(920, 55, cla)
                                time.sleep(1)




            result_alrim_ = go_alrim_(cla)
            if result_alrim_ == True:
                result_ = go_alrim_yes(cla)
                if result_[0] == True:
                    click_pos_reg(result_[1], result_[2], cla)
            time.sleep(1)

    except Exception as e:
        print(e)
        return 0



def go_level(cla):
    try:
        from myfunction import menuOpenCheck, click_pos_2, text_check_get_3, int_put_

        mylevel = 0
        ismenu = False
        ismenuCount = 0
        while ismenu is False:
            result = menuOpenCheck(cla, "go_level")
            time.sleep(0.5)
            if result == True:
                click_pos_2(920, 300, cla)
                time.sleep(1)
                mylevel_get = text_check_get_3(825, 935, 925, 965, 0, cla)
                print('mylevel_get0', mylevel_get)
                mylevel_ = mylevel_get.replace(" ", "")
                print('mylevel_', mylevel_)
                mylevel_ = mylevel_.split("(")
                mylevel_ = int_put_(mylevel_[0])
                print('mylevel_[0]', mylevel_)
                mylevel_bloon = mylevel_.isdigit()
                if mylevel_bloon == True:
                    mylevel = int(mylevel_)
                    if 10 < mylevel < 130:
                        ismenu = True
                        print("mylevel0 : ", mylevel)
                        if cla == 'one':
                            v_.mylevel_1 = int(mylevel)
                        if cla == 'two':
                            v_.mylevel_2 = int(mylevel)
                    else:
                        mylevel_get = text_check_get_3(825, 935, 925, 965, 1, cla)
                        print('mylevel_get1', mylevel_get)
                        mylevel_ = mylevel_get.replace(" ", "")
                        print('mylevel_', mylevel_)
                        mylevel_ = mylevel_.split("(")
                        mylevel_ = int_put_(mylevel_[0])
                        print('mylevel_[0]', mylevel_)
                        mylevel_bloon = mylevel_.isdigit()
                        if mylevel_bloon == True:
                            mylevel = int(mylevel_)
                            if 10 < mylevel < 130:
                                ismenu = True
                                print("mylevel1 : ", mylevel)
                                if cla == 'one':
                                    v_.mylevel_1 = int(mylevel)
                                if cla == 'two':
                                    v_.mylevel_2 = int(mylevel)
                            else:
                                mylevel_get = text_check_get_3(825, 935, 925, 965, 3, cla)
                                print('mylevel_get3', mylevel_get)
                                mylevel_ = mylevel_get.replace(" ", "")
                                print('mylevel_', mylevel_)
                                mylevel_ = mylevel_.split("(")
                                mylevel_ = int_put_(mylevel_[0])
                                print('mylevel_[0]', mylevel_)
                                mylevel_bloon = mylevel_.isdigit()
                                if mylevel_bloon == True:
                                    mylevel = int(mylevel_)
                                    if 10 < mylevel < 130:
                                        ismenu = True
                                        print("mylevel3 : ", mylevel)
                                        if cla == 'one':
                                            v_.mylevel_1 = int(mylevel)
                                        if cla == 'two':
                                            v_.mylevel_2 = int(mylevel)
                                    elif mylevel > 130:
                                        print("wow!!!!!!!!!")
                                        mylevel = str(mylevel)
                                        print("mylevel_[0]", mylevel[0])
                                        print("mylevel_[1]", mylevel[1])
                                        reset_level = str(mylevel[0]) + str(mylevel[1])
                                        print("reset_level", reset_level)
                                        mylevel = int(reset_level)
                                        if cla == 'one':
                                            v_.mylevel_1 = int(mylevel)
                                        if cla == 'two':
                                            v_.mylevel_2 = int(mylevel)
                ismenuCount += 1
                if ismenuCount > 2:
                    print("no my level!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    ismenu = True
                    if cla == 'one':
                        v_.mylevel_1 = 1
                    if cla == 'two':
                        v_.mylevel_2 = 1
            else:
                click_pos_2(920, 55, cla)
                time.sleep(1)

        click_pos_2(920, 55, cla)
        time.sleep(1)
        return mylevel
    except Exception as e:
        print(e)
        return 0


def go_power_bag(cla):
    try:
        from myfunction import text_check_get_3
        import re

        power = 0

        power_read = text_check_get_3(5, 985, 100, 1005, 1, cla)
        power_ = power_read.split("\n")
        print('power_1', power_)
        if len(power_) != 0:
            for list in power_:
                try:
                    list_ = re.sub(r'[^0-9]', '', list)
                    list_bool = list_.isdigit()
                    print("power_bloon", list_bool)
                    if list_bool == True:
                        any_ = int(list_)
                        if 1000 < any_:
                            power = any_
                        print('power', power)
                        if cla == 'one':
                            v_.mypower_1 = int(power)
                        if cla == 'two':
                            v_.mypower_2 = int(power)
                except Exception as e:
                    print(e)
                    return 0
        power_read = text_check_get_3(5, 985, 100, 1005, 3, cla)
        power_ = power_read.split("\n")
        print('power_3', power_)
        if len(power_) != 0:
            for list in power_:
                try:
                    list_ = re.sub(r'[^0-9]', '', list)
                    list_bool = list_.isdigit()
                    print("power_bloon", list_bool)
                    if list_bool == True:
                        any_ = int(list_)
                        if 1000 < any_:
                            power = any_
                        print('power', power)
                        if cla == 'one':
                            v_.mypower_1 = int(power)
                        if cla == 'two':
                            v_.mypower_2 = int(power)
                except Exception as e:
                    print(e)
                    return 0

        return power
    except Exception as e:
        print(e)
        return 0




def go_post_check(cla):
    try:
        from myfunction import imgs_set, text_check_get_3
        import numpy as np
        import cv2

        go_ = False

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\post.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(30, 30, 150, 100, cla, img)

        if imgs_ is None or imgs_ == False:
            print("post 안보여")
        else:
            go_ = True
            print("post 보여", imgs_)


        if go_ == False:
            print("우편한 png로 인식 불가능하여 글자인식으로 파악해보기")
            post_check = text_check_get_3(55, 45, 110, 70, 2, cla)
            post_check = post_check.split("\n")
            post_check = " ".join(post_check).strip()
            print("post_check : 글자 인식 =>", post_check)
            if len(post_check) != 0:
                for list in range(len(post_check)):
                    if post_check[list] == "우" or post_check[list] == '편' or post_check[list] == '함':
                        print("post_check : ", post_check[list])
                        go_ = True

        return go_
    except Exception as e:
        print(e)
        return 0

def go_alrim_boonhae(cla):
    try:
        from myfunction import imgs_set
        import numpy as np
        import cv2

        go_ = False

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\post_end.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(435, 380, 510, 425, cla, img)

        if imgs_ is None or imgs_ == False:
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\item_delete_1.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(435, 430, 510, 470, cla, img)

            if imgs_ is None or imgs_ == False:
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\item_delete_2.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(435, 430, 510, 470, cla, img)

                if imgs_ is None or imgs_ == False:
                    print("아이템삭제도 안보여3")
                else:
                    print("아이템삭제는 보여2")
                    go_ = True
            else:
                print("아이템삭제는 보여1")
                go_ = True
        else:
            print("알림이 보여")
            go_ = True



        return go_
    except Exception as e:
        print(e)
        return 0


def go_alrim_(cla):
    try:
        from myfunction import imgs_set
        import numpy as np
        import cv2

        go_ = False

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\post_end.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(200, 300, 800, 800, cla, img)

        if imgs_ is None or imgs_ == False:
            print("알림이 안보여")
        else:
            print("알림이 보여")
            go_ = True

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\alrim_3.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(200, 300, 800, 800, cla, img)

        if imgs_ is None or imgs_ == False:
            print("alrim_3이 안보여")
        else:
            print("alrim_3이 보여")
            go_ = True

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\item_delete_1.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(200, 300, 800, 800, cla, img)

        if imgs_ is None or imgs_ == False:
            print("아이템삭제도 안보여")
        else:
            print("아이템삭제는 보여")
            go_ = True

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\item_delete_2.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(200, 300, 800, 800, cla, img)

        if imgs_ is None or imgs_ == False:
            print("아이템삭제2도 안보여")
        else:
            print("아이템삭제2는 보여")
            go_ = True

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\maul_bbaln.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(200, 300, 800, 800, cla, img)
        if imgs_ is not None:
            go_ = True

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\free_move_1.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(200, 300, 800, 800, cla, img)
        if imgs_ is not None:
            go_ = True

        return go_
    except Exception as e:
        print(e)
        return 0

def go_alrim_yes(cla):
    try:
        from myfunction import imgs_set_
        import numpy as np
        import cv2

        go_ = False
        x_ = 0
        y_ = 0

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\alrim_yes.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(200, 300, 800, 1030, cla, img, 0.85)
        if imgs_ is not None:
            go_ = True
            print("alrim_yes 보여", imgs_)
            x_ = imgs_.x
            y_ = imgs_.y

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\alrim_yes2.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(200, 300, 800, 1030, cla, img, 0.85)
        if imgs_ is not None:
            go_ = True
            print("alrim_yes2 보여", imgs_)
            x_ = imgs_.x
            y_ = imgs_.y

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\alrim_yes3.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(200, 300, 800, 1030, cla, img, 0.85)
        if imgs_ is not None:
            go_ = True
            print("alrim_yes3 보여", imgs_)
            x_ = imgs_.x
            y_ = imgs_.y
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\alrim_yes4.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(200, 300, 800, 1030, cla, img, 0.85)
        if imgs_ is not None:
            go_ = True
            print("alrim_yes4 보여", imgs_)
            x_ = imgs_.x
            y_ = imgs_.y

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\alrim_yes5.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(200, 300, 800, 1030, cla, img, 0.85)
        if imgs_ is not None:
            go_ = True
            print("alrim_yes5 보여", imgs_)
            x_ = imgs_.x
            y_ = imgs_.y

        full_path = "c:\\my_games\\coobcco2\\data_od\\item\\item_open\\sayong.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(200, 300, 800, 1030, cla, img, 0.85)
        if imgs_ is not None:
            go_ = True
            print("sayong 보여", imgs_)
            x_ = imgs_.x
            y_ = imgs_.y

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\clean\\hwagin_1.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(200, 300, 800, 1030, cla, img, 0.85)
        if imgs_ is not None:
            go_ = True
            print("hwagin_1 보여", imgs_)
            x_ = imgs_.x
            y_ = imgs_.y

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\maul_bbaln_3.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(200, 300, 800, 800, cla, img, 0.85)
        if imgs_ is not None:
            go_ = True
            print("maul_bbaln_3 보여", imgs_)
            x_ = imgs_.x
            y_ = imgs_.y

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\free_move_1.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(200, 300, 800, 800, cla, img, 0.85)
        if imgs_ is not None:
            go_ = True
            print("free_move_1 보여", imgs_)
            x_ = imgs_.x
            y_ = imgs_.y



        return go_, x_, y_
    except Exception as e:
        print(e)
        return 0
def go_boonhae_drag(cla):
    try:
        from myfunction import text_check_get_3, int_put_

        go_ = False
        drag_ready = text_check_get_3(840, 960, 915, 985, 1, cla)
        print("drag_ready", drag_ready)
        drag_re_ = drag_ready.split('/')
        drag_r_ = int_put_(drag_re_[0])
        drag_r_bloon = drag_r_.isdigit()
        if drag_r_bloon == True:
            drag_ = int(drag_r_)
            print("drag_ready", drag_)
            if drag_ > 60:
                go_ = True
        return go_
    except Exception as e:
        print(e)
        return 0





def go_escape(cla):
    try:
        from myfunction import click_pos_2, random_int

        click_pos_2(920, 55, cla)
        time.sleep(random_int())
        click_pos_2(920, 525, cla)
        time.sleep(random_int())
        click_pos_2(640, 110, cla)
        time.sleep(random_int())
        click_pos_2(655, 465, cla)
        time.sleep(3+random_int())
        go_alrim_confirm(cla, 'go_escape')

    except Exception as e:
        print(e)
        return 0

def go_alrim_confirm(cla, story):
    try:
        from myfunction import random_int, click_pos_reg, click_pos_2

        get_story = str(story) + " => go_alrim_confirm"
        print(get_story)
        result = go_alrim_(cla)
        time.sleep(1)
        if result == False:
            print("알림이 없다...")
        else:
            print("알림이 있다...")
            result_ = go_alrim_yes(cla)
            print('go_alrim_confirm', result_)
            if result_[0] == True:
                click_pos_reg(result_[1], result_[2], cla)
            else:
                click_pos_2(560, 640, cla)
            time.sleep(0.5)

    except Exception as e:
        print(e)
        return 0


def go_quickslot(cla):
    try:
        from myfunction import imgs_set
        import numpy as np
        import cv2

        go_ = False

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\quickslot.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(720, 985, 800, 1025, cla, img)

        if imgs_ is None or imgs_ == False:
            print("퀵슬롯 설정이 없다.")
        else:
            print("퀵슬롯 설정이 있다.")
            go_ = True



        return go_
    except Exception as e:
        print(e)
        return 0



def go_quest_ing(cla):
    try:
        from myfunction import imgs_set
        import numpy as np
        import cv2

        go_ = False

        isQuest = False
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\auto_quest.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(860, 860, 930, 910, cla, img)
        if imgs_ is None or imgs_ == False:
            print("quest 안보여")
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\auto_quest_1.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(860, 860, 930, 910, cla, img)
            if imgs_ is None or imgs_ == False:
                print("quest 안보여2")
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\auto_quest_1.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(860, 860, 930, 910, cla, img)
                if imgs_ is None or imgs_ == False:
                    print("quest 안보여3")
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\auto_quest_2.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(860, 860, 930, 910, cla, img)
                    if imgs_ is None or imgs_ == False:
                        print("quest 안보여4")
                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\auto_quest_3.png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(860, 860, 930, 910, cla, img)
                        if imgs_ is None or imgs_ == False:
                            print("quest 진행중 아님.")
                        else:
                            go_ = True
                            print("quest 보여5 :", imgs_)
                    else:
                        go_ = True
                        print("quest 보여4 :", imgs_)
                else:
                    go_ = True
                    print("quest 보여3 :", imgs_)
            else:
                go_ = True
                print("quest 보여2 :", imgs_)
        else:
            go_ = True
            print("quest 보여 : ", imgs_)

        return go_
    except Exception as e:
        print(e)
        return 0





def go_now_hunting_is(cla):
    try:
        from myfunction import imgs_set
        import numpy as np
        import cv2

        x_ = 570
        y_ = 50

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\now_hunting_is_1.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(300, 30, 630, 90, cla, img)
        if imgs_ is not None:
            print("now_hunting_is_1 보여", imgs_)
            x_ = imgs_.x
            y_ = imgs_.y
        else:
            print("now_hunting_is_1 안보여")



        return x_, y_
    except Exception as e:
        print(e)
        return 0

def go_mynumber_(cla):
    try:
        from myfunction import imgs_set, click_pos_2, text_check_get_3, int_put_, menuOpenCheck, random_int
        from schedule import myQuest_number_check
        import numpy as np
        import cv2

        mynumber_ = 0
        isgonumber = False
        while isgonumber is False:
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\clean\\setting.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(30, 30, 160, 80, cla, img)
            if imgs_ is not None and imgs_ != False:
                print("setting", imgs_)
                isgonumber = True

                # 환경
                click_pos_2(400, 115, cla)
                time.sleep(1)

                click_pos_2(265, 825, cla)
                time.sleep(1)
                click_pos_2(410, 670, cla)
                time.sleep(1)

                click_pos_2(425, 205, cla)
                time.sleep(1)
                click_pos_2(865, 255, cla)
                time.sleep(1)
                click_pos_2(500, 785, cla)
                time.sleep(1)

                click_pos_2(640, 105, cla)
                time.sleep(1)
                mynumber_ready = text_check_get_3(150, 250, 260, 270, 1, cla)
                mynumber_ = int_put_(mynumber_ready)
                print("mynumber => ", mynumber_)
                time.sleep(1)
                if cla == 'one':
                    v_.mynumber_1 = mynumber_
                if cla == 'two':
                    v_.mynumber_2 = mynumber_
                myQuest_number_check(cla, "new")
            else:
                isSet_ = False
                while isSet_ is False:
                    result = menuOpenCheck(cla, "go_mynumber_")
                    if result == False:
                        click_pos_2(920, 55, cla)
                        time.sleep(random_int())
                    else:
                        isSet_ = True
                        click_pos_2(910, 650, cla)
                        time.sleep(1)
                        click_pos_2(920, 545, cla)
                        time.sleep(random_int())


        return mynumber_
    except Exception as e:
        print(e)
        return 0

def go_potion_off(cla):
    try:
        from myfunction import imgs_set, click_pos_reg
        import numpy as np
        import cv2

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\potion_hp_set_3.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(725, 815, 770, 865, cla, img)

        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        go_ = False

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\potion_hp_set.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(725, 815, 770, 865, cla, img)

        if imgs_ is None or imgs_ == False:
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\potion_hp_set_2.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(725, 815, 770, 865, cla, img)

            if imgs_ is None or imgs_ == False:
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\potion_hp_set_4.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(725, 815, 770, 865, cla, img)

                if imgs_ is None or imgs_ == False:
                    print("포선 off 안보여.............")
                else:
                    print("potion_hp_set_4 보여2")
                    go_ = True
            else:
                print("포션off가 보여2")
                go_ = True
        else:
            print("포션off가 보여")
            go_ = True



        return go_
    except Exception as e:
        print(e)
        return 0

def go_skip(cla):
    try:
        from myfunction import imgs_set, click_pos_reg, click_pos_2
        import numpy as np
        import cv2

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
                    click_pos_2(920, 55, cla)
            else:
                print("skip_2", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                click_pos_2(920, 55, cla)
        else:
            print("skip_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            click_pos_2(920, 55, cla)

    except Exception as e:
        print(e)
        return 0





def go_collection_on(cla):
    try:
        from myfunction import imgs_set, click_pos_reg
        import numpy as np
        import cv2

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\collection.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(800, 875, 870, 945, cla, img)
        if imgs_ is not None:
            print("collection 보여", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\collection_2.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(800, 875, 870, 945, cla, img)
        if imgs_ is not None:
            print("collection_2 보여", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\collection_3.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(800, 875, 870, 945, cla, img)
        if imgs_ is not None:
            print("collection_3 보여", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

    except Exception as e:
        print(e)
        return 0

def go_juljun(cla, story):
    try:
        from myfunction import imgs_set, random_int, click_pos_2
        import numpy as np
        import cv2

        get_story = str(story) + " => go_juljun"
        print(get_story)
        go_ = False

        if cla == "one":
            cla_ing = v_.one_cla_ing
        elif cla == "two":
            cla_ing = v_.two_cla_ing



        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\juljun_1.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(200, 290, 700, 750, cla, img)

        if imgs_ is None or imgs_ == False:
            print("juljun_1 안보여")
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\juljun_2.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(200, 290, 700, 750, cla, img)

            if imgs_ is None or imgs_ == False:
                print("juljun_2 안보여")
            else:
                print("juljun_2 보여")
                go_ = True
        else:
            print("juljun_1 보여")
            go_ = True

        if go_ == True:
            click_pos_2(30, 325, cla)
            time.sleep(0.5)
            # if cla_ing != "grow":
            #     game_settings(cla, 'juljun')
            #     time.sleep(random_int())
            #     click_pos_2(920, 55, cla)
            #     time.sleep(random_int())



        return go_
    except Exception as e:
        print(e)
        return 0




def mypost(cla):
    try:
        from myfunction import click_pos_2, random_int, menuOpenCheck, text_check_get, int_put_, imgs_set, click_pos_reg
        import numpy as np
        import cv2
        import pyautogui
        from clean import clean_screen

        if cla == 'one':
            plus = 0
        if cla == 'two':
            plus = 960

        post_get = False

        isPost_ = False
        isAnboyuCount = 0
        while isPost_ is False:
            # full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\post.png"
            # img_array = np.fromfile(full_path, np.uint8)
            # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            # imgs_ = imgs_set(30, 30, 150, 100, cla, img)
            result_post = go_post_check(cla)


            if result_post == False:
                print("우편함 안보여")
                isAnboyuCount += 1
                if isAnboyuCount > 4:
                    clean_screen(cla, "mypost")
                click_pos_2(920, 55, cla)
                time.sleep(random_int())
                re_ = menuOpenCheck(cla, "mypost")
                if re_ == True:
                    click_pos_2(680, 525, cla)
                    time.sleep(random_int())
                else:
                    click_pos_2(920, 55, cla)
                    time.sleep(random_int())
                    click_pos_2(680, 525, cla)
                    time.sleep(random_int())
            else:
                print("우편함 보여")
                isPost_ = True
                time.sleep(random_int())
                click_pos_2(240, 105, cla)
                time.sleep(random_int())

                # post 숫자 파악
                post_get_bloon = True
                post_get__ = text_check_get(755, 995, 805, 1020, cla)
                post_get_ = post_get__.split("\n")
                post_get = " ".join(post_get_).strip()
                print("count?", int(int_put_(post_get)))
                if '/' in post_get:
                    print('/가 있당')
                    post_ = post_get.split("/")
                    print("post_", post_)
                    post = int_put_(post_[0])
                    post_bloon = post.isdigit()
                    if post_bloon == True:
                        post = int(post)
                        print("post", post)
                        if post == 0:
                            # 안 받기
                            post_get_bloon = False
                            print("post 현재 페이지에 우편이 없다.")
                    else:
                        print("post 파악 불가")
                        # 전체 받기
                else:
                    print('/가 없당')
                    print("post", post_get)
                    # 전체 받기


                if post_get_bloon != False:
                    full_path2 = "c:\\my_games\\coobcco2\\data_od\\imgs\\post_get.png"
                    img_array2 = np.fromfile(full_path2, np.uint8)
                    img2 = cv2.imdecode(img_array2, cv2.IMREAD_COLOR)
                    imgs_2 = imgs_set(820, 120, 950, 950, cla, img2)
                    if imgs_2 is not None:
                        print("계정 우편이 있다...1")
                        post_get = True
                    full_path2 = "c:\\my_games\\coobcco2\\data_od\\imgs\\post_get_1.png"
                    img_array2 = np.fromfile(full_path2, np.uint8)
                    img2 = cv2.imdecode(img_array2, cv2.IMREAD_COLOR)
                    imgs_2 = imgs_set(820, 120, 950, 950, cla, img2)
                    if imgs_2 is not None:
                        print("계정 우편이 있다...2")
                        post_get = True

                    if post_get == True:
                        click_pos_2(880, 1005, cla)
                        time.sleep(random_int())
                        isPostGet = False
                        while isPostGet is False:
                            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\post_get_ing.png"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set(390, 440, 550, 480, cla, img)
                            if imgs_ is None or imgs_ == False:
                                print("우편 안보여")
                                isPostGet = True
                            else:
                                print("우편 보여", imgs_)
                                click_pos_2(555, 930, cla)
                                time.sleep(random_int())
                                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\post_get_ing.png"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set(390, 440, 550, 480, cla, img)
                                if imgs_ is None or imgs_ == False:
                                    print("우편 안보여")
                                    isPostGet = True
                                    click_pos_2(85, 105, cla)
                                    time.sleep(random_int())

                else:
                    click_pos_2(85, 105, cla)
                    time.sleep(random_int())
                time.sleep(random_int())

                # 여긴 포스트

                if cla == 'one':
                    plus = 0
                if cla == 'two':
                    plus = 960

                isPostcon = False
                while isPostcon is False:
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\post_get2.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

                    last_x = 0
                    last_y = 0
                    con_cou = 0
                    end_cou = 0
                    last_cou = 0
                    for i in pyautogui.locateAllOnScreen(img, region=(810 + plus, 110, 135, 875), confidence=0.7):
                        # for i in pyautogui.locateAllOnScreen(img, region=(810 + plus, 110, 945 + plus, 985),
                        #                                      confidence=0.7):
                        last_x = i.left
                        last_y = i.top
                        con_cou += 1
                        print("last_x", last_x)
                        print("last_y", last_y)

                    if last_x != 0 and last_y != 0:
                        if end_cou == 0:
                            end_cou = con_cou
                        if end_cou != 0:
                            if last_cou == 0:
                                last_cou = end_cou
                            if last_cou != 0:
                                last_cou -= 1
                                click_pos_reg(last_x, last_y, cla)
                                time.sleep(random_int())
                            else:
                                print("확인 다 받았다")
                                isPostcon = True
                    else:
                        print("확인이 없다")
                        isPostcon = True


                isPost_2 = False
                print('isPost_2', isPost_2)
                isPost_count = 0
                while isPost_2 is False:

                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\post_get.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

                    last_x = 0
                    last_y = 0
                    for i in pyautogui.locateAllOnScreen(img, region=(810 + plus, 110, 135, 875), confidence=0.7):
                    # for i in pyautogui.locateAllOnScreen(img, region=(810 + plus, 110, 945 + plus, 985),
                    #                                      confidence=0.7):
                        last_x = i.left
                        last_y = i.top
                        print("last_x", last_x)
                        print("last_y", last_y)

                    if last_x != 0 and last_y != 0:

                        click_pos_reg(last_x + 20, last_y + 10, cla)

                        time.sleep(3 + random_int())

                        result = go_alrim_(cla)
                        # imgs_2 = pyautogui.locateCenterOnScreen(img2, region=(430 + plus, 430, 510 + plus, 470), confidence=0.7)

                        if result == False:
                            isPost_count += 1
                            print("우편 " + str(isPost_count) + "번 받았다. 5번만 받자.")
                            click_pos_2(480, 780, cla)
                            time.sleep(1 + random_int())
                        else:
                            isPost_2 = True
                            print("우편 그만 받자")
                            result_ = go_alrim_yes(cla)
                            if result_[0] == True:
                                # click_pos_reg(result_[1], result_[2], cla)
                                click_pos_2(400, 610, cla)
                            else:
                                click_pos_2(400, 610, cla)
                        if isPost_count == 5:
                            break
                    else:
                        isPost_2 = True
                        print("우편 받기 끝")
                print("다 받았다. 야호 신난다.")

                ###########
                time.sleep(random_int())
                click_pos_2(930, 55, cla)
                time.sleep(1 + random_int())
    except Exception as e:
        print(e)
        return 0





def game_settings(cla, data):
    try:
        from myfunction import menuOpenCheck, click_pos_2, random_int, imgs_set
        import numpy as np
        import cv2

        if data == 'juljun':
            isSet_ = False
            while isSet_ is False:
                result = menuOpenCheck(cla, "game_settings_start")
                if result == False:
                    click_pos_2(920, 55, cla)
                    time.sleep(random_int())
                else:
                    isSet_ = True
                    click_pos_2(910, 650, cla)
                    time.sleep(random_int())
                    click_pos_2(920, 545, cla)
                    time.sleep(random_int())

            # 게임
            click_pos_2(85, 105, cla)
            time.sleep(random_int())
            click_pos_2(600, 515, cla)
            time.sleep(random_int())
        elif data == 'start':
            # 열기
            # click_pos_2(510, 605, cla)
            # time.sleep(random_int())



            isSet_ = False
            while isSet_ is False:
                result = menuOpenCheck(cla, "game_settings_end")
                if result == False:
                    click_pos_2(920, 55, cla)
                    time.sleep(random_int())
                else:
                    isSet_ = True
                    click_pos_2(910, 650, cla)
                    time.sleep(random_int())
                    click_pos_2(920, 545, cla)
                    time.sleep(random_int())


            # result = menuOpenCheck(cla)
            # click_pos_2(920, 55, cla)
            # time.sleep(random_int())
            #
            # click_pos_2(910, 650, cla)
            # time.sleep(random_int())
            # click_pos_2(920, 545, cla)
            # time.sleep(random_int())

            #환경
            click_pos_2(400, 115, cla)
            time.sleep(1)

            click_pos_2(265, 825, cla)
            time.sleep(1)
            click_pos_2(410, 670, cla)
            time.sleep(1)

            click_pos_2(425, 205, cla)
            time.sleep(1)
            click_pos_2(865, 255, cla)
            time.sleep(1)

            click_pos_2(430, 310, cla)
            time.sleep(1)
            click_pos_2(430, 360, cla)
            time.sleep(1)

            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\settings\\skill_4_8.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(720, 490, 950, 540, cla, img)

            if imgs_ is not None and imgs_ != False:
                print('anti', imgs_)
            else:
                print('anti not')
                click_pos_2(790, 515, cla)
            time.sleep(1)
            click_pos_2(615, 570, cla)
            time.sleep(1)

            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\settings\\skill_4_8.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(720, 700, 950, 750, cla, img)

            if imgs_ is not None and imgs_ != False:
                print('hud', imgs_)
            else:
                print('hud not')
                click_pos_2(790, 720, cla)
            time.sleep(1)
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\settings\\skill_4_8.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(720, 740, 950, 800, cla, img)

            if imgs_ is not None and imgs_ != False:
                print('skill', imgs_)
            else:
                print('skill not')
                click_pos_2(790, 770, cla)
                time.sleep(1)


            click_pos_2(500, 840, cla)
            time.sleep(1)

            # 계정
            go_mynumber_(cla)

            #게임
            click_pos_2(85, 105, cla)
            time.sleep(1)
            click_pos_2(600, 515, cla)
            time.sleep(1)
            #전투
            click_pos_2(220, 105, cla)
            time.sleep(1)

            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\settings\\skill_4_8.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(720, 640, 950, 700, cla, img)

            if imgs_ is not None and imgs_ != False:
                print('player_attack', imgs_)
            else:
                print('player_attack not')
                click_pos_2(800, 670, cla)
                time.sleep(1)

            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\settings\\skill_4_8.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(720, 695, 950, 750, cla, img)

            if imgs_ is not None and imgs_ != False:
                print('player_attack', imgs_)
                click_pos_2(800, 720, cla)
                time.sleep(1)
            else:
                print('player_attack not')



            click_pos_2(85, 195, cla)
            time.sleep(1)
            click_pos_2(750, 205, cla)
            time.sleep(1)
            click_pos_2(840, 155, cla)
            time.sleep(1)
            click_pos_2(840, 155, cla)
            time.sleep(1)
            click_pos_2(840, 155, cla)
            time.sleep(1)
            click_pos_2(570, 155, cla)
            time.sleep(1)
            #나가기
            click_pos_2(930, 55, cla)
            time.sleep(1)

            # 다시 메뉴 클릭
            click_pos_2(930, 55, cla)
            time.sleep(1)
            # 아바타
            click_pos_2(800, 140, cla)
            time.sleep(1)
            # 아바타 선택
            click_pos_2(650, 180, cla)
            time.sleep(1)
            click_pos_2(880, 1005, cla)
            time.sleep(1)
            # 나가기
            click_pos_2(930, 55, cla)
            time.sleep(1)

            #다시 메뉴 클릭
            click_pos_2(930, 55, cla)
            time.sleep(1)
            #탈 것
            click_pos_2(860, 140, cla)
            time.sleep(1)
            #지상 탈 것
            click_pos_2(675, 200, cla)
            time.sleep(1)
            click_pos_2(880, 1005, cla)
            time.sleep(1)
            #공중 탈 것
            click_pos_2(800, 200, cla)
            time.sleep(1)
            click_pos_2(880, 1005, cla)
            time.sleep(1)
            # 나가기
            click_pos_2(930, 55, cla)
            time.sleep(1)

            # 다시 메뉴 클릭
            click_pos_2(930, 55, cla)
            time.sleep(1)
            # 무기형상
            click_pos_2(680, 440, cla)
            time.sleep(1)
            click_pos_2(650, 190, cla)
            time.sleep(1)
            click_pos_2(880, 1005, cla)
            time.sleep(1)
            # 나가기
            click_pos_2(930, 55, cla)
            time.sleep(1)
        elif data == 'change_start':

            # 열기
            isSet_ = False
            while isSet_ is False:
                result = menuOpenCheck(cla, "game_settings_end")
                if result == False:
                    click_pos_2(920, 55, cla)
                    time.sleep(random_int())
                else:
                    isSet_ = True
                    click_pos_2(910, 650, cla)
                    time.sleep(1)
                    click_pos_2(920, 545, cla)
                    time.sleep(random_int())


            # 절전모드 끄기
            click_pos_2(85, 105, cla)
            time.sleep(0.5)
            click_pos_2(600, 515, cla)
            time.sleep(0.5)

            # 전투
            click_pos_2(220, 105, cla)
            time.sleep(1)

            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\settings\\skill_4_8.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(720, 640, 950, 700, cla, img)

            if imgs_ is not None and imgs_ != False:
                print('player_attack', imgs_)
            else:
                print('player_attack not')
                click_pos_2(800, 670, cla)
                time.sleep(1)

            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\settings\\skill_4_8.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(720, 695, 950, 750, cla, img)

            if imgs_ is not None and imgs_ != False:
                print('player_attack', imgs_)
                click_pos_2(800, 720, cla)
                time.sleep(1)
            else:
                print('player_attack not')

            # 계정
            go_mynumber_(cla)
            # 나가기
            click_pos_2(930, 55, cla)
            time.sleep(1)

            # 다시 메뉴 클릭
            click_pos_2(930, 55, cla)
            time.sleep(1)
            # 아바타
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\settings\\e_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(600, 110, 650, 160, cla, img)
            if imgs_ is not None and imgs_ != False:
                print("아바타", imgs_)
            else:
                click_pos_2(800, 140, cla)
                time.sleep(0.5)
                # 아바타 선택
                click_pos_2(650, 180, cla)
                time.sleep(0.5)
                click_pos_2(880, 1005, cla)
                time.sleep(0.5)
            # 나가기
            click_pos_2(930, 55, cla)
            time.sleep(1)

            # 다시 메뉴 클릭
            click_pos_2(930, 55, cla)
            time.sleep(1)
            # 탈 것
            click_pos_2(860, 140, cla)
            time.sleep(0.5)

            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\settings\\e_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(600, 110, 650, 200, cla, img)
            if imgs_ is not None and imgs_ != False:
                print("지상", imgs_)
            else:
                # 지상 탈 것
                click_pos_2(675, 200, cla)
                time.sleep(0.5)
                click_pos_2(880, 1005, cla)
                time.sleep(0.5)

            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\settings\\e_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(715, 155, 765, 200, cla, img)
            if imgs_ is not None and imgs_ != False:
                print("공중", imgs_)
            else:
                # 공중 탈 것
                click_pos_2(800, 200, cla)
                time.sleep(0.5)
                click_pos_2(880, 1005, cla)
                time.sleep(0.5)


            # 나가기
            click_pos_2(930, 55, cla)
            time.sleep(1)

            # 다시 메뉴 클릭
            click_pos_2(930, 55, cla)
            time.sleep(0.5)
            # 무기형상
            click_pos_2(680, 440, cla)
            time.sleep(0.5)
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\settings\\e_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(600, 110, 650, 200, cla, img)
            if imgs_ is not None and imgs_ != False:
                print("무기형상", imgs_)
            else:
                click_pos_2(650, 190, cla)
                time.sleep(0.5)
                click_pos_2(880, 1005, cla)
                time.sleep(0.5)
            # 나가기
            click_pos_2(930, 55, cla)
            time.sleep(1)


    except Exception as e:
        print(e)
        return 0


def swim_out(cla, story):
    try:
        from myfunction import imgs_set, click_pos_2, random_int
        from where import go_worldmap
        import numpy as np
        import cv2

        get_story = str(story) + " => swim_out"
        print(get_story)
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\swim.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(850, 920, 950, 1020, cla, img)

        if imgs_ is not None:
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
            time.sleep(30 + random_int())  # 중복
    except Exception as e:
        print(e)
        return 0


def now_hunting_is(data, cla):
    try:
        from myfunction import imgs_set, click_pos_reg, random_int, text_check_get_3, int_put_, click_pos_2, text_check_get
        from schedule import myQuest_grow_check
        from clean import clean_screen
        import numpy as np
        import cv2
        import pyautogui
        from massenger import line_to_me

        ing_Check_ = False

        maul_ = False

        dir_path = "C:\\my_games\\coobcco2\\data_od"
        file_path = dir_path + "\\imgs\\maul\\maul.txt"

        with open(file_path, "r", encoding='utf-8-sig') as file:
            maul = file.read().splitlines()
            print("&&&&&&2222222222", maul)

        for i in range(len(maul)):
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\maul\\" + maul[i] + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(600, 900, 840, 1040, cla, img)
            if imgs_ is not None and imgs_ != False:
                print(maul[i], "있다있다 마을 포시 있다있다")
                maul_ = True

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\maul\\maul_mana.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(200, 70, 400, 130, cla, img)
        if imgs_ is not None:
            print("maul_mana")
            maul_ = True
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\maul\\yotoon.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(200, 70, 400, 130, cla, img)
        if imgs_ is not None:
            print("yotoon")
            maul_ = True
        else:
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\maul\\yotoon2.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(200, 70, 400, 130, cla, img)
            if imgs_ is not None:
                print("yotoon2")
                maul_ = True
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\maul\\maul_nida.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(200, 70, 400, 130, cla, img)
        if imgs_ is not None:
            print("maul_nida")
            maul_ = True

        if maul_ == False:


            check_count = 0

            gold_1 = 0
            gold_2 = 0

            print("///////////////////////////////////////now_hunting_is//////////////////////////////////////////////////")
            isgoldCheck = False
            while isgoldCheck is False:
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\gold_check.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(350, 60, 440, 100, cla, img)
                if imgs_ is not None:
                    isgoldCheck = True
                    print("gold_check 보여", imgs_)

                else:
                    print("gold_check 안보여")
                    result = go_now_hunting_is(cla)
                    click_pos_reg(result[0], result[1], cla)
                    pyautogui.moveTo(480, 550, 0.2)
                    time.sleep(random_int())
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\gold_check.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(350, 60, 440, 100, cla, img)
                    if imgs_ is not None:
                        isgoldCheck = True
                        print("gold_check 보여2", imgs_)

                    else:
                        check_count += 1
                        print("gold_check 안보여2")
                        clean_screen(cla, "now_hunting_is")
                        time.sleep(0.3)
                        result = go_now_hunting_is(cla)
                        click_pos_reg(result[0], result[1], cla)
                        pyautogui.moveTo(480, 550, 0.2)
                        time.sleep(1)
                        if check_count > 3:
                            isgoldCheck = True
                            print("gold_check 안보여서 가방으로 체크")

            if check_count > 3:
                go_bag(cla, "now_hunting_is")

                mygold_check = text_check_get_3(810, 40, 900, 70, 1, cla)
                mygold_ = int_put_(mygold_check)
                mygold_bool = mygold_.isdigit()
                if mygold_bool == True:
                    print("mygold_", mygold_)
                    gold_1 = int(mygold_)
                    time.sleep(12)

                    mygold_check = text_check_get_3(810, 40, 900, 70, 1, cla)
                    mygold_ = int_put_(mygold_check)
                    mygold_bool = mygold_.isdigit()
                    if mygold_bool == True:
                        print("mygold_", mygold_)
                        gold_2 = int(mygold_)
                else:
                    print("파악 불가")
                click_pos_2(920, 55, cla)
            else:
                golded_ = text_check_get(505, 70, 585, 95, cla)
                gold_ = golded_.split("\n")
                gold = int_put_(gold_[0])
                gold_bloon = gold.isdigit()
                if len(gold) >= 1 and gold_bloon == True:
                    gold_1 = int(gold)
                    time.sleep(1 + random_int())
                    print("gold_1", gold_1)
                    time.sleep(12)

                    golded_2 = text_check_get(505, 70, 585, 95, cla)
                    gold_22_ = golded_2.split("\n")
                    gold_22 = int_put_(gold_22_[0])
                    gold2_bloon = gold_22.isdigit()
                    if len(gold_22) >= 1 and gold2_bloon == True:
                        gold_2 = int(gold_22)
                        time.sleep(1 + random_int())
                        print("gold_2", gold_2)

            if gold_1 == gold_2:
                # 현재 가만히 있는 중...
                if cla == "one":
                    v_.one_cla_stop += 1
                    if v_.one_cla_stop > 3:
                        line_to_me(cla, "가만히 있는 중")
                if cla == "two":
                    v_.two_cla_stop += 1
                    if v_.two_cla_stop > 3:
                        line_to_me(cla, "가만ㅅ만히 있는 중")
                print("shit_..." + data)
                click_pos_2(900, 890, cla)
                time.sleep(1)
            else:
                if cla == "one":
                    v_.one_cla_stop = 0
                if cla == "two":
                    v_.two_cla_stop = 0
                # 현재 뭔가 잡는 중...
                print("현재? 뭔가를 잡는중", data)
                ing_Check_ = True
                time.sleep(1)
        else:
            what = str(data) + "=> 마을이란다"
            line_to_me(cla, what)
            print("now_hunting_is : 현재 마을이다")
            if cla == 'one':
                v_.one_cla_ing ='check'
            if cla == 'two':
                v_.two_cla_ing = 'check'

        print("ing2", ing_Check_)

        return ing_Check_
    except Exception as e:
        print(e)
        return 0

def now_hunting(data, cla):
    try:
        # data => cla_ing
        # clean_screen(cla)
        ing_Check_ = False

        # data_ = str(data)
        ing_check_result = now_hunting_is(data, cla)
        if ing_check_result == True:
            ing_Check_ = True



        return ing_Check_
    except Exception as e:
        print(e)
        return 0
