# Внешние библиотеки
# Документы по шаблону (template.docx)
# Word - DOCX (docxtpl)
# pip freeze > requirements.txt - создание файла зависимости
# pip install -r requirements.txt - установка списка библиотек
from docxtpl import DocxTemplate

# Загрузка шаблона
doc = DocxTemplate('Docs/template.docx')

# Данные для подстановки в шаблон
content = {
    'company': 'OOO "Монолит"',
    'employee': 'Петров Д.И.',
    'position': 'Менеджер',
    'date': '01/01/2025'
}

doc.render(content)
doc.save('docs/about.docx')