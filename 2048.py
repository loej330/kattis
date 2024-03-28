import sys

transpose = lambda mat: [ [ mat[j][i] for j in range(4) ] for i in range(4) ]
flip = lambda mat: [ row[::-1] for row in mat ]
pull = lambda row, i, k: (row[:i] + row[k:] + (3 * [0]))[:4]

input_lines = sys.stdin.readlines()
board = [ list(map(int, line.split())) for line in input_lines[0:4] ]
move = int(input_lines[4])

if move in [1, 3]: board = transpose(board)
if move in [2, 3]: board = flip(board)

for i in range(4):    
    for j in range(3):
        k = j + 1
        while k < 4 and board[i][k] == 0:
            k += 1
        if k > 3: continue
        if board[i][j] == 0:
            board[i] = pull(board[i], j, k)            
        elif board[i][j] == board[i][k]:
            board[i][k] *= 2
            board[i] = pull(board[i], j, k)            
                
if move in [2, 3]: board = flip(board)
if move in [1, 3]: board = transpose(board)

for row in board:
    print(*row)