 


chess_grid = [
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'], 
    [' ', ' ', ' ', ' ', ' ', 'K', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', 'b', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', 'b', ' '],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'], 
    ['r', 'n', ' ', 'q', 'k', ' ', 'n', 'r']
]

def piyon(grid, row, col): 
    moves = []
    
    r,c = row - 1 , col 
        
    if(grid[r][c] == " "):
            move.append((r,c))
    else:
            break 
        
    r -= 1
    c = 1
    r,c = row + 1 , col 
    
    if(grid[r][c] == " "):
            move.append((r,c))
    else:
            break 
        
    r += 1
        

def at_hareket(grid, row, col): 
    moves = []
    
    r,c = row + 2, col -1 
    while r >= 0 and c < len(grid[0]):
        if(grid[r][c] == " "):
            move.append((r,c))
        else:
            break 
        
        r += 2
        c -= 1
    
    r,c = row + 2 , col + 1
    while r >= 0 and c < len(grid[0]):
        if(grid[r][c] == " "):
            move.append((r,c))
        else:
            break 
        
        r += 2
        c += 1
    
    r,c = row - 1 , col + 2
    while r <= 0 and c > len(grid[0]):
        if(grid[r][c] == " "):
            move.append((r,c))
        else:
            break 
        
        r -= 1
        c += 2
        
    r,c = row + 1 , col + 2
    while r <= 0 and c > len(grid[0]):
        if(grid[r][c] == " "):
            move.append((r,c))
        else:
            break 
        
        r += 1
        c += 2
    


def line(grid, row, col):
    moves = []
    #upper move
    r,c = row - 1 , col 
    while r >= 0 and c < len(grid[0]):
        if(grid[r][c] == " "):
            move.append((r,c))
        elif(grid[r][c].isupper()):
            move.append((r,c))
            break
        else:
            break 
        
        r -=1
        c = 1
    
    
    
    r,c = row + 1 , col 
    while r >= 0 and c < len(grid[0]):
        if(grid[r][c] == " "):
            move.append((r,c))
        elif(grid[r][c].islower()):
            move.append((r,c))
            break
        else:
            break 
        
        r +=1
        c = 1
        
    r,c = row , col + 1 
    while r >= 0 and c < len(grid[0]):
        if(grid[r][c] == " "):
            move.append((r,c))
        elif(grid[r][c].isupper()):
            move.append((r,c))
            break
        else:
            break 
        
        r = 1
        c += 1
    
    
    r,c = row , col - 1 
    while r >= 0 and c < len(grid[0]):
        if(grid[r][c] == " "):
            move.append((r,c))
        elif(grid[r][c].islower()):
            move.append((r,c))
            break
        else:
            break 
        
        r =1
        c -= 1


def diagnonal_moves(grid, row, col):
    moves = []
    r, c = row - 1, col + 1
    #upper right moves
    while r >= 0 and c < len(grid[0]):
        if(grid[r][c] == " "):
            moves.append((r, c))
        elif(grid[r][c].isupper()):
            moves.append((r, c))
            break
        else:
            break
        r -= 1
        c += 1

    #upper left moves
    r, c = row - 1, col - 1
    while r >= 0 and c >= 0:
        if(grid[r][c] == " "):
            moves.append((r, c))
        elif(grid[r][c].isupper()):
            moves.append((r, c))
            break
        else:
            break
        r -= 1
        c -= 1

    #bottom right moves
    r, c = row + 1, col + 1
    while r >= len(grid) and c >= len(grid[0]):
        if(grid[r][c] == " "):
            moves.append((r, c))
        elif(grid[r][c].islower()):
            moves.append((r, c))
            break
        else:
            break
        r += 1
        c += 1
    
    #bottom left moves
    r, c = row + 1, col - 1
    while r < len(grid) and c >= 0:
        if(grid[r][c] == " "):
            moves.append((r, c))
        elif(grid[r][c].islower()):
            moves.append((r, c))
            break
        else:
            break
        r += 1
        c -= 1

    return moves
    

    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if(grid[row][col] == "P"):
                moves = Piyon_moves(grid, row, col)
                for move in moves:
                    if(grid[move[0]][move[1]] == "K"):
                        return True
    return False
    
    
    
    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if(grid[row][col] == "Q"):
                moves = queen_moves(grid, row, col)
                for move in moves:
                    if(grid[move[0]][move[1]] == "k"):
                        return True
    return False
    

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if(grid[row][col] == "R"):
                moves = rook_moves(grid, row, col)
                for move in moves:
                    if(grid[move[0]][move[1]] == "k"):
                        return True
    return False

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if(grid[row][col] == "N"):
                moves = at_moves(grid, row, col)
                for move in moves:
                    if(grid[move[0]][move[1]] == "k"):
                        return True
    return False

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if(grid[row][col] == "B"):
                moves = bishop_moves(grid, row, col)
                for move in moves:
                    if(grid[move[0]][move[1]] == "k"):
                        return True
    return False
   
 
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if(grid[row][col] == "q"):
                moves = queen_moves(grid, row, col)
                for move in moves:
                    if(grid[move[0]][move[1]] == "K"):
                        return True
    return False
    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if(grid[row][col] == "p"):
                moves = piyon_moves(grid, row, col)
                for move in moves:
                    if(grid[move[0]][move[1]] == "K"):
                        return True
    return False

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if(grid[row][col] == "r"):
                moves = rook_moves(grid, row, col)
                for move in moves:
                    if(grid[move[0]][move[1]] == "K"):
                        return True
    return False

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if(grid[row][col] == "n"):
                moves = at_moves(grid, row, col)
                for move in moves:
                    if(grid[move[0]][move[1]] == "K"):
                        return True
    return False
    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if(grid[row][col] == "b"):
                moves = bishop_moves(grid, row, col)
                for move in moves:
                    if(grid[move[0]][move[1]] == "K"):
                        return True
    return False
        
if(check_if_checking()):
   ...