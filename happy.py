import pandas as pd
import matplotlib.pyplot as plt
import scipy
import numpy
import seaborn as sns #heatmap, stripplot
from csv import DictReader
import plotly #choropleth map
import plotly.plotly as py #choropleth map
import plotly.graph_objs as go #choropleth map

happy = pd.read_csv('/Users/andiedonovan/myProjects/happy_report/happy15.csv', ',')

happy.columns=['country','region','happiness_rank',
'happiness_score','standard_error','gdp',
'family','life_expectancy','freedom',
'government_trust','generosity','dystopia_residual']

happy.describe()
happy.head()

plt.scatter(happy['gdp'], happy['life_expectancy'])
plt.show()

happy.corr(method='pearson')
corrmap = happy.corr()
sns.heatmap(corrmap, vmax=.8, square=True)

plt.scatter(happy['gdp'], happy['happiness_rank'])
plt.show()

regions = happy.region.unique()
print(regions) # countries categorized into 10 regions
#regionslist= happy['region']
rlist = list(happy.region)
print(rlist)

a = sns.stripplot(x="region", y="happiness_rank", data=happy, jitter=True)
plt.xticks(rotation=90)

numpy.mean('happiness_score')

print('region, count')
#want to add in average rank & score
for i in regions:
    print(i, rlist.count(i), numpy.mean(i))
