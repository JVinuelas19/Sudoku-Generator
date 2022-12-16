from random import randint
import time
import sys

sequence = [1,2,3,4,5,6,7,8,9]
rows, columns, blocks = [], [], []

for i in range(9):
    rows.append([]), columns.append([]), blocks.append([])

tic = time.time()
for row in rows:
    needs_reset = True
    reset = False
    while needs_reset is True:
        for column in columns:
            is_valid = False
            pool = [1,2,3,4,5,6,7,8,9]
            while(is_valid is False):
                try:
                    index = randint (0, len(pool)-1)
                    if pool[index] in column or pool[index] in row:
                        pool.pop(index)             
                    else:
                        number = pool[index]
                        column.append(number)
                        row.append(number)
                        is_valid = True
                except:
                    print('Rollback')
                    #Hacer reset de columnas y de fila
                    reset = True
                    row.clear()
                    for i in range(columns.index(column)):
                        selected_column = columns[i]
                        selected_column.pop(-1)
                        print(selected_column)
                    break
                    #sys.exit()
            if reset is True:
                break        
        if reset is False:
            print (f'La fila {rows.index(row)} es:{row}')
            needs_reset = False
            reset = False
        else:
            reset = False

toc = time.time()
print(f'El sudoku se ha generado en {round((toc-tic), 4)} segundos y es:')
for row in rows:
    print (row)

