# import numpy as np
# import cv2
import time
# import pyautogui
# import random

import sys
sys.path.append('C:/my_games/coobcco2/data_od/mymodule')

# from myfunction import imgs_set, menuOpenCheck, random_int, click_pos_2, text_check_get, int_put_, click_pos_reg
# from action import go_boonhae, go_alrim_confirm, swim_out
# from where import go_maul_

import variable as v_

def go_test(cla):
    print('hi test! maul', cla)

def go_maul_bosang(cla):
    try:
        import numpy as np
        import cv2
        import random
        from myfunction import imgs_set, random_int, click_pos_2
        go_ = False

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\maul_bosang_2.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(780, 970, 950, 1030, cla, img)
        if imgs_ is None or imgs_ == False:
            print("def go_maul_bosang(cla): 보상받기 안보여")
        else:
            print("def go_maul_bosang(cla): 보상받기 보여", imgs_)
            time.sleep(random_int())
            click_pos_2(870, 1005, cla)
            time.sleep(1 + random_int())
            result_int = random.randint(0, 4)
            # 350, 415, 480, 545, 610 // 625
            x_ = 350 + (int(result_int) * 65)
            click_pos_2(x_, 625, cla)
            time.sleep(random_int())
            click_pos_2(x_, 625 + 300, cla)
            x_ = 0
            time.sleep(random_int())
            click_pos_2(920, 65, cla)
            time.sleep(random_int())

        return go_
    except Exception as e:
        print(e)
        return 0

def maul_cou_(cla):
    try:
        import numpy as np
        import cv2
        import pyautogui
        from myfunction import imgs_set, menuOpenCheck, random_int, click_pos_2, text_check_get, int_put_
        print("maul_cou_ 입니당")

        # maul_count_0, maul_count_1, maul_counted_, maul_count_2, maul_count_3, maul_counted_2
        maul_count_0 = 0
        maul_count_1 = 0
        maul_counted_ = 0
        maul_count_2 = 0
        maul_count_3 = 0
        maul_counted_2 = 0


        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\maul.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(30, 30, 160, 80, cla, img)
        if imgs_ is None or imgs_ == False:
            print("def maul_cou_(cla): 마을이 없다...")
            ismenu = False
            while ismenu is False:
                result_ = menuOpenCheck(cla, "maul_cou_")
                time.sleep(random_int())
                if result_ == True:
                    ismenu = True
                    click_pos_2(860, 220, cla)
                    time.sleep(random_int())
                else:
                    click_pos_2(920, 65, cla)
                    time.sleep(random_int())
        else:
            print("def maul_cou_(cla): 마을이 있다...")


        if cla == 'one':
            plus = 0
        if cla == 'two':
            plus = 960
        # 마을 수락함 갯수
        cou_ = 0
        cou_1 = 0
        cou_2 = 0
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\maul_complete_get.png"  # '완료' 글자 갯수 파악
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # for list in pyautogui.locateAllOnScreen(img, region=(230 + plus, 120, 90 + plus, 480), confidence=0.7):
        for list in pyautogui.locateAllOnScreen(img, region=(230 + plus, 120, 90, 480), confidence=0.7):
            cou_ += 1
            cou_1 += 1
        print("cou_1", cou_)
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\maul_soolockham.png"  # '수락함' 글자 갯수 파악
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # for list in pyautogui.locateAllOnScreen(img, region=(230 + plus, 120, 80 + plus, 840), confidence=0.7):
        for list in pyautogui.locateAllOnScreen(img, region=(230 + plus, 120, 90, 840), confidence=0.7):
            cou_ += 1
            cou_2 += 1
        print("cou_2", cou_)

        # 마을의뢰 갯수
        maul_count_ = text_check_get(190, 955, 270, 985, cla)
        print('포함?', maul_count_)
        maul_count_ = int_put_(maul_count_)
        print('포함 len?', len(maul_count_))
        #if len(maul_count_)
        if len(maul_count_) > 0:
            if '/' in maul_count_:
                print('포함1', maul_count_)
                maul_count = maul_count_.split("/")
                maul_count_0 = int_put_(maul_count[0])
                maul_count_1 = int_put_(maul_count[1])
            else:
                result_ = int_put_(maul_count_)
                print('미포함', result_)
                maul_count_0 = result_[0]
                maul_count_1 = result_[len(result_) - 1]
                print('maul_count_0', maul_count_0)
                print('maul_count_1', maul_count_1)

            maul_count_0 = int(maul_count_0)
            maul_count_1 = int(maul_count_1)
            maul_counted_ = maul_count_1 - maul_count_0
            print("maul_count_0", maul_count_0)
            print("maul_count_1", maul_count_1)
            # print("maul_counted_", print(maul_counted_))
        # 진행중인 의뢰
        maul_count__ = text_check_get(900, 95, 940, 120, cla)
        if len(maul_count__) > 0:
            if '/' in maul_count__:
                print('포함2', maul_count__)
                maul_count2 = maul_count__.split("/")
                maul_count_2 = int_put_(maul_count2[0])
                maul_count_3 = int_put_(maul_count2[1])
            else:
                result_2 = int_put_(maul_count__)
                print('미포함', result_2)
                maul_count_2 = result_2[0]
                maul_count_3 = result_2[len(result_2) - 1]


            print('maul_count_2', maul_count_2)
            print('maul_count_3', maul_count_3)

            maul_count_2 = int(maul_count_2)
            maul_count_3 = int(maul_count_3)
            maul_counted_2 = maul_count_3 - maul_count_2
            print("maul_count_2", maul_count_2)
            print("maul_count_3", maul_count_3)
            # print("maul_counted_", print(maul_counted_))

        return maul_count_0, maul_count_1, maul_counted_, cou_1, cou_2, cou_, maul_count_2, maul_count_3, maul_counted_2
    except Exception as e:
        print(e)
        return 0


def maul_mission_add(cla, maul):
    try:
        import numpy as np
        import cv2
        from myfunction import click_pos_2, random_int, imgs_set
        print("maul_mission_add 입니당")

        if maul == '미드가르드':  # 마나하임은 미드가르드..
            click_pos_2(70, 105, cla)
            print("미드가르등")
        if maul == '요툰하임':  # 요툰..
            click_pos_2(200, 105, cla)
            print("요퉁")

        result_cou_ = maul_cou_(cla)
        # [0]수락 및 완료, [1]총갯수, [2]총갯수 - 수락 및 완료, [3]완료 글자 갯수, [4]수락함 글자 갯수, [5]완료 글자 + 수락함 글자 갯수
        # [6] 진행중 의뢰 갯수, [7] 진행중 의뢰 총 갯수 [8] 진행중의뢰 총갯수 - 진행중 의뢰 갯수
        # 미션추가
        start_num_ = 0
        click_start_ = 0
        if result_cou_[8] > result_cou_[2]:
        # if result_cou_[8] < result_cou_[2]:
            end__ = result_cou_[2]
        else:
            end__ = result_cou_[8]
        print("result_cou_[8]", result_cou_[8])
        for k in range(10):
            print("k", k)
            y_ = click_start_ * 55

            if start_num_ == end__:
                break
            if click_start_ == 3 and start_num_ != end__:
                print("ii", click_start_)
                click_start_ = 0
                click_pos_2(140, 1005, cla)
                time.sleep(random_int())
                click_pos_2(540, 635, cla)
                time.sleep(random_int())

                print("iii", click_start_)
            elif click_start_ < 6 and start_num_ != end__:

                click_start_ += 1
                click_pos_2(160, 165 + y_, cla)
                time.sleep(random_int())
                data = 'goodbell\nweg\njungsoo_2'
                datas = data.split("\n")

                bloon_ = False
                for i in range(len(datas)):
                    if start_num_ == end__:
                        print("끝!!!!!!!!!!!!!!!!!!!!")
                        break
                    else:
                        item_list = datas[i].split(":")
                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\jangbi_in\\" + item_list[0] + ".png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(440, 625, 770, 700, cla, img)
                        # imgs_ = pyautogui.locateCenterOnScreen(img, region=(440 + plus, 625, 330 + plus, 75),
                        #                                        confidence=0.7)

                        if imgs_ is None or imgs_ == False:
                            print("imgs_ 없다...")
                        else:
                            print("imgs_ 있다...", imgs_)
                            bloon_ = True

                if bloon_ == True:
                    start_num_ += 1
                    print("start_num_", start_num_)
                    print("end__", end__)
                    click_pos_2(870, 1005, cla)

                if start_num_ == end__:
                    print("start_num_!!!!!!!!!!!!!!!!!!1", start_num_)
                    print("end__!!!!!!!!!!!!!!!!!!!!!!!1", end__)
                    print("끝")
                    print("미션하러가기")
                    time.sleep(random_int())
                    maul_mission_start(cla)

                    break
                time.sleep(random_int())
    except Exception as e:
        print(e)
        return 0



def maul_mission_complete(cla):
    try:
        import numpy as np
        import cv2
        from myfunction import imgs_set
        print("maul_mission_complete 입니당")
        complete_ = False

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\maul_bosang_3.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(100, 400, 800, 800, cla, img)

        if imgs_ is None or imgs_ == False:
            print("maul_bosang_3 안보여1")
        else:
            print("maul_bosang_3 보여1")
            complete_ = True


        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\maul_complete_2.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(280, 570, 640, 660, cla, img)
        # imgs_ = pyautogui.locateCenterOnScreen(img, region=(280 + plus, 570, 640 + plus, 660),
        #                                        confidence=0.7)

        if imgs_ is None or imgs_ == False:
            print("maul_complete_2 안보여2")
        else:
            print("maul_complete_2 보여2")
            complete_ = True


        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\maul_complete_3.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(370, 330, 570, 475, cla, img)
        # imgs_ = pyautogui.locateCenterOnScreen(img, region=(370 + plus, 330, 570 + plus, 475),
        #                                        confidence=0.7)

        if imgs_ is None or imgs_ == False:
            print("maul_complete_3 안보여3")
        else:
            print("maul_complete_3 보여3")
            complete_ = True

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\maul_complete_4.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(400, 330, 540, 470, cla, img)
        # imgs_ = pyautogui.locateCenterOnScreen(img, region=(370 + plus, 330, 570 + plus, 475),
        #                                        confidence=0.7)

        if imgs_ is None or imgs_ == False:
            print("maul_complete_4 안보여")
        else:
            print("maul_complete_4 보여")
            complete_ = True



        return complete_
    except Exception as e:
        print(e)
        return 0

def maul_mission_complete_get(cla, story):
    try:
        import numpy as np
        import cv2
        import random
        from myfunction import imgs_set, click_pos_2, random_int, text_check_get
        from action import go_boonhae
        get_story = str(story) + "maul_mission_complete_get"
        print(get_story)

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\maul_bosang_2.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(780, 970, 950, 1030, cla, img)
        # imgs_ = pyautogui.locateCenterOnScreen(img, region=(370 + plus, 330, 570 + plus, 475),
        #                                        confidence=0.7)

        if imgs_ is None or imgs_ == False:
            print("maul_complete_4 안보여")
        else:
            print("maul_complete_4 보여")
            complete_ = True
            click_pos_2(870, 1005, cla)
            time.sleep(1 + random_int())
        result_int = random.randint(0, 4)
        # 350, 415, 480, 545, 610 // 625
        x_ = 350 + (int(result_int) * 65)
        print("x_ : ????? ", x_)
        click_pos_2(x_, 625, cla)
        # print()
        # 가방의 공간이 부족합니다
        maul_gongan__ = text_check_get(200, 110, 800, 520, cla)
        print("maul_gongan__", maul_gongan__)
        maul_gongan_ = maul_gongan__.split("\n")
        print("maul_gongan_[0] ", maul_gongan_[0])
        maul_gongan = " ".join(maul_gongan_[0]).strip()
        print("maul_gongan def maul_mission", maul_gongan)
        ismaul_gongan = False
        if len(maul_gongan) != 0:
            for list in range(len(maul_gongan)):
                try:
                    if maul_gongan[list] == '방' or maul_gongan[list] == '족' or maul_gongan[list] == '합' or maul_gongan[list] == '공' or maul_gongan[list] == '간':
                        ismaul_gongan = True
                        print("ismaul_gongan maul_mission", maul_gongan[list])
                except:
                    pass
        if ismaul_gongan == True:
            time.sleep(random_int())
            click_pos_2(920, 65, cla)
            time.sleep(random_int())
            go_boonhae(cla, get_story)
            click_pos_2(920, 65, cla)
            time.sleep(random_int())
            click_pos_2(860, 220, cla)
            time.sleep(random_int())
        else:
            time.sleep(random_int())
            click_pos_2(x_, 625 + 300, cla)
            x_ = 0
            time.sleep(random_int())
    except Exception as e:
        print(e)
        return 0

def maul_mission_ready(cla):
    try:
        import numpy as np
        import cv2
        from myfunction import imgs_set, random_int
        isMission_ = False
        while isMission_ is False:
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\maul_complete_get.png"  # '완료' 글자 클릭 후 보상 받기 버튼...
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(230, 120, 320, 600, cla, img)

            if imgs_ is None or imgs_ == False:
                print("마을 외뢰 완료가 없땅.", cla)
                isMission_ = True
                time.sleep(random_int())
            else:
                print("마을 외뢰 완료가 있땅.", cla)
                maul_mission_complete_get(cla, 'maul_mission_ready')
                time.sleep(random_int())

        maul_mission_start(cla)

    except Exception as e:
        print(e)
        return 0

def maul_mission_start(cla):
    try:
        import numpy as np
        import cv2
        from myfunction import imgs_set, click_pos_2, click_pos_reg, random_int, text_check_get
        from action import go_alrim_confirm, swim_out
        print("maul_mission_start 입니당")

        print("마을의뢰 진행중")
        print("마을의뢰 수락함 => 빠른 이동...재시작")
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\maul_soolockham.png"  # '수락함' 글자 파악
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(230, 120, 310, 960, cla, img)
        # imgs_ = pyautogui.locateCenterOnScreen(img, region=(230 + plus, 120, 80 + plus, 840),
        #                                        confidence=0.7)
        if imgs_ is None or imgs_ == False:
            print("수락함이 없다...")
        else:
            print("마을의뢰 스타트(수락함 클릭)", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(random_int())

            isAllMonsterCancle = False
            while isAllMonsterCancle is False:
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\maul_all_monster.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(320, 480, 900, 600, cla, img)
                if imgs_ is not None:
                    click_pos_2(870, 1005, cla)
                    time.sleep(random_int())
                    go_alrim_confirm(cla, 'maul_mission_start')
                    time.sleep(1)
                else:
                    isAllMonsterCancle = True
                    # 빠른 이동...
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\maul_bbaln_2.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(650, 980, 780, 1040, cla, img)
                    # imgs_ = pyautogui.locateCenterOnScreen(img, region=(660 + plus, 980, 770 + plus, 1030),
                    #                                        confidence=0.7)
                    if imgs_ is None or imgs_ == False:
                        print("빠른이동 안보여...추후 상황보고 수정...")
                    else:
                        print("빠른이동 보여", imgs_)

                        click_pos_2(730, 1005, cla)
                        time.sleep(random_int())

                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\maul_bbaln.png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(400, 410, 510, 460, cla, img)

                        if imgs_ is None or imgs_ == False:
                            print("빠른 안보여")
                            # 350, 120, 600, 155
                            click_pos_2(730, 1005, cla)
                            maul_bbaln__ = text_check_get(350, 110, 600, 210, cla)
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
                            if ismaul_bbaln == True:
                                click_pos_2(580, 1005, cla)
                            else:
                                click_pos_2(580, 1005, cla)

                                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\swim.png"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set(850, 920, 950, 1020, cla, img)

                                if imgs_ is None or imgs_ == False:
                                    print("어떤 상태인지 파악 불가")
                                else:
                                    print("이새끼 수영한다.")
                                    swim_out(cla, 'maul_mission_start')
                        else:
                            print("빠른 보여", imgs_)
                            click_pos_2(550, 610, cla)
                            time.sleep(random_int())
                            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\maul.png"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set(30, 40, 100, 75, cla, img)
                            # imgs_ = pyautogui.locateCenterOnScreen(img, region=(30 + plus, 40, 100 + plus, 75),
                            #                                        confidence=0.7)
                            if imgs_ is None or imgs_ == False:
                                print("빠른이동 후 마을의뢰 진행중")
                            else:
                                print("현재 위취와 가까운 곳에서 마을의뢰 진행중", imgs_)
                                click_pos_2(920, 65, cla)


    except Exception as e:
        print(e)
        return 0




def maul_mission_give_up(cla):
    try:
        import numpy as np
        import cv2
        from myfunction import imgs_set, click_pos_reg, random_int
        from action import go_alrim_confirm
        isGiveUp = False
        while isGiveUp is False:
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\maul_soolockham.png"  # '수락함' 글자 파악
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(230, 120, 310, 960, cla, img)
            if imgs_ is None or imgs_ == False:
                isGiveUp = True
                print("maul_mission_give_up 수락함이 없다...")
            else:
                print("maul_mission_give_up (수락함 클릭)", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(1)
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\maul_give_up.png"  # '수락함' 글자 파악
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(770, 970, 950, 1030, cla, img)
                if imgs_ is None or imgs_ == False:
                    time.sleep(1)
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\maul_give_up.png"  # '수락함' 글자 파악
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(770, 970, 950, 1030, cla, img)
                    time.sleep(1)
                    if imgs_ is None or imgs_ == False:
                        print("maul_give_up 없다...")
                    else:
                        print("maul_give_up2", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(1)
                        go_alrim_confirm(cla, 'maul_mission_give_up')
                        time.sleep(1)
                else:
                    print("maul_give_up", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(1)
                    go_alrim_confirm(cla, 'maul_mission_give_up')
                    time.sleep(1)
        isMission_ = False
        while isMission_ is False:
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\maul_complete_get.png"  # '완료' 글자 클릭 후 보상 받기 버튼...
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(230, 120, 320, 600, cla, img)

            if imgs_ is None or imgs_ == False:
                print("마을 외뢰 완료가 없땅.", cla)
                isMission_ = True
                time.sleep(random_int())
            else:
                print("마을 외뢰 완료가 있땅.", cla)
                maul_mission_complete_get(cla, 'maul_mission_give_up')
                time.sleep(random_int())
    except Exception as e:
        print(e)
        return 0

def maul_mission(cla, maul):
    try:
        import numpy as np
        import cv2
        from myfunction import imgs_set, menuOpenCheck, random_int, click_pos_2
        from where import go_maul_
        # 어느 마을인지
        print("maul_mission 입니당", maul)
        if cla == 'one':
            v_.one_cla_ing = 'maul'
        if cla == 'two':
            v_.two_cla_ing = 'maul'

        the_end_maul = False


        # 오류로 화면에 클리어 화면이 있는지 체크 후 제거하기
        compl_ready = maul_mission_complete(cla)
        if compl_ready == True:
            maul_mission_complete_get(cla, 'maul_mission')

        # 마을 의뢰 화면 켜기

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\maul.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(30, 30, 160, 80, cla, img)
        if imgs_ is None or imgs_ == False:
            print("마을이 없다...")
            ismenu = False
            while ismenu is False:
                result_ = menuOpenCheck(cla, "maul_mission_start")
                time.sleep(random_int())
                if result_ == True:
                    ismenu = True
                    click_pos_2(860, 220, cla)
                    time.sleep(random_int())
                else:
                    click_pos_2(920, 65, cla)
                    time.sleep(random_int())
        else:
            print("마을", imgs_)

        # 혹시나 있을 남은 미션 정리하기
        # [0]수락 및 완료, [1]총갯수, [2]총갯수 - 수락 및 완료, [3]완료 글자 갯수, [4]수락함 글자 갯수, [5]완료 글자 + 수락함 글자 갯수
        # [6] 진행중 의뢰 갯수, [7] 진행중 의뢰 총 갯수 [8] 진행중의뢰 총갯수 - 진행중 의뢰 갯수
        maul_nida_ = False
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\maul\\maul_nida.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(200, 70, 400, 130, cla, img)
        if imgs_ is not None:
            maul_nida_ = True
        if maul == '미드가르드':  # 마나하임은 미드가르드..
            print("미드가르등 마을 의뢰 전 다른 마을 클리어 하기")
            if maul_nida_ == True:
                print("니다")
                click_pos_2(330, 105, cla)
                time.sleep(1)
                maul_mission_give_up(cla)

            print("요툰하임")
            click_pos_2(200, 105, cla)
            time.sleep(1)
            maul_mission_give_up(cla)

        if maul == '요툰하임':  # 요툰..
            print("요툰하임 마을 의뢰 전 다른 마을 클리어 하기")

            if maul_nida_ == True:
                print("니다")
                click_pos_2(330, 105, cla)
                time.sleep(1)
                maul_mission_give_up(cla)

            print("미드가르드")
            click_pos_2(70, 105, cla)
            time.sleep(1)
            maul_mission_give_up(cla)




        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\maul.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(30, 30, 160, 80, cla, img)
        if imgs_ is not None:
            click_pos_2(920, 65, cla)

        # 현재 퀘스트 중이면 그대로 진행하도록...체크...
        isQuest = False
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\auto_quest.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(860, 860, 930, 910, cla, img)
        if imgs_ is None or imgs_ == False:
            print("quest 안보여(maul_mission)")
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\auto_quest_1.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(860, 860, 930, 910, cla, img)
            if imgs_ is None or imgs_ == False:
                print("quest 안보여2(maul_mission)")
            else:
                isQuest = True
                print("quest 보여2(maul_mission) : 마을퀘스트 연속해서 진행중")
        else:
            isQuest = True
            print("quest 보여(maul_mission) : 마을퀘스트 연속해서 진행중")

        if isQuest == False:
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\maul.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(30, 30, 160, 80, cla, img)
            if imgs_ is None or imgs_ == False:
                print("마을이 없다...")
                ismenu = False
                while ismenu is False:
                    result_ = menuOpenCheck(cla, "maul_mission_middle")
                    time.sleep(random_int())
                    if result_ == True:
                        ismenu = True
                        click_pos_2(860, 220, cla)
                        time.sleep(random_int())
                    else:
                        click_pos_2(920, 65, cla)
                        time.sleep(random_int())

            else:
                print("마을", imgs_)

            time.sleep(1)
            # 의뢰할 마을 선택하기
            if maul == '미드가르드':  # 마나하임은 미드가르드..
                click_pos_2(70, 105, cla)
                print("미드가르등")
            if maul == '요툰하임':  # 요툰..
                click_pos_2(200, 105, cla)
                print("요퉁")

            print("??????????????????")

            result_cou_ = maul_cou_(cla)
            print('result_cou_[0]', result_cou_[0])
            print('result_cou_[1]', result_cou_[1])
            print('result_cou_[2]', result_cou_[2])
            print('result_cou_[3]', result_cou_[3])
            print('result_cou_[4]', result_cou_[4])
            print('result_cou_[5]', result_cou_[5])
            print('result_cou_[6]', result_cou_[6])
            print('result_cou_[7]', result_cou_[7])
            print('result_cou_[8]', result_cou_[8])
            # [0]수락 및 완료, [1]총갯수, [2]총갯수 - 수락 및 완료, [3]완료 글자 갯수, [4]수락함 글자 갯수, [5]완료 글자 + 수락함 글자 갯수
            # [6] 진행중 의뢰 갯수, [7] 진행중 의뢰 총 갯수 [8] 진행중의뢰 총갯수 - 진행중 의뢰 갯수
            if result_cou_[2] != 0:

                if result_cou_[3] == 0 and result_cou_[4] == 0:
                    print("result_cou_[2] != 0, result_cou_[3] == 0 and result_cou_[4] == 0")
                    # 미션추가 및 실행
                    maul_mission_add(cla, maul)
                # [0]수락 및 완료, [1]총갯수, [2]총갯수 - 수락 및 완료, [3]완료 글자 갯수, [4]수락함 글자 갯수, [5]완료 글자 + 수락함 글자 갯수
                # [6] 진행중 의뢰 갯수, [7] 진행중 의뢰 총 갯수 [8] 진행중의뢰 총갯수 - 진행중 의뢰 갯수
                # elif result_cou_[4] > 0 and result_cou_[3] == 0:

                # [0]수락 및 완료, [1]총갯수, [2]총갯수 - 수락 및 완료, [3]완료 글자 갯수, [4]수락함 글자 갯수, [5]완료 글자 + 수락함 글자 갯수
                # [6] 진행중 의뢰 갯수, [7] 진행중 의뢰 총 갯수 [8] 진행중의뢰 총갯수 - 진행중 의뢰 갯수
                elif result_cou_[3] > 0 and result_cou_[4] == 0:
                    print("result_cou_[2] != 0, result_cou_[3] > 0 and result_cou_[4] == 0")
                    print("보상받고 미션추가 후 미션 시작")
                    # 미션 완료된거인지 파악하기기
                    isMission_ = False
                    while isMission_ is False:
                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\maul_complete_get.png"  # '완료' 글자 클릭 후 보상 받기 버튼...
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(230, 120, 320, 600, cla, img)
                        # imgs_ = pyautogui.locateCenterOnScreen(img, region=(230 + plus, 120, 90 + plus, 480),
                        #                                        confidence=0.7)
                        # imgs_ = pyautogui.locateCenterOnScreen(img, region=(230 + plus, 120, 320 + plus, 600),
                        #                                        confidence=0.7)

                        if imgs_ is None or imgs_ == False:
                            print("마을 외뢰 완료가 없다.", cla)

                            compl_ = maul_mission_complete(cla)

                            if compl_ == False:
                                # 한번 더 체크
                                print("완료 안보영")
                                result_cou_ = maul_cou_(cla)
                                if result_cou_[2] > 0:
                                    maul_mission_add(cla, maul)
                                isMission_ = True
                            else:
                                print("마을 외뢰 완료가 있다_2", cla)
                                time.sleep(1)
                                maul_mission_complete_get(cla, 'elif result_cou_[3] > 0 and result_cou_[4] == 0:')
                                isGetMaul = False
                                thisCounter_ = 0
                                while isGetMaul is False:
                                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\maul.png"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set(30, 30, 160, 80, cla, img)
                                    if imgs_ is not None:
                                        isGetMaul = True
                                        print("계속 진행")
                                    else:
                                        print("아직 보상 수령중")
                                        time.sleep(0.5)
                                        thisCounter_ += 1
                                        if thisCounter_ > 15:
                                            go_maul_(cla)
                        else:
                            print("마을 외뢰 완료가 있다.", cla)
                            time.sleep(1)
                            maul_mission_complete_get(cla, 'elif result_cou_[3] > 0 and result_cou_[4] == 0:')
                            isGetMaul = False
                            thisCounter_ = 0
                            while isGetMaul is False:
                                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\maul.png"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set(30, 30, 160, 80, cla, img)
                                if imgs_ is not None:
                                    isGetMaul = True
                                    print("계속 진행")
                                else:
                                    print("아직 보상 수령중")
                                    time.sleep(0.5)
                                    thisCounter_ += 1
                                    if thisCounter_ > 15:
                                        go_maul_(cla)
                # [0]수락 및 완료, [1]총갯수, [2]총갯수 - 수락 및 완료, [3]완료 글자 갯수, [4]수락함 글자 갯수, [5]완료 글자 + 수락함 글자 갯수
                # [6] 진행중 의뢰 갯수, [7] 진행중 의뢰 총 갯수 [8] 진행중의뢰 총갯수 - 진행중 의뢰 갯수
                elif result_cou_[4] > 0:
                    print("result_cou_[2] != 0, result_cou_[4] > 0", cla)
                    maul_mission_start(cla)
                elif 0 < result_cou_[2] <= 2:
                    print("result_cou_[2] != 0, 0 < result_cou_[2] <= 2", cla)
                    maul_mission_add(cla, maul)
            # [0]수락 및 완료, [1]총갯수, [2]총갯수 - 수락 및 완료, [3]완료 글자 갯수, [4]수락함 글자 갯수, [5]완료 글자 + 수락함 글자 갯수
            # [6] 진행중 의뢰 갯수, [7] 진행중 의뢰 총 갯수 [8] 진행중의뢰 총갯수 - 진행중 의뢰 갯수
            else:
                if result_cou_[4] > 0:
                    print("result_cou_[2] == 0, result_cou_[4] > 0", cla)
                    maul_mission_start(cla)
                # [0]수락 및 완료, [1]총갯수, [2]총갯수 - 수락 및 완료, [3]완료 글자 갯수, [4]수락함 글자 갯수, [5]완료 글자 + 수락함 글자 갯수
                # [6] 진행중 의뢰 갯수, [7] 진행중 의뢰 총 갯수 [8] 진행중의뢰 총갯수 - 진행중 의뢰 갯수
                elif result_cou_[3] > 0 and result_cou_[4] == 0:
                    print("보상받고 미션끝", cla)
                    isMission_ = False

                    while isMission_ is False:
                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\maul_complete_get.png"  # '완료' 글자 클릭 후 보상 받기 버튼...
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(230, 120, 320, 600, cla, img)
                        # imgs_ = pyautogui.locateCenterOnScreen(img, region=(230 + plus, 120, 90 + plus, 480),
                        #                                        confidence=0.7)
                        # imgs_ = pyautogui.locateCenterOnScreen(img, region=(230 + plus, 120, 320 + plus, 600),
                        #                                        confidence=0.7)

                        if imgs_ is None or imgs_ == False:
                            print("마을 외뢰 완료가 없땅.", cla)
                            if cla == 'one':
                                v_.one_cla_ing = 'check'
                            if cla == 'two':
                                v_.two_cla_ing = 'check'
                            the_end_maul = True
                            isMission_ = True
                            click_pos_2(920, 65, cla)
                            time.sleep(random_int())
                        else:
                            print("마을 외뢰 완료가 있땅.", cla)
                            maul_mission_complete_get(cla, 'elif result_cou_[3] > 0 and result_cou_[4] == 0:')
                            time.sleep(random_int())
                elif result_cou_[3] == 0 and result_cou_[4] == 0 and result_cou_[2] == 0:
                    print("미션완료", cla)
                    the_end_maul = True
                    time.sleep(random_int())

        if the_end_maul == True:
            if cla == 'one':
                v_.one_cla_ing = 'check'
            if cla == 'two':
                v_.two_cla_ing = 'check'
            click_pos_2(920, 65, cla)
        time.sleep(random_int())

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\maul.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(30, 40, 100, 75, cla, img)
        if imgs_ is None or imgs_ == False:
            print("마을이 없다...", cla)

        else:
            print("마을이 있다...", cla)
            click_pos_2(920, 65, cla)
            time.sleep(random_int())


        print("maul_mission_result", the_end_maul)
        return the_end_maul
    except Exception as e:
        print(e)
        return 0