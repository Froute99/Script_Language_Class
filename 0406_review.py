# 어떤 자료구조를 사용할지 먼저 생각
# 파일 리스터

file_info = {}

# 폴더 search 파일을 찾아줌

import os

for root, subfolders, files in os.walk('C:/Python Environment'):
    for file in files:
        abs_path = root + '/' + file
        size = os.path.getsize(abs_path)
        file_info[abs_path] = size

print(file_info)

# sort
def get_key(x): return x[1]


file_info_list = [item for item in file_info.items()]
sorted_file_info_list = sorted(file_info_list, key=get_key, reverse=True)
