import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
titanic = sns.load_dataset('titanic')
sns.barplot(data=titanic, x='pclass', y='fare')
plt.show()

# HUE parameter
sns.barplot(data=titanic, x='pclass', y='fare', hue='sex')
plt.show()

#Plotting Specific Subsets
titanic_cherbourg = titanic[titanic['embarked'] == 'C']
sns.barplot(data=titanic_cherbourg, x='pclass', y='fare')
plt.show()

# Custom Estimators
sns.barplot(data=titanic, x='pclass', y='age', estimator=np.median)
plt.show()


# HEATMAP

# Basic heatmap
flights = sns.load_dataset('flights')
flights_pivot = flights.pivot('month', 'year', 'passengers')
sns.heatmap(data=flights_pivot)
plt.show()

# Adding Custom Tick Labels
sns.heatmap(data=flights_pivot)
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.xlabel('Year')
plt.ylabel('Month')
plt.show()

# Heatmap with Masking
mask = np.triu(np.ones_like(flights_pivot, dtype=bool))
sns.heatmap(data=flights_pivot, mask=mask, cmap='viridis')
plt.show()





