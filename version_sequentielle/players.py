MAX_DEPTH = 4

def human(etat, fct_but, fct_transitions, str_joueur):
    print "depart"
    s = raw_input()
    x,y = s.split()
    y = int(y)
    x = ord(x.upper()) - 65
    depart = x,y     
    s = raw_input()
    x,y,c = s.split()
    y = int(y)
    x = ord(x.upper()) - 65
    fin = x,y,c

    return fin

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