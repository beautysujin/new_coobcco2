# import random
# import pyautogui
# import pytesseract
# import numpy as np
# import numpy
# from PIL import Image
# import re
# import cv2
import time
import sys
sys.path.append('C:/my_games/coobcco2/data_od/mymodule')

import variable as v_

def go_test(cla):
    print('hi test!', cla)

def get_region(start_x, start_y, end_x, end_y, cla):
    coordinate = 0
    if cla == 'one':
        coordinate = 0
    if cla == 'two':
        coordinate = 960


    # pyautogui.moveTo(pos_1 + random_int() + coordinate, pos_2 + random_int(), abc)

    value = (start_x + random_int() + coordinate, start_y, end_x - start_x + random_int() + coordinate, end_y - start_y)
    return value

# 이미지 특정 색상 제외함
def image_processing(src, min_color, max_color):
    import cv2
    import numpy
    img_ = cv2.cvtColor(numpy.array(src), cv2.COLOR_RGB2BGR)
    exception_img = cv2.inRange(img_, min_color, max_color)
    return exception_img

def random_int():
    try:
        import random
        result = random.randint(1, 4)
        return result
    except Exception as e:
        print(e)

def random_int_2():
    try:
        import random
        result = random.randint(100, 200)
        return result
    except Exception as e:
        print(e)

def isNumber_(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def int_put_(data):
    try:
        import re
        data_ = data.replace(',', '').strip()
        data_2 = data_.replace('.', '').strip()
        data_3 = data_2.replace(' ', '').strip()
        data_4 = data_3.replace('/', '').strip()

        # data_2 = data_.strip().replace('.', '')
        # data_3 = data_2.strip().replace(' ', '')
        # data_4 = data_3.strip().replace('/', '')
        result = re.sub(r'[^0-9]', '', data_4)
        return result
    except ValueError:
        return False

def imgs_set(a, b, c, d, cla, img):
    try:
        import pyautogui
        if cla == 'one':
            plus = 0
        if cla == 'two':
            plus = 960
        result = pyautogui.locateCenterOnScreen(img, region=(a + plus, b, c - a + 10 , d - b + 10),
                                               confidence=0.7)
        return result
    except ValueError:
        return False

def imgs_set_(a, b, c, d, cla, img, data):
    try:
        import pyautogui
        if cla == 'one':
            plus = 0
        if cla == 'two':
            plus = 960
        result = pyautogui.locateCenterOnScreen(img, region=(a + plus, b, c - a + 10 , d - b + 10),
                                               confidence=data)
        return result
    except ValueError:
        return False


def click_with_image(image_path):
    try:
        import pyautogui
        isClick = False
        while isClick is False:
            location = pyautogui.locateOnScreen(image_path)
            if location is not None:
                pyautogui.click(location)
                isClick = True
    except Exception as e:
        print(e)


def click_pos(pos):
    try:
        import pyautogui
        pyautogui.moveTo(pos[0] + random_int(), pos[1] + random_int())
        time.sleep(random_int())
        pyautogui.click()
    except Exception as e:
        print(e)


def click_pos_2(pos_1, pos_2, cla):
    try:
        import pyautogui
        coordinate = 0
        if cla == 'one':
            coordinate = 0
        if cla == 'two':
            coordinate = 960

        xy_ = pyautogui.position()

        k_ = random_int()
        if k_ == 1 or k_ ==2:
            x_ = xy_[0] + random_int_2()
        if k_ == 3 or k_ == 4:
            x_ = -xy_[0] - random_int_2()
            if x_ < 0:
                x_ = 0
        k_ = random_int()
        if k_ == 1 or k_ ==2:
            abc = 0.3
            y_ = xy_[1] + random_int_2()
        if k_ == 3 or k_ == 4:
            abc = 0.4
            y_ = -xy_[1] - random_int_2()
            if y_ < 0:
                y_ = 0

        pyautogui.moveTo(pos_1 + random_int() + coordinate, pos_2 + random_int())
        # time.sleep(0.2)
        # pyautogui.click()
        pyautogui.click(pos_1 + random_int() + coordinate, pos_2 + random_int())
        time.sleep(0.5)
    except Exception as e:
        print(e)

def click_pos_reg(pos_1, pos_2, cla):
    try:
        import pyautogui
        coordinate = 0
        if cla == 'one':
            coordinate = 0
        if cla == 'two':
            coordinate = 0

        xy_ = pyautogui.position()

        k_ = random_int()
        if k_ == 1 or k_ ==2:
            x_ = xy_[0] + random_int_2()
        if k_ == 3 or k_ == 4:
            x_ = -xy_[0] - random_int_2()
            if x_ < 0:
                x_ = 0
        k_ = random_int()
        if k_ == 1 or k_ ==2:
            abc = 0.3
            y_ = xy_[1] + random_int_2()
        if k_ == 3 or k_ == 4:
            abc = 0.4
            y_ = -xy_[1] - random_int_2()
            if y_ < 0:
                y_ = 0

        pyautogui.moveTo(pos_1 + random_int() + coordinate, pos_2 + random_int())

        pyautogui.click(pos_1 + random_int() + coordinate, pos_2 + random_int())
        time.sleep(0.5)
        # pyautogui.click()
    except Exception as e:
        print(e)


def drag_pos(pos_1, pos_2, pos_3, pos_4, cla):
    try:
        import pyautogui
        coordinate = 0
        if cla == 'one':
            coordinate = 0
        if cla == 'two':
            coordinate = 960
        pyautogui.moveTo(pos_1 + random_int() + coordinate, pos_2 + random_int(), 0.5)
        pyautogui.dragTo(pos_3 + random_int() + coordinate, pos_4 + random_int(), 1)
        time.sleep(0.3)
    except Exception as e:
        print(e)


# def text_check(posX1, posY1, posX2, posY2, text, method, method_pos):
#     try:
#         isClick = False
#         pos = (posX1, posY1, posX2 - posX1, posY2 - posY1)
#         while isClick is False:
#             pic = pyautogui.screenshot("asd.png", region=pos)
#             pic_ = numpy.array(pic)
#             # result = reader.readtext(pic_)
#             for txt in result:
#                 if txt is not None:
#                     print(txt[1])
#                     for text_ in text:
#                         if txt[1] == text_:
#                             print("aaa!!")
#                             method(method_pos)
#                             isClick = True
#     except Exception as e:
#         print(e)

def text_check_get(posX1, posY1, posX2, posY2, cla):
    try:
        import cv2
        import pytesseract
        import numpy
        import pyautogui
        coordinate = 0
        if cla == 'one':
            coordinate = 0
        if cla == 'two':
            coordinate = 960
        pos = (posX1 + coordinate, posY1, posX2 - posX1, posY2 - posY1)
        pyautogui.screenshot("asd.png", region=pos)
        pic = cv2.imread("asd.png", cv2.IMREAD_COLOR)  # 사진을 컬러로 읽어오기
        cv2.imwrite("asd.png", pic)
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        pic_ = numpy.array(pic)
        result = pytesseract.image_to_string(pic_, lang='kor+eng')

        ##
        return result
    except Exception as e:
        print(e)
        return 0

def text_check_get_2(posX1, posY1, posX2, posY2, cla):
    try:
        import cv2
        import pytesseract
        import numpy
        import pyautogui
        coordinate = 0
        if cla == 'one':
            coordinate = 0
        if cla == 'two':
            coordinate = 960
        isClick = False
        pos = (posX1 + coordinate, posY1, posX2 - posX1, posY2 - posY1)
        pyautogui.screenshot("asd.png", region=pos)
        pic = cv2.imread("asd.png", cv2.IMREAD_COLOR)  # 사진을 컬러로 읽어오기
        cv2.imwrite("asd.png", pic)
        ##
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        # path = Image.open(r'asd.png')
        pic_ = numpy.array(pic)
        rgb_image = cv2.cvtColor(pic_, cv2.COLOR_BGR2RGB)
        result = pytesseract.image_to_string(rgb_image, lang='kor+eng')

        ##
        return result
    except Exception as e:
        print(e)
        return 0

def text_check_get_3(posX1, posY1, posX2, posY2, color, cla):
    try:
        import cv2
        import pytesseract
        import numpy
        from PIL import Image
        import pyautogui
        # color change
        coordinate = 0
        if cla == 'one':
            coordinate = 0
        if cla == 'two':
            coordinate = 960
        pos = (posX1 + coordinate, posY1, posX2 - posX1, posY2 - posY1)
        pyautogui.screenshot("asd.png", region=pos)
        pic = cv2.imread("asd.png", cv2.IMREAD_COLOR)  # 사진을 컬러로 읽어오기
        cv2.imwrite("asd.png", pic)
        ##
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        path = Image.open(r'asd.png')
        pic_ = numpy.array(pic)
        if color == 0:
            rgb_image = cv2.cvtColor(pic_, cv2.COLOR_BGR2RGB)
        if color == 1:
            rgb_image = cv2.cvtColor(pic_, cv2.COLOR_BGR2GRAY)
        if color == 2:
            rgb_image = cv2.cvtColor(pic_, cv2.COLOR_BGR2HSV)
        if color == 3:
            rgb_image = cv2.cvtColor(pic_, cv2.COLOR_BGR2YUV)
        if color == 4:
            rgb_image = cv2.cvtColor(pic_, cv2.COLOR_BGR2RGB)
        if color == 5:
            rgb_image = cv2.cvtColor(pic_, cv2.COLOR_BGR2RGB)
        if color == 6:
            rgb_image = cv2.cvtColor(pic_, cv2.COLOR_BGR2RGB)
        result = pytesseract.image_to_string(rgb_image, lang='kor+eng')

        ##
        return result
    except Exception as e:
        print(e)
        return 0

def text_check_get_4(posX1, posY1, posX2, posY2, color, cla):
    try:
        import numpy as np
        import cv2
        import pytesseract
        import numpy
        import pyautogui
        # color change
        coordinate = 0
        if cla == 'one':
            coordinate = 0
        if cla == 'two':
            coordinate = 960
        pos = (posX1 + coordinate, posY1, posX2 - posX1, posY2 - posY1)
        pyautogui.screenshot("asd.png", region=pos)
        pic = cv2.imread("asd.png")
        cv2.imwrite("asd.png", pic)
        ##
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        # path = Image.open(r'asd.png')
        pic_ = numpy.array(pic)

        rgb_image_ = cv2.cvtColor(pic_, cv2.COLOR_BGR2HSV)

        lower_yellow = np.array([60, 100, 100])
        upper_yellow = np.array([90, 255, 255])

        lower_green = np.array([50, 100, 100])
        upper_green = np.array([70, 255, 255])

        lower_red = np.array([-10, 100, 100])
        upper_red = np.array([10, 255, 255])

        if color == 0:
            rgb_image_ready = cv2.inRange(rgb_image_, lower_yellow, upper_yellow)
            rgb_image = cv2.bitwise_and(pic, pic, mask = rgb_image_ready)
        if color == 1:
            rgb_image_ready = cv2.inRange(rgb_image_, lower_green, upper_green)
            rgb_image = cv2.bitwise_and(pic, pic, mask=rgb_image_ready)
        if color == 2:
            rgb_image_ready = cv2.inRange(rgb_image_, lower_red, upper_red)
            rgb_image = cv2.bitwise_and(pic, pic, mask=rgb_image_ready)
        result = pytesseract.image_to_string(rgb_image, lang='kor+eng')

        cv2.imshow('img_color', pic)

        ##
        return result
    except Exception as e:
        print(e)
        return 0



def menuOpenCheck(cla, story):
    try:
        from clean import lotation_change_ready
        import numpy as np
        import cv2
        from stop_18 import is_stop

        # x 같은 이벤트
        is_stop(cla)

        get_story = str(story) + " => menuOpenCheck"
        lotation_change_ready(cla, get_story)

        ismenu_ = False
        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\pk.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(830, 330, 890, 410, cla, img)
        if imgs_ is None or imgs_ == False:
            print("pk 없..")
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\post_menu.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(645, 500, 710, 570, cla, img)
            if imgs_ is None or imgs_ == False:
                print("post_menu 없..")
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\setting_menu.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(870, 480, 950, 580, cla, img)
                if imgs_ is None or imgs_ == False:
                    print("setting_menu 없..")
                else:
                    print("setting_menu imgs", imgs_)
                    ismenu_ = True
            else:
                print("post_menu imgs", imgs_)
                ismenu_ = True
        else:
            print("pk imgs", imgs_)
            ismenu_ = True



        return ismenu_
    except Exception as e:
        print(e)
        return 0

def menuOpen(cla):
    try:
        from clean import lotation_change_ready, clean_screen
        from massenger import line_to_me
        import numpy as np
        import cv2
        from stop_18 import is_stop

        # x 같은 이벤트
        is_stop(cla)

        is_menu = False
        is_menu_count = 0
        while is_menu is False:
            is_menu_count += 1
            if is_menu_count > 5:
                is_menu = True
                line_to_me(cla, "메뉴 여는데 문제있당")

            result = menuOpenCheck(cla, "menu_open")
            print("result???????????????????", result)
            if result == True:
                is_menu = True
                time.sleep(0.3)
            else:
                clean_screen(cla, "menu_open..")
                time.sleep(1)
                click_pos_2(920, 55, cla)
            time.sleep(1)

    except Exception as e:
        print(e)
        return 0

def go_to_home(data, cla):
    try:
        import re
        from maul import maul_mission_complete, go_maul_bosang, maul_mission
        from chango import in_village_go_to, in_village_go, go_chango
        from action import go_boonhae, go_escape, go_bag
        from where import go_somopoom
        from dungeon import dunjeon_cla_play, jadong_cla_play
        from schedule import myQuest_play_check
        print("def go_to_home(cla): start", data)
        print("소모품 상점 가기전에 분해부터 ㄱㄱ", cla)


        pass_ = True
        isPotionChecked = False

        isGoToHome = False
        gohome_count = 0
        while isGoToHome is False:
            gohome_count += 1
            if gohome_count >= 6:
                isGoToHome = True

            compl_ = maul_mission_complete(cla)
            if compl_ == True:
                print("def go_to_home(data, cla): 완료 보영")
                go_maul_bosang(cla)


            print("어디에서 왔니?", data)
            print("넌 몇클라?", cla)
            this_nida = False
            this_yotoon = False
            this_mana = False
            result_vil = in_village_go(cla)
            if result_vil == 'nida':
                this_nida = True
            else:
                result__ = in_village_go_to(cla)
                if result__ == 'nida':
                    this_nida = True
                if result__ == 'yotoon':
                    this_yotoon = True
                if result__ == 'mana':
                    this_mana = True


            if cla == 'one':
                mypotion_cla = v_.mypotion_1
                mymoney_ = v_.mymoney_1
            if cla == 'two':
                mypotion_cla = v_.mypotion_2
                mymoney_ = v_.mymoney_2
            print("myMoney", mymoney_)


            go_bag(cla, "go_to_home")
            go_boonhae(cla, "go_to_home")

            time.sleep(1)
            click_pos_2(920, 55, cla)
            time.sleep(1)
        ###########################################
            if this_mana == True:
                print("분해 후 이제 소모품 상점으로 가는 길")
                result_go_chango = go_chango(cla, 'village')
                if result_go_chango == False:
                    result_menu = menuOpenCheck(cla, "go_to_home_start")
                    if result_menu == True:
                        click_pos_2(920, 55, cla)
                        time.sleep(1)
                else:
                    isSomopoom = False
                    isSomopoomCount = 0
                    while isSomopoom is False:
                        isSomopoomCount += 1
                        if isSomopoomCount >=20:
                            isSomopoom = True

                        result_somopoom = go_somopoom(cla)
                        print('result_somopoom1 = go_somopoom(cla)', result_somopoom)
                        time.sleep(random_int())
                        if result_somopoom == False:
                            result_go_chango = go_chango(cla, 'village')
                            if result_go_chango == True:

                                click_pos_2(770, 910, cla)
                                if this_yotoon == True:
                                    time.sleep(1)
                                    click_pos_2(810, 980, cla)
                                    time.sleep(1)
                                    click_pos_2(810, 980, cla)
                                time.sleep(10 + random_int())
                                if isSomopoomCount == 12:
                                    isSomopoomCount = 0
                                    go_escape(cla)
                            else:
                                result_menu = menuOpenCheck(cla, "go_to_home_middle1")
                                if result_menu == True:
                                    click_pos_2(920, 55, cla)
                                    time.sleep(1)

                        else:
                            isSomopoom = True
                            print("def go_to_home(data, cla): 소모품 상점 도착")
                            # 물약
                            time.sleep(1)
                            # print("물약")
                            click_pos_2(150, 165, cla)
                            #
                            potioned_ch_ = text_check_get(325, 115, 515, 150, cla)
                            potioned_ch = potioned_ch_.split("\n")
                            pk1 = " ".join(potioned_ch).strip()
                            if len(pk1) != 0:
                                for list in range(len(pk1)):
                                    try:
                                        if pk1[list] == "아" or pk1[list] == '이' or pk1[list] == '템' or pk1[
                                            list] == '최' or \
                                                pk1[
                                                    list] == '대' or pk1[list] == '보':
                                            isPotionChecked = True
                                            print("hahay_as", pk1[list])
                                    except:
                                        pass
                            potioned_ch_ = text_check_get(445, 355, 500, 385, cla)
                            potioned_ch = potioned_ch_.split("\n")
                            pk1 = " ".join(potioned_ch).strip()
                            print("구매? ", pk1)
                            print("구매??", len(pk1))
                            #
                            if pk1 == '구매' or len(pk1) != 0:
                                isPotionChecked = False
                                print('구매시작', pk1)
                            else:
                                time.sleep(random_int())
                                click_pos_2(580, 590, cla)
                                time.sleep(1)
                                click_pos_2(550, 690, cla)
                                time.sleep(1)

                            print("hahay_", isPotionChecked)
                            ##########№#########
                            if isPotionChecked == False and len(pk1) != 0:
                                time.sleep(random_int())
                                item_how_manyed_ = text_check_get(448, 482, 515, 505, cla)
                                item_how_many_ = item_how_manyed_.split("\n")
                                if len(item_how_many_[0]) >= 1:
                                    result_ = re.sub(r'[^0-9]', '', item_how_many_[0])
                                    result_ = int_put_(result_)
                                    list_bool = result_.isdigit()
                                    if list_bool == True:
                                        potionready_ = item_how_many_[0].split("/")
                                        print(potionready_)
                                        potionready_1 = re.sub(r'[^0-9]', '', potionready_[0])
                                        potionready_2 = re.sub(r'[^0-9]', '', potionready_[1])
                                        list_bool1 = potionready_1.isdigit()
                                        list_bool2 = potionready_2.isdigit()
                                        if list_bool1 == True and list_bool2 == True:
                                            if int(potionready_1) == int(potionready_2):
                                                mypotion_cla = int(potionready_2)
                                                print("내 물약 갯수1", potionready_2)
                                                pass_ = True
                                            else:
                                                mypotion_cla = int(potionready_2) - int(potionready_1)
                                                print("내 물약 갯수2", mypotion_cla)
                                                pass_ = False
                                time.sleep(1)
                                click_pos_2(580, 590, cla)
                                time.sleep(1)
                                click_pos_2(550, 690, cla)

                                isGoToHome = True
                            else:
                                isGoToHome = True
                                print('물약꽉찼다')

                            # 순간이동서
                            time.sleep(1)
                            click_pos_2(150, 560, cla)
                            imme_ = False
                            fly_ch_ = text_check_get(340, 125, 515, 150, cla)
                            fly_ch = fly_ch_.split("\n")
                            fly_ch = " ".join(fly_ch)
                            print("fly_ch...", fly_ch)
                            if len(fly_ch) != 0:
                                for list in fly_ch:
                                    try:
                                        if list == "일" or list == '제' or list == '한' or list == '수':
                                            imme_ = True
                                    except:
                                        pass

                            if imme_ != True:

                                time.sleep(1)
                                item_how_manyed_ = text_check_get(448, 484, 490, 500, cla)
                                print("순간 파악", item_how_manyed_)
                                result_ = re.sub(r'[^0-9]', '', item_how_manyed_)
                                print("순간 숫자 파악", result_)
                                result_ = int_put_(result_)
                                print("순간 숫자 파악2", result_)
                                item_how_manyed_bool = result_.isdigit()
                                print("순간 숫자 변환", item_how_manyed_bool)
                                if item_how_manyed_bool == False:
                                    click_pos_2(580, 590, cla)
                                    time.sleep(1)
                                    click_pos_2(550, 690, cla)
                                    time.sleep(1)

                                print('순간이동서', item_how_manyed_)
                                if len(item_how_manyed_) >= 1:
                                    result_ = re.sub(r'[^0-9]', '', item_how_manyed_)
                                    result_ = int_put_(result_)
                                    list_bool = result_.isdigit()
                                    if list_bool == True:
                                        item_how_many = int(result_)
                                        print('순간이동서', item_how_many)
                                        if item_how_many < 50:
                                            click_pos_2(580, 590, cla)
                                            time.sleep(1)
                                            click_pos_2(550, 690, cla)
                                            time.sleep(1)
                                        else:

                                            click_pos_2(550, 690, cla)
                                            time.sleep(1)
                                            # click_pos_2(410, 690, cla)
                                            # time.sleep(1)

                            # if mymoney_ >= 1000000:
                            # 순록 스테이크
                            click_pos_2(150, 240, cla)
                            time.sleep(1)
                            item_how_manyed_ = text_check_get(448, 482, 515, 505, cla)
                            print('순록스테이크', item_how_manyed_)
                            if len(item_how_manyed_) >= 1:
                                result_ = re.sub(r'[^0-9]', '', item_how_manyed_)
                                result_ = int_put_(result_)
                                list_bool = result_.isdigit()
                                if list_bool == True:
                                    item_how_many = int(result_)
                                    print('순록스테이크', item_how_many)
                                    if item_how_many < 50:
                                        click_pos_2(480, 590, cla)
                                        time.sleep(1)
                                        click_pos_2(550, 690, cla)
                                        time.sleep(1)
                                    else:
                                        click_pos_2(410, 690, cla)
                                        time.sleep(1)
                            else:
                                print('순록 수량 파악 못해서 11개 사버리기')
                                click_pos_2(380, 590, cla)
                                time.sleep(1)
                                click_pos_2(550, 690, cla)
                                time.sleep(1)
                            # 벌꿀술
                            click_pos_2(150, 330, cla)
                            time.sleep(1)
                            item_how_manyed_ = text_check_get(448, 482, 515, 505, cla)
                            print('벌꿀술', item_how_manyed_)
                            if len(item_how_manyed_) >= 1:
                                result_ = re.sub(r'[^0-9]', '', item_how_manyed_)
                                result_ = int_put_(result_)
                                list_bool = result_.isdigit()
                                if list_bool == True:
                                    item_how_many = int(result_)
                                    print('벌꿀술', item_how_many)
                                    if item_how_many < 50:
                                        click_pos_2(480, 590, cla)
                                        time.sleep(1)
                                        click_pos_2(550, 690, cla)
                                        time.sleep(1)
                                    else:
                                        click_pos_2(410, 690, cla)
                                        time.sleep(1)
                            else:
                                print('벌꿀 수량 파악 못해서 11개 사버리기')
                                click_pos_2(380, 590, cla)
                                time.sleep(1)
                                click_pos_2(550, 690, cla)
                                time.sleep(1)
                            # 프라낭 연어
                            click_pos_2(150, 410, cla)
                            time.sleep(1)
                            item_how_manyed_ = text_check_get(448, 482, 515, 505, cla)
                            print('프라낭 연어', item_how_manyed_)
                            if len(item_how_manyed_) >= 1:
                                result_ = re.sub(r'[^0-9]', '', item_how_manyed_)
                                result_ = int_put_(result_)
                                list_bool = result_.isdigit()
                                if list_bool == True:
                                    item_how_many = int(result_)
                                    print('프라낭 연어', item_how_many)
                                    if item_how_many < 50:
                                        click_pos_2(480, 590, cla)
                                        time.sleep(1)
                                        click_pos_2(550, 690, cla)
                                        time.sleep(random_int())
                                    else:
                                        click_pos_2(410, 690, cla)
                                        time.sleep(1)
                            else:
                                print('연어 수량 파악 못해서 11개 사버리기')
                                click_pos_2(380, 590, cla)
                                time.sleep(1)
                                click_pos_2(550, 690, cla)
                                time.sleep(1)
                            # 사리풀
                            click_pos_2(150, 480, cla)
                            time.sleep(1)
                            item_how_manyed_ = text_check_get(448, 482, 515, 505, cla)
                            print('사리풀', item_how_manyed_)
                            if len(item_how_manyed_) >= 1:
                                result_ = re.sub(r'[^0-9]', '', item_how_manyed_)
                                result_ = int_put_(result_)
                                list_bool = result_.isdigit()
                                if list_bool == True:
                                    item_how_many = int(result_)
                                    print('사리풀', item_how_many)
                                    if item_how_many < 11:
                                        click_pos_2(380, 590, cla)
                                        time.sleep(1)
                                        click_pos_2(380, 590, cla)
                                        time.sleep(1)
                                        click_pos_2(550, 690, cla)
                                        time.sleep(1)
                                    else:
                                        click_pos_2(410, 690, cla)
                                        time.sleep(1)
                            else:
                                print('사리풀 수량 파악 못해서 11개 사버리기')
                                click_pos_2(380, 590, cla)
                                time.sleep(1)
                                click_pos_2(550, 690, cla)
                                time.sleep(1)

            #if data == 'start':
            elif this_nida == True or this_yotoon == True:
                # 소모품 상점으로 가는 중

                print("분해 후 이제 소모품 상점으로 가는 길")
                result_go_chango = go_chango(cla, 'village')
                if result_go_chango == False:
                    result_menu = menuOpenCheck(cla, "go_to_home_middle2")
                    if result_menu == True:
                        click_pos_2(920, 55, cla)
                        time.sleep(1)
                else:
                    isSomopoom = False
                    isSomopoomCount = 0
                    while isSomopoom is False:
                        result_somopoom = go_somopoom(cla)
                        print('result_somopoom1 = go_somopoom(cla)', result_somopoom)
                        time.sleep(1)
                        if result_somopoom == False:
                            result_go_chango = go_chango(cla, 'village')
                            if result_go_chango == True:
                                isSomopoomCount += 1
                                click_pos_2(770, 910, cla)
                                if this_yotoon == True:
                                    time.sleep(1)
                                    click_pos_2(810, 980, cla)
                                    time.sleep(1)
                                    click_pos_2(810, 980, cla)
                                time.sleep(10 + random_int())
                                if isSomopoomCount == 12 or isSomopoomCount == 24:
                                    isSomopoomCount = 0
                                    go_escape(cla)
                            else:
                                result_menu = menuOpenCheck(cla, "go_to_home_middle3")
                                if result_menu == True:
                                    click_pos_2(920, 55, cla)
                                    time.sleep(1)

                        else:
                            isSomopoom = True
                            print("def go_to_home(data, cla): 소모품 상점 도착")
                            # 물약
                            time.sleep(1)
                            # print("물약")
                            click_pos_2(150, 165, cla)
                            #
                            potioned_ch_ = text_check_get(325, 115, 515, 150, cla)
                            potioned_ch = potioned_ch_.split("\n")
                            pk1 = " ".join(potioned_ch).strip()
                            if len(pk1) != 0:
                                for list in range(len(pk1)):
                                    try:
                                        if pk1[list] == "아" or pk1[list] == '이' or pk1[list] == '템' or pk1[list] == '최' or \
                                                pk1[
                                                    list] == '대' or pk1[list] == '보':
                                            isPotionChecked = True
                                            print("hahay_as", pk1[list])
                                    except:
                                        pass
                            potioned_ch_ = text_check_get(445, 355, 500, 385, cla)
                            potioned_ch = potioned_ch_.split("\n")
                            pk1 = " ".join(potioned_ch).strip()
                            print("pkpk", pk1)
                            print("pkpk2", len(pk1))
                            #
                            if pk1 == '구매' or len(pk1) != 0:
                                isPotionChecked = False
                                print('구매시작', pk1)
                            else:
                                time.sleep(1)
                                click_pos_2(580, 590, cla)
                                time.sleep(1)
                                click_pos_2(550, 690, cla)
                                time.sleep(1)

                            print("hahay_", isPotionChecked)
                            ##########№#########
                            if isPotionChecked == False and len(pk1) != 0:
                                time.sleep(1)
                                item_how_manyed_ = text_check_get(448, 482, 515, 505, cla)
                                item_how_many_ = item_how_manyed_.split("\n")
                                if len(item_how_many_[0]) >= 1:
                                    result_ = re.sub(r'[^0-9]', '', item_how_many_[0])
                                    result_ = int_put_(result_)
                                    list_bool = result_.isdigit()
                                    if list_bool == True:
                                        potionready_ = item_how_many_[0].split("/")
                                        print(potionready_)
                                        potionready_1 = re.sub(r'[^0-9]', '', potionready_[0])
                                        potionready_2 = re.sub(r'[^0-9]', '', potionready_[1])
                                        list_bool1 = potionready_1.isdigit()
                                        list_bool2 = potionready_2.isdigit()
                                        if list_bool1 == True and list_bool2 == True:
                                            if int(potionready_1) == int(potionready_2):
                                                mypotion_cla = int(potionready_2)
                                                print("내 물약 갯수1", potionready_2)
                                                pass_ = True
                                            else:
                                                mypotion_cla = int(potionready_2) - int(potionready_1)
                                                print("내 물약 갯수2", mypotion_cla)
                                                pass_ = False
                                time.sleep(1)
                                click_pos_2(580, 590, cla)
                                time.sleep(1)
                                click_pos_2(550, 690, cla)

                                isGoToHome = True
                            else:
                                isGoToHome = True
                                print('물약꽉찼다')

                            # if pass_ == False:
                            time.sleep(1)
                            click_pos_2(580, 590, cla)
                            time.sleep(1)
                            click_pos_2(550, 690, cla)
                            time.sleep(1)
                            # 순간이동서
                            if this_yotoon == True:
                                click_pos_2(150, 640, cla)
                            if this_nida == True:
                                click_pos_2(150, 640 + 80, cla)
                            imme_ = False
                            fly_ch_ = text_check_get(340, 125, 515, 150, cla)
                            fly_ch = fly_ch_.split("\n")
                            fly_ch = " ".join(fly_ch)
                            print("fly_ch...", fly_ch)
                            if len(fly_ch) != 0:
                                for list in fly_ch:
                                    try:
                                        if list == "일" or list == '제' or list == '한' or list == '수':
                                            imme_ = True
                                    except:
                                        pass

                            if imme_ != True:

                                time.sleep(1)
                                item_how_manyed_ = text_check_get(448, 482, 515, 505, cla)
                                print("순간 파악", item_how_manyed_)
                                result_ = re.sub(r'[^0-9]', '', item_how_manyed_)
                                print("순간 숫자 파악", result_)
                                result_ = int_put_(result_)
                                print("순간 숫자 파악2", result_)
                                item_how_manyed_bool = result_.isdigit()
                                print("순간 숫자 변환", item_how_manyed_bool)
                                if item_how_manyed_bool == False:
                                    click_pos_2(580, 590, cla)
                                    time.sleep(1)
                                    click_pos_2(550, 690, cla)
                                    time.sleep(1)
                                print('순간이동서', item_how_manyed_)
                                if len(item_how_manyed_) >= 1:
                                    result_ = re.sub(r'[^0-9]', '', item_how_manyed_)
                                    result_ = int_put_(result_)
                                    list_bool = result_.isdigit()
                                    if list_bool == True:
                                        item_how_many = int(result_)
                                        print('순간이동서', item_how_many)
                                        if item_how_many < 50:
                                            click_pos_2(580, 590, cla)
                                            time.sleep(1)
                                            click_pos_2(550, 690, cla)
                                            time.sleep(1)
                                        else:
                                            click_pos_2(380, 590, cla)
                                            time.sleep(1)
                                            click_pos_2(380, 590, cla)
                                            time.sleep(1)
                                            click_pos_2(550, 690, cla)
                                            time.sleep(1)
                                            # click_pos_2(410, 690, cla)
                                            # time.sleep(1)

                            # if mymoney_ >= 1000000:
                            # 순록 스테이크
                            if this_yotoon == True:
                                click_pos_2(150, 320, cla)
                            if this_nida == True:
                                click_pos_2(150, 320 + 80, cla)
                            time.sleep(1)
                            item_how_manyed_ = text_check_get(448, 482, 515, 505, cla)
                            print('순록스테이크', item_how_manyed_)
                            if len(item_how_manyed_) >= 1:
                                result_ = re.sub(r'[^0-9]', '', item_how_manyed_)
                                result_ = int_put_(result_)
                                list_bool = result_.isdigit()
                                if list_bool == True:
                                    item_how_many = int(result_)
                                    print('순록스테이크', item_how_many)
                                    if item_how_many < 50:
                                        click_pos_2(480, 590, cla)
                                        time.sleep(1)
                                        click_pos_2(550, 690, cla)
                                        time.sleep(1)
                                    else:
                                        click_pos_2(410, 690, cla)
                                        time.sleep(1)
                            else:
                                print('순록 수량 파악 못해서 101개 사버리기')
                                click_pos_2(480, 590, cla)
                                time.sleep(1)
                                click_pos_2(550, 690, cla)
                                time.sleep(1)
                            # 벌꿀술
                            if this_yotoon == True:
                                click_pos_2(150, 400, cla)
                            if this_nida == True:
                                click_pos_2(150, 400 + 80, cla)
                            time.sleep(1)
                            item_how_manyed_ = text_check_get(448, 482, 515, 505, cla)
                            print('벌꿀술', item_how_manyed_)
                            if len(item_how_manyed_) >= 1:
                                result_ = re.sub(r'[^0-9]', '', item_how_manyed_)
                                result_ = int_put_(result_)
                                list_bool = result_.isdigit()
                                if list_bool == True:
                                    item_how_many = int(result_)
                                    print('벌꿀술', item_how_many)
                                    if item_how_many < 50:
                                        click_pos_2(480, 590, cla)
                                        time.sleep(1)
                                        click_pos_2(550, 690, cla)
                                        time.sleep(1)
                                    else:
                                        click_pos_2(410, 690, cla)
                                        time.sleep(1)
                            else:
                                print('벌꿀 수량 파악 못해서 101개 사버리기')
                                click_pos_2(480, 590, cla)
                                time.sleep(1)
                                click_pos_2(550, 690, cla)
                                time.sleep(1)
                            # 프라낭 연어
                            if this_yotoon == True:
                                click_pos_2(150, 480, cla)
                            if this_nida == True:
                                click_pos_2(150, 480 + 80, cla)
                            time.sleep(1)
                            item_how_manyed_ = text_check_get(448, 482, 515, 505, cla)
                            print('프라낭 연어', item_how_manyed_)
                            if len(item_how_manyed_) >= 1:
                                result_ = re.sub(r'[^0-9]', '', item_how_manyed_)
                                result_ = int_put_(result_)
                                list_bool = result_.isdigit()
                                if list_bool == True:
                                    item_how_many = int(result_)
                                    print('프라낭 연어', item_how_many)
                                    if item_how_many < 50:
                                        click_pos_2(480, 590, cla)
                                        time.sleep(1)
                                        click_pos_2(550, 690, cla)
                                        time.sleep(1)
                                    else:
                                        click_pos_2(410, 690, cla)
                                        time.sleep(1)
                            else:
                                print('연어 수량 파악 못해서 101개 사버리기')
                                click_pos_2(480, 590, cla)
                                time.sleep(random_int())
                                click_pos_2(550, 690, cla)
                                time.sleep(random_int())
                            # 사리풀
                            if this_yotoon == True:
                                click_pos_2(150, 560, cla)
                            if this_nida == True:
                                click_pos_2(150, 560 + 80, cla)
                            time.sleep(1)
                            item_how_manyed_ = text_check_get(448, 482, 515, 505, cla)
                            print('사리풀', item_how_manyed_)
                            if len(item_how_manyed_) >= 1:
                                result_ = re.sub(r'[^0-9]', '', item_how_manyed_)
                                result_ = int_put_(result_)
                                list_bool = result_.isdigit()
                                if list_bool == True:
                                    item_how_many = int(result_)
                                    print('사리풀', item_how_many)
                                    if item_how_many < 50:
                                        click_pos_2(380, 590, cla)
                                        time.sleep(1)
                                        click_pos_2(380, 590, cla)
                                        time.sleep(1)
                                        click_pos_2(380, 590, cla)
                                        time.sleep(1)
                                        click_pos_2(380, 590, cla)
                                        time.sleep(1)
                                        click_pos_2(380, 590, cla)
                                        time.sleep(1)
                                        click_pos_2(550, 690, cla)
                                        time.sleep(1)
                                    else:
                                        click_pos_2(410, 690, cla)
                                        time.sleep(1)
                            else:
                                print('사리풀 수량 파악 못해서 51개 사버리기')
                                click_pos_2(380, 590, cla)
                                time.sleep(1)
                                click_pos_2(380, 590, cla)
                                time.sleep(1)
                                click_pos_2(380, 590, cla)
                                time.sleep(1)
                                click_pos_2(380, 590, cla)
                                time.sleep(1)
                                click_pos_2(380, 590, cla)
                                time.sleep(1)
                                click_pos_2(550, 690, cla)
                                time.sleep(1)
                        # 여긴 아직 while

                            if cla == 'one':
                                v_.mypotion_1 = mypotion_cla
                            if cla == 'two':
                                v_.mypotion_2 = mypotion_cla

                            result_somopoom = go_somopoom(cla)
                            print('result_somopoom2 = go_somopoom(cla)', result_somopoom)
                            time.sleep(1)
                            if result_somopoom == True:
                                click_pos_2(920, 55, cla)
                                time.sleep(1)
                                result_go_chango = go_chango(cla, 'village')
                                if result_go_chango == False:
                                    click_pos_2(920, 55, cla)
                                    time.sleep(1)
                                else:
                                    isGoToHome = True
                                    print("마을화면이라 진행")

                                    if data == 'start':
                                        # 이건 다음에 게임 시작하는 명령어 있을 경우

                                        print("게임 시작 하러 ㄱㄱ : ", data)
                                        # 자동사냥도 여기 포함
            if data == 'start':
                isGoToHome = True
                print("게임 시작 하러 ㄱㄱ : start", data)

            elif data == 'grow':
                isGoToHome = True
                print("게임 시작 하러 ㄱㄱ : grow(cla, data)", data)
                click_pos_2(920, 55, cla)

            elif data == '미드가르드' or data == '요툰하임':
                isGoToHome = True
                print("게임 시작 하러 ㄱㄱ : maul_mission(cla, data)", data)
                maul_mission(cla, data)

            # elif data == 'gonghu':
            #     isGoToHome = True
            #     data_ = "check"
            #     print("게임 시작 하러 ㄱㄱ : dunjeon_cla_play(cla, data_, data)", data)
            #     dunjeon_cla_play(cla, data_, data)
            #
            # elif data == 'nanjang':
            #     isGoToHome = True
            #     data_ = "check"
            #     print("게임 시작 하러 ㄱㄱ : dunjeon_cla_play(cla, data_, data)", data)
            #     dunjeon_cla_play(cla, data_, data)
            # elif data == 'underprison':
            #     isGoToHome = True
            #     data_ = "check"
            #     print("게임 시작 하러 ㄱㄱ : dunjeon_cla_play(cla, data_, data)", data)
            #     dunjeon_cla_play(cla, data_, data)
            elif data == 'jadong':
                isGoToHome = True
                # 여긴 자동?
                print("게임 시작 하러 ㄱㄱ : game_play(cla, global_howcla)", data)
                result_where = myQuest_play_check(cla, 'go_to_home')
                jadong_cla_play(cla, result_where[0][2])
        print("def go_to_home(cla): end", data)
        print("def go_to_home(cla): end", cla)

    except Exception as e:
        print(e)
        return 0



def dead_die(cla, story):
    try:
        from action import go_alrim_yes, go_alrim_confirm
        from schedule import go_character_select
        from login_start import get_cla_count
        from chango import go_chango
        from massenger import line_to_me
        import numpy as np
        import cv2

        if cla == 'one':
            cla_ing_ = v_.one_cla_ing
        if cla == 'two':
            cla_ing_ = v_.two_cla_ing
        get_story = str(story) + " => dead_die"
        print(get_story)

        jangsigan = False

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\jangsigan.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(280, 470, 680, 590, cla, img)
        if imgs_ is None or imgs_ == False:
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\jangsigan_2.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(200, 300, 800, 800, cla, img)
            if imgs_ is None or imgs_ == False:
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\jangsigan_3.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(280, 470, 680, 590, cla, img)
                if imgs_ is None or imgs_ == False:
                    print("장시간 없다")
                else:
                    print("장시간 있다", imgs_)
                    jangsigan = True
            else:
                print("장시간 있다", imgs_)
                jangsigan = True
        else:
            print("장시간 있다", imgs_)
            jangsigan = True

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\kakao_games.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(10, 980, 150, 1030, cla, img)
        if imgs_ is not None:
            jangsigan = True

        if jangsigan == True:
            result_ = go_alrim_yes(cla)
            if result_[0] == True:
                click_pos_reg(result_[1], result_[2], cla)
            else:
                click_pos_2(480, 615, cla)
            ischar_sel_ = False
            while ischar_sel_ is False:
                ischar_sel_ = go_character_select
                if ischar_sel_ == False:
                    print("아직 캐릭터 선택 화면이 아니다.")
                    click_pos_2(480, 615, cla)
                    time.sleep(2 + random_int())
                else:
                    print("ㅇㅋㅂㄹ양세바리")
                    ischar_sel_ = True
                    get_cla_count(cla)

        # 여기까지가 장시간 ... 후 캐릭터 선택화면임

        # 아래는 마을에서 부활이라는 글자가 있을 경우...

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\boohwal.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(490, 900, 670, 970, cla, img)
        if imgs_ is None or imgs_ == False:
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\boohwal_3.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(490, 900, 670, 970, cla, img)
            if imgs_ is None or imgs_ == False:
                print("마을에서 부활 없다~솨롸있눼~")

            else:
                print("마을에서 부활 있다2")
                click_pos_2(580, 935, cla)
                time.sleep(random_int())
        else:
            print("마을에서 부활 있다1")
            click_pos_2(580, 935, cla)
            time.sleep(random_int())

            # 마을에 도착했는지 확인하기
            isVillage = False
            while isVillage is False:
                result = go_chango(cla, 'village')
                if result == False:

                    ismenu_ = menuOpenCheck(cla, "dead_die")
                    if ismenu_ == True:
                        click_pos_2(920, 55, cla)
                        time.sleep(1)

                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\boohwal.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(520, 920, 630, 960, cla, img)
                    if imgs_ is None or imgs_ == False:
                        print("아직 도착 안했다")
                    else:
                        print("마을에서 부활 있는데 안 눌려졌네")
                        click_pos_2(580, 935, cla)

                    time.sleep(random_int())
                else:
                    boohwal_cross_x = 295
                    boohwal_cross_y = 60
                    boo_hwal_ = False
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\boohwal_cross_1.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(250, 30, 400, 85, cla, img)
                    if imgs_ is None or imgs_ == False:
                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\boohwal_cross_2.png"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set(250, 30, 400, 85, cla, img)
                        if imgs_ is None or imgs_ == False:
                            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\boohwal_cross_3.png"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set(250, 30, 400, 85, cla, img)
                            if imgs_ is None or imgs_ == False:
                                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\boohwal_cross_4.png"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set(250, 30, 400, 85, cla, img)
                                if imgs_ is not None:
                                    print("부활십자가 보여4", imgs_)
                                    boo_hwal_ = True
                                    boohwal_cross_x = imgs_.x
                                    boohwal_cross_y = imgs_.y
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                print("부활십자가 보여3", imgs_)
                                boo_hwal_ = True
                                boohwal_cross_x = imgs_.x
                                boohwal_cross_y = imgs_.y
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            print("부활십자가 보여2", imgs_)
                            boo_hwal_ = True
                            boohwal_cross_x = imgs_.x
                            boohwal_cross_y = imgs_.y
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        print("부활십자가 보여1", imgs_)
                        boo_hwal_ = True
                        boohwal_cross_x = imgs_.x
                        boohwal_cross_y = imgs_.y
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    if boo_hwal_ == False:
                        print("부활십자가 아직 안 보인다.")
                        time.sleep(random_int())
                        result = go_chango(cla, 'village')
                        if result == True:
                            isVillage = True
                            print("부활 제대로 못하고 끝")
                    else:
                        print("부활십자가 있다")
                        isVillage = True

                        isBoggo_ = False
                        iscount_ = 0
                        while isBoggo_ is False:

                            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\boohwal_boggoo.png"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set(410, 330, 530, 370, cla, img)
                            if imgs_ is None or imgs_ == False:
                                print("경험치 복구가 없다")
                                iscount_ += 1
                                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\boohwal_cross_1.png"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set(250, 30, 400, 85, cla, img)
                                if imgs_ is None or imgs_ == False:
                                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\boohwal_cross_2.png"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set(250, 30, 400, 85, cla, img)
                                    if imgs_ is None or imgs_ == False:
                                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\boohwal_cross_3.png"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set(250, 30, 400, 85, cla, img)
                                        if imgs_ is None or imgs_ == False:
                                            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\boohwal_cross_4.png"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set(250, 30, 400, 85, cla, img)
                                            if imgs_ is not None:
                                                print("부활십자가 보여44", imgs_)
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                        else:
                                            print("부활십자가 보여33", imgs_)
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                    else:
                                        print("부활십자가 보여22", imgs_)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    print("부활십자가 보여11", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                if iscount_ > 100:
                                    line_to_me(cla, "죽고 나서 부활이 잘 안된당ㅠㅠ")
                            else:

                                isBoggo_ = True
                                print("경험치 복구가 있다")
                                isHaegol = False
                                while isHaegol is False:
                                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\boohwal_haegol.png"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set(240, 370, 320, 450, cla, img)
                                    if imgs_ is None or imgs_ == False:
                                        print("경험치 해골이 없다...")
                                        isHaegol = True
                                    else:
                                        print("경험치 해골이 있다")
                                        click_pos_2(480, 420, cla)
                                        time.sleep(random_int())
                                        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\boohwal_free.png"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set(500, 690, 610, 730, cla, img)
                                        if imgs_ is None or imgs_ == False:
                                            isHaegol = True
                                            print("무료복구가 없다")
                                            print("경험치 복구 안하고 끝~그냥 회복안하고 그대로 있기...추후 점검...")
                                            why = "계속 죽는다"
                                            line_to_me(cla, why)
                                            go_alrim_confirm(cla, "dead_die")
                                            click_pos_2(550, 710, cla)
                                        else:
                                            print("무료복구가 있다")
                                            click_pos_2(550, 710, cla)
                                            print("경험치 복구 완료하고 끝")

                time.sleep(random_int())
            go_to_home(cla_ing_, cla)

        # 410, 710 // 550, 710
        # 무료복구 없으면 더이상 부활시키지 말자(경험치 손해)


    except Exception as e:
        print(e)
        return 0




def go_auto(cla, number):
    try:
        import numpy as np
        import cv2
        from stop_18 import is_stop

        # x 같은 이벤트
        is_stop(cla)

        print("go_auto : ", number)

        dead_die(cla, "go_auto")

        go_ = False

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\auto.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(870, 860, 930, 910, cla, img)
        if imgs_ is not None and imgs_ != False:
            go_ = True
        else:
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\auto_2.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(870, 860, 930, 910, cla, img)
            if imgs_ is not None and imgs_ != False:
                go_ = True
            else:
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\auto_3.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(870, 860, 930, 910, cla, img)
                if imgs_ is not None and imgs_ != False:
                    go_ = True
                else:
                    print("auto 안 보여")

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\auto_quest.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(870, 860, 930, 910, cla, img)
        if imgs_ is not None and imgs_ != False:
            go_ = True
        else:
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\auto_quest_1.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(870, 860, 930, 910, cla, img)
            if imgs_ is not None and imgs_ != False:
                go_ = True
            else:
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\auto_quest_2.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(870, 860, 930, 910, cla, img)
                if imgs_ is not None and imgs_ != False:
                    go_ = True
                else:
                    print("auto_quest 안 보여")

        return go_
    except Exception as e:
        print(e)
        return 0

def change_number(many_potion):
    try:

        potion_ = many_potion

        if " " in potion_:
            potion_ = potion_.replace(' ', '')
            print("!!!!!! ['   '] !!!!!!!", potion_)
        if "고" in potion_:
            potion_ = potion_.replace('고', '2')
            print("!!!!!! [' 고 => 2 '] !!!!!!!", potion_)
        if "ㄷ" in potion_:
            potion_ = potion_.replace('ㄷ', '5')
            print("!!!!!! [' ㄷ => 5 '] !!!!!!!", potion_)
        if "요" in potion_:
            potion_ = potion_.replace('요', '8')
            print("!!!!!! [' 요 => 8 '] !!!!!!!", potion_)
        if "°" in potion_:
            potion_ = potion_.replace('°', '0')
            print("!!!!!! [   ° => 0   ] !!!!!!!", potion_)
        if ")" in potion_:
            potion_ = potion_.replace(')', '1')
            print("!!!!!! [   ) => 1   ] !!!!!!!", potion_)
        if "‘" in potion_:
            potion_ = potion_.replace('‘', '1')
            print("!!!!!! [   ‘ => 1   ] !!!!!!!", potion_)
        if "?" in potion_:
            potion_ = potion_.replace('?', '2')
            print("!!!!!! [   ? => 2  ] !!!!!!!", potion_)
        if "L" in potion_:
            potion_ = potion_.replace('L', '1')
            print("!!!!!! [   L => 1  ] !!!!!!!", potion_)
        if "|" in potion_:
            potion_ = potion_.replace('|', '1')
            print("!!!!!!![   | => 1  ]!!!!!!!!!!!", potion_)
        if "A" in potion_:
            potion_ = potion_.replace('A', '4')
            print("!!!!!!!!![  A => 4 ]!!!!!!!!!!!!!", potion_)
        if "D" in potion_:
            potion_ = potion_.replace('D', '2')
            print("!!!!!!!!![  D => 2 ]!!!!!!!!!!!!!", potion_)
        if "G" in potion_:
            potion_ = potion_.replace('G', '6')
            print("!!!!!!!!![  G => 6 ]!!!!!!!!!!!!!", potion_)
        if "B" in potion_:
            potion_ = potion_.replace('B', '8')
            print("!!!!!!!!![  B => 8  ]!!!!!!!!!!!!!", potion_)
        if "T" in potion_:
            potion_ = potion_.replace('T', '7')
            print("!!!!!!!!![  T => 7  ]!!!!!!!!!!!!!", potion_)
        if "S" in potion_:
            potion_ = potion_.replace('S', '5')
            print("!!!!!!!!![  S => 5  ]!!!!!!!!!!!!!", potion_)
        if "Q" in potion_:
            potion_ = potion_.replace('Q', '9')
            print("!!!!!!!!![  Q => 9  ]!!!!!!!!!!!!!", potion_)
        if "R" in potion_:
            potion_ = potion_.replace('R', '8')
            print("!!!!!!!!![  R => 8  ]!!!!!!!!!!!!!", potion_)

        potion_ = int_put_(potion_)

        if potion_[0] == "0":
            potion_ = "1" + potion_
            print("potion_ = '1' + potion_", potion_)

        return potion_
    except Exception as e:
        print(e)

def myPotion_check(data, cla):
    try:
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

        iwannaPotion = False
        if ispotion__ == True:
            while iwannaPotion is False:
                if potion < 150:
                    iwannaPotion = True
                    print('result_po potion < 150:')
                    if cla_ing == 'grow':
                        result_po = potion_count_grow(cla)
                        time.sleep(0.5)
                        click_pos_2(920, 55, cla)
                        if cla == 'one':
                            v_.mypotion_1 = result_po
                        if cla == 'two':
                            v_.mypotion_2 = result_po
                    else:
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
                elif potion < 250:
                    iwannaPotion = True
                    print('result_po potion < 250:')
                    print("여기에는 가방 => 물약 갯수 직접 다시 확인하고 상점을 가는 방향으로...")
                    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\gabang.png"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set(30, 40, 100, 75, cla, img)
                    if imgs_ is None or imgs_ == False:
                        print("가방이 없다...")
                        ismenu = False
                        while ismenu is False:
                            result_ = menuOpenCheck(cla, "myPotion_check_middle")
                            time.sleep(1)

                            if result_ == True:
                                ismenu = True
                                # hp 파악 ######
                                myhped_ = text_check_get(67, 37, 160, 73, cla)
                                print("myhp", myhped_)
                                if '/' in myhped_:
                                    print("파악 함")
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
                                            # 물약 파악
                                            if cla_ing == 'grow':
                                                result__ = potion_count_grow(cla)
                                            else:
                                                result__ = potion_count(cla)
                                            time.sleep(1)
                                            click_pos_2(920, 55, cla)
                                            time.sleep(1)
                                            click_pos_2(800, 840, cla)
                                            time.sleep(1)
                                            # click_pos_2(700, 840, cla)  #여기서 시작
                                            # time.sleep(random_int())

                                            if myhp_per < 0.6 or result__ < 150:
                                                time.sleep(1)
                                                go_to_home(data, cla)
                                else:
                                    print("파악 못함")

                                # click_pos_2(860, 55, cla)
                                # time.sleep(1)
                            else:
                                click_pos_2(920, 55, cla)
                                time.sleep(1)
                    else:
                        print("가방이 있다...")
                else:
                    iwannaPotion = True
                    print("물약 많지렁")
        else:
            print("물약 많아서 당장 파악 불가능")
            if isPotion_ < 150:
                if cla_ing == 'grow':
                    result_po = potion_count_grow(cla)
                    time.sleep(0.5)
                    click_pos_2(920, 55, cla)
                    if cla == 'one':
                        v_.mypotion_1 = result_po
                    if cla == 'two':
                        v_.mypotion_2 = result_po
                    print('result_po : grow', result_po)
                    if result_po < 100:
                        go_to_home('start', cla)

                else:
                    result_po = potion_count(cla)
                    time.sleep(0.5)
                    click_pos_2(920, 55, cla)
                    if cla == 'one':
                        v_.mypotion_1 = result_po
                    if cla == 'two':
                        v_.mypotion_2 = result_po
                    print('result_po', result_po)
                    if result_po < 200:
                        if cla_ing == 'gonghu' or cla_ing == 'nanjang' or cla_ing == 'underprison' or cla_ing == 'jadong':
                            go_to_home(cla_ing, cla)
                        else:
                            go_to_home('start', cla)


        dead_die(cla, "myPotion_check")

        print("def myPotion_check(data, cla): end")
        return data
    except Exception as e:
        print(e)
        return 0

def background_myPotion_check(data):
    try:
        from action import go_potion_off
        from clean import clean_screen
        import numpy as np
        import cv2

        print("def background_myPotion_check(data, cla): start")
        cla = data
        print("백그라운드 몇 클라?", cla)

        if cla == 'one':
            cla_ing = v_.one_cla_ing
            isPotion_ = v_.mypotion_1
        if cla == 'two':
            cla_ing = v_.two_cla_ing
            isPotion_ = v_.mypotion_2

        # if cla_ing == 'check':
        #     cla_ing = '바위해안'

        ispotion__ = False
        ispotionOff = False
        while ispotionOff is False:

            result = go_potion_off(cla)
            if result == False:

                result___ = menuOpenCheck(cla, "background_myPotion_check_start")
                if result___ == True:
                    click_pos_2(920, 55, cla)
                    time.sleep(1)
                else:

                    result____ = go_auto(cla, '4')
                    if result____ == True:
                        click_pos_2(800, 840, cla)
                        time.sleep(1)

                    else:
                        print("화면 초기화")
                        clean_screen(cla, "background_myPotion_check")


            else:
                ispotionOff = True
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
                print('result_po potion < 150:')
                if cla_ing == 'grow':
                    result_po = potion_count_grow(cla)
                    time.sleep(0.5)
                    click_pos_2(920, 55, cla)
                    if cla == 'one':
                        v_.mypotion_1 = result_po
                    if cla == 'two':
                        v_.mypotion_2 = result_po
                    print('result_po : grow', result_po)
                    if result_po < 100:
                        go_to_home('start', cla)
                else:
                    result_po = potion_count(cla)
                    time.sleep(0.5)
                    click_pos_2(920, 55, cla)
                    if cla == 'one':
                        v_.mypotion_1 = result_po
                    if cla == 'two':
                        v_.mypotion_2 = result_po
                    print('result_po', result_po)
                    if result_po < 200:
                        if cla_ing == 'gonghu' or cla_ing == 'nanjang' or cla_ing == 'underprison' or cla_ing == 'jadong':
                            go_to_home(cla_ing, cla)
                        else:
                            go_to_home('start', cla)    #이거 잘못 된거임

                    # isvil_go = False
                    # while isvil_go is False:
                    #     result = go_auto(cla)
                    #     if result == True:
                    #         isvil_go = True
                    #         click_pos_2(30, 225, cla)
                    #         time.sleep(random_int())
                    #         click_pos_2(550, 610, cla)
                    #     else:
                    #         click_pos_2(920, 55, cla)
                    #         time.sleep(random_int())
                    else:
                        print("휴...안가도 된다")
            elif potion < 250:
                print('result_po potion < 250:')
                print("여기에는 가방 => 물약 갯수 직접 다시 확인하고 상점을 가는 방향으로...")
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\gabang.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(30, 40, 100, 75, cla, img)
                if imgs_ is None or imgs_ == False:
                    print("가방이 없다...")
                    ismenu = False
                    while ismenu is False:
                        result_ = menuOpenCheck(cla, "background_myPotion_check_middle")
                        time.sleep(1)

                        if result_ == True:
                            ismenu = True
                            # hp 파악 ######
                            myhped_ = text_check_get(67, 37, 160, 73, cla)
                            print("myhp", myhped_)
                            if '/' in myhped_:
                                print("파악 함")
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
                                        # 물약 파악
                                        if cla_ing == 'grow':
                                            result__ = potion_count_grow(cla)
                                        else:
                                            result__ = potion_count(cla)
                                        time.sleep(1)
                                        click_pos_2(920, 55, cla)
                                        time.sleep(1)
                                        click_pos_2(800, 840, cla)
                                        time.sleep(1)

                                        if myhp_per < 0.6 or result__ < 150:
                                            if cla_ing == 'gonghu' or cla_ing == 'nanjang' or cla_ing == 'underprison' or cla_ing == 'jadong':
                                                go_to_home(cla_ing, cla)
                                            else:
                                                go_to_home('start', cla)    # 이거 잘못 된거임
                            else:
                                print("파악 못함")

                            # click_pos_2(860, 55, cla)
                            # time.sleep(1)
                        else:
                            click_pos_2(920, 55, cla)
                            time.sleep(1)
                else:
                    print("가방이 있다...")
            else:
                print("물약 충분하다...")
        else:
            print("물약 많아서 당장 파악 불가능")
            if isPotion_ < 150:
                if cla_ing == 'grow':
                    result_po = potion_count_grow(cla)
                    time.sleep(0.5)
                    click_pos_2(920, 55, cla)
                    if cla == 'one':
                        v_.mypotion_1 = result_po
                    if cla == 'two':
                        v_.mypotion_2 = result_po
                    print('result_po : grow', result_po)
                    if result_po < 100:
                        go_to_home('start', cla)
                else:
                    result_po = potion_count(cla)
                    time.sleep(0.5)
                    click_pos_2(920, 55, cla)
                    if cla == 'one':
                        v_.mypotion_1 = result_po
                    if cla == 'two':
                        v_.mypotion_2 = result_po
                    print('result_po', result_po)
                    if result_po < 200:
                        if cla_ing == 'gonghu' or cla_ing == 'nanjang' or cla_ing == 'underprison' or cla_ing == 'jadong':
                            go_to_home(cla_ing, cla)
                        else:
                            go_to_home('start', cla)


        print("def background_myPotion_check(data, cla): end")
    except Exception as e:
        print(e)
        return 0

def potion_count(cla):
    print('def potion_count(cla):')
    try:
        from action import go_bag, go_alrim_, go_alrim_yes
        import numpy as np
        import cv2
        import pytesseract
        import pyautogui

        print("def potion_count(cla):")

        potion__ = 0

        result_ = go_bag(cla, "potion_count")
        if result_ == True:
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\potion_small.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(580, 120, 950, 950, cla, img)

            if imgs_ is None or imgs_ == False:
                print("작은 물약 안보여")
                drag_pos(770, 890, 770, 200, cla)
                time.sleep(1)
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\potion_small.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(580, 120, 950, 950, cla, img)

                if imgs_ is None or imgs_ == False:
                    print("작은 물약 안보여2")

                else:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    print("작은 물약 보여2")
                    time.sleep(1)
                    click_pos_2(120, 770, cla)
                    time.sleep(1)
                    click_pos_2(550, 628, cla)
                    time.sleep(1)
                    result__ = go_alrim_(cla)
                    if result__ == False:
                        print("아이템 삭제 안보여2")

                    else:
                        print("아이템 삭제 보여2")
                        result_ = go_alrim_yes(cla)
                        if result_[0] == True:
                            click_pos_reg(result_[1], result_[2], cla)
                        else:
                            click_pos_2(550, 628, cla)
                        time.sleep(1)

            else:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                print("작은 물약 보여")
                time.sleep(1)
                click_pos_2(120, 770, cla)
                time.sleep(1)
                click_pos_2(550, 628, cla)
                time.sleep(1)
                result__ = go_alrim_(cla)
                if result__ == False:
                    print("아이템 삭제 안보여1")

                else:
                    print("아이템 삭제 보여1")
                    result_ = go_alrim_yes(cla)
                    if result_[0] == True:
                        click_pos_reg(result_[1], result_[2], cla)
                    else:
                        click_pos_2(550, 628, cla)
                    time.sleep(1)

            time.sleep(0.5)
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\potion_middle.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(580, 120, 950, 950, cla, img)

            if imgs_ is None or imgs_ == False:
                print("중간 물약 안보여")
                # drag_pos(770, 890, 770, 200, cla)
                time.sleep(random_int())
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\potion_middle.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(580, 120, 950, 950, cla, img)

                if imgs_ is None or imgs_ == False:
                    print("중간 물약 안보여2")

                else:
                    # pyautogui.moveTo(imgs_.x, imgs_.y, 1)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    print("중간 물약 보여2", imgs_)

                    mid_potion = False
                    mid_potion_count = 0
                    while mid_potion is False:
                        mid_potion_count += 1
                        if mid_potion_count > 15:
                            mid_potion = True

                        img = pyautogui.screenshot(region=(get_region(105, 410, 165, 440, cla)))
                        white_img = image_processing(img, (148, 148, 148), (255, 255, 255))
                        result = pytesseract.image_to_string(white_img, lang=None)
                        digit_bloon = int_put_(result).isdigit()
                        if digit_bloon == True:
                            num_ = int(int_put_(result))
                            print("num_", num_)
                            potion__ += num_
                            mid_potion = True
                        else:
                            if result == '':
                                print("비웠니랑..")
                            else:
                                print("보이질 않아", result)
                        time.sleep(0.5)


            else:
                # pyautogui.moveTo(imgs_.x, imgs_.y, 1)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                print("중간 물약 보여", imgs_)

                mid_potion = False
                mid_potion_count = 0
                while mid_potion is False:
                    mid_potion_count += 1
                    if mid_potion_count > 15:
                        mid_potion = True

                    img = pyautogui.screenshot(region=(get_region(105, 410, 165, 440, cla)))
                    white_img = image_processing(img, (148, 148, 148), (255, 255, 255))
                    result = pytesseract.image_to_string(white_img, lang=None)
                    digit_bloon = int_put_(result).isdigit()
                    if digit_bloon == True:
                        num_ = int(int_put_(result))
                        print("num_", num_)
                        potion__ += num_
                        mid_potion = True
                    else:
                        if result == '':
                            print("비웠니랑..")
                        else:
                            print("보이질 않아", result)
                    time.sleep(0.5)

            time.sleep(0.5)
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\potion_big.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(580, 120, 950, 950, cla, img)

            if imgs_ is None or imgs_ == False:
                print("큰 물약 안보여")
                # drag_pos(770, 890, 770, 200, cla)
                time.sleep(random_int())
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\potion_big.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(580, 120, 950, 950, cla, img)

                if imgs_ is None or imgs_ == False:
                    print("큰 물약 안보여2")

                else:
                    # pyautogui.moveTo(imgs_.x, imgs_.y, 1)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    print("큰 물약 보여2", imgs_)

                    big_potion = False
                    big_potion_count = 0
                    while big_potion is False:
                        big_potion_count += 1
                        if big_potion_count > 15:
                            big_potion = True

                        img = pyautogui.screenshot(region=(get_region(105, 410, 165, 440, cla)))
                        white_img = image_processing(img, (148, 148, 148), (255, 255, 255))
                        result = pytesseract.image_to_string(white_img, lang=None)
                        digit_bloon = int_put_(result).isdigit()
                        if digit_bloon == True:
                            num_ = int(int_put_(result))
                            print("num_", num_)
                            potion__ += num_
                            big_potion = True
                        else:
                            if result == '':
                                print("비웠니랑..")
                            else:
                                print("보이질 않아", result)
                        time.sleep(0.5)

            else:
                # pyautogui.moveTo(imgs_.x, imgs_.y, 1)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                print("큰 물약 보여", imgs_)

                big_potion = False
                big_potion_count = 0
                while big_potion is False:
                    big_potion_count += 1
                    if big_potion_count > 15:
                        big_potion = True

                    img = pyautogui.screenshot(region=(get_region(105, 410, 165, 440, cla)))
                    white_img = image_processing(img, (148, 148, 148), (255, 255, 255))
                    result = pytesseract.image_to_string(white_img, lang=None)
                    digit_bloon = int_put_(result).isdigit()
                    if digit_bloon == True:
                        num_ = int(int_put_(result))
                        print("num_", num_)
                        potion__ += num_
                        big_potion = True
                    else:
                        if result == '':
                            print("비웠니랑..")
                        else:
                            print("보이질 않아", result)
                    time.sleep(0.5)


                # potioned_ = text_check_get(100, 410, 165, 440, cla)
                # print("potioon", potioned_)
                # if potioned_ == '':
                #     print("비웠니라")
                # else:
                #     potion__ += int(int_put_(potioned_))
        result__ = go_alrim_(cla)
        if result__ == False:
            print("아이템 삭제 안보여3")

        else:
            print("아이템 삭제 보여3")
            result_ = go_alrim_yes(cla)
            if result_[0] == True:
                click_pos_reg(result_[1], result_[2], cla)
            else:
                click_pos_2(550, 628, cla)
            time.sleep(random_int())
        print("potion", potion__)

        return potion__
    except Exception as e:
        print(e)
        return 0

def potion_count_grow(cla):
    print('def potion_count_grow(cla):')
    try:
        from action import go_bag, go_alrim_, go_alrim_yes
        import numpy as np
        import cv2
        import pytesseract
        import pyautogui
        print("def potion_count_grow(cla):")

        potion__ = 0

        result_ = go_bag(cla, "potion_count_grow")
        if result_ == True:
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\potion_small.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(580, 120, 950, 950, cla, img)
            # imgs_ = pyautogui.locateCenterOnScreen(img, region=(580 + plus, 120, 950 + plus, 950),
            #                                        confidence=0.7)

            if imgs_ is None or imgs_ == False:
                print("작은 물약 안보여")
                drag_pos(770, 890, 770, 200, cla)
                time.sleep(random_int())
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\potion_small.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(580, 120, 950, 950, cla, img)
                # imgs_ = pyautogui.locateCenterOnScreen(img, region=(580 + plus, 120, 950 + plus, 950),
                #                                        confidence=0.7)

                if imgs_ is None or imgs_ == False:
                    print("작은 물약 안보여2")

                else:
                    # pyautogui.moveTo(imgs_.x, imgs_.y, 1)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    print("작은 물약 보여2")

                    img = pyautogui.screenshot(region=(get_region(105, 410, 165, 440, cla)))
                    white_img = image_processing(img, (148, 148, 148), (255, 255, 255))
                    result = pytesseract.image_to_string(white_img, lang=None)
                    digit_bloon = int_put_(result).isdigit()
                    if digit_bloon == True:
                        num_ = int(int_put_(result))
                        print("num_", num_)
                        potion__ += num_
                    else:
                        if result == '':
                            print("비웠니랑..")
                        else:
                            print("보이질 않아", result)

            else:
                # pyautogui.moveTo(imgs_.x, imgs_.y, 1)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                print("작은 물약 보여")

                img = pyautogui.screenshot(region=(get_region(105, 410, 165, 440, cla)))
                white_img = image_processing(img, (148, 148, 148), (255, 255, 255))
                result = pytesseract.image_to_string(white_img, lang=None)
                digit_bloon = int_put_(result).isdigit()
                if digit_bloon == True:
                    num_ = int(int_put_(result))
                    print("num_", num_)
                    potion__ += num_
                else:
                    if result == '':
                        print("비웠니랑..")
                    else:
                        print("보이질 않아", result)





            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\potion_middle.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(580, 120, 950, 950, cla, img)

            if imgs_ is None or imgs_ == False:
                print("중간 물약 안보여")
                # drag_pos(770, 890, 770, 200, cla)
                time.sleep(random_int())
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\potion_middle.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(580, 120, 950, 950, cla, img)

                if imgs_ is None or imgs_ == False:
                    print("중간 물약 안보여2")

                else:
                    # pyautogui.moveTo(imgs_.x, imgs_.y, 1)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    print("중간 물약 보여2", imgs_)

                    img = pyautogui.screenshot(region=(get_region(105, 410, 165, 440, cla)))
                    white_img = image_processing(img, (148, 148, 148), (255, 255, 255))
                    result = pytesseract.image_to_string(white_img, lang=None)
                    digit_bloon = int_put_(result).isdigit()
                    if digit_bloon == True:
                        num_ = int(int_put_(result))
                        print("num_", num_)
                        potion__ += num_
                    else:
                        if result == '':
                            print("비웠니랑..")
                        else:
                            print("보이질 않아", result)


            else:
                # pyautogui.moveTo(imgs_.x, imgs_.y, 1)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                print("중간 물약 보여", imgs_)

                img = pyautogui.screenshot(region=(get_region(105, 410, 165, 440, cla)))
                white_img = image_processing(img, (148, 148, 148), (255, 255, 255))
                result = pytesseract.image_to_string(white_img, lang=None)
                digit_bloon = int_put_(result).isdigit()
                if digit_bloon == True:
                    num_ = int(int_put_(result))
                    print("num_", num_)
                    potion__ += num_
                else:
                    if result == '':
                        print("비웠니랑..")
                    else:
                        print("보이질 않아", result)



            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\potion_big.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(580, 120, 950, 950, cla, img)

            if imgs_ is None or imgs_ == False:
                print("큰 물약 안보여")
                # drag_pos(770, 890, 770, 200, cla)
                time.sleep(random_int())
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\potion_big.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(580, 120, 950, 950, cla, img)

                if imgs_ is None or imgs_ == False:
                    print("큰 물약 안보여2")

                else:
                    # pyautogui.moveTo(imgs_.x, imgs_.y, 1)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    print("큰 물약 보여2", imgs_)

                    img = pyautogui.screenshot(region=(get_region(105, 410, 165, 440, cla)))
                    white_img = image_processing(img, (148, 148, 148), (255, 255, 255))
                    result = pytesseract.image_to_string(white_img, lang=None)
                    digit_bloon = int_put_(result).isdigit()
                    if digit_bloon == True:
                        num_ = int(int_put_(result))
                        print("num_", num_)
                        potion__ += num_
                    else:
                        if result == '':
                            print("비웠니랑..")
                        else:
                            print("보이질 않아", result)


            else:
                # pyautogui.moveTo(imgs_.x, imgs_.y, 1)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                print("큰 물약 보여", imgs_)

                img = pyautogui.screenshot(region=(get_region(105, 410, 165, 440, cla)))
                white_img = image_processing(img, (148, 148, 148), (255, 255, 255))
                result = pytesseract.image_to_string(white_img, lang=None)
                digit_bloon = int_put_(result).isdigit()
                if digit_bloon == True:
                    num_ = int(int_put_(result))
                    print("num_", num_)
                    potion__ += num_
                else:
                    if result == '':
                        print("비웠니랑..")
                    else:
                        print("보이질 않아", result)


                # potioned_ = text_check_get(100, 410, 165, 440, cla)
                # print("potioon", potioned_)
                # if potioned_ == '':
                #     print("비웠니라")
                # else:
                #     potion__ += int(int_put_(potioned_))
        result__ = go_alrim_(cla)
        if result__ == False:
            print("아이템 삭제 안보여3")

        else:
            print("아이템 삭제 보여3")
            result_ = go_alrim_yes(cla)
            if result_[0] == True:
                click_pos_reg(result_[1], result_[2], cla)
            else:
                click_pos_2(550, 628, cla)
            time.sleep(random_int())
        print("potion", potion__)

        return potion__
    except Exception as e:
        print(e)
        return 0


