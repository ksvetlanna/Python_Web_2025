# ДЗ
# Фраз: ну я типо вообще короче не понимаю этот язык
# 2) способ
stop_words = {'ну','типо','короче'}
message = input('Введите сообщение: ')
lst = message.split() # все слова
res = sorted(set(lst) - stop_words)
for a,b in enumerate(res, 1):
    print(f'{a}. {b}')