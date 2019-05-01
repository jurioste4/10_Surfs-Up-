I  need to do some climate analysis on Honolulu, Hawaii!.

#Climate Analysis and Exploration

I started with useing  Python and SQLAlchemy to do basic climate analysis and data exploration of your climate database. the  analysis was done  using SQLAlchemy ORM queries, Pandas, and Matplotlib.

* (climate_starter.ipynb) and [hawaii.sqlite](Resources/hawaii.sqlite) files were used to  complete  climate analysis and data exploration.

* I Choose a start date of 1-1-2010 and end date of 1-1-2011
* I Use SQLAlchemy `create_engine` to connect to your sqlite database.

* and  SQLAlchemy `automap_base()` to reflect your tables into classes and save a reference to those classes called `Station` and `Measurement`.

### Precipitation Analysis

* I Design a query to retrieve the  12 months of precipitation data useing my start and end date.

* Useing only  `date` and `prcp` values.

* then put the data in a data frame and plot 

 
* Use Pandas to print the summary statistics for the precipitation data.

### Station Analysis

*I Design a query to calculate the total number of stations.

* and  a query to find the most active stations.

  
* I then Design a query to retrieve the last 12 months of temperature observation data (tobs).

  and Filter by the station with the highest number of observations.

  then Plot the results as a histogram with `bins=12`.

  

## REQUIRED: Step 2 - create a Climate App


*  I then used FLASK to create your routes.

### Routes were below 

* `/`

  * Home page.

  * List all routes that are available.

* `/api/precipitation`

  * Convert the query results to a Dictionary using `date` as the key and `prcp` as the value.

  * Return the JSON representation of your dictionary.

* `/api/stations`

  * Return a JSON list of stations from the dataset.

* `/api/temperature`
  * query for the dates and temperature observations from a year from the last data point.
  * Return a JSON list of Temperature Observations (tobs) for the previous year.

* 

*