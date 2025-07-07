# Внешние библиотеки
# Документы по шаблону (template.docx)
# Excel (openpyxl)
#pip install openpyxl
#pip freeze > requirements.txt

#Пустой Excel -файл
'''from openpyxl import Workbook

wb = Workbook()

ws = wb.active
ws.title = 'Отчет'

wb.save('Docs/report.xlsx')'''

#Запись данных в существующий файл
from openpyxl import load_workbook

wb = load_workbook('Docs/report.xlsx')

ws = wb.active

#Заголовки
ws['A1'] = 'ФИО'
ws['B1'] = 'Должность'
ws['C1'] = 'Отдел'

#Данные
employees = [
    ['Ивано И.И.', 'Менеджер', 'Продажи'],
    ['Петров И.И.', 'Бухгалтер', 'Финансы'],
    ['Сидорова И.И.', 'Аналитик', 'ИТ',],
]

for row, data in enumerate(employees, start=2):
    ws.cell(row=row, column=1, value=data[0])
    ws.cell(row=row, column=2, value=data[1])
    ws.cell(row=row, column=3, value=data[2])
wb.save('Docs/employees.xlsx')