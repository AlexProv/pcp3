def generate_top_line_moves(x,y):
    moves = []
    #tmp coords
    _x, _y = x, y
    #generate straight top line
    while _y >= 0:
        # if we hit a piece, stop there
        if self.tableau[_x][_y] != "-":
            moves.append((_x,_y))
            return moves
        moves.append((_x,_y))
        _y+=1
    return moves

def generate_down_line_moves(x,y):
    moves = []
    #reset coords
    _x, _y = x, y
    #generate straight down line
    while _y <= 7:
        # if we hit a piece, stop there
        if self.tableau[_x][_y] != "-":
            moves.append((_x,_y))
            return moves
        moves.append((_x,_y))
        _y-=1
    return moves


def generate_horizontal_line_moves(x,y):
    moves = []
    #reset coords
    _x, _y = x, y
    #generate straight down line
    while _y <= 7:
        # if we hit a piece, stop there
        if self.tableau[_x][_y] != "-":
            moves.append((_x,_y))
            break
        moves.append((_x,_y))
        x-=1

        #tmp coords
    _x, _y = x, y
    #generate straight top line
    while _y >= 0:
        # if we hit a piece, stop there
        if self.tableau[_x][_y] != "-":
            moves.append((_x,_y))
            break
        moves.append((_x,_y))
        x+=1
    return moves

def generate_diagonal_line_moves(x,y):
    moves = []
    #reset coords
    _x, _y = x, y
    #generate down right diag
    while _y <= 7 and _x <= 7:
        # if we hit a piece, stop there
        if self.tableau[_x][_y] != "-":
            moves.append((_x,_y))
            break
        moves.append((_x,_y))
        _y+=1
        _x+=1

    _x, _y = x, y
    #generate down left diagonal
    while _y <= 7 and _x >= 0:
        # if we hit a piece, stop there
        if self.tableau[_x][_y] != "-":
            moves.append((_x,_y))
            break
        moves.append((_x,_y))
        _y+=1
        _x-=1

    #reset coords
    _x, _y = x, y
    #generate top left diagonal
    while _y >= 0 and _x >= 0:
        # if we hit a piece, stop there
        if self.tableau[_x][_y] != "-":
            moves.append((_x,_y))
            break
        moves.append((_x,_y))
        _y-=1
        _x-=1

    #reset coords
    _x, _y = x, y
    #generate top right idag
    while _y >= 0 and _x >= 0:
        # if we hit a piece, stop there
        if self.tableau[_x][_y] != "-":
            moves.append((_x,_y))
            break
        moves.append((_x,_y))
        _y-=1
        _x+=1

    return moves

def generate_knight_attack_moves(x,y):
    moves = []
    moves.append((x+2,y+1))
    moves.append((x+2,y-1))
    moves.append((x-2,y+1))
    moves.append((x-2,y-1))
    moves.append((x+1,y+2))
    moves.append((x-1,y-2))
    moves.append((x+1,y-2))
    moves.append((x-1,y+2))
    #validation
    moves = [(x,y) for x,y in moves if pos_is_in_board(x,y)]

def pos_is_in_board(x,y):
    if x<= 7 and x>= 0 and y <= 7 and y >= 0:
        return True
    else
        return False


def get_attack_moves_for_piece(piece, x, y):
    moves = []
    if piece == "w":
        return [(x+1,y),(x+1,y+1),(x,y+1),(x-1,y),(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y+1)]
    if piece == "W":
        return [(x+1,y),(x+1,y+1),(x,y+1),(x-1,y),(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y+1)]
    if piece == "Q" or piece == "q":
        moves.append(generate_top_line_moves(x,y))
        moves.append(generate_down_line_moves(x,y))
        moves.append(generate_diagonal_line_moves(x,y))
        moves.append(generate_horizontal_line_moves(x,y))
    if piece == "P":
        return [(x+1, y-1),(x-1,y-1)]
    if piece == "p":
        return [(x+1, y+1),(x-1,y+1)]
    if piece == "R" or piece =="r":
        moves.append(generate_top_line_moves(x,y))
        moves.append(generate_down_line_moves(x,y))
        moves.append(generate_horizontal_line_moves(x,y))
    if piece == "K" or "k":
        moves.append(generate_knight_attack_moves)
    if piece == "B" or "b":
        moves.append(generate_diagonal_line_moves(x,y))

    return moves