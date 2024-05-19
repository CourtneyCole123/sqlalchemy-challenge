# Part 1: Analyze and Explore the Climate Data 📈 #

• Use the SQLAlchemy create_engine() function to connect to your SQLite database

• Use the SQLAlchemy automap_base() function to reflect your tables into classes

• Save references to the classes named station and measurement

• Link Python to the database by creating a SQLAlchemy session

• Close your session at the end of your notebook

  ## Precipitation Analysis 🌧️ ##

• Create a query that finds the most recent date in the dataset (8/23/2017)

• Create a query that collects only the date and precipitation for the last year of data without passing the date as a variable

• Save the query results to a Pandas DataFrame to create date and precipitation columns

• Sort the DataFrame by date

• Plot the results by using the DataFrame plot method with date as the x and precipitation as the y variables

• Use Pandas to print the summary statistics for the precipitation data

  ## Station Analysis 🌐 ##

• Design a query that correctly finds the number of stations in the dataset (9)

• Design a query that correctly lists the stations and observation counts in descending order and finds the most active station (USC00519281)

• Design a query that correctly finds the min, max, and average temperatures for the most active station (USC00519281)

• Design a query to get the previous 12 months of temperature observation (TOBS) data that filters by the station that has the greatest number of observations

• Save the query results to a Pandas DataFrame

• Correctly plot a histogram with bins=12 for the last year of data using tobs as the column to count.

  <pre> Special Note: I learned to sort tuples in a list using https://www.geeksforgeeks.org/sort-in-python/.</pre>

# Part 2: Design Your Climate App ☀️ #

• Correctly generate the engine to the correct sqlite file

• Use automap_base() and reflect the database schema

• Correctly save references to the tables in the sqlite file (measurement and station)

• Correctly create and binds the session between the python app and database

• Display the available routes on the landing page

<ins> API Static Routes: </ins> 

• A precipitation route that:

    - Returns json with the date as the key and the value as the precipitation

    - Only returns the jsonified precipitation data for the last year in the database

• A stations route that:

    - Returns jsonified data of all of the stations in the database

• A tobs route that:

    - Returns jsonified data for the most active station (USC00519281)

    - Only returns the jsonified data for the last year of data
    
<ins> API Dynamic Route </ins>

• A start route that:

    - Accepts the start date as a parameter from the URL

    - Returns the min, max, and average temperatures calculated from the given start date to the end of the dataset

• A start/end route that:

    - Accepts the start and end dates as parameters from the URL

    - Returns the min, max, and average temperatures calculated from the given start date to the given end date

