import numpy as np


tableau = np.array([['r','k','b','q','w','b','k','r'],
                                 ['p','p','p','p','p','p','p','p'],
                                 ['-','-','-','-','-','-','-','-'],
                                 ['-','-','-','-','-','-','-','-'],
                                 ['-','-','-','-','-','-','-','-'],
                                 ['-','-','-','-','-','-','-','-'],
                                 ['P','P','P','P','P','P','P','P'],
                                 ['R','K','B','Q','W','B','K','R']])


def change_my_dict(dictio):

	dictio[1] = "lol"


dictio = {}
print dictio
change_my_dict(dictio)
print dictio