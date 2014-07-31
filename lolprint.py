from mpi4py import MPI
import os
import sys

#data = sys.argv[1]

#print data
comm = MPI.Comm.Get_parent()

data = comm.recv(source=0, tag=11)

if comm.Get_rank() == 1:
    print data
comm.Disconnect()