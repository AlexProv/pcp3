from mpi4py import MPI
from alphabeta import joueur_echec
import chess
import numpy as np


comm = MPI.Comm.Get_parent()
data = comm.recv(source=0,tag=1)

etat,player = data
action = joueur_echec(etat,chess.chess_but,chess.chess_transitions,player)

print action

comm.send('done', dest=0, tag=1)
comm.Disconnect()