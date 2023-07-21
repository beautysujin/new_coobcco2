# import numpy as np
# import cv2
import time
# import os.path
# import clipboard
# import webbrowser

import sys
sys.path.append('C:/my_games/coobcco2/data_od/mymodule')
# from myfunction import *
# from dungeon import jadong_cla_ready
# from schedule import myQuest_number_check_bool, start_id_search
# from guild import guild_join_
# from event_get import achieve_get_
# from action import *
# from chango import chango_
# from grow import potion_grow, tuto_grow, common_grow, yotoon_grow

import variable as v_

def go_test(cla):
    print('hi test! login_start', cla)



def login_start_ready(howcla):
    try:
        from schedule import myQuest_grow_check, go_character_select, myQuest_number_check_bool
        from clean import lotation_change_ready, bangchi_mode
        from action import go_mynumber_, go_bag, go_power_bag
        from myfunction import click_pos_2, go_to_home, imgs_set
        from chango import chango_
        from dungeon import jadong_cla_ready, go_jadong_cla_mypower

        v_.now_cla = 'one'
        cla = v_.now_cla
        v_.global_howcla = howcla

        turn = False

        result = login_start_(cla)
        print("def game_play_test(howcla):def game_play_test(howcla):def game_play_test(howcla):", result)
        if result == True:
            v_.now_cla = 'one'
            turn = True
            print("진정한 게임 스타트!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!11111", turn)
        else:
            print("아직 2클라 안 돌렸느니라1111111", turn)
            print("아직 2클라 안 돌렸느니라1111111", v_.now_cla)
            result_ = login_start_(v_.now_cla)
            print('result_ : ??? ', result_)
            if result_ == True:
                myQuest_grow_result = myQuest_grow_check(v_.now_cla)
                print("myQuest_grow_result", myQuest_grow_result)
                # print("myQuest_grow_result[1]", myQuest_grow_result[1])
                # print("myQuest_grow_result[2]", myQuest_grow_result[2])
                # print("myQuest_grow_result[3]", myQuest_grow_result[3])
                if myQuest_grow_result[2] == '요툰육성' or myQuest_grow_result[2] == '니다육성':
                    print("육성모드 돌입")
                    print("육성을 시작해볼까")
                    v_.now_cla = 'one'
                    turn = True
                else:
                    lotation_change_ready(v_.now_cla, 'login_start_ready')
                    bangchi_mode(cla)

                    result_cha_select = go_character_select(v_.now_cla)
                    if result_cha_select == False:

                        mynum_ = go_mynumber_(v_.now_cla)
                        time.sleep(0.2)
                        click_pos_2(920, 65, v_.now_cla)
                        time.sleep(0.2)

                        num_bool = myQuest_number_check_bool(v_.now_cla, mynum_)
                        # print("mynumbers_[0] / number =>", mynumbers_[0])
                        # print("mynumbers_[1] / cla_ing_ =>", mynumbers_[1])
                        # print("mynumbers_[2] / myid =>", mynumbers_[2])
                        # print("mynumbers_[3] / mylevel =>", mynumbers_[3])
                        # print("mynumbers_[4] / mypower =>", mynumbers_[4])
                        # print("mynumbers_[5] / mymoney =>", mynumbers_[5])
                        # print("mynumbers_[6] / cla_count =>", mynumbers_[6])
                        # print("mynumbers_[7] / mypotion_ =>", mynumbers_[7])
                        # print("mynumbers_[8] / event_bool =>", mynumbers_[8])
                        # print("mynumbers_[9] / now_growing_ =>", mynumbers_[9])

                        if num_bool[0] == True:
                            if num_bool[1] != "check":
                                go_bag(v_.now_cla, "처음 사냥터 보내기1")
                                go_power_bag(v_.now_cla)
                                click_pos_2(920, 65, v_.now_cla)
                                go_to_home(num_bool[1], v_.now_cla)
                            else:
                                print("파워측정 후 사냥터")
                                go_bag(v_.now_cla, "처음 사냥터 보내기1")
                                go_power_bag(v_.now_cla)
                                click_pos_2(920, 65, v_.now_cla)
                                go_jadong_cla_mypower(v_.now_cla)

                            time.sleep(1)
                            v_.now_cla = 'one'
                            turn = True
                        else:
                            get_cla_count(v_.now_cla)
                            time.sleep(1)
                            chango_(v_.now_cla, 'after')
                            time.sleep(1)
                            go_bag(v_.now_cla, "처음 사냥터 보내기2")
                            go_power_bag(v_.now_cla)
                            click_pos_2(920, 65, v_.now_cla)
                            go_jadong_cla_mypower(v_.now_cla)
                            time.sleep(1)
                            v_.now_cla = 'one'
                            turn = True
                    else:
                        get_cla_count(v_.now_cla)
                        time.sleep(1)
                        chango_(v_.now_cla, 'after')
                        time.sleep(1)
                        go_bag(v_.now_cla, "처음 사냥터 보내기3")
                        go_power_bag(v_.now_cla)
                        click_pos_2(920, 65, v_.now_cla)
                        go_jadong_cla_mypower(v_.now_cla)
                        time.sleep(1)
                        v_.now_cla = 'one'
                        turn = True
                    print("진정한 게임 스타트!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!22222", turn)
            else:
                print("아직 2클라 안 돌렸느니라2222222", turn)

        return turn
    except Exception as e:
        print(e)
        return 0
def login_start_(cla):
    try:
        from myfunction import imgs_set, random_int, click_pos_reg
        from schedule import go_character_select
        import pyautogui
        import numpy as np
        import cv2

        turn = False
        offline_start = False

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\odin.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        if cla == 'one':
            imgs_ = imgs_set(0, 0, 60, 30, cla, img)
            # imgs_ = pyautogui.locateCenterOnScreen(img, region=(0, 0, 60 , 30), confidence=0.7)
            if imgs_ is None or imgs_ == False:
                offline_start = True
                login_starting(cla)

            else:
                print("이미 창은 켜져있고, 무엇을 실행중인지 파악하고 대처하자1", cla)
                result = go_character_select(cla)
                if result == True:
                    print("캐릭터 창이다!(이건 생각해보자1)", cla)
                    offline_start = True
                    # game_play(cla, global_howcla)
                else:
                    print("캐릭터 창이 아니다. 보통은 게임 진행중일 것이다. 이건 파악해보자1", cla)
                    offline_start = True
        elif cla == 'two':

            imgs_ = imgs_set(0, 0, 60, 30, cla, img)
            # imgs_ = pyautogui.locateCenterOnScreen(img, region=(960, 0, 60 , 30), confidence=0.7)
            if imgs_ is None or imgs_ == False:
                offline_start = True
                login_starting(cla)
            else:
                print("이미 창은 켜져있고, 무엇을 실행중인지 파악하고 대처하자2", cla)
                result = go_character_select(cla)
                if result == True:
                    print("캐릭터 창이다!(이건 생각해보자2)", cla)
                    offline_start = True
                    # game_play(cla, global_howcla)
                else:
                    print("캐릭터 창이 아니다. 보통은 게임 진행중일 것이다. 이건 파악해보자2", cla)
                    offline_start = True




        if offline_start == True:
            if v_.global_howcla == 'onecla' and cla == 'one':
                turn = True
                print("one cla 게임 진행")
            elif v_.global_howcla == 'onetwocla' and cla == 'one':
                print("onetwocla 게임 진행")
                v_.now_cla = 'two'
                print("onetwocla 게임 진행", v_.now_cla)

            elif v_.global_howcla == 'onetwocla' and cla == 'two':
                print("완벽하다, onetwocla 게임 진행")
                time.sleep(random_int())

                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\lastclick2.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = pyautogui.locateCenterOnScreen(img, region=(0, 1000, 1500, 1080), confidence=0.7)
                if imgs_ is None or imgs_ == False:
                    print("lastclick2 안보여")
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\lastclick2_2.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = pyautogui.locateCenterOnScreen(img, region=(0, 1000, 1500, 1080), confidence=0.7)
                    if imgs_ is None or imgs_ == False:
                        print("lastclick2_2 안보여")
                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\lastclick3.png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = pyautogui.locateCenterOnScreen(img, region=(0, 1000, 1500, 1080), confidence=0.7)
                        if imgs_ is None or imgs_ == False:
                            print("lastclick3 안보여")
                            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\my_games\\coobcco2\\data_od.png"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = pyautogui.locateCenterOnScreen(img, region=(0, 1000, 1500, 1080), confidence=0.7)
                            if imgs_ is None or imgs_ == False:
                                print("my_games\\coobcco2\\data_od 안보여")
                                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\my_games\\coobcco2\\data_od2.png"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = pyautogui.locateCenterOnScreen(img, region=(0, 1000, 1500, 1080),
                                                                       confidence=0.7)
                                if imgs_ is None or imgs_ == False:
                                    print("my_games\\coobcco2\\data_od2 안보여")
                                    print("다른 방법 찾자!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                                else:
                                    print("my_games\\coobcco2\\data_od2 보여", imgs_)
                                    time.sleep(random_int())
                                    click_pos_reg(imgs_.x + 50, imgs_.y, cla)
                                    time.sleep(random_int())
                                    click_pos_reg(imgs_.x, imgs_.y - 100, cla)
                                    time.sleep(random_int())

                                    turn = True
                            else:
                                print("my_games\\coobcco2\\data_od 보여", imgs_)
                                time.sleep(random_int())
                                click_pos_reg(imgs_.x + 50, imgs_.y, cla)
                                time.sleep(random_int())
                                click_pos_reg(imgs_.x, imgs_.y - 100, cla)
                                time.sleep(random_int())

                                turn = True
                        else:
                            print("lastclick3 보여", imgs_)
                            time.sleep(random_int())
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(random_int())
                            click_pos_reg(imgs_.x - 50, imgs_.y - 100, cla)
                            time.sleep(random_int())

                            turn = True
                    else:
                        print("lastclick2_2 보여", imgs_)
                        time.sleep(random_int())
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(random_int())
                        click_pos_reg(imgs_.x - 50, imgs_.y - 100, cla)
                        time.sleep(random_int())

                        turn = True
                else:
                    print("lastclick2 보여", imgs_)
                    time.sleep(random_int())
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(random_int())
                    click_pos_reg(imgs_.x - 50, imgs_.y - 100, cla)
                    time.sleep(random_int())

                    turn = True
        else:
            turn = True


        print("def login_start_(cla): def login_start_(cla): def login_start_(cla): ", turn)
        return turn
    except Exception as e:
        print(e)
        return 0

###########

def login_starting(cla):
    try:
        from myfunction import random_int, click_pos_reg, drag_pos, imgs_set
        import pyautogui
        import numpy as np
        import cv2
        import os.path
        import clipboard
        import webbrowser

        dir_path = "C:\\my_games\\coobcco2"
        if cla == 'one':
            file_path = dir_path + "\\odin_schedule\\onecla.txt"
        elif cla == 'two':
            file_path = dir_path + "\\odin_schedule\\twocla.txt"

        if os.path.isfile(file_path) == True:
            # 파일 읽기
            with open(file_path, "r", encoding='utf-8-sig') as file:
                lines_ = file.read().splitlines()
                cla_id = lines_[0]
                cla_pw = lines_[1]



        webbrowser.open_new("https://odin.game.daum.net/odin/")
        time.sleep(random_int())

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\refresh.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.7)
        time.sleep(random_int())
        if imgs_ is None:
            print("refresh 안보여")
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\refresh2.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.7)
            time.sleep(random_int())
            if imgs_ is None:
                print("refresh2 안보여")
            else:
                print("refresh2 보여", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(random_int())
        else:
            print("refresh 보여", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(random_int())





        isLogin = False
        isLogin_count = 0
        while isLogin is False:

            isLogin_count += 1
            if isLogin_count > 7:
                isLogin = True
            time.sleep(random_int())
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\log_out.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.9)
            if imgs_ is not None:
                print("log_out 보여", imgs_)
                # click_with_image("c:\\my_games\\coobcco2\\data_od\\imgs\\log_out.png")
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\log_out.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.9)
                if imgs_ is not None:
                    print("log_out 보여2", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(random_int())
                else:
                    isLogin = True
            else:
                print("log_out 안보여")
                pyautogui.scroll(500)
                isLogin = True
                time.sleep(random_int())

        isLogin = False
        isLogin_count = 0
        while isLogin is False:

            isLogin_count += 1
            if isLogin_count > 7:
                isLogin = True

            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\game_start.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.7)
            gs_x = imgs_.x
            gs_y = imgs_.y
            if imgs_ is not None:
                print("게임스타트 보여", imgs_)
                # click_with_image("c:\\my_games\\coobcco2\\data_od\\imgs\\game_start.png")
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\yes.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.7)
                if imgs_ is not None:
                    isLogin = True
                    print("확인 보여")
                else:
                    click_pos_reg(gs_x, gs_y, cla)
                    print("확인 안보여")
                    time.sleep(random_int())
            else:
                print("게임스타트 안보여")
                time.sleep(random_int())

        isLogin = False
        isLogin_count = 0
        while isLogin is False:

            isLogin_count += 1
            if isLogin_count > 7:
                isLogin = True

            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\kakao_login.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.7)

            if imgs_ is None or imgs_ == False:
                print("카카오로그인 안보여", imgs_)
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\yes.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.7)
                if imgs_ is not None:
                    print("확인 보여", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(random_int())
                else:
                    print("확인 안보여")
                    time.sleep(random_int())

            else:
                print("카카오로그인 보여")
                isLogin = True
                time.sleep(random_int())

        isLogin = False
        isLogin_count = 0
        while isLogin is False:

            isLogin_count += 1
            if isLogin_count > 7:
                isLogin = True
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\kakao.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.7)

            if imgs_ is None or imgs_ == False:
                print("kakao 안보여")
                # click_with_image("c:\\my_games\\coobcco2\\data_od\\imgs\\kakao_login.png")
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\kakao_login.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.7)
                if imgs_ is not None:
                    print("kakao_login 보여", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(random_int())
                else:
                    print("kakao_login 안보여")
                    time.sleep(random_int())
            else:
                # full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\login\\id_in.png"
                # img_array = np.fromfile(full_path, np.uint8)
                # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                # imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.7)
                # if imgs_ is not None:
                #     print("id_in", imgs_)
                # full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\login\\pw_in.png"
                # img_array = np.fromfile(full_path, np.uint8)
                # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                # imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.7)
                # if imgs_ is not None:
                #     print("pw_in", imgs_)
                print("kakao 보여")
                isLogin = True
                time.sleep(random_int())
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\login\\id_in.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.7)
                if imgs_ is not None:
                    print("id_in", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    clipboard.copy(cla_id)
                    pyautogui.hotkey("ctrl", "v")
                else:
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\login\\id_in_2.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.7)
                    if imgs_ is not None:
                        print("id_in", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        clipboard.copy(cla_id)
                        pyautogui.hotkey("ctrl", "v")
                time.sleep(random_int())
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\login\\pw_in.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.7)
                if imgs_ is not None:
                    print("pw_in", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    clipboard.copy(cla_pw)
                    pyautogui.hotkey("ctrl", "v")


        time.sleep(random_int())


        # click_with_image("c:\\my_games\\coobcco2\\data_od\\imgs\\final_login.png")

        isLogin = False
        isLogin_count = 0
        while isLogin is False:

            isLogin_count += 1
            if isLogin_count > 7:
                isLogin = True

            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\final_login.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.7)
            if imgs_ is not None:
                print("final_login 보여", imgs_)
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\final_login.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.7)
                if imgs_ is not None:
                    print("final_login 보여2", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(7 + random_int())
                else:
                    isLogin = True
                    print("final_login 안보여2")
                    time.sleep(random_int())
            else:
                isLogin = True
                print("final_login 안보여")
                time.sleep(random_int())


        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\daumstarter.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.5)
        time.sleep(random_int())
        if imgs_ is not None:
            print("다음스타터 보여", imgs_)
            #click_with_image("c:\\my_games\\coobcco2\\data_od\\imgs\\daumstarter.png")
            # click_pos_reg(imgs_.x, imgs_.y, cla)
            click_pos_reg(735, 165, cla)
            time.sleep(random_int())
            click_pos_reg(1020, 220, cla)
            time.sleep(random_int())
        else:
            print("다음스타터 안보여")
        time.sleep(20 + random_int())

        # isTouch = False
        # while isTouch is False:
        #     full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\pc.png"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = pyautogui.locateCenterOnScreen(img, region=(400, 0, 1000, 1000), confidence=0.7)
        #
        #     if imgs_ is not None:
        #         isTouch = True
        #         print("pc", imgs_)
        #         if imgs_.y  < 60:
        #             if cla == 'one':
        #                 drag_pos(imgs_.x, imgs_.y - 30, imgs_.x, imgs_.y + 100, cla)
        #             else:
        #                 drag_pos(imgs_.x - 960, imgs_.y-30, imgs_.x - 960, imgs_.y + 100, cla)
        #     else:
        #         print("pc안보영")
        #         time.sleep(random_int())

        isTouch = False
        isTouchCount = 0
        while isTouch is False:
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\odin.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.7)
            time.sleep(random_int())
            if imgs_ is not None:
                print("odin 보여")

                time.sleep(10 + random_int())
                click_pos_reg(imgs_.x + 100, imgs_.y, cla)
                pyautogui.keyDown('win')
                if cla == 'one':
                    pyautogui.press('left')
                elif cla == 'two':
                    pyautogui.press('right')
                pyautogui.keyUp('win')

                time.sleep(3 + random_int())
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\odin.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.7)
                click_pos_reg(imgs_.x + 100, imgs_.y, cla)
                if cla == 'one':
                    if imgs_.x < 60 and imgs_.y < 30:
                        print("통과1")
                        isTouch = True
                    else:
                        print("긴 싸움 시작1")
                        isTouch = True
                    time.sleep(random_int())
                elif cla == 'two':
                    if 960 < imgs_.x < 60 + 960 and imgs_.y < 30:
                        print("통과2")
                        isTouch = True
                    else:
                        print("긴 싸움 시작2")
                        isTouch = True
                    time.sleep(random_int())



            else:
                isTouchCount += 1
                if isTouchCount > 100:
                    print("odin 아직 안 보여, if isTouchCount > 100:")
                    pyautogui.keyDown('win')
                    if cla == 'one':
                        pyautogui.press('left')
                    elif cla == 'two':
                        pyautogui.press('right')
                    pyautogui.keyUp('win')
                else:
                    print("odin 아직 안 보여")
                    time.sleep(random_int())
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\pc.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

                    imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.7)

                    if imgs_ is not None:
                        print("pc", imgs_)
                        if imgs_.y < 60:
                            if cla == 'one':
                                drag_pos(imgs_.x, imgs_.y - 30, imgs_.x, imgs_.y + 100, cla)
                            else:
                                drag_pos(imgs_.x - 960, imgs_.y - 30, imgs_.x - 960, imgs_.y + 100, cla)
                    else:
                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\pc2.png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.7)
                        if imgs_ is not None:
                            print("pc2 보여2", imgs_)
                            if cla == 'one':
                                drag_pos(imgs_.x, imgs_.y - 30, imgs_.x, imgs_.y + 100, cla)
                            else:
                                drag_pos(imgs_.x - 960, imgs_.y - 30, imgs_.x - 960, imgs_.y + 100, cla)
                        else:
                            print("pc2 안보여2")
                            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\pc3.png"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = pyautogui.locateCenterOnScreen(img, region=(50, 0, 1800, 120), confidence=0.8)
                            if imgs_ is not None:
                                print("pc3 보여3", imgs_)
                                if cla == 'one':
                                    drag_pos(imgs_.x, imgs_.y , imgs_.x, imgs_.y + 100, cla)
                                else:
                                    drag_pos(imgs_.x - 960, imgs_.y, imgs_.x - 960, imgs_.y + 100, cla)
                            else:
                                print("pc3 안 보여3")
                                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\pc4.png"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = pyautogui.locateCenterOnScreen(img, region=(50, 0, 1800, 120), confidence=0.7)
                                if imgs_ is not None:
                                    print("pc4 보여4", imgs_)
                                    if cla == 'one':
                                        drag_pos(imgs_.x, imgs_.y, imgs_.x, imgs_.y + 100, cla)
                                    else:
                                        drag_pos(imgs_.x - 960, imgs_.y, imgs_.x - 960, imgs_.y + 100, cla)
                                else:
                                    print("pc4도 안 보여")
                                    if cla == 'one':
                                        x_point = 0
                                    if cla == 'two':
                                        x_point = 100
                                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\lastclick2.png"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = pyautogui.locateCenterOnScreen(img, region=(0, 1000, 1500, 1080),
                                                                           confidence=0.7)
                                    if imgs_ is None or imgs_ == False:
                                        print("lastclick2 안보여")
                                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\lastclick2_2.png"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = pyautogui.locateCenterOnScreen(img, region=(0, 1000, 1500, 1080),
                                                                               confidence=0.7)
                                        if imgs_ is None or imgs_ == False:
                                            print("lastclick2_2 안보여")
                                            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\lastclick3.png"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = pyautogui.locateCenterOnScreen(img, region=(0, 1000, 1500, 1080),
                                                                                   confidence=0.7)
                                            if imgs_ is None or imgs_ == False:
                                                print("lastclick3 안보여")
                                                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\my_games\\coobcco2\\data_od.png"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = pyautogui.locateCenterOnScreen(img,
                                                                                       region=(0, 1000, 1500, 1080),
                                                                                       confidence=0.7)
                                                if imgs_ is None or imgs_ == False:
                                                    print("my_games\\coobcco2\\data_od 안보여")
                                                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\my_games\\coobcco2\\data_od2.png"
                                                    img_array = np.fromfile(full_path, np.uint8)
                                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                    imgs_ = pyautogui.locateCenterOnScreen(img,
                                                                                           region=(0, 1000, 1500, 1080),
                                                                                           confidence=0.7)
                                                    if imgs_ is None or imgs_ == False:
                                                        print("my_games\\coobcco2\\data_od2 안보여")
                                                        print(
                                                            "다른 방법 찾자!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                                                    else:
                                                        print("my_games\\coobcco2\\data_od2 보여", imgs_)
                                                        time.sleep(random_int())
                                                        click_pos_reg(imgs_.x + 50, imgs_.y, cla)
                                                        time.sleep(random_int())
                                                        click_pos_reg(imgs_.x + x_point, imgs_.y - 100, cla)
                                                        time.sleep(random_int())
                                                else:
                                                    print("my_games\\coobcco2\\data_od 보여", imgs_)
                                                    time.sleep(random_int())
                                                    click_pos_reg(imgs_.x + 50, imgs_.y, cla)
                                                    time.sleep(random_int())
                                                    click_pos_reg(imgs_.x + x_point, imgs_.y - 100, cla)
                                                    time.sleep(random_int())
                                            else:
                                                print("lastclick3 보여", imgs_)
                                                time.sleep(random_int())
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                                time.sleep(random_int())
                                                click_pos_reg(imgs_.x - 50 + x_point, imgs_.y - 100, cla)
                                                time.sleep(random_int())
                                        else:
                                            print("lastclick2_2 보여", imgs_)
                                            time.sleep(random_int())
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            time.sleep(random_int())
                                            click_pos_reg(imgs_.x - 50 + x_point, imgs_.y - 100, cla)
                                            time.sleep(random_int())
                                    else:
                                        print("lastclick2 보여", imgs_)
                                        time.sleep(random_int())
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(random_int())
                                        click_pos_reg(imgs_.x - 50 + x_point, imgs_.y - 100, cla)
                                        time.sleep(random_int())




        isTouch = False
        isCount_last = 0
        while isTouch is False:
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\odin.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.7)


            print("odin 보여!!!")
            full_path2 = "c:\\my_games\\coobcco2\\data_od\\imgs\\char_select2.png"
            img_array2 = np.fromfile(full_path2, np.uint8)
            img2 = cv2.imdecode(img_array2, cv2.IMREAD_COLOR)
            imgs_2 = imgs_set(5, 30, 170, 200, cla, img2)
            full_path3 = "c:\\my_games\\coobcco2\\data_od\\imgs\\char_select3.png"
            img_array3 = np.fromfile(full_path3, np.uint8)
            img3 = cv2.imdecode(img_array3, cv2.IMREAD_COLOR)
            imgs_3 = imgs_set(5, 30, 170, 200, cla, img3)
            full_path4 = "c:\\my_games\\coobcco2\\data_od\\imgs\\char_select.png"
            img_array4 = np.fromfile(full_path4, np.uint8)
            img4 = cv2.imdecode(img_array4, cv2.IMREAD_COLOR)
            imgs_4 = imgs_set(5, 30, 170, 200, cla, img4)

            if imgs_2 is not None or imgs_3 is not None or imgs_4 is not None:
                isTouch = True
                print("드디어 정상적인 캐릭터 화면~!!!!!!!!!!")
                time.sleep(random_int())



            else:
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\odin.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.7)
                print("캐릭터가 제 위치가 아니야")
                if imgs_ is not None:
                    click_pos_reg(imgs_.x + 100, imgs_.y + 100, cla)
                    isCount_last += 1
                    if isCount_last > 10:
                        click_pos_reg(imgs_.x + 100, imgs_.y, cla)
                        pyautogui.keyDown('win')
                        if cla == 'one':
                            pyautogui.press('left')
                        elif cla == 'two':
                            pyautogui.press('right')
                        pyautogui.keyUp('win')
                else:
                    print("아직 odin 글씨가 안 보여")
                time.sleep(10 + random_int())


    except Exception as e:
        print(e)
        return 0

def just_login(cla):
    try:
        from myfunction import random_int, click_pos_reg, drag_pos, imgs_set
        import pyautogui
        import numpy as np
        import cv2
        import os.path
        import clipboard
        import webbrowser

        dir_path = "C:\\my_games\\coobcco2"
        if cla == 'one':
            file_path = dir_path + "\\odin_schedule\\onecla.txt"
        elif cla == 'two':
            file_path = dir_path + "\\odin_schedule\\twocla.txt"

        if os.path.isfile(file_path) == True:
            # 파일 읽기
            with open(file_path, "r", encoding='utf-8-sig') as file:
                lines_ = file.read().splitlines()
                cla_id = lines_[0]
                cla_pw = lines_[1]

        if '@' in cla_id:
            print("good", cla_id)

        else:
            print("id를 확인해 주세요.")

        webbrowser.open_new("https://odin.game.daum.net/odin/")
        time.sleep(random_int())

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\refresh.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.7)
        time.sleep(random_int())
        if imgs_ is None:
            print("refresh 안보여")
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\refresh2.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.7)
            time.sleep(random_int())
            if imgs_ is None:
                print("refresh2 안보여")
            else:
                print("refresh2 보여", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(random_int())
        else:
            print("refresh 보여", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(random_int())

        isLogin = False
        while isLogin is False:
            time.sleep(random_int())
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\log_out.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.9)
            if imgs_ is not None:
                print("log_out 보여", imgs_)
                # click_with_image("c:\\my_games\\coobcco2\\data_od\\imgs\\log_out.png")
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\log_out.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.9)
                if imgs_ is not None:
                    print("log_out 보여2", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(random_int())
                else:
                    isLogin = True
            else:
                print("log_out 안보여")
                pyautogui.scroll(500)
                isLogin = True
                time.sleep(random_int())

        isLogin = False
        while isLogin is False:

            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\game_start.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.7)
            gs_x = imgs_.x
            gs_y = imgs_.y
            if imgs_ is not None:
                print("게임스타트 보여", imgs_)
                # click_with_image("c:\\my_games\\coobcco2\\data_od\\imgs\\game_start.png")
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\yes.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.7)
                if imgs_ is not None:
                    isLogin = True
                    print("확인 보여")
                else:
                    click_pos_reg(gs_x, gs_y, cla)
                    print("확인 안보여")
                    time.sleep(random_int())
            else:
                print("게임스타트 안보여")
                time.sleep(random_int())

        isLogin = False
        while isLogin is False:

            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\kakao_login.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.7)

            if imgs_ is None or imgs_ == False:
                print("카카오로그인 안보여", imgs_)
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\yes.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.7)
                if imgs_ is not None:
                    print("확인 보여", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(random_int())
                else:
                    print("확인 안보여")
                    time.sleep(random_int())

            else:
                print("카카오로그인 보여")
                isLogin = True
                time.sleep(random_int())

        isLogin = False
        while isLogin is False:
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\kakao.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.7)

            if imgs_ is None or imgs_ == False:
                print("kakao 안보여")
                # click_with_image("c:\\my_games\\coobcco2\\data_od\\imgs\\kakao_login.png")
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\kakao_login.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.7)
                if imgs_ is not None:
                    print("kakao_login 보여", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(random_int())
                else:
                    print("kakao_login 안보여")
                    time.sleep(random_int())
            else:
                # full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\login\\id_in.png"
                # img_array = np.fromfile(full_path, np.uint8)
                # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                # imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.7)
                # if imgs_ is not None:
                #     print("id_in", imgs_)
                # full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\login\\pw_in.png"
                # img_array = np.fromfile(full_path, np.uint8)
                # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                # imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.7)
                # if imgs_ is not None:
                #     print("pw_in", imgs_)
                print("kakao 보여")
                isLogin = True
                time.sleep(random_int())
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\login\\id_in.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.7)
                if imgs_ is not None:
                    print("id_in", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    clipboard.copy(cla_id)
                    pyautogui.hotkey("ctrl", "v")
                else:
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\login\\id_in_2.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.7)
                    if imgs_ is not None:
                        print("id_in", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        clipboard.copy(cla_id)
                        pyautogui.hotkey("ctrl", "v")
                time.sleep(random_int())
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\login\\pw_in.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.7)
                if imgs_ is not None:
                    print("pw_in", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    clipboard.copy(cla_pw)
                    pyautogui.hotkey("ctrl", "v")

        time.sleep(random_int())

        # click_with_image("c:\\my_games\\coobcco2\\data_od\\imgs\\final_login.png")

        isLogin = False
        while isLogin is False:

            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\final_login.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.7)
            if imgs_ is not None:
                print("final_login 보여", imgs_)
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\final_login.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.7)
                if imgs_ is not None:
                    print("final_login 보여2", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(7 + random_int())
                else:
                    isLogin = True
                    print("final_login 안보여2")
                    time.sleep(random_int())
            else:
                isLogin = True
                print("final_login 안보여")
                time.sleep(random_int())

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\daumstarter.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.5)
        time.sleep(random_int())
        if imgs_ is not None:
            print("다음스타터 보여", imgs_)
            # click_with_image("c:\\my_games\\coobcco2\\data_od\\imgs\\daumstarter.png")
            # click_pos_reg(imgs_.x, imgs_.y, cla)
            click_pos_reg(735, 165, cla)
            time.sleep(random_int())
            click_pos_reg(1020, 220, cla)
            time.sleep(random_int())
        else:
            print("다음스타터 안보여")
    except Exception as e:
        print(e)
        return 0



def get_cla_count(cla):
    try:
        import numpy as np
        import cv2
        from schedule import go_character_select, start_id_search
        from myfunction import menuOpenCheck, click_pos_2, click_pos_reg, random_int, imgs_set, go_auto, dead_die

        print("몇배럭, 몇클라냐?(get_cla_count) : start", cla)

        time.sleep(1)

        result = go_character_select(cla)

        if result == False:
            print("캐릭터 선택이 없다...")
        else:
            # 스케쥴 불러와서 선택하기
            print("캐릭터 선택_OK")

            in_check_ = False
            in_check_count = 0
            while in_check_ is False:
                in_check_count += 1
                if in_check_count > 30:
                    in_check_ = True
                result_out = go_auto(cla, 1)
                if result_out == True:
                    in_check_ = True
                    print("진입 성공!")
                else:
                    dir_path = "C:\\my_games\\coobcco2"
                    file_path = dir_path + "\\odin_schedule\\schedule.txt"

                    with open(file_path, "r", encoding='utf-8-sig') as file:
                        read_file = file.read()
                        print("read_file", read_file)

                    newstart_ = start_id_search(cla, "start")
                    newstart_ = int(newstart_)

                    if newstart_ == 1:
                        click_pos_2(895, 115, cla)
                        # 880 135
                    if newstart_ == 2:
                        click_pos_2(895, 200, cla)
                        # 880 245
                    if newstart_ == 3:
                        click_pos_2(895, 285, cla)
                        # 880 350
                    if newstart_ == 4:
                        click_pos_2(895, 370, cla)
                        # 460
                    if newstart_ == 5:
                        click_pos_2(895, 455, cla)
                        # 560\
                    time.sleep(0.2)
                    click_pos_2(840, 990, cla)
                print("진입 중...", in_check_count)
                time.sleep(2)
    except Exception as e:

        print(e)
        return 0



def characterChange_before(cla):
    try:
        from myfunction import text_check_get, text_check_get_2, random_int
        import re

        power = 0
        level = 0
        char_staus_ = text_check_get(770, 90, 810, 115, cla)
        ready_ = char_staus_.split('\n')
        print("선택된 캐릭 스텟 펼치기", ready_)

        char_staus_ = text_check_get_2(130, 315, 175, 330, cla)
        ready_ = char_staus_.split('\n')
        print("선택된 캐릭 스텟 펼치기", ready_)

        character_power_level = False
        character_power_level_count = 0
        while character_power_level is False:

            character_power_level_count += 1
            if character_power_level_count > 7:
                character_power_level = True
            time.sleep(0.2)
            power_ran = random_int()
            if power_ran == 1:
                char_staus_ = text_check_get_2(111, 274, 230, 335, cla)
            if power_ran == 2:
                char_staus_ = text_check_get_2(130, 315, 175, 330, cla)
            if power_ran == 3:
                char_staus_ = text_check_get_2(14, 292, 190, 362, cla)
            if power_ran == 4:
                char_staus_ = text_check_get_2(23, 274, 230, 335, cla)
            ready_ = char_staus_.split('\n')
            if len(ready_) != 0:
                for list in ready_:
                    try:
                        list_ = re.sub(r'[^0-9]', '', list)
                        list_bool = list_.isdigit()
                        if list_bool == True:
                            any_ = int(list_)
                            if 3 < any_ < 100:
                                level = any_
                            elif 1000 < any_ < 100000:
                                power = any_
                    except:
                        pass

            if level == 0 or power == 0:
                #######################
                if power_ran == 1:
                    char_staus_ = text_check_get_2(150, 300, 245, 410, cla)
                if power_ran == 2:
                    char_staus_ = text_check_get_2(25, 330, 245, 410, cla)
                if power_ran == 3:
                    char_staus_ = text_check_get_2(150, 360, 245, 410, cla)
                if power_ran == 4:
                    char_staus_ = text_check_get_2(150, 300, 260, 460, cla)
                ready_ = char_staus_.split('\n')
                ######################
                if len(ready_) != 0:
                    for list in ready_:
                        try:
                            list_ = re.sub(r'[^0-9]', '', list)
                            list_bool = list_.isdigit()
                            if list_bool == True:
                                any_ = int(list_)
                                if 3 < any_ < 200:
                                    level = any_
                                elif 1000 < any_:
                                    power = any_
                        except:
                            pass

            if power != 0:
                if level is None:
                    level = 1
                character_power_level = True
                if cla == 'one':
                    v_.mylevel_1 = level
                    v_.mypower_1 = power
                if cla == "two":
                    v_.mylevel_2 = level
                    v_.mypower_2 = power
                print("level", level)
                print("power", power)
                time.sleep(0.2)
            else:
                character_power_level = True
                if cla == 'one':
                    v_.mylevel_1 = 1
                    v_.mypower_1 = 1000
                if cla == "two":
                    v_.mylevel_2 = 1
                    v_.mypower_2 = 1000
                print("no!!")
                print("level", level)
                print("power", power)
                print("no!!")


        return level, power
    except Exception as e:
        print(e)
        return 0


def characterChange(data, cla):
    try:
        import numpy as np
        import cv2
        import os
        from myfunction import click_pos_2, random_int, menuOpenCheck, go_auto, click_pos_reg, imgs_set
        from schedule import go_character_select
        from chango import chango_
        from action import go_alrim_, go_alrim_yes, game_settings, go_alrim_confirm
        from clean import lotation_change_ready, clean_screen
        from guild import guild_join_
        from event_get import achieve_get_
        from massenger import line_to_me
        from stop_18 import is_stop

        print("캐릭터체인지", data)
        print("캐릭터체인지", cla)

        dir_path = "C:\\my_games\\coobcco2"

        if cla == 'one':
            v_.myId_1 = int(data)
            file_path = dir_path + "\\odin_schedule\\one_now_id.txt"
        if cla == 'two':
            v_.myId_2 = int(data)
            file_path = dir_path + "\\odin_schedule\\two_now_id.txt"

        with open(file_path, "w", encoding='utf-8-sig') as file:
            file.write(str(data))

        if cla == 'one':
            v_.gonghu_1 = False
            v_.nanjang_1 = False
            v_.underprison_1 = False
            v_.one_cla_ing = 'check'
            v_.mypotion_1 = 0
            v_.mymoney_1 = 0
        if cla == 'two':
            v_.gonghu_2 = False
            v_.nanjang_2 = False
            v_.underprison_2 = False
            v_.two_cla_ing = 'check'
            v_.mypotion_2 = 0
            v_.mymoney_2 = 0


        if cla == 'one':
            v_.myId_1 = data
            print("myid_1 : ")
            print(v_.myId_1)
        if cla == 'two':
            v_.myId_2 = data
            print("myid_2 : ")
            print(v_.myId_2)

        result_char_select = go_character_select(cla)
        if result_char_select == False:
            print("characterChange, isCount == 0:")
            chango_(cla, 'before')
            time.sleep(0.5)
            click_pos_2(920, 65, cla)
            time.sleep(0.5)

        isChecked = False
        isCount = 0
        while isChecked is False:
            isCount += 1
            if isCount > 20:
                isChecked = True
                line_to_me(cla, "캐릭체인지에 문제 있다")
            result_char_select = go_character_select(cla)

            if result_char_select == False:
                clean_screen(cla, "character change")
                mo_ = False
                mo_count = 0
                while mo_ is False:
                    mo_count += 1
                    if mo_count > 7:
                        mo_ = True
                    result__ = menuOpenCheck(cla, "characterChange")
                    if result__ != True:
                        result_char_select = go_character_select(cla)
                        if result_char_select == True:
                            mo_ = True
                        else:
                            click_pos_2(920, 65, cla)
                            time.sleep(1)
                            click_pos_2(740, 530, cla)
                            time.sleep(1)
                            click_pos_2(550, 610, cla)
                            time.sleep(1)
                    else:
                        click_pos_2(740, 530, cla)
                        time.sleep(1)
                        click_pos_2(550, 610, cla)
                        time.sleep(1)
                    time.sleep(1)


                # result__ = menuOpenCheck(cla, "characterChange")
                # time.sleep(0.5)
                # if result__ != True:
                #
                #     click_pos_2(920, 65, cla)
                #     time.sleep(1)
                # else:
                #
                #     click_pos_2(740, 530, cla)
                #     time.sleep(1)
                #
                #     result = go_alrim_(cla)
                #     if result == True:
                #         result_ = go_alrim_yes(cla)
                #         if result_[0] == True:
                #             click_pos_reg(result_[1], result_[2], cla)
                #         else:
                #             click_pos_2(550, 610, cla)
            else:
                isChecked = True
                isChecked2 = False
                isCount2 = 0
                while isChecked2 is False:
                    isCount2 += 1
                    if isCount2 > 20:
                        isChecked2 = True
                        line_to_me(cla, "캐릭체인지에 문제 있다2")
                    if isCount2 < 2:
                        print("진입")
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\playgame.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(780, 970, 880, 1010, cla, img)
                    if imgs_ is not None and imgs_ != False:
                        print("게임하기 보여.", imgs_)
                        if int(data) == 1:
                            click_pos_2(800, 115, cla)
                        if int(data) == 2:
                            click_pos_2(800, 200, cla)
                        if int(data) == 3:
                            click_pos_2(800, 285, cla)
                        if int(data) == 4:
                            click_pos_2(800, 370, cla)
                        if int(data) == 5:
                            click_pos_2(800, 455, cla)
                        time.sleep(0.2)
                        characterChange_before(cla)
                        click_pos_2(835, 990, cla)
                        time.sleep(0.2)
                        click_pos_2(835, 990, cla)
                    else:
                        # 진입하기
                        is_in = False
                        is_in_count = 0
                        while is_in is False:
                            is_in_count += 1
                            if is_in_count > 30:
                                is_in = True
                            result_in = go_auto(cla, '9')
                            if result_in == False:
                                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\playgame.png"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set(780, 970, 880, 1010, cla, img)
                                if imgs_ is None or imgs_ == False:
                                    print("게임하기 안보여...로딩중...")
                                    time.sleep(random_int())
                                else:
                                    print("게임하기 보여")
                                    click_pos_2(835, 990, cla)
                                    time.sleep(random_int())
                            else:
                                print("게임 진입")
                                isChecked2 = True
                                is_in = True
                            time.sleep(1)
                        print("게임진입2")
                        time.sleep(0.2)
                        # 게임진입 후

                        # x 같은 이벤트
                        is_stop(cla)


                        lotation_change_ready(cla, 'characterchange_Playing')
                        chango_(cla, 'after')
                        guild_join_(cla)
                        achieve_get_(cla)
                        game_settings(cla, 'change_start')

            time.sleep(1)
    except Exception as e:
        print(e)
        return 0



def today_lotation(cla, changeid_):
    try:
        from clean import clean_screen
        print("cla?로테이션", cla)
        # start_ready[0] 진행중인 정보 [0][1] = id, [0][2] = 던전(공허, 난쟁이, 지하감옥, 자동사냥(들소황무지...), [0][3] = 완료 or 대기중
        # 몇번째 인자에 정보가 담겨있는지 여부
        time.sleep(1)
        clean_screen(cla, "today_lotation")


        print("로테이션2", cla)
        # 여기에 스케쥴 초기화 and 정지 후 다시 실행
        characterChange(changeid_, cla)


    except Exception as e:
        print(e)
        return 0


def grow_chango_check(cla):
    try:
        import numpy as np
        import cv2
        from myfunction import menuOpenCheck, click_pos_2, imgs_set, text_check_get_3, drag_pos, imgs_set_, click_pos_reg
        from action import go_alrim_confirm

        quest_check_ = False
        isquestCheck_1 = False
        isquestCheck_1_count = 0
        while isquestCheck_1 is False:

            isquestCheck_1_count += 1
            if isquestCheck_1_count > 7:
                isquestCheck_1 = True
            result_menu = menuOpenCheck(cla, "grow_chango_check")
            if result_menu == True:
                click_pos_2(800, 220, cla)
                time.sleep(2)

                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\clean\\quest.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(30, 30, 160, 80, cla, img)
                if imgs_ is not None:
                    time.sleep(0.5)

                    # quest_check_midgard testttttttt
                    # full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\quest_check_midgard.png"
                    # img_array = np.fromfile(full_path, np.uint8)
                    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    # imgs_ = imgs_set(400, 80, 550, 130, cla, img)
                    midgard_get = text_check_get_3(400, 90, 550, 120, 0, cla)
                    print('midgard_get', midgard_get)
                    if '미드' in midgard_get:
                        print("good")

                        time.sleep(0.5)
                        drag_pos(150, 300, 150, 900, cla)
                        time.sleep(1)
                        drag_pos(150, 300, 150, 900, cla)
                        time.sleep(1)
                        # 트루 추출에 앞서 펄스 추출
                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\quest_check_false_1.png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 200, 300, 1030, cla, img, 0.85)
                        if imgs_ is None or imgs_ == False:
                            print("개개끼?1", imgs_)
                            # 여긴 트루 추출
                            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\quest_check_true_3.png"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 200, 300, 1030, cla, img, 0.85)
                            if imgs_ is None or imgs_ == False:
                                print("개개끼?2", imgs_)
                                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\quest_check_true_2.png"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(0, 750, 300, 1030, cla, img, 0.85)
                                if imgs_ is not None:
                                    print("quest_check_true_2", imgs_)
                                    isquestCheck_1 = True
                                    quest_check_ = True
                                else:
                                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\quest_check_true_1.png"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(0, 200, 300, 1030, cla, img, 0.85)
                                    if imgs_ is not None:
                                        print("quest_check_true_1", imgs_)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(1)
                                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\quest_check_true_2.png"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(0, 750, 300, 1030, cla, img, 0.85)
                                        if imgs_ is not None:
                                            print("quest_check_true_22", imgs_)
                                            isquestCheck_1 = True
                                            quest_check_ = True
                                        else:
                                            print("없음.")
                                            isquestCheck_1 = True
                            else:
                                print("어디고", imgs_)
                                isquestCheck_1 = True
                                quest_check_ = True
                        else:
                            print("어디고 뭐꼬?", imgs_)
                            isquestCheck_1 = True
                    else:
                        print("어디고 여가?", imgs_)
                        isquestCheck_1 = True
                        quest_check_ = True
                else:
                    result_menu = menuOpenCheck(cla, "grow_chango_check_2")
                    if result_menu == True:
                        isquestCheck_1 = True
                        time.sleep(0.5)
                        click_pos_2(920, 65, cla)
                        time.sleep(0.5)
                        click_pos_2(30, 225, cla)
                        time.sleep(0.5)
                        go_alrim_confirm(cla, "grow_chango_check_2")
                    else:
                        time.sleep(0.5)
                        click_pos_2(920, 65, cla)
                        time.sleep(0.5)
            else:
                time.sleep(1)
                click_pos_2(920, 65, cla)
                time.sleep(1)

        print("quest_check_", quest_check_)
        click_pos_2(920, 65, cla)
        time.sleep(1)
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\clean\\quest.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(30, 30, 160, 80, cla, img)
        if imgs_ is not None:
            click_pos_2(920, 65, cla)
            time.sleep(1)

        return quest_check_
    except Exception as e:
        print(e)
        return 0

def status_check_get(cla):
    try:
        import numpy as np
        import cv2
        from action import go_bag, go_power_bag
        from myfunction import text_check_get, int_put_, isNumber_, potion_count_grow, potion_count, random_int, imgs_set, click_pos_2

        # status_check_ = False
        isPower = False
        isGold = False
        print("스텟체크중, 넌 몇클라?", cla)
        print("점검_____________27_______________", cla)

        if cla == 'one':
            print('mypower_1', v_.mypower_1)
            cla_ing = v_.one_cla_ing
        if cla == 'two':
            print('mypower_2', v_.mypower_2)
            cla_ing = v_.two_cla_ing


        print("골드파악")

        go_bag(cla, 'status_get')

        golded_ = text_check_get(815, 40, 891, 65, cla)
        print("gold??", golded_)
        gold_ = golded_.split("\n")
        result_ = int_put_(gold_[0])
        gold_bloon = isNumber_(result_)
        if len(result_) >= 1 and gold_bloon == True:
            gold = int(result_)
            isGold = True
            print("gold", gold)
        else:
            gold = 1000000
            print("noGold = True")

        print("전투혁 측정 및 포션 갯수 파악")
        go_power_bag(cla)

        if cla_ing == 'grow':
            potion = potion_count_grow(cla)
        else:
            potion = potion_count(cla)
        print("potion", potion)
        time.sleep(random_int())

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\gabang.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(30, 40, 100, 75, cla, img)
        if imgs_ is None or imgs_ == False:
            print("가방표시 없다. 포션 파악 끝")
        else:
            print("가방표시 있다. 포션 파악 끝")
            # 여기서 전투력 파악하기

            time.sleep(0.5)
            click_pos_2(920, 65, cla)
            time.sleep(1)





        print("전투력파악")
        if cla == 'one':
            power = v_.mypower_1
            isPower = True
        if cla == 'two':
            power = v_.mypower_2
            isPower = True

        print("ID파악")
        if cla == 'one':
            print("myid_1")
            myId = v_.myId_1
            print(v_.myId_1)
        if cla == 'two':
            print("myid_2")
            myId = v_.myId_2
            print(v_.myId_2)



        time.sleep(random_int())
        print('몇클? : ', cla)
        print('ID : ', myId)
        print('전투력 : ', power)
        print('포션', potion)
        print('골드', gold)
        time.sleep(random_int())

        if isGold == True and isPower == True:



            if power > 0:
                print("=>poeer")
                if cla == 'one':
                    v_.mypower_1 = power
                if cla == 'two':
                    v_.mypower_2 = power
            if potion > 0:
                print("=>potion")
                if cla == 'one':
                    v_.mypotion_1 = potion
                if cla == 'two':
                    v_.mypotion_2 = potion
            if gold > 0:
                print("=>money")
                if cla == 'one':
                    v_.mymoney_1 = gold
                if cla == 'two':
                    v_.mymoney_2 = gold
        else:
            print("스텟체크 실패")
        return myId

    except Exception as e:
        print(e)
        return 0

def go_tuto_grow_menu(cla):
    try:
        from action import go_juljun
        from myfunction import imgs_set
        import numpy as np
        import cv2

        print("오른쪽 위에 메뉴표시 있을때 True 리턴하기")

        go_ = False
        # juljun
        print("Grow_juljun")
        go_juljun(cla, 'tuto_grow')

        # tuto_menu
        full_path = "c:\\coobcco\\imgs\\grow\\menu_1.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(890, 30, 950, 80, cla, img)
        if imgs_ is not None:
            print("menu_1", imgs_)
            go_ = True
        else:
            full_path = "c:\\coobcco\\imgs\\grow\\menu_2.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(890, 30, 950, 80, cla, img)
            if imgs_ is not None:
                print("menu_2", imgs_)
                go_ = True
            else:
                full_path = "c:\\coobcco\\imgs\\grow\\menu_3.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(890, 30, 950, 80, cla, img)
                if imgs_ is not None:
                    print("menu_3", imgs_)
                    go_ = True

        return go_
    except Exception as e:
        print(e)
        return 0