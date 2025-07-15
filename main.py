# Декораторы

def answer(question):
    return 'думайте сами'

def dialog():
    def answer(question):
        if question.lower().startswith('когда'):
            return 'Никогда'
        else:
            return 'Упппс'

    question = input()
    while question != '':
         print(answer(question))
         question = input()

dialog()
