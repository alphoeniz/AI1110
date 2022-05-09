# CBSE Class 9 Probablility Section 15.2 Example 9
# Varun Gupta (cs21btech11060)

# Plotting the binomial distribution using matplotlib.

from scipy.stats import binom
import numpy as np

n = 2
p = 0.5
rv = binom(n, p)
X = np.arange((n+1))
pmf_val = rv.pmf(X)
prob_zero = pmf_val[0]
ans = 1 - prob_zero
print(ans)