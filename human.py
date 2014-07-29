
def human():
    print "depart"
    s = raw_input()
    x,y = s.split()
    y = int(y)
    x = int(x.toupper()) - 65
    depart = x,y     
    s = raw_input()
    x,y,c = s.split()
    y = int(y)
    x = int(x.toupper()) - 65
    fin = x,y,c
    return  depart,fin
