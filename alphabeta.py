MAX_DEPTH = 5

def joueur_echec(etat,fct_but,fct_transitions,str_joueur):
   

    _,action = Max_Tour(etat,float("-infinity"),float("infinity"),fct_but,fct_transitions,str_joueur)
    return action

#max est joueur utilite, etat
def Max_Tour(etat,alpha,beta,fct_but,fct_transitions,str_joueur, current_depth = 0):
    utilite = fct_but(etat)

    if utilite >= 1000000 or current_depth == MAX_DEPTH:
        if str_joueur == 'B':
            return utilite, None
        else:
            return -utilite,None

    utilite = float("-infinity")
    
    action = None
    for actionPrime, etatPrime in fct_transitions(str_joueur, etat).items():
        utiliteTemporaire, actionTemporiare = Min_Tour(etatPrime,alpha,beta,fct_but,fct_transitions,str_joueur, current_depth+1)
        if utilite < utiliteTemporaire:
            utilite = utiliteTemporaire
            action = actionPrime
        if utilite >= beta:
            return utilite, action
        alpha = max(alpha,utilite)

    return utilite, action
        

def Min_Tour(etat,alpha,beta,fct_but,fct_transitions,str_joueur, current_depth):
    utilite = fct_but(etat)
    if utilite <= -1000000 or current_depth == MAX_DEPTH:
        if str_joueur == 'n':
            return utilite, None
        else:
            return -utilite,None

    utilite = float("infinity")
    
    action = None
    for actionPrime, etatPrime in fct_transitions(str_joueur, etat).items():
        utiliteTemporaire, actionTemporiare = Max_Tour(etatPrime,alpha,beta,fct_but,fct_transitions,str_joueur, current_depth+1)
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
