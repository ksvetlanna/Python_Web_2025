# CRON имя скрипта и когда он будет рассылаться
# Переодические задачи
#pip install schedule
#pip freeze > requirements.txt

import schedule
import datetime

i = 1 #глобальная переменная, менять нельзя!!!!!!!!!

def job():
    global i
    print(f'Скрипт запустился {i} - раз')
    i += 1
    t = datetime.datetime.now()
    print('Время:', t.strftime('%H:%M:%S'))


schedule.every(3).seconds.do(job)
# сделать по рассписанию каждые 3 сек возвращает время


while True: #запуск
    schedule.run_pending() #отслеживать выполнение (запускать)