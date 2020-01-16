from sys import stdin
import math
import copy

def solve(index, board, sets, mapping):
    if index == len(board)**2:
        for row in board:
            print(' '.join([str(x) for x in row]))
        return True
    else:
        i = index // len(board)
        j = index % len(board)
        if board[i][j] == 0:
            for k in range(1, len(board) + 1):
                if validate_row(k, i, board) and validate_col(k, j, board) and validate_square(k, sets[mapping[i][j]]):
                    board[i][j] = k
                    sets[mapping[i][j]][k] = 1
                    if solve(index + 1, board, sets, mapping):
                        return True
                    else:
                        board[i][j] = 0
                        sets[mapping[i][j]][k] = 0
            return False
        else:
            return solve(index + 1, board, sets, mapping)

def validate_square(k, s):
    return s[k] != 1

def validate_row(k, i, board):
    val = True
    for x in board[i]:
        if x == k:
            val = False
    return val

def validate_col(k, j, board):
    val = True
    for i in range(len(board)):
        if k == board[i][j]:
            val = False
    return val

def main():
    case = 1
    while True:
        line = stdin.readline().strip()
        if line == '':
            break
        n = int(line)
        board = []
        dic = {}
        cont = 0
        for i in range(0, n):
            for j in range(0, n):
                dic[(i, j)] = cont
                cont = cont + 1
        sets = [[0 for j in range(0, n**2 + 1)] for x in range(0, cont)]
        for i in range(0, n**2):
            board.append([int(x) for x in stdin.readline().split()])
        stdin.readline()
        mapping = []
        for i in range(0, n**2):
            mapping.append([0 for x in range(0, n**2)])
            for j in range(0, n**2):
                mapping[i][j] = dic[(i//n, j//n)]
                if board[i][j] != 0:
                    sets[mapping[i][j]][board[i][j]] = 1
        if case != 1:
            print()
        if not solve(0, board, sets, mapping):
            print('NO SOLUTION')
        case = case + 1

main()
