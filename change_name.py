import os

for dir_name in os.listdir('.'):
    if '_' in dir_name and '.py' not in dir_name:
        for file_name in os.listdir(dir_name):
            new_name = '-'.join(file_name.split('_')[:])
            print(file_name)
            os.rename(dir_name + '/' + file_name, dir_name + '/' + new_name)