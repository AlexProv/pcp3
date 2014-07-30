
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

    #import pdb; pdb.set_trace()
    fct_transitions(etat)[(x,y,c)]

    return fin