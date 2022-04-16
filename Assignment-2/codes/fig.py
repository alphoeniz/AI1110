# ICSE 2018 Grade 12 22
# Varun Gupta (cs21btech11060)

# This code shades feasible region for the solution.  

# Python libraries for math and graphics
import matplotlib.pyplot as plt
import numpy as np
from params import *

#3x+4y=90

def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

#Intersection of two lines
def line_intersect(n1,A1,n2,A2):
  N=np.vstack((n1,n2))
  print(type(N))
  p = np.zeros(2)
  p[0] = n1@A1
  p[1] = n2@A2
  #Intersection
  P=np.linalg.inv(N)@p
  return P

def norm_vec(A,B):
  return np.matmul(omat, dir_vec(A,B))

def plt_point(A):
  plt.plot(A[0],A[1],marker = "o", markersize = 3, color = 'black')

plt.axes()
plt.xlim(0, 25)
plt.ylim(0, 25);

plt.ylabel('Y-axis')
plt.xlabel('X-axis')
plt.legend(loc = 'best')
plt.grid()
plt.show()