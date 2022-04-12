from matplotlib import pyplot as plt
import numpy as np

#line_gen returns a line between two points A & B
def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

#plt_point plots point A
def plt_point(A):
  plt.plot(A[0],A[1],marker = "o", markersize = 3, color = 'black') 

figure, axes = plt.subplots( 1 )
R = 20 #R is radius of circle
n = 64
t = np.linspace(0, 2*np.pi, n)
x = R*np.cos(t)
y = R*np.sin(t)
plt.plot(x,y,linewidth=2.5, label='Circle') #plotting the circle

# Let, A be (h,k) 
h = 12
k = -16

theta = np.pi*(70/180) #theta is angle DAE given as 70 degree
O = np.array([0,0]) #Let, center of circle be origin
A = np.array([h,k])
REF_Y_AXIS = np.array([[-1,0],[0,1]])
B = REF_Y_AXIS @ A #B is reflection of A about Y-axis
ROTATE = np.array([[np.cos(2*theta),-np.sin(2*theta)],[np.sin(2*theta), np.cos(2*theta)]]) #RotationMatrix
D = ROTATE @ B #D can be obtained by rotating B by 2theta ACW about O

c = -10 #c stands for x-coordinate of C
f = np.sqrt(R**2 - c**2) #f will find y-coordinate of C using equation of circle
C = np.array([c,f])

e = 25 #e stands for x-coordinate of E
E = np.array([e,k])

x_BE = line_gen(B,E)
x_BD = line_gen(B,D)
x_OB = line_gen(O,B)
x_OD = line_gen(O,D)
x_BC = line_gen(B,C)
x_CD = line_gen(C,D)
x_AD = line_gen(A,D)

plt.plot(x_BE[0,:],x_BE[1,:], label = 'Line BE')
plt.plot(x_BD[0,:],x_BD[1,:], label = 'Chord BD')
plt.plot(x_OB[0,:],x_OB[1,:], label = 'Radius OB')
plt.plot(x_OD[0,:],x_OD[1,:], label = 'Radius OD')
plt.plot(x_BC[0,:],x_BC[1,:], label = 'Chord BC')
plt.plot(x_CD[0,:],x_CD[1,:], label = 'Chord CD')
plt.plot(x_AD[0,:],x_AD[1,:], label = 'Chord AD')

plt.annotate("A",A,xytext=(0,-12),textcoords="offset points")
plt.annotate("B",B,xytext=(-5,-12),textcoords="offset points")
plt.annotate("O",O,xytext=(0,5),textcoords="offset points")
plt.annotate("D",D,xytext=(0,5),textcoords="offset points")
plt.annotate("C",C,xytext=(-5,5),textcoords="offset points")
plt.annotate("E",E,xytext=(0,-12),textcoords="offset points")

plt_point(O)
plt_point(A)
plt_point(B)
plt_point(C)
plt_point(D)
plt_point(E)

plt.ylabel('Y-axis')
plt.xlabel('X-axis')
plt.legend(prop = {'size' : 5.9}, loc = 'upper right', shadow = True)
plt.grid()
axes.set_aspect( 1 )
plt.show()