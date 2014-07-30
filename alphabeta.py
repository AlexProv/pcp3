def joueur_echec(etat,fct_but,fct_transitions,str_joueur):
   
    _,action = Max_Tour(etat,float("-infinity"),float("infinity"),fct_but,fct_transitions,str_joueur)
    return action

#max est joueur utilite, etat
def Max_Tour(etat,alpha,beta,fct_but,fct_transitions,str_joueur):
    utilite = fct_but(etat)
    if utilite is not None:
        if str_joueur == 'X':
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
    utilite = fct_but(etat)
    if utilite is not None:
        if str_joueur == 'X':
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