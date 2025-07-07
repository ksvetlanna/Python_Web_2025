# Внешние библиотеки
# Графика
# Word - DOCX (python-docx)
# pip freeze > requirements.txt - создание файла зависимости
# pip install -r requirements.txt - установка списка библиотек

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Cm, Inches, Mm, Pt # для размера см, дюймы, мм, поинт

doc = Document() # создание экземпляра документа

#добавили одину пустую строку
paragraph = doc.add_paragraph()
# Добавление заголовка
doc.add_heading('Отчет за месяц', 1) # заголовок 1го уровня

#Добавляем абзац
paragraph = doc.add_paragraph('В этом отчете представлены')

# что-то добавляем в абзац
paragraph.add_run(' ключевые показатели').bold = True # делаем жирным

#добавили одину пустую строку
paragraph = doc.add_paragraph()
paragraph_format = paragraph.paragraph_format

#ненумерованный
paragraph = paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
paragraph = doc.add_paragraph('Первый пункт', style='list Bullet')
paragraph = doc.add_paragraph('Второй пункт', style='list Bullet')

#нумерованный
paragraph = paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
paragraph = doc.add_paragraph('Первый пункт', style='list Number')
paragraph = doc.add_paragraph('Второй пункт', style='list Number')



#Добавляем таблицу
table = doc.add_table(rows=3, cols=3)
#Заполняем
for i,row in enumerate(table.rows):
    for j, cell in enumerate(table.columns()):
        cell.text = f'Строка {i+1}, Столбец {j+1}'


doc.add_paragraph()
doc.add_picture('images/sunny_day.jpg', width=Mm(105))
doc.save('docs/report.docx')