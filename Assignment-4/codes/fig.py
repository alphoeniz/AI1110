# CBSE Class 9 Probablility Section 15.2 Example 9
# Varun Gupta (cs21btech11060)

# Plotting the binomial distribution using matplotlib.

from scipy.stats import binom
import numpy as np
import matplotlib.pyplot as plt

fig1, (ax1, ax2) = plt.subplots(1, 2)
n = 2
p = 0.5
rv = binom(n, p)
X = np.arange((n+1))
pmf_val = rv.pmf(X)
ax1.plot(X, pmf_val, 'bo')
ax1.vlines(X, 0, pmf_val, label='Probability')
ax1.legend(loc = 'upper left')
ax1.set_title("Probability Mass Distribution") 
cdf_val = rv.cdf(X)
ax2.plot(X, cdf_val, 'bo')
ax2.vlines(X, 0, cdf_val, label='Cumulative')
ax2.legend()
ax2.set_title("Cumulative Distribution")
plt.show()