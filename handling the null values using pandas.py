import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Handling the null values

data = {
    'Product': ['A', 'B', 'C', 'D', 'E'],
    'Region': ['North', 'South', 'East', 'West', None],
    'Sales_Q1': [200, 180, None, 300, 150],
    'Sales_Q2': [None, 210, 190, 280, 160],
    'Sales_Q3': [220, None, 195, 290, None],
    'Sales_Q4': [230, 220, None, 310, 170]
}

df = pd.DataFrame(data)
print(df)

# Step 1: Identify null values

print("\nIdentifying null values using isnull:")
print(df.isnull())
print(df.isnull().sum())
print("\nDataFrame summary using info:")
df.info()


# Step 2: Handle null values

# Replace all NaN values with a specified constant value (e.g., 0)
df_filled_constant = df.fillna(0)
print("\nDataFrame after replacing NaN with 0:")
print(df_filled_constant)

# Use the 'pad' method to forward fill missing values
df_filled_pad = df.fillna(method='pad')
print("\nDataFrame after forward fill (pad method):")
print(df_filled_pad)

# Use the 'bfill' method to backward fill missing values
df_filled_bfill = df.fillna(method='bfill')
print("\nDataFrame after backward fill (bfill method):")
print(df_filled_bfill)

# Perform column-wise filling with different values for different columns
fill_values = {
    'Region': 'Unknown',
    'Sales_Q1': df['Sales_Q1'].mean(),
    'Sales_Q2': df['Sales_Q2'].median(),
    'Sales_Q3': df['Sales_Q3'].mode()[0],  # Most frequent value
    'Sales_Q4': 0
}

df_filled_columnwise = df.fillna(fill_values)
print("\nDataFrame after column-wise filling:")
print(df_filled_columnwise)

# Fill missing values along columns
df_filled_row_axis = df.fillna(df.mean(axis=1), axis=1)
print("\nDataFrame after filling along the row axis:")
print(df_filled_row_axis)

# Fill NaN with mean of each column
df_filled_mean = df.fillna(df.mean(numeric_only=True))
print("\nDataFrame after filling NaN with mean:")
print(df_filled_mean)

# Fill NaN with median of each column
df_filled_median = df.fillna(df.median(numeric_only=True))
print("\nDataFrame after filling NaN with median:")
print(df_filled_median)

# Fill NaN with mode of each column
df_filled_mode = df.fillna(df.mode().iloc[0])
print("\nDataFrame after filling NaN with mode:")
print(df_filled_mode)

# Fill NaN with minimum value of each column
df_filled_min = df.fillna(df.min(numeric_only=True))
print("\nDataFrame after filling NaN with minimum value:")
print(df_filled_min)

# Fill NaN with maximum value of each column
df_filled_max = df.fillna(df.max(numeric_only=True))
print("\nDataFrame after filling NaN with maximum value:")
print(df_filled_max)


# Step 3: Plot graphs to visualize the effect of filling NaN values

fig, axes = plt.subplots(3, 2, figsize=(15, 18))

# Plot a bar graph comparing the original data with data after filling with mean
df.set_index('Product')[['Sales_Q1', 'Sales_Q2', 'Sales_Q3', 'Sales_Q4']].plot(kind='bar', ax=axes[0, 0], title="Original Data")
df_filled_mean.set_index('Product')[['Sales_Q1', 'Sales_Q2', 'Sales_Q3', 'Sales_Q4']].plot(kind='bar', ax=axes[0, 1], title="Filled with Mean")

# Plot a line graph showing the trends before and after filling with median
df.set_index('Product')[['Sales_Q1', 'Sales_Q2', 'Sales_Q3', 'Sales_Q4']].plot(kind='line', marker='o', ax=axes[1, 0], title="Original Data")
df_filled_median.set_index('Product')[['Sales_Q1', 'Sales_Q2', 'Sales_Q3', 'Sales_Q4']].plot(kind='line', marker='o', ax=axes[1, 1], title="Filled with Median")

# Plot scatter plots to compare original and mode-filled data
axes[2, 0].scatter(df.index, df['Sales_Q1'], label='Original Sales_Q1', color='blue')
axes[2, 0].scatter(df_filled_mode.index, df_filled_mode['Sales_Q1'], label='Filled Sales_Q1', color='red')
axes[2, 0].set_title("Original vs Mode-filled Sales_Q1")
axes[2, 0].legend()

axes[2, 1].scatter(df.index, df['Sales_Q2'], label='Original Sales_Q2', color='blue')
axes[2, 1].scatter(df_filled_mode.index, df_filled_mode['Sales_Q2'], label='Filled Sales_Q2', color='red')
axes[2, 1].set_title("Original vs Mode-filled Sales_Q2")
axes[2, 1].legend()
plt.tight_layout()
plt.show()


# Step 4: Drop NaN values using various parameters

# Drop rows with any NaN values
df_dropped_any = df.dropna()
print("\nDataFrame after dropping rows with any NaN values:")
print(df_dropped_any)

# Drop columns with any NaN values
df_dropped_columns_any = df.dropna(axis=1)
print("\nDataFrame after dropping columns with any NaN values:")
print(df_dropped_columns_any)

# Drop rows with NaN values only in specified columns
df_dropped_subset = df.dropna(subset=['Sales_Q3', 'Sales_Q4'])
print("\nDataFrame after dropping rows with NaN values in 'Sales_Q3' and 'Sales_Q4':")
print(df_dropped_subset)

# Drop rows if a specified number of non-NaN values are not present (thresh)
df_dropped_thresh = df.dropna(thresh=4)
print("\nDataFrame after dropping rows with less than 4 non-NaN values:")
print(df_dropped_thresh)

# Drop NaN values based on different axes (row and column)
df_dropped_rows = df.dropna(axis=0)  # Default, drops rows
print("\nDataFrame after dropping rows with any NaN values (axis=0):")
print(df_dropped_rows)

df_dropped_columns = df.dropna(axis=1)
print("\nDataFrame after dropping columns with any NaN values (axis=1):")
print(df_dropped_columns)

# Drop rows or columns based on 'how' parameter ('all' or 'any')
df_dropped_all_rows = df.dropna(how='all')
print("\nDataFrame after dropping rows where all values are NaN:")
print(df_dropped_all_rows)

# Adding a column with all NaNs for demonstration
df['All_NaN'] = np.nan

df_dropped_all_columns = df.dropna(axis=1, how='all')
print("\nDataFrame after dropping columns where all values are NaN:")
print(df_dropped_all_columns)