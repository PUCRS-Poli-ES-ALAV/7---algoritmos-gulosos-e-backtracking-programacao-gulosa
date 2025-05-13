

def nQueens(n):
    return 0

#Onde estiver rainha tera um R
table = [[]]
def isSafe(row, col, table):
    for i in range(row):
        if table[i][col] == 1:
            return False
    for i in range(col):
            if table[row][i] == 1:
                return False 
    for i, j in zip(range(row - 1, -1, -1), 
                    range(col - 1, -1, -1)):
        if table[i][j]:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row - 1, -1, -1), 
                    	range(col + 1, len(table))):
         if table[i][j] == 1:
              return False
    return True

def posiciona_rainha(n):
    table = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if isSafe(i, j, table):
                table[i][j] = 1
                break
    return table

def print_table(table): 
    for i in range(len(table)):
        for j in range(len(table)):
            print(table[i][j], end=" ")
        print()
    return table

table = posiciona_rainha(8)

print_table(table)