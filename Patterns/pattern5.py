'''
for i in range(5, 0, -1):
    print("*"*i)
    '''

rows = 5

for i in range(rows, 0, -1):
    spaces = " " * (rows - i)
    stars = "*" * i
    print(spaces + stars)

    