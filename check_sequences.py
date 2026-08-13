import os, os.path, sys
import openpyxl

SEQUENCES = [['E', 1104],
             ['I',  682],
             ['M', 1086],
             ['Q',  669],
             ['U', 1113],
             ['Y', 1120],
             ['AC',1110],
             ['AG',1118]]

WB_NAME = r'C:\Users\gslin\OneDrive\DAnn\battelle.xlsx'

wb = openpyxl.load_workbook(WB_NAME)
ws = wb['Scaled Scores']

for column, end_row in SEQUENCES:
    print(f'Looking at column {column} rows 5 - {end_row}')
    value = 0
    for row_number in range(5,end_row):
        #print(f'{column}-{row_number}')
        next_value = ws[f'{column}{row_number}'].value
        if next_value <= value:
            print(f'Column {column} Row {row_number} {value} {next_value}')
        value = next_value

print('Done')
    
