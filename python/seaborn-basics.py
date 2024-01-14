
import seaborn as sns 
import matplotlib.pyplot as plt 
sns.set_theme(style="darkgrid")


# load an example data set 

tips = sns.load_dataset('tips')

# Create a visualization 

sns.relplot(
    data = tips,
    x = 'total_bill', y = 'tip', col = 'time',
    hue = 'smoker', style = 'smoker', size = 'size',
)

# Show the plot

plt.show()




