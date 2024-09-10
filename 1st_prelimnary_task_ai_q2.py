# -*- coding: utf-8 -*-
"""1st-prelimnary-task-ai-q2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UvsG_3162ok5-3qp-jgoHaMqw8vQZMwI

**QUESTION 2.1**
"""

import pandas as pd

data = [
    [170, 65, 19, 85, 5],
    [180, 75, 20, 90, 6],
    [160, 55, 18, 80, 4],
    [175, 70, 21, 88, 7],
    [155, 50, 19, 82, 5],
    [165, 62, 22, 89, 6],
    [178, 80, 23, 91, 7],
    [162, 58, 20, 78, 3],
    [172, 68, 19, 86, 5],
    [169, 66, 20, 84, 4],
    [171, 64, 22, 87, 6],
    [177, 72, 21, 90, 9],
    [174, 76, 24, 88, 8],
    [158, 52, 18, 75, 3],
    [164, 63, 19, 81, 4]
]
# column names being ‘Height’, ‘Weight’, ‘Age’, ‘Avg_Grade’ and ‘Courses’ in that order.

df = pd.DataFrame(data, columns = ['Height', 'weight', 'Age', 'Avg_Grade', 'Courses'])


print(df)

"""**QUESTION 2.2**"""

print(df.describe())

"""**QUESTION 2.3**"""

print(df['Age'].value_counts())

"""**QUESTION 2.4**"""

print(df[df['Age'] > 20])

"""**QUESTION 2.5**"""

grouped_by_age = df.groupby('Age').mean()

print(grouped_by_age)