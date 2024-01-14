
# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')
tips = sns.load_dataset('tips')


# import pdb 
# pdb.set_trace() 


# # Example 1: Scatter Plot
# sns.scatterplot(x='sepal_length', y='sepal_width', data=iris)
# plt.title('Scatter Plot of Sepal Length vs. Sepal Width')
# plt.show()

# # Example 2: Line Plot
# sns.lineplot(x='day', y='total_bill', data=tips)
# plt.title('Line Plot of Total Bill over Days')
# plt.show()

# # Example 3: Box Plot
# sns.boxplot(x='species', y='petal_length', data=iris)
# plt.title('Box Plot of Petal Length by Species')
# plt.show()

# # Example 4: Violin Plot
# sns.violinplot(x='species', y='petal_width', data=iris)
# plt.title('Violin Plot of Petal Width by Species')
# plt.show()

# # Example 5: Bar Plot
# sns.barplot(x='day', y='total_bill', data=tips)
# plt.title('Bar Plot of Total Bill by Day')
# plt.show()

# Example 6: Heatmap
# correlation_matrix = tips.corr()
# import pdb 
# pdb.set_trace() 
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
# plt.title('Correlation Heatmap of Tips Data')
# plt.show()

# # Example 7: Pair Plot
# sns.pairplot(iris, hue='species')
# plt.suptitle('Pair Plot of Iris Dataset by Species', y=1.02)
# plt.show()

# # Example 8: Histogram
# sns.histplot(tips['total_bill'], bins=30, kde=True)
# plt.title('Histogram of Total Bill')
# plt.show()

# # Example 9: Count Plot
# sns.countplot(x='day', data=tips)
# plt.title('Count Plot of Days')
# plt.show()

# Example 10: Joint Plot
sns.jointplot(x='sepal_length', y='sepal_width', data=iris, kind='scatter')
plt.suptitle('Joint Plot of Sepal Length vs. Sepal Width')
plt.show()
