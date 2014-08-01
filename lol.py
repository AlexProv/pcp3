from mpi4py import MPI
import numpy as np
import sys

comm = MPI.COMM_SELF.Spawn(sys.executable,
                           args=['lolprint.py'],
                           maxprocs=5)


data = np.array([['r','k','b','q','w','b','k','r'],
                     ['p','p','p','p','p','p','p','p'],
                     ['-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-'],
                     ['P','P','P','P','P','P','P','P'],
                     ['R','K','B','Q','W','B','K','R']])



comm.send(data, dest=1, tag=11)
ize = comm.Get_size()
rank = comm.Get_rank()

data = comm.recv(source=1,tag=12)
print data

#comm.Disconnect()
