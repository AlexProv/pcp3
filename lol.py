from mpi4py import MPI
import numpy
import sys

data = {'a':1, 'b':2, 'c':3 }

comm = MPI.COMM_SELF.Spawn(sys.executable,
                           args=['lolprint.py'],
                           maxprocs=5)


comm.send(data, dest=2, tag=11)
size = comm.Get_size()
rank = comm.Get_rank()

comm.Disconnect()