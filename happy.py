import pandas as pd
import matplotlib.pyplot as plt
import scipy
import seaborn

happy = pd.read_csv('/Users/andiedonovan/Documents/Projects/happy15.csv', ',')

happy.columns=['country','region','happiness_rank',
'happiness_score','standard_error','gdp',
'family','life_expectancy','freedom',
'government_trust','generosity','dystopia_residual']

happy.describe()
plt.scatter(happy['gdp'], happy['life_expectancy'])
plt.show()
happy.corr(method='pearson')
plt.scatter(happy['gdp'], happy['happiness_rank'])
plt.show()
