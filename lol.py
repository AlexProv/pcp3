from mpi4py import MPI
import numpy as np
import sys
import chess

NB_PROCESS = 10 

comm = MPI.COMM_SELF.Spawn(sys.executable,
                           args=['slavechild.py'],
                           maxprocs=NB_PROCESS)


data = np.array([['r','k','b','q','w','b','k','r'],
                     ['p','p','p','p','p','p','p','p'],
                     ['-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-'],
                     ['P','P','P','P','P','P','P','P'],
                     ['R','K','B','Q','W','B','K','R']]),'B'

data = chess.ChessEtat(),'B'


for i in range(NB_PROCESS):
    comm.send(data, dest=i, tag=1)

ack = 0
while True:
    data = comm.recv(source=1,tag=1)
    if data == "done":
        #comm.Disconnect()
        ack+=1
        print ack
        if ack > 3:
            break
