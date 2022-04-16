import matplotlib.pyplot as plt
import numpy as np

def dir_vec(A,B):
  return B-A

def norm_vec(A,B):
  return np.matmul(omat, dir_vec(A,B))

def line_dir_pt(m,A,k1,k2):
  len = 10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB

def line_intersect(n1,A1,n2,A2):
  N=np.vstack((n1,n2))
  print(type(N))
  p = np.zeros(2)
  p[0] = n1@A1
  p[1] = n2@A2
  #Intersection
  P=np.linalg.inv(N)@p
  return P

def plt_point(A):
  plt.plot(A[0],A[1],marker = "o", markersize = 3, color = 'black') 

x_AB = line_dir_pt(np.array([3,4]),np.array([12,6]),0,25);
x_CD = line_dir_pt(np.array([1,3]),np.array([12,6]),0,25);

plt.plot(x_AB[0,:],x_AB[1,:], label = 'Line AB')
plt.plot(x_AB[0,:],x_AB[1,:], label = 'Line AB')

P_5 = line_intersect(np.array([3,4]),np.array([20,0]),np.array([1,3]),np.array([0,10]));
plt_point(P_5)

plt.show()
