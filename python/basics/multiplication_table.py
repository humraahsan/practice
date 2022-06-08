"""
Write a function print_table(int) that accepts integer input and prints its table up to 10 as following for `3`:
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30

Use for loop for this program
"""
def print_table(table):
    for i in range(1, 11):
        step = table * i
        print(table, 'x', i, '=', step)

if __name__ == '__main__':
    print_table(13)