# CBSE Class 9 Statistics Example 5
# Varun Gupta (cs21btech11060)

# Solving given problem using pandas.

import pandas as pd 
df = pd.read_excel("../tables/data.xlsx")
df.index += 1
months = df.months
students = df.students
print(students[11])
print(months[students.idxmax()])