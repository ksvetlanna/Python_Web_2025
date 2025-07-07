# Внешние библиотеки
# Документы по шаблону (template.docx)
# Word - DOCX (docxtpl)
# pip freeze > requirements.txt - создание файла зависимости
# pip install -r requirements.txt - установка списка библиотек
from docxtpl import DocxTemplate

# Загрузка шаблона
doc = DocxTemplate('docs/template.docx')

# Данные для подстановки в шаблон
content = [
    {
        'company': 'OOO "Монолит"',
        'employee': 'Петров Д.И.',
        'position': 'Менеджер',
        'date': '01/01/2025'
    },
    {
        'company': 'OOO "Арсенал"',
        'employee': 'Иванов Д.И.',
        'position': 'Инженер',
        'date': '01/01/2025'
    }
]

count = 1
for item in content:
    doc.render(item)
    doc.save(f'docs/about{count}.docx')
    count += 1