# Библиотека pymorphy
# устанавливем в Terminal
# pip install pymorphy3 -сама pymorphy3
# pip install -U pymorphy3-dicts-ru - словарь
# pip freeze > requirements.txt

from pymorphy3 import MorphAnalyzer

form = MorphAnalyzer().parse('бутылка')[0]

for btl in reversed(range(99)):
    print(f'В холодильнике {btl + 1} {form.make_agree_with_number(btl + 1).word} пива')
    print('Возьмём одну и выпьем')
    if btl % 10 == 1 and btl != 11:
        remain = 'Осталась'
    else:
        remain = 'Осталось'
    print(f'{remain} {btl} {form.make_agree_with_number(btl).word} пива.')

