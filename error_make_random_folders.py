import os
import random
import logging
logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s')

folder_no = 0

ext = ['doc', 'ppt', 'pdf', 'hwp', 'jpg']

# quota 를 가지고서, 폴더에 들어간 후에, 남겨진 quota 를 다시 분배해서 들어가면 된다.


def make_random_folders(count):
    global folder_no

    if not count: return

    logging.info(f'created folder{folder_no}')

    os.mkdir(f'folder{folder_no}')
    os.chdir(f'folder{folder_no}')

    folder_no += 1
    count -= 1
    logging.info(os.getcwd())
    while count:
        subcount = random.randint(0, count)
        make_random_folders(subcount)
        count -= subcount
    os.chdir('../')       # 밖으로 빠져나오는게 없음(랜덤 구조가 만들어지지 않고 계속 deeper 해지는 이유)


report_home = 'C:/ScriptLang/Class/LabFolder'


def make_random_root_folder():
    os.mkdir('root_folder')
    os.chdir('root_folder')
    make_random_folders(10)
    os.chdir('..')


os.chdir(report_home)
make_random_root_folder()

