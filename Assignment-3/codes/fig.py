# CBSE Class 9 Statistics Example 5
# Varun Gupta (cs21btech11060)

# Plotting given bar graph using matplotlib.

import matplotlib.pyplot as plt
data = {'Jan':3, 'Feb':4, 'Mar':2, 'Apr':2, 'May':5, 'June':1, 'July':2, 'Aug':6, 'Sept':3, 'Oct':4, 'Nov':4, 'Dec':4}
months = list(data.keys())
students = list(data.values())
fig = plt.figure(figsize=(10,5))
plt.bar(months, students, color='skyblue', width= 0.4)
plt.xlabel('Months of Birth')
plt.ylabel('Number of Students')
plt.show()