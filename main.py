# ДЗ
# Фраз: ну я типо вообще короче не понимаю этот язык
# 1) способ
stop_words = ['ну','типо','короче']
temp = []
message = input('Введите сообщение: ')
lst = message.split() # все слова
for item in lst:
    if item not in stop_words:
        temp.append(item)
res = sorted(temp)
for a,b in enumerate(res, 1):
    print(f'{a}. {b}')

# 2) способ