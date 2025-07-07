# Файлы и ОС - модуль
import os

path = os.getcwd() # get current working directory
os.chdir(path + '/images')

all_files = [f for f in os.listdir('.')] # выводим все что содержится в директории images

print(all_files)

