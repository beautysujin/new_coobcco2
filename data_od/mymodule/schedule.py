# from datetime import datetime
# from datetime import date, timedelta
# import os.path
# import numpy as np
# import cv2
import sys
sys.path.append('C:/my_games/coobcco2/data_od/mymodule')
# from myfunction import *
# from chango import auction

import variable as v_

def go_test(cla):
    print('hi test! schedule', cla)



def go_character_select(cla):
    try:
        import numpy as np
        import cv2
        from myfunction import imgs_set, text_check_get_3
        go_ = False

        full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\char_select.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(20, 20, 200, 200, cla, img)

        if imgs_ is None or imgs_ == False:
            print("캐릭터 선택이 안보여")
            full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\char_select2.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set(20, 20, 200, 200, cla, img)

            if imgs_ is None or imgs_ == False:
                print("캐릭터 선택2이 안보여")
                full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\char_select4.png"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set(20, 20, 200, 200, cla, img)

                if imgs_ is None or imgs_ == False:
                    print("캐릭터 선택이 안보여4")
                else:
                    print("캐릭터 선택2이 보여4", imgs_)
                    go_ = True
            else:
                print("캐릭터 선택2이 보여", imgs_)
                go_ = True
        else:
            print("캐릭터 선택이 보여", imgs_)
            go_ = True

        if go_ == False:
            print("캐릭터 선택 화면...png로 해결 불가능하여 글자인식하기")
            character_selected_ = text_check_get_3(55, 45, 110, 70, 2, cla)
            character_selected_ = character_selected_.split("\n")
            character_selected_ = " ".join(character_selected_).strip()
            print("character_selected_ : 글자인식 =>", character_selected_)
            if len(character_selected_) != 0:
                for list in range(len(character_selected_)):
                    if character_selected_[list] == "캐" or character_selected_[list] == '릭' or character_selected_[
                        list] == '터':
                        print("character_selected_ : ", character_selected_[list])
                        go_ = True

        if go_ == True:
            myQuest_number_check(cla, 'one_refresh')
        return go_
    except Exception as e:
        print(e)
        return 0



def myQuest_number_check_bool(cla, data):
    try:
        same_ = False
        if cla == 'one':
            cla_ing_ = v_.one_cla_ing
        if cla == 'two':
            cla_ing_ = v_.two_cla_ing

        if data == "" or data == None:
            print("myQuest_number_check_bool : data => ", data)
            print("data 값이 파악이 안된다")
        else:

            start_ready = myQuest_play_check(cla, 'with_myquest_number_check')

            # start_ready[0] 진행중인 정보 [0][1] = id, [0][2] = 던전(공허, 난쟁이, 지하감옥, 자동사냥(들소황무지...), [0][3] = 완료 or 대기중, [3]진행되거나 진행중인 퀘스트
            # 몇번째 인자에 정보가 담겨있는지 여부

            # result[0] == number, result[1] == cla_ing_, result[2] == myid, result[3] == mylevel, result[4] == mypower, result[5] == mymoney, result[6] == cla_count, result[7] == mypotion_, result[8] == event_bool
            result_num = myQuest_number_check(cla, 'load')
            print("result_num", result_num)

            if result_num != "none":
                mynumbers_ = result_num.split(':')
                print("mynumbers_[0] / number =>", mynumbers_[0])
                print("mynumbers_[1] / cla_ing_ =>", mynumbers_[1])
                print("mynumbers_[2] / myid =>", mynumbers_[2])
                print("mynumbers_[3] / mylevel =>", mynumbers_[3])
                print("mynumbers_[4] / mypower =>", mynumbers_[4])
                print("mynumbers_[5] / mymoney =>", mynumbers_[5])
                print("mynumbers_[6] / cla_count =>", mynumbers_[6])
                print("mynumbers_[7] / mypotion_ =>", mynumbers_[7])
                print("mynumbers_[8] / event_bool =>", mynumbers_[8])
                print("mynumbers_[9] / now_growing_ =>", mynumbers_[9])

                number_bool_ = mynumbers_[0].isdigit()

                if number_bool_ == False:
                    print("회원 번호 정보가 없다")
                    myQuest_number_check(cla, "one_refresh")
                else:
                    cla_ing_ = mynumbers_[1]
                    if mynumbers_[1] == 'grow' and mynumbers_[9] == 'none':
                        cla_ing_ = 'check'



                    if int(data) == int(mynumbers_[0]) and str(mynumbers_[1]) == str(start_ready[3]):
                        same_ = True
                        print("같은 캐릭터 재접속")
                        if cla == 'one':
                            v_.mynumber_1 = int(mynumbers_[0])
                            v_.one_cla_ing = cla_ing_
                            v_.myId_1 = int(mynumbers_[2])
                            v_.mylevel_1 = int(mynumbers_[3])
                            v_.mypower_1 = int(mynumbers_[4])
                            v_.mymoney_1 = int(mynumbers_[5])
                            v_.one_cla_count = int(mynumbers_[6])
                            v_.mypotion_1 = int(mynumbers_[7])
                            if mynumbers_[8] == 'true':
                                v_.one_cla_get_event = True
                            else:
                                v_.one_cla_get_event = False
                            v_.one_now_growing_ = mynumbers_[9]
                        if cla == 'two':
                            v_.mynumber_2 = int(mynumbers_[0])
                            v_.two_cla_ing = cla_ing_
                            v_.myId_2 = int(mynumbers_[2])
                            v_.mylevel_2 = int(mynumbers_[3])
                            v_.mypower_2 = int(mynumbers_[4])
                            v_.mymoney_2 = int(mynumbers_[5])
                            v_.two_cla_count = int(mynumbers_[6])
                            v_.mypotion_2 = int(mynumbers_[7])
                            if mynumbers_[8] == 'true':
                                v_.two_cla_get_event = True
                            else:
                                v_.two_cla_get_event = False
                            v_.two_now_growing_ = mynumbers_[9]
                    else:
                        print("다른 캐릭터 재접속")
                        myQuest_number_check(cla, "one_refresh")
                        if str(mynumbers_[1]) != str(start_ready[3]):
                            if cla == 'one':
                                v_.one_cla_ing = 'check'
                            if cla == 'two':
                                v_.two_cla_ing = 'check'
        return same_, cla_ing_
    except Exception as e:
        print(e)
        return 0
def myQuest_number_check(cla, data):
    try:
        import os.path

        dir_path = "C:\\my_games\\coobcco2"
        if cla == 'one':
            file_path11 = dir_path + "\\odin_quest\\one.txt"
            number_ = v_.mynumber_1
            cla_ing_ = v_.one_cla_ing
            myid = v_.myId_1
            mylevel = v_.mylevel_1
            mypower = v_.mypower_1
            mymoney = v_.mymoney_1
            cla_count = v_.one_cla_count
            mypotion_ = v_.mypotion_1
            cla_get_event = v_.one_cla_get_event
            now_growing_ = v_.one_now_growing_

        if cla == 'two':
            file_path11 = dir_path + "\\odin_quest\\two.txt"
            number_ = v_.mynumber_2
            cla_ing_ = v_.two_cla_ing
            myid = v_.myId_2
            mylevel = v_.mylevel_2
            mypower = v_.mypower_2
            mymoney = v_.mymoney_2
            cla_count = v_.two_cla_count
            mypotion_ = v_.mypotion_2
            cla_get_event = v_.two_cla_get_event
            now_growing_ = v_.two_now_growing_

        if cla != 'all':
            if cla_get_event == True:
                event_bool = 'true'
            else:
                event_bool = 'false'

        if data == 'load':
            print("myQuest_number_check : load => ", number_)
            isload = False
            while isload is False:
                if os.path.isfile(file_path11) == True:
                    # 파일 읽기
                    isload = True
                    with open(file_path11, "r", encoding='utf-8-sig') as file:
                        line = file.read()

                        if line != "none":
                            mynumbers_ = line.split(':')
                            print("data == 'load': mynumbers_[0] / number =>", mynumbers_[0])
                            # print("data == 'load': mynumbers_[1] / cla_ing_ =>", mynumbers_[1])
                            # print("data == 'load': mynumbers_[2] / myid =>", mynumbers_[2])
                            # print("mynumbers_[3] / mylevel =>", mynumbers_[3])
                            # print("mynumbers_[4] / mypower =>", mynumbers_[4])
                            # print("mynumbers_[5] / mymoney =>", mynumbers_[5])
                            # print("mynumbers_[6] / cla_count =>", mynumbers_[6])
                            # print("mynumbers_[7] / mypotion_ =>", mynumbers_[7])
                            # print("mynumbers_[8] / event_bool =>", mynumbers_[8])
                            # print("mynumbers_[9] / now_growing_ =>", mynumbers_[9])

                            number_bool_ = mynumbers_[0].isdigit()

                            if number_bool_ == False:
                                print("회원 번호 정보가 없다")
                                myQuest_number_check(cla, "one_refresh")
                                with open(file_path11, "r", encoding='utf-8-sig') as file:
                                    line = file.read()

                else:
                    with open(file_path11, "w", encoding='utf-8-sig') as file:
                        file.write("none")
        # result[0] == number, result[1] == cla_ing_, result[2] == myid, result[3] == mylevel, result[4] == mypower, result[5] == mymoney, result[6] == cla_count, result[7] == mypotion_, result[8] == event_bool
        if data == 'new':
            print("myQuest_number_check : new => ", number_)
            numbers = str(number_) + ":" + str(cla_ing_) + ":" + str(myid) + ":" + str(mylevel) + ":" + str(mypower) + ":" + str(mymoney) + ":" + str(cla_count) + ":" + str(mypotion_) + ":" + str(event_bool) + ":" + str(now_growing_)

            with open(file_path11, "w", encoding='utf-8-sig') as file:
                file.write(numbers)
            with open(file_path11, "r", encoding='utf-8-sig') as file:
                line = file.read()

        if data == 'refresh':

            file_path11 = dir_path + "\\odin_quest\\one.txt"
            print("myQuest_number_check : refresh => ")
            with open(file_path11, "w", encoding='utf-8-sig') as file:
                file.write("none")
            with open(file_path11, "r", encoding='utf-8-sig') as file:
                line = file.read()
            file_path11 = dir_path + "\\odin_quest\\two.txt"
            print("myQuest_number_check : refresh => ")
            with open(file_path11, "w", encoding='utf-8-sig') as file:
                file.write("none")
            with open(file_path11, "r", encoding='utf-8-sig') as file:
                line = file.read()

        if data == 'one_refresh':
            print("one_refrest~!")
            with open(file_path11, "w", encoding='utf-8-sig') as file:
                file.write("none")
            with open(file_path11, "r", encoding='utf-8-sig') as file:
                line = file.read()

        return line
    except Exception as e:
        print(e)
        return 0




def myQuest_play_check(cla, data):
    try:
        import os.path
        from datetime import datetime
        from datetime import date, timedelta

        print("myQuest_play_check...")
        if cla == 'one':
            id_cla = v_.myId_1
            cla_start = v_.one_cla_start
        if cla == 'two':
            id_cla = v_.myId_2
            cla_start = v_.two_cla_start
        id_cla = str(id_cla)
        start_ = cla_start
        refresh_ = False

        # 닉네임 받아와서 전역변수 설정하기
        nowDay_ = datetime.today().strftime("%Y%m%d")
        nowDay = int(nowDay_)
        nowTime = int(datetime.today().strftime("%H"))
        yesterday_ = date.today() - timedelta(1)
        yesterday = int(yesterday_.strftime('%Y%m%d'))

        dir_path = "C:\\my_games\\coobcco2"
        file_path = dir_path + "\\odin_schedule\\schedule.txt"
        file_path2 = dir_path + "\\odin_schedule\\quest.txt"
        file_path3 = dir_path + "\\odin_schedule\\schedule2.txt"
        file_path13 = dir_path + "\\odin_schedule\\refresh_time.txt"

        isRefresh = False
        while isRefresh is False:
            if os.path.isfile(file_path13) == True:
                with open(file_path13, "r", encoding='utf-8-sig') as file:
                    isRefresh = True
                    refresh_time = file.read()
                    print("refresh_time", refresh_time)
            else:
                with open(file_path13, "w", encoding='utf-8-sig') as file:
                    file.write(str(6))


        if nowTime >= int(refresh_time):
            nowDay = str(nowDay)
            print("1 : 퀘스트 갱신된 상황이라 체크 후 진행", nowDay)
        else:
            nowDay = yesterday
            nowDay = str(nowDay)
            print("날짜가 다르다")
            print("2 : 퀘스트 갱신되기 전이라 그냥 진행", nowDay)

        #스케쥴 초기화 관련
        if os.path.isfile(file_path2) == True:
            print("nowDay : ", nowDay)
            # 파일 읽기
            with open(file_path2, "r", encoding='utf-8-sig') as file:
                lines2 = file.read().splitlines()
                day_ = lines2[0].split(":")
            if day_[0] == nowDay:
                print("nowDay ing good")
            else:

                myQuest_number_check(cla, 'refresh')

                if datetime.today().weekday() == 0:

                    with open(file_path2, "w", encoding='utf-8-sig') as file:
                        file.write(str(nowDay) + ":" + str(refresh_time) + "\n")
                        # 새로 갱신이니 1번 캐릭 선택으로...and 스케쥴 초기화 tttttttttttttttttttttttttttttttttttttttttttt
                        print("새로 갱신..and 스케쥴 초기화")
                        reset_schedule_ = ""
                        with open(file_path, "r", encoding='utf-8-sig') as file:
                            lines = file.read().splitlines()
                            lines = ' '.join(lines).split()

                            isSchedule_ = False
                            while isSchedule_ is False:
                                if lines == [] or lines == "":
                                    print("스케쥴이 비었다 : myQuest_play_check")
                                    with open(file_path3, "r", encoding='utf-8-sig') as file:
                                        schedule_ready = file.read()
                                    with open(file_path, "w", encoding='utf-8-sig') as file:
                                        file.write(schedule_ready)
                                    with open(file_path, "r", encoding='utf-8-sig') as file:
                                        lines = file.read().splitlines()
                                else:
                                    isSchedule_ = True

                            for i in range(len(lines)):
                                complete_ = lines[i].split(":")
                                for j in range(len(complete_)):
                                    if j < 3:
                                        reset_schedule_ += complete_[j] + ":"
                                    if j == 3:
                                        reset_schedule_ += '대기중:'
                                    if 3 < j < 7:
                                        reset_schedule_ += complete_[j] + ":"
                                    if j == 7:
                                        reset_schedule_ += "대기중\n"
                            print('reset_schedule_', reset_schedule_)
                            with open(file_path, "w", encoding='utf-8-sig') as file:
                                file.write(reset_schedule_)
                            with open(file_path3, "w", encoding='utf-8-sig') as file:
                                file.write(reset_schedule_)
                else:
                    with open(file_path2, "w", encoding='utf-8-sig') as file:
                        file.write(str(nowDay) + ":" + str(refresh_time) + "\n")
                        # 새로 갱신이니 1번 캐릭 선택으로...and 스케쥴 초기화 tttttttttttttttttttttttttttttttttttttttttttt
                        print("새로 갱신..and 스케쥴 초기화")
                        reset_schedule_ = ""
                        with open(file_path, "r", encoding='utf-8-sig') as file:
                            lines = file.read().splitlines()
                            lines = ' '.join(lines).split()

                            isSchedule_ = False
                            while isSchedule_ is False:
                                if lines == [] or lines == "":
                                    print("스케쥴이 비었다 : myQuest_play_check")
                                    with open(file_path3, "r", encoding='utf-8-sig') as file:
                                        schedule_ready = file.read()
                                    with open(file_path, "w", encoding='utf-8-sig') as file:
                                        file.write(schedule_ready)
                                    with open(file_path, "r", encoding='utf-8-sig') as file:
                                        lines = file.read().splitlines()
                                else:
                                    isSchedule_ = True

                            for i in range(len(lines)):
                                complete_ = lines[i].split(":")
                                for j in range(len(complete_)):
                                    if j < 3:
                                        reset_schedule_ += complete_[j] + ":"
                                    if j == 3:

                                        if '_' in complete_[2]:
                                            dunjeon_spl_ = complete_[2].split("_")
                                            print("dunjeon_spl_[0]", dunjeon_spl_[0])
                                            print("dunjeon_spl_[1]", dunjeon_spl_[1])

                                            if dunjeon_spl_[0] == "지하감옥":
                                                reset_schedule_ += complete_[j] + ":"
                                            else:
                                                reset_schedule_ += '대기중:'
                                        else:
                                            reset_schedule_ += '대기중:'

                                        # if complete_[2] == "지하감옥":
                                        #     reset_schedule_ += complete_[j] + ":"
                                        # else:
                                        #     reset_schedule_ += '대기중:'
                                    if 3 < j < 7:
                                        reset_schedule_ += complete_[j] + ":"
                                    if j == 7:

                                        if '_' in complete_[6]:
                                            dunjeon_spl_ = complete_[6].split("_")
                                            print("dunjeon_spl_[0]", dunjeon_spl_[0])
                                            print("dunjeon_spl_[1]", dunjeon_spl_[1])

                                            if dunjeon_spl_[0] == "지하감옥":
                                                reset_schedule_ += complete_[j] + "\n"
                                            else:
                                                reset_schedule_ += "대기중\n"
                                        else:
                                            reset_schedule_ += "대기중\n"

                                        # if complete_[6] == "지하감옥":
                                        #     reset_schedule_ += complete_[j] + "\n"
                                        # else:
                                        #     reset_schedule_ += "대기중\n"

                            print('reset_schedule_', reset_schedule_)
                            with open(file_path, "w", encoding='utf-8-sig') as file:
                                file.write(reset_schedule_)
                            with open(file_path3, "w", encoding='utf-8-sig') as file:
                                file.write(reset_schedule_)
                refresh_ = True
                # change_ = 1
                # characterChange(change_, cla)
                # myQuest_play_check(cla, 'check')
                v_.one_cla_count = 0
                v_.two_cla_count = 0
                v_.one_cla_ing = 'check'
                v_.two_cla_ing = 'check'
                v_.one_cla_get_event = False
                v_.two_cla_get_event = False
                # myQuest_number_check(cla, "new")


        else:
            with open(file_path2, "w", encoding='utf-8-sig') as file:
                file.write(str(nowDay) + ":" + str(refresh_time) + "\n")
                myQuest_play_check(cla, data)

        #스케쥴 관련
        cla_schedule = ""
        if os.path.isfile(file_path) == True:
            print("3_", nowDay)
            # 파일 읽기
            with open(file_path, "r", encoding='utf-8-sig') as file:
                lines = file.read().splitlines()

                isSchedule_ = False
                while isSchedule_ is False:
                    if lines == [] or lines == "":
                        print("스케쥴이 비었다 : myQuest_grow_check")
                        with open(file_path3, "r", encoding='utf-8-sig') as file:
                            schedule_ready = file.read()
                        with open(file_path, "w", encoding='utf-8-sig') as file:
                            file.write(schedule_ready)
                        with open(file_path, "r", encoding='utf-8-sig') as file:
                            lines = file.read().splitlines()
                    else:
                        isSchedule_ = True

                for i in range(len(lines)):
                    complete_ = lines[i].split(":")
                    for j in range(len(complete_)):
                        if cla == 'one':
                            if j < 3:
                                cla_schedule += complete_[j] + ":"
                            if j == 3:
                                cla_schedule += complete_[3] + "\n"
                        if cla == 'two':
                            if 3 < j < 7:
                                cla_schedule += complete_[j] + ":"
                            if j == 7:
                                cla_schedule += complete_[7] + "\n"
            print('id_cla', id_cla)
            #시작 스케쥴 파악하기
            forBreak = False
            schedule_ = cla_schedule.split("\n")
            schedule_ = ' '.join(schedule_).split()
            print("schedule_", schedule_)
            for i in range(len(schedule_)):
                schedule_2 = schedule_[i].split(":")
                for j in range(len(schedule_2)):
                    if schedule_2[3] != "완료":
                        forBreak = True
                        print("대기중인 첫번째", i)
                        start_ = i
                        break
                if forBreak == True:
                    break
            print("start!", start_)
            start = schedule_[start_].split(":")
            start = ' '.join(start).split()
            print("start[1]!", start[1])

            dunjeon_spl_re = "none"
            if '_' in start[2]:
                dunjeon_spl_ = start[2].split("_")
                print("dunjeon_spl_[0]", dunjeon_spl_[0])
                print("dunjeon_spl_[1]", dunjeon_spl_[1])
                dunjeon_spl_re = dunjeon_spl_[0]

            if start[2] == '미드가르드' or start[2] == '요툰하임':
                now_ing = 'maul'
            elif start[2] == '공허' or dunjeon_spl_re == '공허':
                now_ing = 'gonghu'
            elif start[2] == '난쟁이' or dunjeon_spl_re == '난쟁이':
                now_ing = 'nanjang'
            elif start[2] == '지하감옥' or dunjeon_spl_re == '지하감옥':
                now_ing = 'underprison'
            elif start[2] == '요툰육성' or start[2] == '니다육성':
                now_ing = 'grow'
            else:
                now_ing = 'jadong'





###################################################################################################

        else:
            print('파일 없당')
            if os.path.isdir(dir_path) == True:
                print('디렉토리 존재함')
                with open(file_path3, "r", encoding='utf-8-sig') as file:
                    shcedule = file.read().splitlines()
                with open(file_path, "w", encoding='utf-8-sig') as file:
                    file.write(shcedule)
                    myQuest_play_check(cla, data)
            else:
                print('디렉토리 존재하지 않음')
                os.makedirs(dir_path)
                with open(file_path3, "r", encoding='utf-8-sig') as file:
                    shcedule = file.read().splitlines()
                with open(file_path, "w", encoding='utf-8-sig') as file:
                    file.write(shcedule)
                    myQuest_play_check(cla, data)

        return start, start_, refresh_, now_ing
    except Exception as e:
        print(e)
        return 0


def myQuest_play_add(cla, data):
    try:
        import os.path
        from datetime import datetime
        from datetime import date, timedelta
        from chango import go_chango
        newCharacter = True
        add = True
        # cla는 몇번째 클라우드인지...
        print(cla)
        print(data)
        if data == 'gonghu':
            clear_mission = '공허'
        elif data == 'nanjang':
            clear_mission = '난쟁이'
            # go_chango(cla, 'in')
        elif data == 'underprison':
            clear_mission = '지하감옥'
        else:
            clear_mission = data
        print("점검_____________19_______________", cla)
        if cla == 'one':
            clalal_ = 'One'
            cla_start = v_.one_cla_start
        if cla == 'two':
            clalal_ = 'Two'
            cla_start = v_.two_cla_start

        start_ = cla_start
        nowDay_ = datetime.today().strftime("%Y%m%d")
        nowDay = int(nowDay_)
        nowTime = int(datetime.today().strftime("%H"))
        yesterday_ = date.today() - timedelta(1)
        yesterday = int(yesterday_.strftime('%Y%m%d'))



        dir_path = "C:\\my_games\\coobcco2"
        file_path = dir_path + "\\odin_schedule\\schedule.txt"
        file_path2 = dir_path + "\\odin_schedule\\quest.txt"
        file_path3 = dir_path + "\\odin_schedule\\schedule2.txt"
        file_path13 = dir_path + "\\odin_schedule\\refresh_time.txt"

        isRefresh = False
        while isRefresh is False:
            if os.path.isfile(file_path13) == True:
                with open(file_path13, "r", encoding='utf-8-sig') as file:
                    isRefresh = True
                    refresh_time = file.read()
                    print("refresh_time", refresh_time)
            else:
                with open(file_path13, "w", encoding='utf-8-sig') as file:
                    file.write(str(6))

        if nowTime >= int(refresh_time):
            nowDay = str(nowDay)
            print("1", nowDay)
        else:
            nowDay = yesterday
            nowDay = str(nowDay)
            print("2", nowDay)

        if os.path.isdir(dir_path) == True:
            print('디렉토리 존재')
        else:
            os.makedirs(dir_path)

        if os.path.isfile(file_path2) == True:
            # 파일 읽기
            with open(file_path2, "r", encoding='utf-8-sig') as file:
                lines2 = file.read().splitlines()
            day_ = lines2[0].split(":")
            print("lines", lines2)
            print("day_", day_)
            print("day_[0]", day_[0])
        else:
            print('없다')

            isNowday = False
            while isNowday is False:
                if os.path.isfile(file_path2) == True:
                    with open(file_path2, "r", encoding='utf-8-sig') as file:
                        isNowday = True
                        lines2 = file.read().splitlines()
                        day_ = lines2[0].split(":")
                        print("day_", day_)
                else:
                    with open(file_path2, "w", encoding='utf-8-sig') as file:
                        file.write(str(nowDay) + ":" + str(refresh_time) + "\n")

            # with open(file_path2, "w", encoding='utf-8-sig') as file:
            #     file.write(str(nowDay) + ":" + str(refresh_time) + "\n")
            # with open(file_path2, "r", encoding='utf-8-sig') as file:
            #     lines2 = file.read().splitlines()
            #     day_ = lines2[0].split(":")




        if day_[0] == nowDay:
            print("nowDay ing good")
            # 스케쥴 관련

            cla_schedule1 = ""
            cla_schedule2 = ""
            if os.path.isfile(file_path) == True:
                print("3_", nowDay)
                # 파일 읽기
                with open(file_path, "r", encoding='utf-8-sig') as file:
                    lines = file.read().splitlines()
                    lines = ' '.join(lines).split()

                    isSchedule_ = False
                    while isSchedule_ is False:
                        if lines == [] or lines == "":
                            print("스케쥴이 비었다 : myQuest_grow_check")
                            with open(file_path3, "r", encoding='utf-8-sig') as file:
                                schedule_ready = file.read()
                            with open(file_path, "w", encoding='utf-8-sig') as file:
                                file.write(schedule_ready)
                            with open(file_path, "r", encoding='utf-8-sig') as file:
                                lines = file.read().splitlines()
                        else:
                            isSchedule_ = True

                    for i in range(len(lines)):
                        complete_ = lines[i].split(":")
                        for j in range(len(complete_)):
                            if j < 3:
                                cla_schedule1 += complete_[j] + ":"
                            if j == 3:
                                cla_schedule1 += complete_[3] + "\n"
                            if 3 < j < 7:
                                cla_schedule2 += complete_[j] + ":"
                            if j == 7:
                                cla_schedule2 += complete_[7] + "\n"
                #여기서 현재 부분 체크...
                cla_schedule1_ = cla_schedule1.split("\n")
                cla_schedule2_ = cla_schedule2.split("\n")
                print('lines', lines)
                print('lines[0]', lines[0])
                print('cla_schedule1', cla_schedule1)
                print('cla_schedule2', cla_schedule2)
                print('cla_schedule1_[0]', cla_schedule1_[0])
                print('cla_schedule2_[0]', cla_schedule2_[0])
                if cla == 'one':
                    cla_schedule = cla_schedule1
                if cla == 'two':
                    cla_schedule = cla_schedule2
                # 시작 스케쥴 파악하기
                forBreak = False
                schedule_ = cla_schedule.split("\n")
                print("schedule_", schedule_)
                for i in range(len(schedule_)):
                    schedule_2 = schedule_[i].split(":")
                    for j in range(len(schedule_2)):
                        if schedule_2[3] != "완료":
                            forBreak = True
                            print("대기중인 첫번째", i)
                            start_ = i
                            break
                    if forBreak == True:
                        break
                print("start!", start_)
                start = schedule_[start_].split(":")
                start = ' '.join(start).split()
                print("start[start_]!", start[1])
            # ############################################################################################################
            print('start', start)
            print('clear_mission', clear_mission)
            print('start', start[2])
            print('start[1]', start[1])
            print('clalal_', clalal_)
            print('start[0]', start[0])

            dunjeon_spl_re = "none"
            if '_' in start[2]:
                dunjeon_spl_ = start[2].split("_")
                print("dunjeon_spl_[0]", dunjeon_spl_[0])
                print("dunjeon_spl_[1]", dunjeon_spl_[1])
                dunjeon_spl_re = dunjeon_spl_[0]
            else:
                dunjeon_spl_re = start[2]

            if clear_mission == dunjeon_spl_re and clalal_ == start[0]:

                if cla == 'one':
                    v_.one_cla_ing = 'check'
                    start_re = start[0] + ":" + start[1] + ":" + start[2] + ":" + '완료' + ":" + cla_schedule2_[start_]
                if cla == 'two':
                    v_.two_cla_ing = 'check'
                    start_re = cla_schedule1_[start_] + ":" + start[0] + ":" + start[1] + ":" + start[2] + ":" + '완료'

                print("start_re", start_re)

                print('lines111', lines)
                del lines[start_]
                lines.insert(start_, start_re)
                print('lines222', lines)

                last_result = ""
                for i in range(len(lines)):
                    last_result += lines[i] + "\n"
                print('lines333', last_result)

                with open(file_path, "w", encoding='utf-8-sig') as file:
                    file.write(last_result)
            else:
                print("아직 미션 진행중")
        else:

            myQuest_number_check(cla, 'refresh')

            # with open(file_path2, "w", encoding='utf-8-sig') as file:
            #     file.write(str(nowDay) + ":" + str(refresh_time) + "\n")
            # with open(file_path3, "r", encoding='utf-8-sig') as file:
            #     shcedule = file.read().splitlines()
            # with open(file_path, "w", encoding='utf-8-sig') as file:
            #     file.write(shcedule)
            # isEmpty = False
            # while isEmpty is False:
            #     with open(file_path, "r", encoding='utf-8-sig') as file:
            #         refresh_scheduel = file.read()
            #     if refresh_scheduel == "" or refresh_scheduel == []:
            #         print("empty")
            #         with open(file_path3, "r", encoding='utf-8-sig') as file:
            #             shcedule = file.read().splitlines()
            #         with open(file_path, "w", encoding='utf-8-sig') as file:
            #             file.write(shcedule)
            #     else:
            #         isEmpty = True
            #         print("refresh_scheduel", refresh_scheduel)

            if datetime.today().weekday() == 0:

                with open(file_path2, "w", encoding='utf-8-sig') as file:
                    file.write(str(nowDay) + ":" + str(refresh_time) + "\n")
                    # 새로 갱신이니 1번 캐릭 선택으로...and 스케쥴 초기화 tttttttttttttttttttttttttttttttttttttttttttt
                    print("새로 갱신..and 스케쥴 초기화")
                    reset_schedule_ = ""
                    with open(file_path, "r", encoding='utf-8-sig') as file:
                        lines = file.read().splitlines()
                        lines = ' '.join(lines).split()

                        isSchedule_ = False
                        while isSchedule_ is False:
                            if lines == [] or lines == "":
                                print("스케쥴이 비었다 : myQuest_play_check")
                                with open(file_path3, "r", encoding='utf-8-sig') as file:
                                    schedule_ready = file.read()
                                with open(file_path, "w", encoding='utf-8-sig') as file:
                                    file.write(schedule_ready)
                                with open(file_path, "r", encoding='utf-8-sig') as file:
                                    lines = file.read().splitlines()
                            else:
                                isSchedule_ = True

                        for i in range(len(lines)):
                            complete_ = lines[i].split(":")
                            for j in range(len(complete_)):
                                if j < 3:
                                    reset_schedule_ += complete_[j] + ":"
                                if j == 3:
                                    reset_schedule_ += '대기중:'
                                if 3 < j < 7:
                                    reset_schedule_ += complete_[j] + ":"
                                if j == 7:
                                    reset_schedule_ += "대기중\n"
                        print('reset_schedule_', reset_schedule_)
                        with open(file_path, "w", encoding='utf-8-sig') as file:
                            file.write(reset_schedule_)
                        with open(file_path3, "w", encoding='utf-8-sig') as file:
                            file.write(reset_schedule_)
            else:
                with open(file_path2, "w", encoding='utf-8-sig') as file:
                    file.write(str(nowDay) + ":" + str(refresh_time) + "\n")
                    # 새로 갱신이니 1번 캐릭 선택으로...and 스케쥴 초기화 tttttttttttttttttttttttttttttttttttttttttttt
                    print("새로 갱신..and 스케쥴 초기화")
                    reset_schedule_ = ""
                    with open(file_path, "r", encoding='utf-8-sig') as file:
                        lines = file.read().splitlines()
                        lines = ' '.join(lines).split()

                        isSchedule_ = False
                        while isSchedule_ is False:
                            if lines == [] or lines == "":
                                print("스케쥴이 비었다 : myQuest_play_check")
                                with open(file_path3, "r", encoding='utf-8-sig') as file:
                                    schedule_ready = file.read()
                                with open(file_path, "w", encoding='utf-8-sig') as file:
                                    file.write(schedule_ready)
                                with open(file_path, "r", encoding='utf-8-sig') as file:
                                    lines = file.read().splitlines()
                            else:
                                isSchedule_ = True

                        for i in range(len(lines)):
                            complete_ = lines[i].split(":")
                            for j in range(len(complete_)):
                                if j < 3:
                                    reset_schedule_ += complete_[j] + ":"
                                if j == 3:

                                    if '_' in complete_[2]:
                                        dunjeon_spl_ = complete_[2].split("_")
                                        print("dunjeon_spl_[0]", dunjeon_spl_[0])
                                        print("dunjeon_spl_[1]", dunjeon_spl_[1])

                                        if dunjeon_spl_[0] == "지하감옥":
                                            reset_schedule_ += complete_[j] + ":"
                                        else:
                                            reset_schedule_ += '대기중:'
                                    else:
                                        reset_schedule_ += '대기중:'

                                    # if complete_[2] == "지하감옥":
                                    #     reset_schedule_ += complete_[j] + ":"
                                    # else:
                                    #     reset_schedule_ += '대기중:'
                                if 3 < j < 7:
                                    reset_schedule_ += complete_[j] + ":"
                                if j == 7:

                                    if '_' in complete_[6]:
                                        dunjeon_spl_ = complete_[6].split("_")
                                        print("dunjeon_spl_[0]", dunjeon_spl_[0])
                                        print("dunjeon_spl_[1]", dunjeon_spl_[1])

                                        if dunjeon_spl_[0] == "지하감옥":
                                            reset_schedule_ += complete_[j] + "\n"
                                        else:
                                            reset_schedule_ += "대기중\n"
                                    else:
                                        reset_schedule_ += "대기중\n"

                                    # if complete_[6] == "지하감옥":
                                    #     reset_schedule_ += complete_[j] + "\n"
                                    # else:
                                    #     reset_schedule_ += "대기중\n"

                        print('reset_schedule_', reset_schedule_)
                        with open(file_path, "w", encoding='utf-8-sig') as file:
                            file.write(reset_schedule_)
                        with open(file_path3, "w", encoding='utf-8-sig') as file:
                            file.write(reset_schedule_)

            myQuest_play_add(cla, data)

            # 새로 갱신이니 1번 캐릭 선택으로...and 스케쥴 초기화
            # 스케쥴 초기화 후 다시 진행
            v_.one_cla_count = 0
            v_.two_cla_count = 0
            v_.one_cla_ing = 'check'
            v_.two_cla_ing = 'check'
            v_.one_cla_get_event = False
            v_.two_cla_get_event = False
            # myQuest_number_check(cla, "new")
            # change_ = 1
            # characterChange(change_, cla)




        add_result = 'check'
        return add_result

    except Exception as e:
        print(e)
        return 0

def myQuest_grow_check(cla):
    try:
        import os.path

        print("myQuest_grow_check...")
        if cla == 'one':
            id_cla = v_.myId_1
            cla_start = v_.one_cla_start
        if cla == 'two':
            id_cla = v_.myId_2
            cla_start = v_.two_cla_start
        id_cla = str(id_cla)
        start_ = cla_start



        dir_path = "C:\\my_games\\coobcco2"
        file_path = dir_path + "\\odin_schedule\\schedule.txt"
        file_path2 = dir_path + "\\odin_schedule\\quest.txt"
        file_path3 = dir_path + "\\odin_schedule\\schedule2.txt"



        #스케쥴 관련
        cla_schedule = ""
        if os.path.isfile(file_path) == True:
            print("grow_read")
            # 파일 읽기
            with open(file_path, "r", encoding='utf-8-sig') as file:
                lines = file.read().splitlines()

                isSchedule_ = False
                while isSchedule_ is False:
                    if lines == [] or lines == "":
                        print("스케쥴이 비었다 : myQuest_grow_check")
                        with open(file_path3, "r", encoding='utf-8-sig') as file:
                            schedule_ready = file.read()
                        with open(file_path, "w", encoding='utf-8-sig') as file:
                            file.write(schedule_ready)
                        with open(file_path, "r", encoding='utf-8-sig') as file:
                            lines = file.read().splitlines()
                    else:
                        isSchedule_ = True


                for i in range(len(lines)):
                    complete_ = lines[i].split(":")
                    for j in range(len(complete_)):
                        if cla == 'one':
                            if j < 3:
                                cla_schedule += complete_[j] + ":"
                            if j == 3:
                                cla_schedule += complete_[3] + "\n"
                        if cla == 'two':
                            if 3 < j < 7:
                                cla_schedule += complete_[j] + ":"
                            if j == 7:
                                cla_schedule += complete_[7] + "\n"
            print('id_cla', id_cla)
            #시작 스케쥴 파악하기
            forBreak = False
            schedule_ = cla_schedule.split("\n")
            schedule_ = ' '.join(schedule_).split()
            print("schedule_", schedule_)
            for i in range(len(schedule_)):
                schedule_2 = schedule_[i].split(":")
                for j in range(len(schedule_2)):
                    if schedule_2[3] != "완료":
                        forBreak = True
                        print("대기중인 첫번째", i)
                        start_ = i
                        break
                if forBreak == True:
                    break
            print("start!", start_)
            start = schedule_[start_].split(":")
            start = ' '.join(start).split()
            print("start[1]!", start[1])

        print("myQuest_grow_check : ", start)
        return start
    except Exception as e:
        print(e)
        return 0


def start_id_search(cla, data):
    try:
        import os.path
        from datetime import datetime
        from datetime import date, timedelta

        newstart_ = 1


        # 닉네임 받아와서 전역변수 설정하기
        nowDay_ = datetime.today().strftime("%Y%m%d")
        nowDay = int(nowDay_)
        nowTime = int(datetime.today().strftime("%H"))
        yesterday_ = date.today() - timedelta(1)
        yesterday = int(yesterday_.strftime('%Y%m%d'))



        dir_path = "C:\\my_games\\coobcco2"
        file_path = dir_path + "\\odin_schedule\\schedule.txt"
        file_path2 = dir_path + "\\odin_schedule\\quest.txt"
        file_path3 = dir_path + "\\odin_schedule\\schedule2.txt"
        file_path13 = dir_path + "\\odin_schedule\\refresh_time.txt"

        isRefresh = False
        while isRefresh is False:
            if os.path.isfile(file_path13) == True:
                with open(file_path13, "r", encoding='utf-8-sig') as file:
                    isRefresh = True
                    refresh_time = file.read()
                    print("refresh_time", refresh_time)
            else:
                with open(file_path13, "w", encoding='utf-8-sig') as file:
                    file.write(str(6))


        if nowTime >= int(refresh_time):
            nowDay = str(nowDay)
            print("1 : 퀘스트 갱신된 상황이라 체크 후 진행", nowDay)
        else:
            nowDay = yesterday
            nowDay = str(nowDay)
            print("날짜가 다르다")
            print("2 : 퀘스트 갱신되기 전이라 그냥 진행", nowDay)

        #스케쥴 초기화 관련 ttttttttttttttttttttttttttttttttt
        if os.path.isfile(file_path2) == True:
            print("3", nowDay)
            # 파일 읽기
            with open(file_path2, "r", encoding='utf-8-sig') as file:
                lines2 = file.read().splitlines()
                day_ = lines2[0].split(":")
            if day_[0] == nowDay:
                print("nowDay ing good")
            else:

                myQuest_number_check(cla, 'refresh')

                if datetime.today().weekday() == 0:

                    with open(file_path2, "w", encoding='utf-8-sig') as file:
                        file.write(str(nowDay) + ":" + str(refresh_time) + "\n")
                    print("hello")
                    # 새로 갱신이니 1번 캐릭 선택으로...and 스케쥴 초기화
                    print("새로 갱신이니 1번 캐릭 선택으로...and 스케쥴 초기화____")
                    #######초기화 부분 1번 읽고 3번으로 모두 대기중으로 저장하기#######################

                    #################################
                    reset_schedule_ = ""
                    with open(file_path, "r", encoding='utf-8-sig') as file:
                        lines = file.read().splitlines()
                        lines = ' '.join(lines).split()

                        isSchedule_ = False
                        while isSchedule_ is False:
                            if lines == [] or lines == "":
                                print("스케쥴이 비었다 : myQuest_grow_check")
                                with open(file_path3, "r", encoding='utf-8-sig') as file:
                                    schedule_ready = file.read()
                                with open(file_path, "w", encoding='utf-8-sig') as file:
                                    file.write(schedule_ready)
                                with open(file_path, "r", encoding='utf-8-sig') as file:
                                    lines = file.read().splitlines()
                            else:
                                isSchedule_ = True

                        for i in range(len(lines)):
                            complete_ = lines[i].split(":")
                            for j in range(len(complete_)):
                                if j < 3:
                                    reset_schedule_ += complete_[j] + ":"
                                if j == 3:
                                    reset_schedule_ += '대기중:'
                                if 3 < j < 7:
                                    reset_schedule_ += complete_[j] + ":"
                                if j == 7:
                                    reset_schedule_ += "대기중\n"
                        print('reset_schedule_', reset_schedule_)
                    with open(file_path, "w", encoding='utf-8-sig') as file:
                        file.write(reset_schedule_)
                    with open(file_path3, "w", encoding='utf-8-sig') as file:
                        file.write(reset_schedule_)
                else:
                    with open(file_path2, "w", encoding='utf-8-sig') as file:
                        file.write(str(nowDay) + ":" + str(refresh_time) + "\n")
                        # 새로 갱신이니 1번 캐릭 선택으로...and 스케쥴 초기화 tttttttttttttttttttttttttttttttttttttttttttt
                        print("새로 갱신..and 스케쥴 초기화")
                        reset_schedule_ = ""
                        with open(file_path, "r", encoding='utf-8-sig') as file:
                            lines = file.read().splitlines()
                            lines = ' '.join(lines).split()

                            isSchedule_ = False
                            while isSchedule_ is False:
                                if lines == [] or lines == "":
                                    print("스케쥴이 비었다 : myQuest_play_check")
                                    with open(file_path3, "r", encoding='utf-8-sig') as file:
                                        schedule_ready = file.read()
                                    with open(file_path, "w", encoding='utf-8-sig') as file:
                                        file.write(schedule_ready)
                                    with open(file_path, "r", encoding='utf-8-sig') as file:
                                        lines = file.read().splitlines()
                                else:
                                    isSchedule_ = True

                            for i in range(len(lines)):
                                complete_ = lines[i].split(":")
                                for j in range(len(complete_)):
                                    if j < 3:
                                        reset_schedule_ += complete_[j] + ":"
                                    if j == 3:

                                        if '_' in complete_[2]:
                                            dunjeon_spl_ = complete_[2].split("_")
                                            print("dunjeon_spl_[0]", dunjeon_spl_[0])
                                            print("dunjeon_spl_[1]", dunjeon_spl_[1])

                                            if dunjeon_spl_[0] == "지하감옥":
                                                reset_schedule_ += complete_[j] + ":"
                                            else:
                                                reset_schedule_ += '대기중:'
                                        else:
                                            reset_schedule_ += '대기중:'

                                        # if complete_[2] == "지하감옥":
                                        #     reset_schedule_ += complete_[j] + ":"
                                        # else:
                                        #     reset_schedule_ += '대기중:'
                                    if 3 < j < 7:
                                        reset_schedule_ += complete_[j] + ":"
                                    if j == 7:

                                        if '_' in complete_[6]:
                                            dunjeon_spl_ = complete_[6].split("_")
                                            print("dunjeon_spl_[0]", dunjeon_spl_[0])
                                            print("dunjeon_spl_[1]", dunjeon_spl_[1])

                                            if dunjeon_spl_[0] == "지하감옥":
                                                reset_schedule_ += complete_[j] + "\n"
                                            else:
                                                reset_schedule_ += "대기중\n"
                                        else:
                                            reset_schedule_ += "대기중\n"

                                        # if complete_[6] == "지하감옥":
                                        #     reset_schedule_ += complete_[j] + "\n"
                                        # else:
                                        #     reset_schedule_ += "대기중\n"

                            print('reset_schedule_', reset_schedule_)
                            with open(file_path, "w", encoding='utf-8-sig') as file:
                                file.write(reset_schedule_)
                            with open(file_path3, "w", encoding='utf-8-sig') as file:
                                file.write(reset_schedule_)
                v_.one_cla_count = 0
                v_.two_cla_count = 0
                v_.one_cla_ing = 'check'
                v_.two_cla_ing = 'check'
                v_.one_cla_get_event = False
                v_.two_cla_get_event = False
                # myQuest_number_check(cla, "new")


        else:
            with open(file_path2, "w", encoding='utf-8-sig') as file:
                file.write(str(nowDay) + ":" + str(refresh_time) + "\n")

        #스케쥴 관련
        cla_schedule = ""
        if os.path.isfile(file_path) == True:
            print("3_", nowDay)
            # 파일 읽기
            with open(file_path, "r", encoding='utf-8-sig') as file:
                lines = file.read().splitlines()

                isSchedule_ = False
                while isSchedule_ is False:
                    if lines == [] or lines == "":
                        print("스케쥴이 비었다 : myQuest_grow_check")
                        with open(file_path3, "r", encoding='utf-8-sig') as file:
                            schedule_ready = file.read()
                        with open(file_path, "w", encoding='utf-8-sig') as file:
                            file.write(schedule_ready)
                        with open(file_path, "r", encoding='utf-8-sig') as file:
                            lines = file.read().splitlines()
                    else:
                        isSchedule_ = True

                for i in range(len(lines)):
                    complete_ = lines[i].split(":")
                    for j in range(len(complete_)):
                        if cla == 'one':
                            if j < 3:
                                cla_schedule += complete_[j] + ":"
                            if j == 3:
                                cla_schedule += complete_[3] + "\n"
                        if cla == 'two':
                            if 3 < j < 7:
                                cla_schedule += complete_[j] + ":"
                            if j == 7:
                                cla_schedule += complete_[7] + "\n"
            #시작 스케쥴 파악하기
            forBreak = False
            schedule_ = cla_schedule.split("\n")
            schedule_ = ' '.join(schedule_).split()
            print("schedule_", schedule_)
            for i in range(len(schedule_)):
                schedule_2 = schedule_[i].split(":")
                for j in range(len(schedule_2)):
                    if schedule_2[3] != "완료":
                        forBreak = True
                        print("대기중인 첫번째", i)
                        start_ = i
                        break
                if forBreak == True:
                    break
            print("start!", start_)
            start = schedule_[start_].split(":")
            start = ' '.join(start).split()
            print("start[1]!", start[1])
            # start[1] 이걸로 처음 시작하면 됨.
            newstart_ = int(start[1])



###################################################################################################

        else:
            print('파일 없당')
            if os.path.isdir(dir_path) == True:
                print('디렉토리 존재함')
                if os.path.isfile(file_path3) == True:
                    with open(file_path3, "r", encoding='utf-8-sig') as file:
                        shcedule = file.read().splitlines()
                    with open(file_path, "w", encoding='utf-8-sig') as file:
                        file.write(shcedule)
                else:
                    data = "One:1:각종템받기:대기중\n"

                    with open(file_path3, "w", encoding='utf-8-sig') as file:
                        file.write(data)
                    with open(file_path3, "r", encoding='utf-8-sig') as file:
                        shcedule = file.read().splitlines()
                    with open(file_path, "w", encoding='utf-8-sig') as file:
                        file.write(shcedule)
            else:
                print('디렉토리 존재하지 않음')
                os.makedirs(dir_path)
                data = "One:1:각종템받기:대기중\n"

                with open(file_path3, "w", encoding='utf-8-sig') as file:
                    file.write(data)
                with open(file_path3, "r", encoding='utf-8-sig') as file:
                    shcedule = file.read().splitlines()
                with open(file_path, "w", encoding='utf-8-sig') as file:
                    file.write(shcedule)

        return newstart_
    except Exception as e:
        print(e)
        return 0


