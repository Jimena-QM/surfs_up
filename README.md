# Surfs_up
SQLite data hawaii.sqlite was explored with SQLAlchemy that connects and generates queries. Jupyter Lab with Python was used for analysis. 

# Overview
The purpose of this analysis is to present statistical weather analysis in Oahu to a possible investor, in order to open Surf n' Shake shop. The shop will sell surf boards and ice cream year round. The investor is a bit reluctant since he invested previously in something similar and the business failed because of weather conditions. June and December temperature data was queried using SQLAlchemy. With Python the data was transformed to a DataFrame in order to get the statistical analysis. 
For a deeper analysis the months of March, June, September and December were concatenated into a single DataFrame with temperature and precipitation. With this new DataFrame a statistical analysis was genereated. 

# Results
Three key differences in weather between June and December are:
- December min temperature is 8 degrees lower than June. Dec (56) / June (64)
- December has 183 less data points than June. Dec (1517) / June (1700)
- The average temperature varies only by 4 degrees. 
Given those minor differences in temperature between the two months, we can preliminary conclude that the temperature does not fluctuate considerably throughout the year. 


# Summary
