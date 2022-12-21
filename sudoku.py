from random import randint
import time
import re

def insert_into_block(row, column, blocks):
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

def gen_9x9_sudoku(print_me):
    rows, columns, blocks = [], [], []
    for i in range(9):
        rows.append([]), columns.append([]), blocks.append([])

    sudoku_reset = True
    while sudoku_reset is True:
        regen = False
        tic = time.time()
        for row in rows:
            reset = False
            row_index = rows.index(row)
            row_reset = True
            while row_reset is True:
                for column in columns:
                    column_index = columns.index(column)
                    block = insert_into_block(row_index, column_index, blocks)
                    #Calcular current block de blocks
                    column_reset = True
                    pool = [1,2,3,4,5,6,7,8,9]
                    while(column_reset is True):
                        try:
                            index = randint (0, len(pool)-1)
                            if pool[index] in column or pool[index] in row or pool[index] in block:
                                pool.pop(index)             
                            else:
                                number = pool[index]
                                column.append(number)
                                row.append(number)
                                block.append(number)
                                column_reset = False
                        except:
                            
                            if time.time()-tic>0.011:
                                rows.clear(), columns.clear(), blocks.clear()
                                #After the clear we need to reset the lists, otherwise the algoritm will get stuck
                                for i in range(9):
                                    rows.append([]), columns.append([]), blocks.append([])
                                regen = True
                            else:
                                row.clear()
                                for i in range(column_index):
                                    block = insert_into_block (row_index, i, blocks)
                                    block.pop(-1)
                                    selected_column = columns[i]
                                    selected_column.pop(-1)
                            reset = True
                            break
                            #sys.exit()
                    if reset is True:
                        break  

                if reset is False:
                    row_reset = False
                    if row_index == 8:
                        sudoku_reset = False
                elif reset is True and regen is False:
                    reset = False
                else:
                    break
            if regen is True:
                break
    if print_me is True:
        for row in rows:
            print(row)

    toc = time.time()
    #print(f'El sudoku se ha generado en {round((toc-tic), 4)} segundos y es:')
    #for row in rows:
    #    print (row)
    return rows

def gen_6x6_sudoku():
    rows, columns, blocks = [],[],[]
    for i in range(6):
        rows.append([]), columns.append([]), blocks.append([])

def gen_4x4_sudoku():
    rows, columns, blocks = [],[],[]
    for i in range(4):
        rows.append([]), columns.append([]), blocks.append([])

def export_sudokus(number, dimensions):
    try:
        tic = time.time()
        with open ('stuff/sudokus.txt', 'w') as sudokus:
            if dimensions == 9:
                for i in range (number):
                    rows = gen_9x9_sudoku(False)
                    for row in rows:
                        sudokus.write(str(row))
                        sudokus.write(',')
                    sudokus.write('\n')
            elif dimensions == 6:
                for i in range (number):
                    rows = gen_6x6_sudoku()
                    for row in rows:
                        sudokus.write(str(row))
                        sudokus.write(',')
                    sudokus.write('\n')
            elif dimensions == 4:
                for i in range (number):
                    rows = gen_4x4_sudoku()
                    for row in rows:
                        sudokus.write(str(row))
                        sudokus.write(',')
                    sudokus.write('\n')
        toc = time.time()
        print(f'{number} sudokus of {dimensions}x{dimensions} generated in {round(toc-tic , 2)}')
    except:
        print('Error. Dimensions must be 4, 6 or 9 and number of sudokus generated must be greater than zero.')

def read_sudokus(path):
    try:
        with open (f'{path}.txt', 'r') as sudokus:
            for i, line in enumerate(sudokus):
                formatted_sudoku = re.split('(?<=]),', line)
                formatted_sudoku.pop(-1)
                print(f'Sudoku {i+1}:')
                for row in formatted_sudoku:
                    print(row)

    except:
        print('Incorrect file or path.')

#We need to format using regex in order to avoid the 8] and 6[ characters. LookBehind and LookAfter regex makes this possible
def pick_sudoku(path):
    tic = time.time()
    try:
        MAX_SUDOKUS = number_of_sudokus(path)
        with open (f'{path}.txt', 'r') as sudokus:
            chosen = randint(0, MAX_SUDOKUS-1)
            for i, line in enumerate(sudokus):
                if(i == chosen):
                    formatted_sudoku = re.split('(?<=]),', line)
                    formatted_sudoku.pop(-1)
                    toc = time.time()
                    print(f'Time elapsed is {round(toc-tic, 5)} seconds')
                    print(f'The chosen sudoku is {i+1} between the {MAX_SUDOKUS} available:')
                    for row in formatted_sudoku:
                        print(row)
                    break
    except:
        print('Incorrect file or path.')

def number_of_sudokus(path):
    with open (f'{path}.txt', 'r') as sudokus:
        lines = sum(1 for line in sudokus)
        return lines

def main():
    while(True):
        option = input('Welcome to sudoku generator. What do you want to do?:\n1 - Generate a 9x9 sudoku\n2 - Generate a 6x6 sudoku'+
        '\n3 - Generate a 4x4 sudoku\n4 - Export sudokus to a txt file\n5 - Read sudokus from a txt file\n6 - Pick a random sudoku from a file\n'+
        '7 - Exit\nType your option: ')
        if option == '1':
            gen_9x9_sudoku(True)
        elif option == '2':
            gen_6x6_sudoku()
        elif option == '3':
            gen_4x4_sudoku()
        elif option == '4':
            number = input('How many sudokus do you want to generate?:')
            dimensions = input('Enter the dimensions of the sudoku [4 to gen a 4x4, 6 to gen a 6x6 or 9 to gen a 9x9]: ') 
            export_sudokus(int(number), int(dimensions))
        elif option == '5':
            path = input('Enter the path for the txt file you want to read from:')
            read_sudokus(path)
        elif option == '6':
            path = input('Enter the path for the txt file you want to read from:')
            pick_sudoku(path)  
        elif option == '7':
            print('See you soon!')
            quit()  
        else:
            print('Invalid option. Type a number (1, 2, 3, 4, 5 or 6) to continue ')

if __name__ == "__main__":
    main()