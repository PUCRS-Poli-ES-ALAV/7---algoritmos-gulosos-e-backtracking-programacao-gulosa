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

def solve_n_queens(self, n: int) -> List[List[str]]:
    def backtrack(r):
        if r == n:
            ans.append(board[:])
            return
            
        for c in range(n):            
            if c in placedCol or r + c in placedPos or r - c in placedNeg:
                continue

            board[r][c] = "Q"
            placedCol.add(c)
            placedPos.add(r + c)
            placedNeg.add(r - c)

            backtrack(r + 1)

            board[r][c] = "."
            placedCol.remove(c)
            placedPos.remove(r + c)
            placedNeg.remove(r - c)

    board = [["."] * n for _ in range(n)]
    
    placedCol = set()  # Columns with queens
    placedPos = set()  # Positive diagonals (r + c)
    placedNeg = set()  # Negative diagonals (r - c)
    ans = [] 
    
    backtrack(0)
    return ans
