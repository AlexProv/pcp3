# A bunch of utility functions that return a list of possible moves for every piece on the board


def isSameColor(a, b):
    if a.islower() and b.islower():
        return True
    if a.isupper() and b.isupper():
        return True
    return False


def generate_top_line_moves(etat,piece,x,y):
    moves = []
    #tmp coords
    _x, _y = x, y-1
    #generate straight top line
    while _y >= 0:
        # if we hit a piece, stop there
        if pos_is_in_board(_x, _y):
            if isSameColor(etat.tableau[_y][_x],piece):
                break
            else:
                moves.append((_x,_y))
        else:
            break
        _y+-1
        
    return moves

def generate_down_line_moves(etat,piece,x,y):
    moves = []
    #reset coords
    _x, _y = x, y+1

    #generate straight down line
    while _y <= 7:
        # if we hit a piece, stop there
        if pos_is_in_board(_x, _y):
            if isSameColor(etat.tableau[_y][_x],piece):
                break
            else:
                moves.append((_x,_y))
        else:
            break
        _y+=1
    return moves


def generate_horizontal_line_moves(etat,piece,x,y):
    moves = []
    #reset coords
    _x, _y = x, y
    #generate straight down line
    _x-=1
    while _x >= 0:
        # if we hit a piece, stop there
        if pos_is_in_board(_x, _y):
            if isSameColor(etat.tableau[_y][_x],piece):
                break
            else:
                moves.append((_x,_y))
        else:
            break
        _x-=1

        #tmp coords
    _x, _y = x, y
    #generate straight top line
    _x+=1
    while _y <= 7:
        # if we hit a piece, stop there
        if pos_is_in_board(_x, _y):
            if isSameColor(etat.tableau[_y][_x],piece):
                break
            else:
                moves.append((_x,_y))
        else:
            break
        _x+=1
    return moves

def generate_diagonal_line_moves(etat,piece,x,y):
    moves = []
    #reset coords
    _x, _y = x+1, y+1
    #generate down right diag
    while _y <= 7 and _x <= 7:
        # if we hit a piece, stop there
        if pos_is_in_board(_x, _y):
            if isSameColor(etat.tableau[_y][_x],piece):
                break
            else:
                moves.append((_x,_y))
        else:
            break
        _y+=1
        _x+=1

    _x, _y = x-1, y+1
    #generate down left diagonal
    while _y <= 7 and _x >= 0:
        # if we hit a piece, stop there
        if pos_is_in_board(_x, _y):
            if isSameColor(etat.tableau[_y][_x],piece):
                break
            else:
                moves.append((_x,_y))
        else:
            break
        _y+=1
        _x-=1

    #reset coords
    _x, _y = x-1, y-1
    #generate top left diagonal
    while _y >= 0 and _x >= 0:
        # if we hit a piece, stop there
        if pos_is_in_board(_x, _y):
            if isSameColor(etat.tableau[_y][_x],piece):
                break
            else:
                moves.append((_x,_y))
        else:
            break
        _y-=1
        _x-=1

    #reset coords
    _x, _y = x+1, y-1
    #generate top right idag
    while _y >= 0 and _x <= 7:
        # if we hit a piece, stop there
        if pos_is_in_board(_x, _y):
            if isSameColor(etat.tableau[_y][_x],piece):
                break
            else:
                moves.append((_x,_y))
        else:
            break
        _y-=1
        _x+=1

    return moves

def generate_knight_attack_moves(etat,piece,x,y):
    possible_moves = []
    possible_moves.append((x+2,y+1))
    possible_moves.append((x+2,y-1))
    possible_moves.append((x-2,y+1))
    possible_moves.append((x-2,y-1))
    possible_moves.append((x+1,y+2))
    possible_moves.append((x-1,y-2))
    possible_moves.append((x+1,y-2))
    possible_moves.append((x-1,y+2))

    return get_only_valid(etat, possible_moves, piece)

def generate_pawn_moves(etat,piece,x,y):
    moves = []
    if piece.islower():
        try:
            if etat.tableau[y+1][x] == "-":
                moves.append((x,y+1))
                if etat.tableau[y+1][x+1].isupper():
                    moves.append((x+1,y+1))
                if etat.tableau[y+1][x-1].isupper():
                    moves.append((x-1,y+1))
        except IndexError:
            pass

        if y == 1 and etat.tableau[3][x] == "-":
            moves.append((x,y+2))
    else:
        try:
            if etat.tableau[y-1][x] == "-":
                moves.append((x,y-1))
            if etat.tableau[y-1][x+1].isupper():
                moves.append((x+1,y-1))
            if etat.tableau[y-1][x-1].isupper():
                moves.append((x-1,y-1))
        except IndexError:
            pass

        if y == 6 and etat.tableau[4][x] == "-":
            moves.append((x,y-2))

    return get_only_valid(etat, moves, piece)

def generate_king_moves(etat,piece,x,y):
    possible_moves = [(x+1,y),(x+1,y+1),(x,y+1),(x-1,y),(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y+1)]
    return get_only_valid(etat, possible_moves, piece)


#valider quon ne canibalise pas et quon ne sort pas en dehors du board
def get_only_valid(etat, moves, piece):
    moves = [(x,y) for x,y in moves if pos_is_in_board(x,y)]
    return [(x,y) for x,y in moves if not isSameColor(etat.tableau[y][x], piece)]



def pos_is_in_board(x,y):
    if x<= 7 and x>= 0 and y <= 7 and y >= 0:
        return True
    else:
        return False


def get_attack_moves_for_piece(etat, piece, x, y):
    moves = []
    if piece == "w" or piece == "W":
        moves += generate_king_moves(etat,piece,x,y)
    if piece == "Q" or piece == "q":
        moves += generate_top_line_moves(etat,piece,x,y)
        moves += generate_down_line_moves(etat,piece,x,y)
        moves += generate_diagonal_line_moves(etat,piece,x,y)
        moves += generate_horizontal_line_moves(etat,piece,x,y)
    if piece == "P" or piece == "p":
        moves += generate_pawn_moves(etat,piece,x,y)
    if piece == "R" or piece == "r":
        moves += generate_top_line_moves(etat,piece,x,y)
        moves += generate_down_line_moves(etat,piece,x,y)
        moves += generate_horizontal_line_moves(etat,piece,x,y)
    if piece == "K" or piece == "k":
        moves += generate_knight_attack_moves(etat,piece,x,y)
    if piece == "B" or piece == "b":
        moves += generate_diagonal_line_moves(etat,piece,x,y)
    return moves