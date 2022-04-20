# ICSE 2018 Grade 12 22
# Varun Gupta (cs21btech11060)

# Plotting the feasible region for the solution.

import matplotlib.pyplot as plt
import numpy as np

plt.xlim(-2, 25)
plt.ylim(-2, 15)

def f(x):
    return (60-3*x)/4
def g(x):
    return (30-x)/3

fxlist = np.linspace(12,20,num = 1000)
fylist = f(fxlist)
gxlist = np.linspace(0,12,num = 1000)
gylist = g(gxlist)

plt.plot(fxlist, fylist, color = "r", label = "$9x+12y=180$")
plt.plot(gxlist, gylist, color = "b", label = "$x+3y=30$")
plt.plot([0,0], [0,10], color = "g")
plt.plot([0,20], [0,0], color = "orange")

plt.text(-1,-1,"$P_3$")
plt.text(20,-1,"$P_4$")
plt.text(0,10.5,"$P_2$")
plt.text(12.25,6.25,"$P_1$")

plt.fill_between(fxlist, fylist, 0, where = (fxlist > 12) & (fxlist <= 20), color = '#00FFBF', label = 'Feasible Region')
plt.fill_between(gxlist, gylist, 0, where = (gxlist > 0) & (gxlist <= 12), color = '#00FFBF')

xpoints = [0,20,0,12]
ypoints = [0,0,10,6]
plt.scatter(xpoints,ypoints, s=40, marker="o", color='cyan')

plt.legend(loc="best")

plt.grid()
plt.show()
