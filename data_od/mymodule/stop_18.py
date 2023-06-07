import pytesseract
import pyautogui
import sys
sys.path.append('C:/my_games/coobcco2/data_od/mymodule')



def is_stop(cla):
    from action import go_mynumber_, go_bag
    from chango import go_chango, chango_, auction
    from myfunction import imgs_set, click_pos_2, text_check_get, text_check_get_2, text_check_get_3, text_check_get_4, imgs_set_, click_pos_reg
    from event_get import game_event_get_ready, game_event_get, go_item_open, go_ticket_open
    import numpy as np
    from schedule import myQuest_number_check
    import cv2
    import time
    print("is_stop_check...181818", cla)

    cla = "one"

    if cla == 'one':
        plus = 0
    if cla == 'two':
        plus = 960


    # stop_18181818 = False
    # stop_count = 0
    # while stop_18181818 is False:
    #     stop_count += 1
    #     if stop_count > 10:
    #         stop_18181818 = True
    #     full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\stop\\stop_view.PNG"
    #     img_array = np.fromfile(full_path, np.uint8)
    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #     imgs_ = imgs_set(60, 500, 400, 900, cla, img)
    #     if imgs_ is not None and imgs_ != False:
    #         print("stop_view", imgs_)
    #         click_pos_reg(imgs_.x, imgs_.y, cla)
    #         stop_18181818 = True
    #     else:
    #         print("stop_view 없")
    #     time.sleep(0.3)


