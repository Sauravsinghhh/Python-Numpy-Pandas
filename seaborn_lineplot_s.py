import seaborn as sns
import matplotlib.pyplot as plt

# LINEPLOT

# Create a basic line plot
fmri = sns.load_dataset('fmri')
sns.lineplot(data=fmri, x='timepoint', y='signal')
plt.show()

# with colour
fmri = sns.load_dataset('fmri')
sns.lineplot(data=fmri, x='timepoint', y='signal', color='green', linestyle='--')
plt.show()

# Adding Titles and Labels
sns.lineplot(data=fmri, x='timepoint', y='signal')
plt.title('FMRI Signal Over Time')
plt.xlabel('Timepoint')
plt.ylabel('Signal')
plt.show()

# Enhancing with Matplotlib
plt.figure(figsize=(10, 6))
sns.lineplot(data=fmri, x='timepoint', y='signal')
plt.grid(True)

plt.xticks(fontsize=12, rotation=45)
plt.yticks(fontsize=12)
plt.show()




