# -*- coding: utf-8 -*-

#####
# VotreNom (VotreMatricule) .~= À MODIFIER =~.
###

from pdb import set_trace as dbg  # Utiliser dbg() pour faire un break dans votre code.

import random
import numpy as np

########################
# Solution tic-tac-toe #
########################

#####
# joueur_tictactoe : Fonction qui calcule le prochain coup optimal pour gagner la
#                     la partie de Tic-tac-toe à l'aide d'Alpha-Beta Prunning.
#
# etat: Objet de la classe TicTacToeEtat indiquant l'état actuel du jeu.
#
# fct_but: Fonction qui prend en entrée un objet de la classe TicTacToeEtat et
#          qui retourne le score actuel tu plateau. Si le score est positif, les 'X' ont l'avantage
#          si c'est négatif ce sont les 'O' qui ont l'avantage, si c'est 0 la partie est nulle.
#
# fct_transitions: Fonction qui prend en entrée un objet de la classe TicTacToeEtat et
#                   qui retourne une liste de tuples actions-états voisins pour l'état donné.
#
# str_joueur: String indiquant c'est à qui de jouer : les 'X' ou 'O'.
#
# retour: Cette fonction retourne l'action optimal à joeur pour le joueur actuel c.-à-d. 'str_joueur'.
###
def joueur_echec(etat,fct_but,fct_transitions,str_joueur):

    #TODO: Implémenter un joueur alpha-beta

    # Retourne une action aléatoire (.~= À MODIFIER =~.)
    #action,etat = random.choice(fct_transitions(etat).items())
    _,action = Max_Tour(etat,float("-infinity"),float("infinity"),fct_but,fct_transitions,str_joueur)
    return action

#max est joueur utilite, etat
def Max_Tour(etat,alpha,beta,fct_but,fct_transitions,str_joueur):
    import pdb; pdb.set_trace()
    utilite = fct_but(etat)
    print utilite
    if utilite is not None:
        if str_joueur == 'B':
            return utilite, None
        else:
            return -utilite,None

    utilite = float("-infinity")
    
    action = None
    for actionPrime, etatPrime in fct_transitions(etat).items():
        utiliteTemporaire, actionTemporiare = Min_Tour(etatPrime,alpha,beta,fct_but,fct_transitions,str_joueur)
        if utilite < utiliteTemporaire:
            utilite = utiliteTemporaire
            action = actionPrime
        if utilite >= beta:
            return utilite, action
        alpha = max(alpha,utilite)
    return utilite, action
        

def Min_Tour(etat,alpha,beta,fct_but,fct_transitions,str_joueur):
    import pdb; pdb.set_trace()
    utilite = fct_but(etat)
    print utilite
    if utilite is not None:
        if str_joueur == 'n':
            return utilite, None
        else:
            return -utilite,None

    utilite = float("infinity")
    
    action = None
    for actionPrime, etatPrime in fct_transitions(etat).items():
        utiliteTemporaire, actionTemporiare = Max_Tour(etatPrime,alpha,beta,fct_but,fct_transitions,str_joueur)
        if utilite > utiliteTemporaire:
            utilite = utiliteTemporaire
            action = actionPrime
        if utilite <= alpha:
            return utilite, action
        beta = min(beta,utilite)
    return utilite, action


#for action in listAction:
#etatPrime = listAction[action]