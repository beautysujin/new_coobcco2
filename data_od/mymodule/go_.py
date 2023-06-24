import pytesseract
import pyautogui
import sys
sys.path.append('C:/my_games/coobcco2/data_od/mymodule')

import variable as v_


def go_test(cla):
    from action import go_mynumber_, go_bag, go_potion_off, go_quickslot, go_soongan_f5
    from chango import go_chango, chango_, auction
    from myfunction import imgs_set, click_pos_2, text_check_get, text_check_get_2, text_check_get_3, text_check_get_4, imgs_set_, click_pos_reg, menuOpen, myPotion_check, go_to_home, potion_count, drag_pos, get_region, image_processing, int_put_
    from event_get import game_event_get_ready, game_event_get, go_item_open, go_ticket_open, go_get_open
    import numpy as np
    from schedule import myQuest_number_check, start_id_search, myQuest_play_check
    from stop_18 import is_stop
    from dungeon import jadong_cla_play
    import cv2
    import os
    import time
    import re
    from login_start import get_cla_count, characterChange
    from dungeon import dunjeon_cla_ready
    import git
    from dungeon_su import dunjeon_cla_play_su

    v_.global_howcla = "onecla"

    cla = "one"

    if cla == 'one':
        plus = 0
    if cla == 'two':
        plus = 960

    jadong_cla_play(cla, "살얼음언덕")

    # full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\world_nida.png"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set(400, 965, 580, 1010, cla, img)
    # if imgs_ is None or imgs_ == False:
    #     print("니다벨리르가 안보여")
    # else:
    #     print("보여")

    # get_cla_count(cla)

    #dunjeon_cla_ready(cla, "gonghu")
    #menuOpen(cla)

    # myPotion_check("jadong", cla)
    # go_to_home("start", cla)

    # print("aaaaaaaaaaaaaaaaaaaaa")
    #
    #
    #
    # # 수령 다 받을때까지 WHILE  반복
    #
    # dun = "공허_3"
    #
    # dunjeon_spl_ = dun.split("_")
    # print("dunjeon_spl_[0]", dunjeon_spl_[0])
    # print("dunjeon_spl_[1]", dunjeon_spl_[1])



    # dunjeon_cla_play_su(cla, dunjeon_spl_[0], dunjeon_spl_[1])

    # if dun_where == "공허":
    #     imgs_ = imgs_set_(80, 645, 200, 685, cla, img, 0.88)
    # if dun_where == "난쟁이":
    #     imgs_ = imgs_set_(410, 645, 510, 685, cla, img, 0.88)
    # if dun_where == "지하감옥":
    #     imgs_ = imgs_set_(730, 645, 830, 685, cla, img, 0.88)



















        #     # # 카드 있는지 파악 후 있다면 카드 클릭
        #     # for i in range(5):
        #     #     full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\quest\\card.PNG"
        #     #     img_array = np.fromfile(full_path, np.uint8)
        #     #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     #     imgs_ = imgs_set_(300, 550, 680, 680, cla, img, 0.85)
        #     #     if imgs_ is not None and imgs_ != False:
        #     #         print("card", imgs_)
        #     #         click_pos_2(540, 620, cla)
        #     #         break
        #     #     else:
        #     #         print("카드 없다...")
        #     #     time.sleep(1)
        #
        #     # 카드 있는지 파악 후 있다면 카드 클릭_2
        #     card_search_ = False
        #     card_search_count = 0
        #     while card_search_ is False:
        #         card_search_count += 1
        #         if card_search_count > 10:
        #             card_search_ = True
        #
        #         full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\quest\\card.PNG"
        #         img_array = np.fromfile(full_path, np.uint8)
        #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #         imgs_ = imgs_set_(300, 550, 680, 680, cla, img, 0.85)
        #         if imgs_ is not None and imgs_ != False:
        #             print("card", imgs_)
        #             click_pos_2(540, 620, cla)
        #             card_search_ = True
        #
        #             # 카드 수령 마무리 단계
        #             card_search_2 = False
        #             card_search_count2 = 0
        #             while card_search_2 is False:
        #                 card_search_count2 += 1
        #                 if card_search_count2 > 10:
        #                     card_search_2 = True
        #
        #                 full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\quest\\card.PNG"
        #                 img_array = np.fromfile(full_path, np.uint8)
        #                 img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #                 imgs_ = imgs_set_(300, 550, 680, 680, cla, img, 0.85)
        #                 if imgs_ is not None and imgs_ != False:
        #                     print("카드 아직 있다.")
        #                 else:
        #                     card_search_2 = True
        #                     #절대값 REG, 1,2클라 적용 POS_2
        #                     click_pos_2(550, 930, cla)
        #                     print("카드 없다...")
        #                 time.sleep(1)
        #
        #         else:
        #             print("카드 없다...")
        #         time.sleep(1)
        #
        # else:
        #     print("complete_1 없")
        #     a = True
        # time.sleep(3)
    # go_soongan_f5(cla)

    # go_get_open(cla)


    # potion_count_ = text_check_get_3(865, 825, 945, 850, 3, cla)
    # print("potion_count_", potion_count_)
    #
    # img = pyautogui.screenshot(region=(get_region(865, 825, 945, 850, cla)))
    # white_img = image_processing(img, (148, 148, 148), (255, 255, 255))
    # potion_count_ = pytesseract.image_to_string(white_img, lang=None)
    # print("good", potion_count_)

    # bom_wind = text_check_get(670, 397, 715, 415, cla)
    # print("bom_wind", bom_wind)
    #
    # full_path = "c:\\my_games\\coobcco2\\data_od\\item\\six\\sold_out.png"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(380, 560, 460, 640, cla, img, 0.85)
    # if imgs_ is not None and imgs_ != False:
    #     print("sold_out", imgs_)
    # else:
    #     print("sold_out 없")
    #
    # full_path = "c:\\my_games\\coobcco2\\data_od\\item\\six\\sold_out.png"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(530, 560, 610, 640, cla, img, 0.85)
    # if imgs_ is not None and imgs_ != False:
    #     print("sold_out", imgs_)
    # else:
    #     print("sold_out 없")
    #
    # full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\event_complete.png"  # '완료' 그림 갯수 파악
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(0, 0, 900, 900, cla, img, 0.85)
    # if imgs_ is not None and imgs_ != False:
    #     print("event_complete", imgs_)
    #
    #
    # full_path = "c:\\my_games\\coobcco2\\data_od\\item\\six\\complete_1.png"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(300, 530, 380, 600, cla, img, 0.9)
    # if imgs_ is not None and imgs_ != False:
    #     print("complete_1", imgs_)
    #
    # full_path = "c:\\my_games\\coobcco2\\data_od\\item\\55\\zero.png"  # zero 파악
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(230, 380, 275, 435, cla, img, 0.9)
    # if imgs_ is not None and imgs_ != False:
    #     print("zero1", imgs_)
    # else:
    #     full_path = "c:\\my_games\\coobcco2\\data_od\\item\\55\\zero.png"  # zero 파악
    #     img_array = np.fromfile(full_path, np.uint8)
    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #     imgs_ = imgs_set_(230, 380, 380, 435, cla, img, 0.9)
    #     if imgs_ is not None and imgs_ != False:
    #         print("zero2", imgs_)
    #
    # full_path = "c:\\my_games\\coobcco2\\data_od\\item\\six\\black_six_check.png"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(220, 570, 320, 600, cla, img, 0.9)
    # if imgs_ is not None and imgs_ != False:
    #     print("black_six_check_event1", imgs_)
    # else:
    #     print("1 없")
    #
    # full_path = "c:\\my_games\\coobcco2\\data_od\\item\\six\\black_six_check.png"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(490, 570, 590, 600, cla, img, 0.9)
    # if imgs_ is not None and imgs_ != False:
    #     print("black_six_check_event2", imgs_)
    # else:
    #     print("2 없")
    #
    # full_path = "c:\\my_games\\coobcco2\\data_od\\item\\six\\black_six_check.png"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(220, 630, 320, 660, cla, img, 0.9)
    # if imgs_ is not None and imgs_ != False:
    #     print("black_six_check_event3", imgs_)
    # else:
    #     print("3 없")
    #
    # full_path = "c:\\my_games\\coobcco2\\data_od\\item\\six\\yellow_six_check.png"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(220, 570, 320, 600, cla, img, 0.9)
    # if imgs_ is not None and imgs_ != False:
    #     print("black_six_check_event1", imgs_)
    # else:
    #     print("11 없")
    #
    # full_path = "c:\\my_games\\coobcco2\\data_od\\item\\six\\yellow_six_check.png"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(490, 570, 590, 600, cla, img, 0.9)
    # if imgs_ is not None and imgs_ != False:
    #     print("black_six_check_event2", imgs_)
    # else:
    #     print("22 없")
    #
    # full_path = "c:\\my_games\\coobcco2\\data_od\\item\\six\\yellow_six_check.png"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(220, 630, 320, 660, cla, img, 0.9)
    # if imgs_ is not None and imgs_ != False:
    #     print("black_six_check_event3", imgs_)
    # else:
    #     print("33 없")
