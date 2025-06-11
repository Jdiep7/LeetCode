board = [["1","2",".",".","3",".",".",".","."],
 ["2",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","2"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

rowdict = {0:[], 1: [], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[]}
columndict = {0:[], 1: [], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[]}
boxdict = {0:[], 1: [], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[]}
n = len(board)


def isValidSudoku(board):  
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num == ".":
                continue
            box_index = (i//3) * 3 + (j//3)
            if num in rowdict[i] or num in columndict[j] or num in boxdict[box_index]:
                return False
            else:
                rowdict[i].append(num)
                columndict[j].append(num)
                boxdict[box_index].append(num)
                
    return True
                
          
print(isValidSudoku(board))