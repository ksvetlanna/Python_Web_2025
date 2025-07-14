# Zip (собрать в кучу все файл csv, поместить в архив и удалить)

'''from zipfile import ZipFile
import os

#
csv_files = [f for f in os.listdir() if f.endswith('.csv')]
#print(csv_files)
with ZipFile('arhive.zip', 'w') as myzip:
    for file in csv_files:
        myzip.write(file)
        os.remove(file)'''



#------------------------------------------------------------------------------------
# распаковать весь архив (файл arhive.zip)
'''from zipfile import ZipFile
import os

#files_to_extract = ['people.csv', 'file.csv'] # распаковать конкретные файлы из архива
with ZipFile('arhive.zip', 'r') as zip_obj:
    zip_obj.extractall()'''

#------------------------------------------------------------------------------------

from zipfile import ZipFile
import os

# получим список объектов находящихся в архиве arhive.zip
with ZipFile('arhive.zip', 'r') as zip_obj:
    print(zip_obj.namelist())