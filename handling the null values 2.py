import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample DataFrame
data = {
    'Product': ['A', 'B', 'C', 'D', 'E'],
    'Region': ['North', 'South', 'East', 'West', None],
    'Sales_Q1': [200, 180, None, 300, 150],
    'Sales_Q2': [None, 210, 190, 280, 160],
    'Sales_Q3': [220, None, 195, 290, None],
    'Sales_Q4': [230, 220, None, 310, 170]
}

df = pd.DataFrame(data)

# Identify null values
null_info = df.isnull().sum()
print("Null values in the DataFrame:")
print(null_info)


# Interpolation Techniques

# Linear Interpolation
df_interpolated_linear = df.interpolate(method='linear')
print("\nDataFrame after Linear Interpolation:")
print(df_interpolated_linear)

# Padding (Forward Fill)
df_interpolated_pad = df.interpolate(method='pad')
print("\nDataFrame after Padding Interpolation:")
print(df_interpolated_pad)

# Backward Fill
df_interpolated_bfill = df.interpolate(method='bfill')
print("\nDataFrame after Backward Fill Interpolation:")
print(df_interpolated_bfill)


# Replace method

# Replace NaN with specific values
df_replace = df.replace({np.nan: -1, None: 'Unknown'})
print("\nDataFrame after Replacing NaN values:")
print(df_replace)


# End of Distribution Method

# Fill NaN with values at the end of the distribution (e.g., 95th percentile)
df_end_of_dist = df.fillna(df.quantile(0.95, numeric_only=True))
print("\nDataFrame after End of Distribution Imputation:")
print(df_end_of_dist)


# Visualizing Before and After Interpolation


# Boxplots to visualize distributions
fig, axes = plt.subplots(2, 3, figsize=(18, 12))

# Original Data
df[['Sales_Q1', 'Sales_Q2', 'Sales_Q3', 'Sales_Q4']].plot(kind='box', ax=axes[0, 0], title='Original Data')
df[['Sales_Q1', 'Sales_Q2', 'Sales_Q3', 'Sales_Q4']].plot(kind='hist', bins=10, alpha=0.7, ax=axes[1, 0], title='Original Data')

# After Linear Interpolation
df_interpolated_linear[['Sales_Q1', 'Sales_Q2', 'Sales_Q3', 'Sales_Q4']].plot(kind='box', ax=axes[0, 2], title='Linear Interpolation')
df_interpolated_linear[['Sales_Q1', 'Sales_Q2', 'Sales_Q3', 'Sales_Q4']].plot(kind='hist', bins=10, alpha=0.7, ax=axes[1, 2], title='Linear Interpolation')
plt.tight_layout()
plt.show()


# Assessing Skewness and Symmetry with Quartiles

# Calculate quartiles
quartiles = df[['Sales_Q1', 'Sales_Q2', 'Sales_Q3', 'Sales_Q4']].describe()
print("\nQuartiles of the original data:")
print(quartiles)

# Calculate Interquartile Range (IQR)
iqr = quartiles.loc['75%'] - quartiles.loc['25%']
print("\nInterquartile Range (IQR):")
print(iqr)


# Advanced Imputation Techniques

# K-Nearest Neighbors (KNN) Imputation
from sklearn.impute import KNNImputer

knn_imputer = KNNImputer(n_neighbors=2)
df_knn_imputed = pd.DataFrame(knn_imputer.fit_transform(df[['Sales_Q1', 'Sales_Q2', 'Sales_Q3', 'Sales_Q4']]), columns=['Sales_Q1', 'Sales_Q2', 'Sales_Q3', 'Sales_Q4'])
print("\nDataFrame after KNN Imputation:")
print(df_knn_imputed)


# Multiple Imputation by Chained Equations (MICE)

from sklearn.experimental import enable_iterative_imputer  
from sklearn.impute import IterativeImputer

mice_imputer = IterativeImputer(max_iter=10, random_state=0)
df_mice_imputed = pd.DataFrame(mice_imputer.fit_transform(df[['Sales_Q1', 'Sales_Q2', 'Sales_Q3', 'Sales_Q4']]), columns=['Sales_Q1', 'Sales_Q2', 'Sales_Q3', 'Sales_Q4'])
print("\nDataFrame after MICE Imputation:")
print(df_mice_imputed)

