# Surfs_up
SQLite data hawaii.sqlite was explored with SQLAlchemy that connects and generates queries. Jupyter Lab with Python was used for analysis. 

# Overview
The purpose of this analysis is to present statistical weather analysis in Oahu to a possible investor, in order to open Surf n' Shake shop. The shop will sell surf boards and ice cream year round. The investor is a bit reluctant since he invested previously in something similar and the business failed because of weather conditions. June and December temperature data was queried using SQLAlchemy. With Python the data was transformed to a DataFrame in order to get the statistical analysis. 
For a deeper analysis the months of March, June, September and December were concatenated into a single DataFrame with temperature and precipitation. With this new DataFrame a statistical analysis was genereated. 

# Results
Three key differences in weather between June and December are:
- December min temperature is 8 degrees lower than June. Dec (56F) / June (64F)
- December has 183 less data points than June. Dec (1517) / June (1700)
- The average temperature varies only by 4 degrees. 
- The std deviation between the two months is less than 0.5, with this we know that the temperature within each month varies less than 4 degrees. 
Given those minor differences in temperature between the two months, we can preliminary conclude that the temperature does not fluctuate considerably throughout the year. 
![June_Temp_Stats](https://github.com/Jimena-QM/surfs_up/blob/main/Resources/D1_June_Temps.png)
![Dec_Temp_Stats](https://github.com/Jimena-QM/surfs_up/blob/main/Resources/D2_Dec_Temps.png)

# Summary
The average temperature in Oahu through the year is above 70 degrees, though it can be as low as 56 degrees and as high as 87 degrees. If we consider room temperature between 68F -72F and the standar deviation is less than 4 degrees, Oahu has the right temperature for surfing and ice cream year round. Taking into account precipitation, December and March have around 20 average precipitation. June and September have 13 and 16 precipitation respectively. Given this, investing in Surf n' Shake in Oahu is a sound investment that will most likely give a good return. 

Additional queries were executed that included temperature and precipitation for March, June, September and December. 
The data was extracted and concatenated by the following code:

![Temp_Prcpt_Code](https://github.com/Jimena-QM/surfs_up/blob/main/Resources/D3_python_code.png)

Below the statistical analysis of temperature and precipitation:

![Results](https://github.com/Jimena-QM/surfs_up/blob/main/Resources/D3_AdditionalQueries.png)