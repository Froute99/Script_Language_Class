
import os
import shelve

data = shelve.open('data')

for root, subfolders, filenames in os.walk('C:\Program Files\JetBrains\PyCharm Community Edition 2021.3.2'):
    for filename in filenames:
        file_path = os.path.join(root, filename)
        size = os.path.getsize(file_path)
        #print(f'{size}'.ljust(15), file_path)
        #data['size'] = size
        #data['path'] = file_path
        data = {size, file_path}

result = sorted(data.items(), key=lambda x: x[1], reverse=True)
