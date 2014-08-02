MAX_DEPTH = 4


# def alphabeta(etat, depth, fct_but, fct_transitions, alpha, beta, str_joueur):
#     utilite = fct_but(etat)
#     if depth == 0 or fct_but(etat) >= 1000000:
#         return utilite, etat

#     if str_joueur == "B":
#         for actionPrime, etatPrime in fct_transitions(str_joueur, etat).items():
#             alpha, etat = max((alpha,etat), alphabeta(etatPrime, depth-1, fct_but,fct_transitions, alpha, beta, 'n'))
#             if beta <= alpha:
#                 break
#         return alpha, etat
#     else:
#         for actionPrime, etatPrime in fct_transitions(str_joueur, etat).items():
#             beta, etat = min((beta,etat), alphabeta(etatPrime, depth-1, fct_but,fct_transitions, alpha, beta, 'B'))
#             if beta <= alpha:
#                 break
#         return beta, etat


def joueur_echec(etat,fct_but,fct_transitions,str_joueur, depth=MAX_DEPTH):


    if str_joueur == "B":
        _,action = Max_Tour(etat,float("-infinity"),float("infinity"),fct_but,fct_transitions,str_joueur,depth)
    else:
        _,action = Min_Tour(etat,float("-infinity"),float("infinity"),fct_but,fct_transitions,str_joueur,depth)
    return action

#max est joueur utilite, etat
def Max_Tour(etat,alpha,beta,fct_but,fct_transitions,str_joueur, depth):
    utilite = fct_but(etat)
    if depth == 0:
        if str_joueur == 'B':
            return utilite, None
        else:
            return -utilite,None

    utilite = float("-infinity")
    
    action = None
    for actionPrime, etatPrime in fct_transitions(str_joueur,etat).items():
        utiliteTemporaire, actionTemporiare = Min_Tour(etatPrime,alpha,beta,fct_but,fct_transitions,str_joueur, depth-1)
        if utilite < utiliteTemporaire:
            utilite = utiliteTemporaire
            action = actionPrime
        if utilite >= beta:
            return utilite, action
        alpha = max(alpha,utilite)
    return utilite, action
        

def Min_Tour(etat,alpha,beta,fct_but,fct_transitions,str_joueur, depth):
    utilite = fct_but(etat)
    if depth == 0:
        if str_joueur == 'B':
            return utilite, None
        else:
            return -utilite,None

    utilite = float("infinity")
    
    action = None
    for actionPrime, etatPrime in fct_transitions(str_joueur,etat).items():
        utiliteTemporaire, actionTemporiare = Max_Tour(etatPrime,alpha,beta,fct_but,fct_transitions,str_joueur, depth-1)
        if utilite > utiliteTemporaire:
            utilite = utiliteTemporaire
            action = actionPrime
        if utilite <= alpha:
            return utilite, action
        beta = min(beta,utilite)
    return utilite, action



def main():
    print "AA"
    #a = Max_Tour(etat,alpha,beta,fct_but,fct_transitions,str_joueur)

if __name__ == "__main__":
    main()
