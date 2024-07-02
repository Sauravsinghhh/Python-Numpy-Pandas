
# HISTOGRAM

import seaborn as sns
import matplotlib.pyplot as plt

# basic histogram
tips = sns.load_dataset('tips')
sns.histplot(data=tips, x='total_bill')
plt.show()

# KDE parameter
sns.histplot(data=tips, x='total_bill', kde=True)
plt.show()

# Hue Parameter
sns.histplot(data=tips, x='total_bill', hue='sex')
plt.show()

# Multiple(Layer,Dodge,Stack,Fill)
sns.histplot(data=tips, x='total_bill', hue='day', multiple='dodge')
plt.title('Histogram with Dodge Layering')
plt.show()

# ELEMENTS(“bars”, “step”, “poly”)
sns.histplot(data=tips, x='total_bill', element='poly')
plt.title('Histogram with Poly')
plt.show()


