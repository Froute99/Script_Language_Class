
import os
import random
import datetime
import exrex
import zipfile
import shutil

filename_convention = r'[a-z][A-Z][0-9]{10}'
extensions = r'doc|ppt|pdf|hwp|jpg'

recursion_limit = 10


def make_random_folder(recursion_count):
    if recursion_count == recursion_limit:
        return

    all_files = os.listdir()
    folders = []
    for folder_name in all_files:
        if os.path.isdir(folder_name):
            folders.append(folder_name)

    random_number = random.randint(0, 3)
    if random_number == 0:      # in
        if folders:
            filename = folders[random.randint(0, len(folders) - 1)]
            os.chdir(filename)
    elif random_number == 1:
        filename = exrex.getone(filename_convention)
        os.makedirs(filename, exist_ok=True)
    else:                       # create file
        open(exrex.getone(filename_convention) + '.' + exrex.getone(extensions), 'w')

    recursion_count += 1
    make_random_folder(recursion_count)


def zip_jpg():
    zf = zipfile.ZipFile('final.zip', 'a')
    for root, subfolders, filenames in os.walk('.'):
        for file in filenames:
            if file.endswith('.jpg'):
                abspath = os.path.abspath(file)
                create_time = os.path.getctime(abspath)
                timestamp = datetime.datetime.fromtimestamp(create_time).strftime('%y%m%d')
                filename = file.split('.')
                result_name = filename[0] + '_' + timestamp + '.' + filename[1]
                shutil.copy(abspath, result_name)
                zf.write(result_name, compress_type=zipfile.ZIP_DEFLATED)

    zf.close()


os.makedirs('root_folder', exist_ok=True)
os.chdir('root_folder')

make_random_folder(0)
zip_jpg()

