rowcount = 0
colcount = 0
rehi_ = 'none'
thisRow = 0
thisCol = 0
table_datas = ""
onCharacter = 0
onDunjeon = "none"
onHunt = "none"
onMaul = "none"

isgloballoop = False

# 기존 오토모드 관련###############################################
one_cla_id = "none"
one_cla_pw = "none"
two_cla_id = "none"
two_cla_pw = "none"
# 1번
mynumber_1 = 0
mylevel_1 = 0
mymoney_1 = 50000000
mypower_1 = 0
mypotion_1 = 0
gonghu_1 = False
nanjang_1 = False
underprison_1 = False
jadong_1 = False
myId_1 = 0
one_cla_count = 0
one_cla_ing = 'check'
# 2번
mynumber_2 = 0
mylevel_2 = 0
mymoney_2 = 50000000
mypower_2 = 0
mypotion_2 = 0
gonghu_2 = False
nanjang_2 = False
underprison_2 = False
jadong_2 = False
myId_2 = 0
two_cla_count = 0
two_cla_ing = 'check'
# 현재실행중인 클라우드
now_cla = 'none'
one_cla_start = 0
two_cla_start = 0
global_howcla = 'none'
change_ready_main = False
change_ready_step = False

one_now_growing_ = 'none'
two_now_growing_ = 'none'

one_in_dun_count = 0
two_in_dun_count = 0

one_cla_stop = 0
two_cla_stop = 0

potion_count = 0

dir_path = "C:\\my_games\\coobcco2\\data_od"
file_path = dir_path + "\\mymodule\\version.txt"
file_path2 = "C:\\my_games\\mouse\\port.txt"

with open(file_path, "r", encoding='utf-8-sig') as file:
    version_ = file.read()
    print("version???", version_)

with open(file_path2, "r", encoding='utf-8-sig') as file:
    my_mouse = file.read().splitlines()

    COM_ = my_mouse[0]
    speed_ = my_mouse[1]
    print("COM_???", COM_)
    print("speed_???", speed_)

this_game = "오딘"


# 아두이노 관련
now_arduino = "none"
# 마우스 관련
mouse_speed = 20
mouse_pm = 3