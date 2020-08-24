"""
Detecting outliers and fixing them
> Boston House Pricing Datase
"""
#---------------------------------------------
#Import the libraries
import pandas as pd
from sklearn.datasets import load_boston
import matplotlib.pyplot as plt

import seaborn as sns
from scipy import stats
import numpy as np
#---------------------------------------------
# Read the dataset
boston = load_boston()
x = boston.data
y = boston.target
columns = boston.feature_names

#create the dataframe
boston_df = pd.DataFrame(boston.data)
boston_df_o1= boston_df[:]
boston_df_o= boston_df[:]
boston_df.columns = columns
boston_df.head()
#---------------------------------------------------
#1.Discovering the outliers with visualization tools
#Box plot
sns.boxplot(x=boston_df['DIS'])

#Scatter plot
fig, ax = plt.subplots(figsize=(16,8))
ax.scatter(boston_df['INDUS'], boston_df['TAX'])
ax.set_xlabel('Proportion of non-retail business acres per town')
ax.set_ylabel('Full-value property-tax rate per $10,000')
plt.show()

#2. Discover the outlier using the mathamatical function 
# Using Z-score
z = np.abs(stats.zscore(boston_df))
print(z)

threshold = 3
print(np.where(z > 3))

#Using IQR
Q1 = boston_df_o1.quantile(0.25)
Q3 = boston_df_o1.quantile(0.75)
IQR = Q3 - Q1
print(IQR)
print((boston_df_o1 < (Q1 - 1.5 * IQR)) | (boston_df_o1 > (Q3 + 1.5 * IQR)))
#---------------------------------------------------
#Correcting the Outlier: COrrecting or removing
#1. using Z-score
boston_df_o = boston_df_o[(z < 3).all(axis=1)]

#IQR score
boston_df_out = boston_df_o1[~((boston_df_o1 < (Q1 - 1.5 * IQR)) |(boston_df_o1 > (Q3 + 1.5 * IQR))).any(axis=1)]
boston_df_out.shape

