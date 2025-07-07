#Чтение данных
from openpyxl import load_workbook

wb = load_workbook('Docs/employees.xlsx')

ws = wb.active
rows_count = ws.max_row # число заполненных строк

for row in ws.iter_rows(values_only=True):
    fio, pos, dept = row
    print(f'Фамилия: {fio}, Должность: {pos}, Отдел: {dept}')