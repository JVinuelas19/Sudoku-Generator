from random import randint

sequence = [1,2,3,4,5,6,7,8,9]
rows = [] 
columns = []
blocks = []

for i in range(9):
    rows.append([]), columns.append([]), blocks.append([])

for row in rows:
    for column in columns:
        number = randint(1, 9)
        column.append(number)
        row.append(number)


for column in columns:
    print (column)

