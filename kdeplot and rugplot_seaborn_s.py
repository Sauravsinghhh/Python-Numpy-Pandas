import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')
sns.kdeplot(data=titanic, x='fare')
sns.rugplot(data=titanic, x='fare', height=0.1)
plt.show()


# Rug Plot with Scatter Plot
iris = sns.load_dataset('iris')
tips = sns.load_dataset('tips')

plt.figure(figsize=(10, 6))
sns.scatterplot(data=tips, x='total_bill', y=[0]*len(tips), alpha=0.6, edgecolor='w')
sns.rugplot(data=iris, x='petal_width', height=0.1)
plt.title('KDE Plot of Total Bill with Scatter Plot')
plt.show()


# KDE Plot
iris = sns.load_dataset('iris')
sns.kdeplot(data=iris, x='sepal_length')
plt.show()

# Filled KDE Plot
sns.kdeplot(data=iris, x='petal_length', fill=True)
plt.show()

# KDE Plot with Custom Palette
tips = sns.load_dataset('tips')
sns.kdeplot(data=tips, x='total_bill', hue='time', palette='coolwarm')
plt.show()

# KDE Plot with Multiple Layers
penguins = sns.load_dataset('penguins')
sns.kdeplot(data=penguins, x='flipper_length_mm', hue='species', common_norm=False)
plt.show()








