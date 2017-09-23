import pandas as pd
import matplotlib.pyplot as plt
import scipy
import numpy as np
import seaborn as sns #heatmap, stripplot
from csv import DictReader
import plotly.graph_objs as go #Choropleth/ Mixeed Subplot graphs
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)
import plotly.plotly as py #choropleth map
from plotly.graph_objs import *

happy = pd.read_csv('/Users/andiedonovan/myProjects/happy_report/happy15.csv', ',')

happy.columns=['country','region','happiness_rank',
'happiness_score','standard_error','gdp',
'family','life_expectancy','freedom',
'government_trust','generosity','dystopia_residual']

happy.describe()
happy.head()

plt.scatter(happy['gdp'], happy['life_expectancy'])
plt.show()

a = sns.stripplot(x="region", y="happiness_rank", data=happy, jitter=True)
plt.xticks(rotation=90)
plt.show()

happy.corr(method='pearson')
corrmap = happy.corr()
sns.heatmap(corrmap, vmax=.8, square=True)
plt.show()

plt.scatter(happy['gdp'], happy['happiness_rank'])
plt.show()

regions = happy.region.unique()
print(regions) # countries categorized into 10 regions
rarray = np.array(happy.region)

print('region, count, avg rank, avg score')
for i in regions:
    print(i, rlist.count(i))

#https://plot.ly/python/choropleth-maps/
scl = [[0.0, 'rgb(26,50,49)'],[0.2, 'rgb(52,100,98)'],[0.4, 'rgb(70,134,132)'],\
            [0.6, 'rgb(137,193,191)'],[0.8, 'rgb(178,228,227)'],[1.0, 'rgb(238,246,246)']]
#create a dictionary to map color codes to different scale marks
#This will assign different shades of blue to the various levels of happiness with the darkest
#shade correstponding to the highest ranking and the lightest shade corresponding to the lowest
#for color palates: https://www.colorcodehex.com/9ac9ca/

data = dict(type = 'choropleth', 
           locations = happy['country'], #plots the countries on our map
           colorscale = scl, 
           reversescale = True, #true to make higher scoring countries darker 
           locationmode = 'country names', #determines set of locations to match our locations entrie (use country names for world map)
           z = happy['happiness_score'], #the variable we are measuring
           marker= dict(line=dict(color='black', 
                        width=1)), #country outlines
           text = happy['country'], #hover text
           hoverlabel= dict(bgcolor= 'D68C24',
                            font=dict(family='Times New Roman',
                                      color='white')), #changes our hover text style
           colorbar = {'title':'Happiness Score', 'nticks':9}
           ) #titles the bar on the right side of the plot      
layout = dict(title = 'Global Happiness Choropleth Plot', 
             geo = dict(showframe = True, #puts a box around plot
                       projection = {'type': 'Mercator'})) #cylindrical map projection (standard)

My_choromap = go.Figure(data = [data], layout=layout)
iplot(My_choromap)

reg_df= happy.as_matrix(columns=['country','region'])
reg_df= pd.DataFrame(my_df)
reg_df.columns= ['Country', 'Region']
reg_df['Countries in Region'] = my_df2.groupby(['region'])['country'].transform('count')

#locations = Bar(x=reg_df['Region'],y=reg_df['Countries in Region'], marker=dict(color='#CF1020'))
bar_data = [go.Bar(
            x=reg_df['Region'],
            y=reg_df['Countries in Region'],
            marker=dict(color='rgb(192,135,138)',
                        line=dict(color='rgb(117,61,61)')))]
bar_layout = go.Layout(
    title='Regions by Country Count',
    yaxis=dict(
        title='<br>Countries per Region',
        titlefont=dict(
            size=16,
            color='rgb(107, 107, 107)'
        )))
bar_fig = go.Figure(data=bar_data, layout=bar_layout)
iplot(bar_fig)

bar_data2 = [go.Bar(
            x=happy['region'],
            y=happy['happiness_score'],
            marker=dict(color='rgb(206,220,206)',                     
                        line=dict(color='rgb(60,114,60)')))]
bar_layout2 = go.Layout(
    title='Regions by Average Score',
    yaxis=dict(
        title='<br>Average Happiness Score',
        titlefont=dict(
            size=16,
            color='rgb(107, 107, 107)'
        )))
bar_fig2 = go.Figure(data=bar_data2, layout=bar_layout2)
iplot(bar_fig2)

#locations = Bar(x=happy['region'],y=happy['happiness_score'], marker=dict(color='#CF1020'))
bar_data3 = Bar(
            x=happy['region'],
            y=happy['happiness_score'],
            marker=dict(color='rgb(205,205,219)',
                        line=dict(color='rgb(117,61,61)'))
        )
trace3 = dict(
  geo= 'geo3', 
  hoverinfo='text',
  locations=happy['country'],
  locationmode = 'country names',
  marker=dict(
    size= 4,
    opacity= 0.8,
    color= '#CF1020',
    colorscale= 'Viridis'), 
  mode= "markers", 
  type= "scattergeo"
)


layout = {
  "plot_bgcolor": 'black',
  "paper_bgcolor": 'black',
  "titlefont": {
      "size": 45,
      "family": "Raleway"
  },
  "font": {
      "color": 'white'
  },
  "dragmode": "zoom", 
  "geo3": {
    "domain": {
      "x": [0, 0.55], 
      "y": [0, 0.9]
    }, 
    "lakecolor": "rgba(127,205,255,1)",
    "oceancolor": "rgb(6,66,115)",
    "landcolor": 'white',
    "projection": {"type": "orthographic"}, 
    "scope": "world", 
    "showlakes": True,
    "showocean": True,
    "showland": True,
    "bgcolor": 'black'
  }, 
  "margin": {  #margins around the entire box
    "r": 10, 
    "t": 80, 
    "b": 40, 
    "l": 10
  }, 
  "showlegend": False, 
  "title": "Regions Comparison", 
  "xaxis": {
    "anchor": "auto", 
    "domain": [0.6, 0.95],
    "tickangle": "50"
  }, 
  "yaxis": {
    "title": "Happiness Score",
    "anchor": "auto", 
    "domain": [0.65, 0.95],
    "showgrid": False
  }
}

annotations = { "text": "Source: UN Happiness Report",
               "showarrow": False,
               "xref": "paper",
               "yref": "paper",
               "x": 0,
               "y": 0}


layout['annotations'] = [annotations]
data2 = Data([bar_data3, trace3])
fig = Figure(data=data2, layout=layout)
iplot(fig)

choro_data = dict(
           geo= dict(projection=dict(type='orthographic')),
           type = 'choropleth', 
           locations = happy['country'], #plots the countries on our map
           locationmode = 'country names', #determines set of locations to match our locations entrie (use country names for world map)
           z = happy['happiness_score'], #the variable we are measuring
           marker= dict(line=dict(color='black', 
                        width=1)), #country outlines
           text = happy['country'], #hover text
           hoverlabel= dict(bgcolor= 'D68C24',
                            font=dict(family='Times New Roman',
                                      color='white'))) #changes our hover text style   
    
bar_data3 = Bar(
            x=happy['region'],
            y=happy['happiness_score'],
            marker=dict(color='rgb(205,205,219)',
                        line=dict(color='rgb(117,61,61)'))
        )


layout = {
  "plot_bgcolor": 'black',
  "paper_bgcolor": 'black',
  "titlefont": {
      "size": 45,
      "family": "Raleway"
  },
  "font": {
      "color": 'white'
  },
  "margin": {  #margins around the entire box
    "r": 10, 
    "t": 80, 
    "b": 40, 
    "l": 10
  }, 
  "showlegend": False, 
  "title": "Regions By Happiness Score", 
  "xaxis": {
    "anchor": "auto", 
    "domain": [0.6, 0.95],
    "tickangle": "50"
  }, 
  "yaxis": {
    "title": "Happiness Score",
    "anchor": "auto", 
    "domain": [0.65, 0.95],
    "showgrid": False
  },
  "dragmode": "zoom", 
  "geo": {
      "domain": {
      "x": [0, 0.5], 
      "y": [0.2, 0.9]},
      "projection": {'type': "orthographic"},
      "lakecolor": "rgba(127,205,255,1)",
      "oceancolor": "rgb(6,66,115)",
      "landcolor": 'white',
      "projection": {"type": "orthographic"}, 
      "scope": "world", 
      "showlakes": True,
      "showocean": True,
      "showland": True,
      "bgcolor": 'black'
  #"legend": {
  #   "domain": {
  #   "x": [0.5, 0.7],
  #   "y": [0.2, 0.9]}}}
  }}


annotations = { "text": "Source: UN Happiness Report",
               "showarrow": False,
               "xref": "paper",
               "yref": "paper",
               "x": 0,
               "y": 0}


layout['annotations'] = [annotations]
data3 = Data([bar_data3, choro_data])
fig3 = Figure(data=data3, layout=layout)
iplot(fig3)

#https://plot.ly/python/choropleth-maps/
scl = [[0.0, 'rgb(26,50,49)'],[0.2, 'rgb(52,100,98)'],[0.4, 'rgb(70,134,132)'],\
            [0.6, 'rgb(137,193,191)'],[0.8, 'rgb(178,228,227)'],[1.0, 'rgb(238,246,246)']]
#create a dictionary to map color codes to different scale marks
#This will assign different shades of blue to the various levels of happiness with the darkest
#shade correstponding to the highest ranking and the lightest shade corresponding to the lowest
#for color palates: https://www.colorcodehex.com/9ac9ca/

data = dict(type = 'choropleth', 
           locations = happy['country'], #plots the countries on our map
           colorscale = scl, 
           reversescale = True, #true to make higher scoring countries darker 
           locationmode = 'country names', #determines set of locations to match our locations entrie (use country names for world map)
           z = happy['happiness_score'], #the variable we are measuring
           marker= dict(line=dict(color='black', 
                        width=1)), #country outlines
           text = happy['country'], #hover text
           hoverlabel= dict(bgcolor= 'D68C24',
                            font=dict(family='Times New Roman',
                                      color='white')), #changes our hover text style
           colorbar = {'title':'Happiness Score', 'nticks':9}
           ) #titles the bar on the right side of the plot      
layout = dict(title = 'Global Happiness Choropleth Plot', 
             geo = dict(showframe = True, #puts a box around plot
                       projection = {'type': 'orthographic'})) #cylindrical map projection (standard)

My_choromap = go.Figure(data = [data], layout=layout)
iplot(My_choromap)
