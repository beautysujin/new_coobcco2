# import numpy as np
# import cv2
import time

import sys
sys.path.append('C:/my_games/coobcco2/data_od/mymodule')
# from myfunction import *
# from action import swim_out

import variable as v_

def go_test(cla):
    print('hi test! clean', cla)

def clean_screen(cla, story):
    try:
        import numpy as np
        import cv2
        from action import go_juljun, go_alrim_confirm
        # from clean import bangchi_mode, game_event_popup
        from maul import maul_mission_complete, maul_mission_complete_get
        from schedule import myQuest_grow_check
        from myfunction import imgs_set, click_pos_2, click_pos_reg, menuOpenCheck, random_int, go_auto
        from massenger import line_to_me


        get_story = str(story) + " => clean_screen"
        print(get_story)

        go_juljun(cla, get_story)

        bangchi_mode(cla)

        #exit
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\grow\\main_quest_soolock_1.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(880, 30, 960, 150, cla, img)
        if imgs_ is not None and imgs_ != False:
            print("exit")
            click_pos_reg(imgs_.x, imgs_.y, cla)

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

        compl_ready = maul_mission_complete(cla)
        if compl_ready == True:
            maul_mission_complete_get(cla, get_story)

        game_event_popup(cla)

        # X 보이면 클릭(보통 캐시샵)
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\clean\\click_x.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(140, 220, 950, 490, cla, img)
        if imgs_ is not None:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\clean\\active_x.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(300, 100, 350, 150, cla, img)
        if imgs_ is not None:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\clean\\party_x.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(600, 300, 700, 400, cla, img)
        if imgs_ is not None:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\clean\\unreal_error_1.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 700, 960, 850, "one", img)
        if imgs_ is not None:
            line_to_me("one", "블랙스크린")
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\clean\\unreal_error_2.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 700, 960, 850, "two", img)
        if imgs_ is not None:
            line_to_me("two", "블랙스크린")

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\odin.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(0, 0, 960, 1030, "one", img)
        if imgs_ is None:
            line_to_me("one", "꺼진 것 같다")
        if v_.global_howcla == "onetwocla":
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\odin.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(0, 0, 960, 1030, "two", img)
            if imgs_ is None:
                line_to_me("two", "꺼진 것 같다")


        clean_list = ['gabang', 'chashshop', 'character', 'skillbook', 'skillbook2', 'avatar', 'talgut', 'item_soojib', 'auction', 'jejak', 'quest', 'maul_mission', 'upjuk', 'bonginsuk', 'loon', 'gagin', 'umool', 'soonwe', 'guild_join', 'guild', 'dunjeon', 'vs', 'pk', 'friend', 'moogi_hyungsang', 'gongsungjun', 'post', 'setting']

        # 캐시샵 나가기
        for i in range(len(clean_list)):
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\clean\\" + clean_list[i] + ".png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(30, 30, 160, 80, cla, img)
            if imgs_ is not None:
                click_pos_2(920, 65, cla)

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
            click_pos_2(920, 65, cla)

        # # 인터넷창 열릴 때 꺼놓기
        # full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\clean\\click_x.png"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set(1700, 220, 950, 490, cla, img)

        # if imgs_ is not None:
        #     click_pos_reg(imgs_.x, imgs_.y, cla)

        # 키 설정
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\clean\\key_setting_1.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(410, 405, 530, 450, cla, img)

        if imgs_ is not None:
            click_pos_2(480, 620, cla)



        go_alrim_confirm(cla, get_story)


        # result = go_alrim_(cla)
        #
        # if result == False:
        #     print("알림 없다 clean_screen")
        # else:
        #     print("왠 알림이냐! clean_screen")
        #     result_ = go_alrim_yes(cla)
        #     if result_[0] == True:
        #         click_pos_reg(result_[1], result_[2], cla)
        #     else:
        #         click_pos_2(405, 628, cla)



        # mistake__ = text_check_get(45, 35, 150, 70, cla)
        # mistake_ = mistake__.split("\n")
        # mistake = " ".join(mistake_).strip()
        # print("mistake clean_screen", mistake)
        #
        # ismistake = False
        # if len(mistake) != 0:
        #     for list in range(len(mistake)):
        #         try:
        #             if mistake[list] == "소" or mistake[list] == '모' or mistake[list] == '품' or mistake[list] == '상' or \
        #                     mistake[
        #                         list] == '점' or mistake[list] == '스' or mistake[list] == '킬' or mistake[list] == '북' or \
        #                     mistake[
        #                         list] == '월' or mistake[list] == '드' or mistake[list] == '맵' or mistake[list] == '마' or \
        #                     mistake[list] == '을' or mistake[list] == '의' or mistake[list] == '뢰' or mistake[list] == '캐' or \
        #                     mistake[list] == '시' or mistake[list] == '릭' or mistake[list] == '아' or mistake[list] == '바' or \
        #                     mistake[list] == '타' or mistake[list] == '탈' or mistake[list] == '것' or mistake[list] == '이':
        #                 ismistake = True
        #                 print("ismistake clean_screen", mistake[list])
        #         except:
        #             pass
        # if ismistake == True:
        #     click_pos_2(920, 65, cla)

        myQuest_grow_result = myQuest_grow_check(cla)
        print('clean_screen : myQuest_grow_result', myQuest_grow_result)

        if cla == 'one':
            cla_ing_ = v_.one_cla_ing
        if cla == 'two':
            cla_ing_ = v_.two_cla_ing

        if cla_ing_ == 'maul' or cla_ing_ == 'grow' or myQuest_grow_result[2] == '요툰육성' or myQuest_grow_result[
            2] == '니다육성':
            game_event_popup(cla)  # 이벤트창
            print("pass")
        else:

            isClean_ = False
            isClean__count = 0
            while isClean_ is False:

                isClean__count += 1
                if isClean__count > 7:
                    isClean_ = True
                result = menuOpenCheck(cla, get_story)
                if result == True:
                    isClean_ = True
                    click_pos_2(920, 65, cla)
                    time.sleep(0.2)
                    game_event_popup(cla)  # 이벤트창
                else:
                    result = go_auto(cla, '12')
                    if result == False:
                        print("auto_quest 안보여(clean_screen)")
                        click_pos_2(920, 65, cla)
                        game_event_popup(cla)  # 이벤트창
                    else:
                        print("auto_quest 보여(clean_screen)")
                        isClean_ = True
                        game_event_popup(cla)  # 이벤트창

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\active.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(10, 100, 110, 150, cla, img)
        if imgs_ is not None:
            click_pos_2(290, 130, cla)

        time.sleep(1)

        print("def clean_screen(cla): end")

    except Exception as e:
        print(e)
        return 0

def lotation_change_ready(cla, story):
    try:
        from action import go_juljun, go_alrim_confirm, swim_out
        from myfunction import imgs_set, dead_die
        from maul import maul_mission_complete_get
        import numpy as np
        import cv2


        get_story = str(story) + " => lotation_change_ready"
        print(get_story)

        go_juljun(cla, get_story)

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\maul_bosang_3.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(200, 400, 800, 800, cla, img)

        if imgs_ is None or imgs_ == False:
            print("maul_bosang_3 안보여1")
        else:
            print("maul_bosang_3 보여1")
            maul_mission_complete_get(cla, get_story)


        go_alrim_confirm(cla, get_story)

        swim_out(cla, get_story)

        dead_die(cla, get_story)





    except Exception as e:
        print(e)
        return 0


def bangchi_mode(cla):
    try:
        from myfunction import imgs_set, click_pos_2
        import numpy as np
        import cv2

        if cla == 'one':
            plus = 0
        if cla == 'two':
            plus = 960

        full_path2 = "c:\\my_games\\coobcco2\\data_od\\imgs\\bangchi.png"
        img_array2 = np.fromfile(full_path2, np.uint8)
        img2 = cv2.imdecode(img_array2, cv2.IMREAD_COLOR)
        imgs_2 = imgs_set(400, 400, 535, 435, cla, img2)

        if imgs_2 is None or imgs_2 == False:
            print("방치모드 안했다.")
        else:
            print("방치모드 했다")
            click_pos_2(480, 640, cla)


    except Exception as e:
        print(e)
        return 0

def game_event_popup(cla):
    try:
        from myfunction import imgs_set, click_pos_2, text_check_get, random_int

        print("게임이벤트")
        isEvent = False
        evented_ = text_check_get(414, 294, 530, 321, cla)
        event_ = evented_.split("\n")
        if len(event_) != 0:
            for list in event_[0]:
                try:
                    if list == '이' or list == '벤' or list == '트' or list == '보' or list == '상' or list == '특' or list == '별' or list == '패' or list == '키' or list == '지':
                        print("event", event_[0])
                        isEvent = True
                except:
                    pass
        # 랜덤
        time.sleep(0.2)
        if isEvent == True:
            click_pos_2(915, 310, cla)

        # 던전 입장시 갑자기 뜨는 팝업창
        # click_pos_2(120, 735, cla)
        # time.sleep(random_int())


    except Exception as e:
        print(e)
        return 0


