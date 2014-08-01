from mpi4py import MPI
import os
import sys


comm = MPI.Comm.Get_parent()
1/0
print comm.Get_rank()
data = comm.recv(source=0, tag=11)

#print data
#comm.Bcast(data,root = 0)
print "worker ", data


comm.send('done', dest=0, tag=12)
comm.Disconnect()