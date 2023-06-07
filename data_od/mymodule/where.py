# import numpy as np
# import cv2
import time

import sys
sys.path.append('C:/my_games/coobcco2/data_od/mymodule')

# from myfunction import *

def go_test(cla):
    print('hi test! where', cla)

def go_somopoom(cla):
    try:
        import numpy as np
        import cv2
        from myfunction import imgs_set, text_check_get
        go_ = False
        somopoom = False

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\somopoom.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(30, 30, 170, 80, cla, img)

        if imgs_ is None or imgs_ == False:
            print("def go_somopoom(cla): 소모품 상점이 안보여", cla)
            itemed_ = text_check_get(48, 42, 150, 68, cla)
            item_ = itemed_.split("\n")
            itemed_2 = text_check_get(807, 994, 896, 1020, cla)
            item_2 = itemed_2.split("\n")
            if len(item_) != 0:
                print("item_", item_[0])
                for list in item_[0]:
                    try:
                        if list == '소' or list == '모' or list == '품' or list == '상' or list == '점':
                            somopoom = True
                    except:
                        pass
            if len(item_2) != 0:
                print("item_2", item_2[0])
                for list in item_2[0]:
                    try:
                        if list == '전' or list == '리' or list == '품' or list == '정' or list == '리':
                            somopoom = True
                    except:
                        pass
            print('소모품? ', item_)
            print('전리품? ', item_2)
            if len(item_) == 0:
                itemed_ = text_check_get(103, 42, 150, 73, cla)
                item_ = itemed_.split("\n")
                if len(item_) >= 1:
                    item = item_[0]
                    if item == '상점' or somopoom == True:
                        print("ok", item)
        else:
            print("def go_somopoom(cla): 소모품 상점이 보여", cla)
            go_ = True

        if somopoom == True:
            go_ = True

        return go_
    except Exception as e:
        print(e)
        return 0


def go_maul_(cla):
    try:
        import numpy as np
        import cv2
        from myfunction import imgs_set, menuOpenCheck, random_int, click_pos_2
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
                    click_pos_2(920, 55, cla)
                    time.sleep(random_int())

    except Exception as e:
        print(e)
        return 0

def go_tuto_bool(cla):
    try:
        import numpy as np
        import cv2
        from myfunction import imgs_set
        go_ = False

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\event1.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(600, 30, 800, 90, cla, img)
        if imgs_ is None or imgs_ == False:
            print("event1 안보여")
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\mybag_1.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(600, 30, 950, 90, cla, img)
            if imgs_ is None or imgs_ == False:
                print("mybag_1 안안보여")
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\mybag_2.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(600, 30, 950, 90, cla, img)
                if imgs_ is None or imgs_ == False:
                    print("mybag_2 안안보여")
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\mybag_3.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(600, 30, 950, 90, cla, img)
                    if imgs_ is None or imgs_ == False:
                        print("mybag_3 안안보여...tuto일수도 있음.")

                    else:
                        print("mybag_3 보여", imgs_)
                        go_ = True
                else:
                    print("mybag_2 보여", imgs_)
                    go_ = True
            else:
                print("mybag_1 보여", imgs_)
                go_ = True
        else:
            print("event1 보여", imgs_)
            go_ = True



        return go_
    except Exception as e:
        print(e)
        return 0



def go_worldmap(cla, data):
    try:
        import numpy as np
        import cv2
        from myfunction import imgs_set
        go_ = False

        if data == "world":
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\worldmap.png"
        elif data == "world_moglog":
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\worldmap_moglog.png"
        elif data == "maul":
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\midgrd.png"
        elif data == "world_yotoon":
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\world_yotoon.png"

        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        if data == "world":
            imgs_ = imgs_set(40, 940, 115, 970, cla, img)
        elif data == "world_moglog":
            imgs_ = imgs_set(135, 90, 230, 125, cla, img)
        elif data == "maul":
            imgs_ = imgs_set(100, 530, 230, 570, cla, img)
        elif data == "world_yotoon":
            imgs_ = imgs_set(400, 960, 530, 1010, cla, img)

        if imgs_ is None or imgs_ == False:
            if data == "world":
                print("월드보기가 안보여")
            elif data == "world_moglog":
                print("월드맵 목록이 안보여")
            elif data == "maul":
                print("미드가르드가 안보여")
            elif data == "maul":
                print("월드맵 하단에 요툰하임이 안보여")

        else:
            go_ = True
            if data == "world":
                print("월드보기가 보여")
            elif data == "world_moglog":
                print("월드맵 목록이 보여")
            elif data == "maul":
                print("미드가르드가 보여")
            elif data == "maul":
                print("월드맵 하단에 요툰하임이 보여")

        return go_
    except Exception as e:
        print(e)
        return 0






