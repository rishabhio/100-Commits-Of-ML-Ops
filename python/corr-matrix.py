


# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

# Exclude non-numeric columns
numeric_tips = tips.select_dtypes(include=['float64', 'int64'])

# Example 6: Heatmap
correlation_matrix = numeric_tips.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap of Tips Data')
plt.show()
