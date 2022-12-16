from random import randint
import time
import sys

rows, columns, blocks = [], [], []

def insert_into_block(row, column):
    if (row<3):
        if column<3:
            return blocks[0]
        elif column>=3 and column<6:
            return blocks[1]
        else:
            return blocks[2]
    elif row>=3 and row<6:
        if column<3:
            return blocks[3]
        elif column>=3 and column<6:
            return blocks[4]
        else:
            return blocks[5]
    else:
        if column<3:
            return blocks[6]
        elif column>=3 and column<6:
            return blocks[7]
        else:
            return blocks[8]

for i in range(9):
    rows.append([]), columns.append([]), blocks.append([])

tic = time.time()
for row in rows:
    needs_reset = True
    reset = False
    row_index = rows.index(row)
    while needs_reset is True:
        for column in columns:
            column_index = columns.index(column)
            block = insert_into_block(row_index, column_index)
            #Calcular current block de blocks
            is_valid = False
            pool = [1,2,3,4,5,6,7,8,9]
            while(is_valid is False):
                try:
                    index = randint (0, len(pool)-1)
                    if pool[index] in column or pool[index] in row or pool[index] in block:
                        pool.pop(index)             
                    else:
                        number = pool[index]
                        column.append(number)
                        row.append(number)
                        block.append(number)
                        is_valid = True
                except:
                    #Hacer reset de columnas y de fila
                   
                    if time.time()-tic>5:
                        print('Algoritm has reached an endless loop. Shutting down...')
                        sys.exit()
                    reset = True
                    row.clear()
                    for i in range(column_index):
                        block = insert_into_block (row_index, i)
                        block.pop(-1)
                        selected_column = columns[i]
                        selected_column.pop(-1)
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
