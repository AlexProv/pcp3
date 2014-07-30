
import os
import argparse
import random
import copy
import numpy as np
import chess
import copy
import alphabeta

from string import Template
from moves import get_attack_moves_for_piece
from human import human


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


def isSameColor(a, b):
    if a.islower() and b.islower():
        return True
    if a.isupper() and b.isupper():
        return True
    return False

class Jeu:
    def __init__(self, etat_initial, fct_but, fct_transitions):
        self.but = fct_but
        self.transitions = fct_transitions
        self.etat_initial = etat_initial
        self.resultat = None
        self.vainqueur = ''
        self.checkmate = False

    def resultat_partie(self):
        if self.resultat > 0:
            self.vainqueur = 'B'
            return 'Joueur Blanc a gagne'

        if self.resultat < 0:
            self.vainqueur = 'n'
            return 'Joueur Noir a gagne'

        self.vainqueur = ''
        return 'Partie nulle'

    def jouer_partie(self, joueur_max, joueur_min):
        etat = copy.deepcopy(self.etat_initial)
        print etat
        tour = 'B'
        while True:
            # Blanc ###
            action = joueur_max(copy.deepcopy(etat), self.but, self.transitions, 'B')
            etat = self.transitions(tour, etat)[action]

            print etat
            self.resultat = self.but(etat)

            if self.checkmate:
                print self.resultat_partie()
                break

            tour = 'B' if tour == 'n' else 'n'


            # Noir ###
            action = joueur_min(copy.deepcopy(etat), self.but, self.transitions, 'n')
            etat = self.transitions(tour, etat)[action]
            print etat
            self.resultat = self.but(etat)

            if self.checkmate:
                print self.resultat_partie()
                break

            tour = 'B' if tour == 'n' else 'n'

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

        self.actions = {}
        self.hero = 'B'

    def __str__(self):
        t = Template("""
   a   b   c   d   e   f   g   h  
0  $a0 | $b0 | $c0 | $d0 | $e0 | $f0 | $g0 | $h0
  ---+---+---+---+---+---+---+---
1  $a1 | $b1 | $c1 | $d1 | $e1 | $f1 | $g1 | $h1
  ---+---+---+---+---+---+---+---
2  $a2 | $b2 | $c2 | $d2 | $e2 | $f2 | $g2 | $h2
  ---+---+---+---+---+---+---+---
3  $a3 | $b3 | $c3 | $d3 | $e3 | $f3 | $g3 | $h3
  ---+---+---+---+---+---+---+---
4  $a4 | $b4 | $c4 | $d4 | $e4 | $f4 | $g4 | $h4
  ---+---+---+---+---+---+---+---
5  $a5 | $b5 | $c5 | $d5 | $e5 | $f5 | $g5 | $h5
  ---+---+---+---+---+---+---+---
6  $a6 | $b6 | $c6 | $d6 | $e6 | $f6 | $g6 | $h6
  ---+---+---+---+---+---+---+---
7  $a7 | $b7 | $c7 | $d7 | $e7 | $f7 | $g7 | $h7
  ---+---+---+---+---+---+---+---
""")
        return t.substitute(a0=self.tableau[0, 0], b0=self.tableau[0, 1], c0=self.tableau[0, 2], d0=self.tableau[0, 3], e0=self.tableau[0, 4], f0=self.tableau[0, 5], g0=self.tableau[0, 6], h0=self.tableau[0, 7],
                            a1=self.tableau[1, 0], b1=self.tableau[1, 1], c1=self.tableau[1, 2], d1=self.tableau[1, 3], e1=self.tableau[1, 4], f1=self.tableau[1, 5], g1=self.tableau[1, 6], h1=self.tableau[1, 7],
                            a2=self.tableau[2, 0], b2=self.tableau[2, 1], c2=self.tableau[2, 2], d2=self.tableau[2, 3], e2=self.tableau[2, 4], f2=self.tableau[2, 5], g2=self.tableau[2, 6], h2=self.tableau[2, 7],
                            a3=self.tableau[3, 0], b3=self.tableau[3, 1], c3=self.tableau[3, 2], d3=self.tableau[3, 3], e3=self.tableau[3, 4], f3=self.tableau[3, 5], g3=self.tableau[3, 6], h3=self.tableau[3, 7],
                            a4=self.tableau[4, 0], b4=self.tableau[4, 1], c4=self.tableau[4, 2], d4=self.tableau[4, 3], e4=self.tableau[4, 4], f4=self.tableau[4, 5], g4=self.tableau[4, 6], h4=self.tableau[4, 7],
                            a5=self.tableau[5, 0], b5=self.tableau[5, 1], c5=self.tableau[5, 2], d5=self.tableau[5, 3], e5=self.tableau[5, 4], f5=self.tableau[5, 5], g5=self.tableau[5, 6], h5=self.tableau[5, 7],
                            a6=self.tableau[6, 0], b6=self.tableau[6, 1], c6=self.tableau[6, 2], d6=self.tableau[6, 3], e6=self.tableau[6, 4], f6=self.tableau[6, 5], g6=self.tableau[6, 6], h6=self.tableau[6, 7],
                            a7=self.tableau[7, 0], b7=self.tableau[7, 1], c7=self.tableau[7, 2], d7=self.tableau[7, 3], e7=self.tableau[7, 4], f7=self.tableau[7, 5], g7=self.tableau[7, 6], h7=self.tableau[7, 7]
                            )



#verify if king is checked at pos x, y
def king_is_checked(etat, x,y, player):
    for y in etat.tableau:
        for x in y:
            # if theres a piece there check if it can attack the king
            if (player.islower() and etat.tableau[y][x].isupper()) or (player.isupper() and etat.tableau[y][x].islower()):
                    attacked_places = get_attack_moves_for_piece(tableau[y][x], x, y)
                    if (x,y) in attacked_places:
                        return True
    return False


def build_transitions_for_piece(actions, etat, position, piece):
    old_x, old_y = position
    moves = get_attack_moves_for_piece(etat, piece, old_x, old_y)
    #import pdb; pdb.set_trace()
    for x,y in moves:
        actions[(x,y,piece)] = copy.deepcopy(etat)
        actions[(x,y,piece)].tableau[old_y][old_x] = '-'
        actions[(x,y,piece)].tableau[y][x] = piece



def chess_transitions(tour, etat):
    actions = {}
    for y, row in enumerate(etat.tableau):
        for x, piece in enumerate(row):
            if isSameColor(piece, tour) and piece != "-":
                build_transitions_for_piece(actions,etat,(x,y),etat.tableau[y][x])

    return actions


def chess_but(etat):
    pts = 0
    for row in etat.tableau:
        for piece in row:
            if piece == "p":
                pts-=1
            if piece == "k":
                pts-=3  
            if piece == "b":
                pts-=3    
            if piece == "r":
                pts-=5
            if piece == "q":
                pts-=20 
            if piece == "w":
                pts-=1000000

            if piece == "P":
                pts+=1
            if piece == "K":
                pts+=3  
            if piece == "B":
                pts+=3    
            if piece == "R":
                pts+=5
            if piece == "Q":
                pts+=20
            if piece == "W":
                pts+=1000000

    return pts


#####
# Execution en tant que script
###
def main():

    # Jouer une partie d`echec
    chess = Jeu(ChessEtat(), chess_but, chess_transitions)
    chess.jouer_partie(human, alphabeta.joueur_echec)


if __name__ == "__main__":
    main()





