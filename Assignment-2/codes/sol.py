# ICSE 2018 Grade 12 22
# Varun Gupta (cs21btech11060)

# Solving a linear program using cvx
 
# Python libraries for math and graphics
import numpy as np
import cvxpy  as cp

A = np.array(( [3.0, 4.0], [1.0, 3.0 ])).T
b = np.array([ 60.0, 30.0 ]).reshape((2,-1))
c = np.array([ 80.0, 120.0 ])

x = cp.Variable((2,1),nonneg=True)

#Cost function
f = c@x
obj = cp.Maximize(f)

#Constraints
constraints = [A.T@x <= b]

#Solution
cp.Problem(obj, constraints).solve()

print(f.value,x.value)