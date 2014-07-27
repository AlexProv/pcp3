
import os
import argparse
import random
import copy
import numpy as np
import chess

from string import Template

def left(a):
    x,y = a
    x-=1
    if x < 0:
        return None,None
    return x,y
def right(a):
    x,y = a
    x+=1
    if x > 7:
        return None,None
    return x,y

def top(a):
    x,y = a
    y+=1
    if y > 7:
        return None,None
    return x,y
def down(a):
    x,y = a
    y-=1
    if y < 0:
        return None,None
    return x,y
def diagonalLeftTop(a):
    return top(left(a))
def diagonalRightTop(a):
    return top(right(a))
def diagonalLeftDown(a):
    return down(left(a))
def diagonalRightDown(a):
    return down(right(a))

class Jeu:
    def __init__(self, etat_initial, fct_but, fct_transitions, verbose=True):
        self.but = fct_but
        self.transitions = fct_transitions
        self.etat_initial = etat_initial
        self.verbose = verbose
        self.resultat = None
        self.vainqueur = ''

    def resultat_partie(self):
        if self.resultat > 0:
            self.vainqueur = 'B'
            return 'Joueur Blanc a gagné'

        if self.resultat < 0:
            self.vainqueur = 'N'
            return 'Joueur Noir a gagné'

        self.vainqueur = ''
        return 'Partie nulle'

    def afficher(self, str):
        if self.verbose:
            print str

    def jouer_partie(self, joueur_max, joueur_min):
        etat = copy.deepcopy(self.etat_initial)
        self.afficher(etat)
        while True:
            # X ###
            action = joueur_max(copy.deepcopy(etat), self.but, self.transitions, 'B')
            etat = self.transitions(etat)[action]
            self.afficher(etat)
            self.resultat = self.but(etat)

            if self.resultat is not None:
                self.afficher(self.resultat_partie())
                break

            # O ###
            action = joueur_min(copy.deepcopy(etat), self.but, self.transitions, 'N')
            etat = self.transitions(etat)[action]
            self.afficher(etat)
            self.resultat = self.but(etat)

            if self.resultat is not None:
                self.afficher(self.resultat_partie())
                break

class ChessEtat:

#king = W for win 
    def __init__(self):
        self.tableau = np.array([['r','k','b','q','w','b','k','r'],
                                 ['p','p','p','p','p','p','p','p'],
                                 ['-','-','-','-','-','-','-','-'],
                                 ['-','-','-','-','-','-','-','-'],
                                 ['-','-','-','-','-','-','-','-'],
                                 ['-','-','-','-','-','-','-','-'],
                                 ['P','P','P','P','P','P','P','P'],
                                 ['R','K','B','Q','W','B','K','R']])
        self.permissionB = {}
        for i in range(7):
            self.permissionB[i] = 'O'
        #8 = rock    
        self.permissionB[8] = 'O'

        self.permissionW = {}
        for i in range(7):
            self.permissionB[i] = 'O'
        #8 = rock    
        self.permissionW[8] = 'O'

        self.echeque = '-'
        #echeque = b => b en echeque
        #echeque = w => w en echeque

    def __str__(self):
        t = Template("""
   a   b   c   d   e   f   g   h  
     |   |  |   |  |   |  |   |  |   |  |   |
0  $a0 | $b0 | $c0  $d0 | $e0 | $f0 | $g0 | $h0
     |   |  |   |  |   |  |   |  |   |  |   |
  ---+---+---+---+---+---+---+---+---+---
1  $a1 | $b1 | $c1  $d1 | $e1 | $f1 | $g1 | $h1
     |   |  |   |  |   |  |   |  |   |  |   |
  ---+---+---+---+---+---+---+---+---+---
2  $a2 | $b2 | $c2  $d2 | $e2 | $f2 | $g2 | $h2
     |   |  |   |  |   |  |   |  |   |  |   |
  ---+---+---+---+---+---+---+---+---+---
3  $a3 | $b3 | $c3  $d3 | $e3 | $f3 | $g3 | $h3
     |   |  |   |  |   |  |   |  |   |  |   |
  ---+---+---+---+---+---+---+---+---+---
4  $a4 | $b4 | $c4  $d4 | $e4 | $f4 | $g4 | $h4
     |   |  |   |  |   |  |   |  |   |  |   |
  ---+---+---+---+---+---+---+---+---+---
5  $a5 | $b5 | $c5  $d5 | $e5 | $f5 | $g5 | $h5
     |   |  |   |  |   |  |   |  |   |  |   |
  ---+---+---+---+---+---+---+---+---+---
6  $a6 | $b6 | $c6  $d6 | $e6 | $f6 | $g6 | $h6
     |   |  |   |  |   |  |   |  |   |  |   |
  ---+---+---+---+---+---+---+---+---+---
7  $a7 | $b7 | $c7  $d7 | $e7 | $f7 | $g7 | $h7
     |   |  |   |  |   |  |   |  |   |  |   |
  ---+---+---+---+---+---+---+---+---+---            
""")
        return t.substitute(a0=self.tableau[0, 0], b0=self.tableau[0, 1], c0=self.tableau[0, 2], d0=self.tableau[0, 3], e0=self.tableau[0, 4], f0=self.tableau[0, 5], g0=self.tableau[0, 6], h0=self.tableau[0, 7],
                            a0=self.tableau[1, 0], b0=self.tableau[1, 1], c0=self.tableau[1, 2], d0=self.tableau[1, 3], e0=self.tableau[1, 4], f0=self.tableau[1, 5], g0=self.tableau[1, 6], h0=self.tableau[1, 7],
                            a0=self.tableau[2, 0], b0=self.tableau[2, 1], c0=self.tableau[2, 2], d0=self.tableau[2, 3], e0=self.tableau[2, 4], f0=self.tableau[2, 5], g0=self.tableau[2, 6], h0=self.tableau[2, 7],
                            a0=self.tableau[3, 0], b0=self.tableau[3, 1], c0=self.tableau[3, 2], d0=self.tableau[3, 3], e0=self.tableau[3, 4], f0=self.tableau[3, 5], g0=self.tableau[3, 6], h0=self.tableau[3, 7],
                            a0=self.tableau[4, 0], b0=self.tableau[4, 1], c0=self.tableau[4, 2], d0=self.tableau[4, 3], e0=self.tableau[4, 4], f0=self.tableau[4, 5], g0=self.tableau[4, 6], h0=self.tableau[4, 7],
                            a0=self.tableau[5, 0], b0=self.tableau[5, 1], c0=self.tableau[5, 2], d0=self.tableau[5, 3], e0=self.tableau[5, 4], f0=self.tableau[5, 5], g0=self.tableau[5, 6], h0=self.tableau[5, 7],
                            a0=self.tableau[6, 0], b0=self.tableau[6, 1], c0=self.tableau[6, 2], d0=self.tableau[6, 3], e0=self.tableau[6, 4], f0=self.tableau[6, 5], g0=self.tableau[6, 6], h0=self.tableau[6, 7],
                            a0=self.tableau[7, 0], b0=self.tableau[7, 1], c0=self.tableau[7, 2], d0=self.tableau[7, 3], e0=self.tableau[7, 4], f0=self.tableau[7, 5], g0=self.tableau[7, 6], h0=self.tableau[7, 7]
                            )
#merde les pieces vont manger leur allier dans le cas acutelle TODO
def pion(self,player):
    if player.islower():
        x,y = down(position)
        if y not None:
            if self.tableau[x][y] == '-':
                #pion avence de 1
                self.tableau[position[0]][position[1]] = '-'
                self.tableau[x][y] = 'p'
                #action 1 fait
            x,y = diagonalRightDown(position)
            if self.tableau[x][y].isupper():
                #pion a manger a droite
                self.tableau[position[0]][position[1]] = '-'
                self.tableau[x][y] = 'p'
                #action 2 
            x,y = diagonalLeftDown(position)
            if self.tableau[x][y].isupper():
                #pion a manger a droite
                self.tableau[position[0]][position[1]] = '-'
                self.tableau[x][y] = 'p'
                #action 2 
            if position[y] == 1: 
                #avence de 2 au premier tour
                x,y = down(down(position))
                self.tableau[position[0]][position[1]] = '-'
                self.tableau[x][y] = 'p'
                #action 3 
            #je code pas l'action du pion qui coupe vrm trop compliquer
    else: 
        x,y = top(position)
        if y not None:
            if self.tableau[x][y] == '-':
                #pion avence de 1
                self.tableau[position[0]][position[1]] = '-'
                self.tableau[x][y] = 'P'
                #action 1 fait
            x,y = diagonalRighttop(position)
            if player.islower():
                if self.tableau[x][y].isupper():
                    #pion a manger a droite
                    self.tableau[position[0]][position[1]] = '-'
                    self.tableau[x][y] = 'P'
                    #action 2
                else:
                    break
            else:
                if self.tableau[x][y].islower():
                    #pion a manger a droite
                    self.tableau[position[0]][position[1]] = '-'
                    self.tableau[x][y] = 'P'
                    #action 2
                else:
                    break

            x,y = diagonalLefttop(position)
            if player.islower():
                if self.tableau[x][y].isupper():
                    #pion a manger a droite
                    self.tableau[position[0]][position[1]] = '-'
                    self.tableau[x][y] = 'P'
                    #action 2 
                else:
                    break
            else:
                if self.tableau[x][y].islower():
                    #pion a manger a droite
                    self.tableau[position[0]][position[1]] = '-'
                    self.tableau[x][y] = 'P'
                    #action 2 
                else:
                    break

            if position[y] == 1: 
                #avence de 2 au premier tour
                x,y = top(top(position))
                self.tableau[position[0]][position[1]] = '-'
                self.tableau[x][y] = 'P'
                #action 3 

def rock(self,player):      
    moves = [top,down,left,right]
    for m in moves:
        p = position  
        while True:
            x,y = m(p)
            if y is None or x is None:
                break
            #check pour ne pas canibaliser
            if player.islower():
                if self.tableau[x][y].islower():
                    break
            else:
                if self.tableau[x][y].isupper():
                    break    

            xyCase = tableau[x][y]
            self.tableau[p[0]][p[1]] = '-'
            self.tableau[x][y] = player
            p = x,y
            # a avencer ou manger doit adder a la config
            
            #check pour savoir si on a manger
            if player.islower():
                if xyCase:
                    break
            else:
                if xyCase:
                    break  

def bishop(self,player):    
    moves = [diagonalLeftDown,diagonalRightDown,diagonalRightTop,diagonalLeftTop]
    for m in moves:
        p = position
        while True:
            x,y = m(p)
            if y is None or x is None:
                break

            #check pour ne pas canibaliser
            if player.islower():
                if self.tableau[x][y].islower():
                    break
            else:
                if self.tableau[x][y].isupper():
                    break    

            xyCase = tableau[x][y]
            self.tableau[p[0]][p[1]] = '-'
            self.tableau[x][y] = player
            p = x,y
            # a avencer ou manger doit adder a la config
            
            #check pour savoir si on a manger
            if player.islower():
                if xyCase:
                    break
            else:
                if xyCase:
                    break  

def knight(self,player):
    moves = []
    moves.append(top(top(left())))
    moves.append(top(top(right())))
    moves.append(down(down(left())))
    moves.append(down(down(right())))
    moves.append(left(left(top())))
    moves.append(left(left(down())))
    moves.append(right(right(top())))
    moves.append(right(right(down())))

    for m in moves:
        x,y = m(position)
        if x not None and y not None:
            #check pour ne pas canibaliser
            if player.islower():
                if self.tableau[x][y].islower():
                    break
            else:
                if self.tableau[x][y].isupper():
                    break    
                    #mange ou deplace
            self.tableau[p[0]][p[1]] = '-'
            self.tableau[x][y] = player

def queen(self,player):
    moves = [diagonalLeftDown,diagonalRightDown,diagonalRightTop,diagonalLeftTop,left,right,top,down]
    for m in moves:
        p = position  
        while True:
            x,y = m(p)
            if y is None or x is None:
                break
            if player.islower():
                if self.tableau[x][y].islower():
                    break
            else:
                if self.tableau[x][y].isupper():
                    break    
            #mange ou deplace    
            xyCase = tableau[x][y]
            self.tableau[p[0]][p[1]] = '-'
            self.tableau[x][y] = 'b'
            p = x,y
            #a avencer ou manger doit adder a la config
            if player.islower():
                if xyCase:
                    break
            else:
                if xyCase:
                    break  

def king(self,player):
    moves = [diagonalLeftDown,diagonalRightDown,diagonalRightTop,diagonalLeftTop,left,right,top,down]
    for m in moves:
        x,y = m(position)
        if x not None and y not None:
            if player.islower():
                if self.tableau[x][y].islower():
                    break
            else:
                if self.tableau[x][y].isupper():
                    break   
            #faut verifier que rien sur le board peut attaquer cette case la 
            #TODO
            #mange ou deplace
            self.tableau[p[0]][p[1]] = '-'
            self.tableau[x][y] = 'w'
    #manque le rock
    #TODO


def mouvement(self, position, type):
    for i in t:
        if t == 'p' or t == 'P':
            self.pion(t)
        if t == 'r' or t == 'R':
            self.rock(t)
        if t == 'b' or t == 'B':
            self.bishop(t)
        if t == 'k' or t == 'T':
            self.knight(t)
        if t == 'q' or t == 'Q':
            self.queen(t)

        if t == 'w' or t == 'T':
            king(t)


def chess_transitions(etat):
    # Determiner c'est le tour à qui avec etat.turn
    #TODO 
    """
    if np.sum(etat.tableau == 'X') > np.sum(etat.tableau == 'O'):
        # Tour de O
        symbol = 'O'
    else:
        # Tour de X
        symbol = 'X'
    positions_vides = np.nonzero(etat.tableau == ' ')
    actions = {}
    for i, j in zip(positions_vides[0], positions_vides[1]):
        nouvel_etat = copy.deepcopy(etat)
        nouvel_etat.tableau[i, j] = symbol
        actions[(i, j)] = nouvel_etat
    """
    if etat.turn == "B":
        for i in range(etat.tableau):
            for j in range(etat.tableau[i]):
                if etat.tableau[i][j].islower():
                    mouvement((i,j),tableau[i][j]) 
                    #doit constuire le {} d'action 
    else:
        for i in range(etat.tableau):
            for j in range(etat.tableau[i]):
                if not etat.tableau[i][j].islower():
                    mouvement((i,j),tableau[i][j])
                    #doit constuire le {} d'action 
    return actions


def chess_but(etat):
    # Vérifie si X a gagné
    pts = 0
    for i in etat.tableau:
        if i == "p":
            pts-=1
        if i == "k":
            pts-=3  
        if i == "b":
            pts-=3    
        if i == "r":
            pts-=5
        if i == "q":
            pts-=20 

        if i == "P":
            pts+=1
        if i == "K":
            pts+=3  
        if i == "B":
            pts+=3    
        if i == "R":
            pts+=5
        if i == "Q":
            pts+=20

        #verifier si en echeque pas fait
        #TODO
    return pts

#TODO pas encore modifier
def player_factory(player):
    if player == 'aleatoire':
        return joueur_aleatoire

    if player == 'humain':
        return joueur_humain

    if player.endswith('.py'):
        import imp
        player = os.path.abspath(player)
        name = player.replace('/', '.').replace('.', '_')
        solution = imp.load_source(name, player)

        return Joueur(player, solution.joueur_tictactoe)

    return None

#TODO pas encore modifier
DESCRIPTION = "Lancer une partie de Tic-Tac-Toe."

#TODO pas encore modifier
def buildArgsParser():
    p = argparse.ArgumentParser(description=DESCRIPTION,
                                formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # Paramètres globaux
    p.add_argument('-joueur1', dest="player1", metavar="JOUEUR", action='store', type=str, required=False, default="solution_tictactoe.py",
                   help="'humain', 'aleatoire' ou le fichier contenant votre solution.")

    p.add_argument('-joueur2', dest="player2", metavar="JOUEUR", action='store', type=str, required=False, default="solution_tictactoe.py",
                   help="'humain', 'aleatoire' ou le fichier contenant votre solution.")

    p.add_argument('-v', dest='is_verbose', action='store_true', required=False,
                   help='activer le mode verbose')

    return p


    #####
    # Execution en tant que script
    ###
    def main():
        parser = buildArgsParser()
        args = parser.parse_args()
        player1 = args.player1
        player2 = args.player2
        is_verbose = args.is_verbose

        if player1 == "humain" or player2 == "humain":
            is_verbose = True  # Afficher les grilles si c'est un joueur humain.

        if player1 not in ['aleatoire', 'humain'] and not player1.endswith('.py'):
            parser.error('Joueur 1 doit être [aleatoire, humain, solution_tictactoe.py]')

        if player2 not in ['aleatoire', 'humain'] and not player2.endswith('.py'):
            parser.error('Joueur 2 doit être [aleatoire, humain, solution_tictactoe.py]')

        if player1.endswith('.py') and not os.path.isfile(player1):
            parser.error("-joueur1 '{}' must be an existing file!".format(os.path.abspath(player1)))

        if player2.endswith('.py') and not os.path.isfile(player2):
            parser.error("-joueur2 '{}' must be an existing file!".format(os.path.abspath(player2)))

        # Jouer une partie de Tic-Tac-Toe

        chess = Jeu(ChessEtat(), chess_but, chess_transitions, verbose=is_verbose)
        chess.jouer_partie(player_factory(player1), player_factory(player2))



    if __name__ == "__main__":
        main()


