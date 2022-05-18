import random
r = 7 # r is the number of red balls in the urn
b = 9 # b is the number of black balls in the urn
P_replacement = r/(r+b)
print(P_replacement)
x = random.randint(0,1)
if(x == 0):
    P_without_replacement = r-1/(r+b-1)
else:
    P_without_replacement = r/(r+b-1)
print(P_without_replacement)