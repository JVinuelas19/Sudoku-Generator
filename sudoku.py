from random import randint
import time
import re

def insert_into_block(row, column, blocks, dimensions):
    #9x9 block distribution
    if dimensions == 9:
        if row<3:
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

    #6x6 block_distribution
    elif dimensions == 6 :
        if row<2:
            if column<3:
                return blocks[0]
            else:
                return blocks[1]
        elif row>=2 and row<4:
            if column<3:
                return blocks[2]
            else:
                return blocks[3]
        else:
            if column<3:
                return blocks[4]
            else:
                return blocks[5]
    #4x4 block distribution    
    elif dimensions == 4 :
        if row<2:
            if column<2:
                return blocks[0]
            if column>=2:
                return blocks[1]
        else:
            if column<2:
                return blocks[2]
            if column>=2:
                return blocks[3]
    else:
        print(f'Error in insert_into_block function: No matching dimensions. Value for dimensions is {dimensions} .')

def gen_sudoku(print_me, dimensions):
    rows, columns, blocks = [], [], []
    for i in range(dimensions):
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
                    block = insert_into_block(row_index, column_index, blocks, dimensions)
                    column_reset = True
                    if dimensions == 9:
                        pool = [1,2,3,4,5,6,7,8,9]
                    elif dimensions == 6:
                        pool = [1,2,3,4,5,6]
                    else:
                        pool = [1,2,3,4]      

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
                                for i in range(dimensions):
                                    rows.append([]), columns.append([]), blocks.append([])
                                regen = True
                            else:
                                row.clear()
                                for i in range(column_index):
                                    block = insert_into_block (row_index, i, blocks, dimensions)
                                    block.pop(-1)
                                    selected_column = columns[i]
                                    selected_column.pop(-1)
                            reset = True
                            break
                            #sys.exit()
                    if reset is True:
                        break  
                #Boolean values management
                if reset is False:
                    row_reset = False
                    if row_index == dimensions-1:
                        sudoku_reset = False
                elif reset is True and regen is False:
                    reset = False
                else:
                    break
            if regen is True:
                break

    toc = time.time()        
    if print_me is True:
        print(f'El sudoku se ha generado en {round((toc-tic), 4)} segundos y es:')
        for row in rows:
            print(row)
    return rows

def export_sudokus(number, dimensions):
    try:
        tic = time.time()
        with open (f'stuff/sudokus{dimensions}.txt', 'w') as sudokus:
            for i in range (number):
                rows = gen_sudoku(False, dimensions)
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
    NINE_X_NINE = 9
    SIX_X_SIX = 6
    FOUR_X_FOUR = 4
    while(True):
        option = input('Welcome to sudoku generator. What do you want to do?:\n1 - Generate a 9x9 sudoku\n2 - Generate a 6x6 sudoku'+
        '\n3 - Generate a 4x4 sudoku\n4 - Export sudokus to a txt file\n5 - Read sudokus from a txt file\n6 - Pick a random sudoku from a file\n'+
        '7 - Exit\nType your option: ')
        if option == '1':
            gen_sudoku(True, NINE_X_NINE)
        elif option == '2':
            gen_sudoku(True, SIX_X_SIX)
        elif option == '3':
            gen_sudoku(True, FOUR_X_FOUR)
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