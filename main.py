# ДЗ
# Фраз: ну, я типо, вообще- короче, не понимаю этот язык!
# 2) способ
commas = (',','!','.','-','?')
stop_words = {'ну','типо','короче','не'}
message = input('Введите сообщение: ')
for z in commas:
    message = message.replace(z, '')
lst = message.split() # все слова
res = sorted(set(lst) - stop_words)
for a,b in enumerate(res, 1):
    print(f'{a}. {b}')