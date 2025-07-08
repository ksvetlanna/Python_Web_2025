# сериализация и десериализация (процесс преобразования сложных структур)
# сохранение

'''import pickle #Процесс консервирования
d = {
    'стол': 'table',
    'стул': 'chair'
}
# сериализация
with open('dictfile.dat','wb') as p:
    pickle.dump(d, p) # 'd' что будем сериализовать и куда - 'p'
# должен появится файл в корневом коталоге
'''


# десериализация
import pickle
import pprint
with open('dictfile.dat','rb') as p:
    d = pickle.load(p) # 'd' что будем сериализовать и куда - 'p'
pprint.pprint(d, width=15)