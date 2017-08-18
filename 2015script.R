# Load packages
'''

'''

install.packages("ggcorrplot")

library(tidyverse)
library(ggcorrplot)

setwd('C:/Users/Lash/Desktop/Data Science/MyProjects/world_happiness_project/happinessdataset')

wh_15<-read_csv('2015.csv')

colnames(wh_15)<-c('country','region','happiness_rank','happiness_score',
                   'standard_error','gdp','family','life_expectancy',
                   'freedom','government_trust','generosity',
                   'dystopia_residual') #vector

head(wh_15) #first 5 points of data

corr <- wh_15 %>%
  #select(freedom, generosity) %>%
  select_if(is.numeric) %>% 
  cor(., use="all.obs", method = "pearson")

corr %>% 
  ggcorrplot()
  #ggcorrplot(corr, hc.order = TRUE, outline.col = "white")

wh_15%>% 
  #pipe operator followed by functions
  select(freedom, generosity)

wh_15%>%
  ggplot(data=., aes(generosity, freedom))+
  geom_boxplot()

wh_15%>%
  ggplot(data=., aes(freedom, generosity))+
    geom_point()+
    ggtitle("Freedom \nv. \nGenerosity")+
    labs(x = "Freedom", y = "Generosity")+
  theme_minimal()


wh_15%>%
  summary()
