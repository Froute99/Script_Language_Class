
import os
import random

folder_no = 0

ext = ['doc', 'ppt', 'pdf', 'hwp', 'jpg']

def make_random_folders(count):
    global folder_no

    if not count: return

    os.mkdir(f'folder{folder_no}')
    # 하나는 만들어졌다
    os.chdir(f'folder{folder_no}')
    count -= 1

    # 랜덤 파일로 채운다
    # 파일 이름을 만든다
    random_files = [f'file_{folder_no}_{i}.{random.choice(ext)}' for i in range(10)]
    for fn in random_files:
        f = open(fn, 'w')
        f.write('Auto Generated File')
        f.close()

    folder_no += 1


    # 남은 갯수만큼, 아래에 폴더를 랜덤하게 만든다
    while count:
        subcount = random.randint(0, count)
        make_random_folders(subcount)
        count -= subcount

    os.chdir('..')


import zipfile
import datetime

def zip_jpg_files():
    photo_zip = zipfile.ZipFile('photo.zip', 'w')
    for root, subfolders, files in os.walk('./folder0'):
        for file in files:
            if file.endswith('.jpg'):
                abs_path = root + '/' + file
                ctime = os.path.getctime(abs_path)
                cdate = datetime.datetime.fromtimestamp(ctime).strftime('%y%m%d')
                file = file.replace('.jpg', f'_{cdate}.jpg')
                photo_zip.write(abs_path, file, compress_type=zipfile.ZIP_DEFLATED)

    photo_zip.close()

# make_random_folders(100)
zip_jpg_files()

