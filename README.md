# Part 1: Analyze and Explore the Climate Data 📈 #

- Use the SQLAlchemy create_engine() function to connect to your SQLite database

  ![image](https://github.com/CourtneyCole123/sqlalchemy-challenge/assets/162069113/7b374d0a-480d-42cb-99d4-bdc9a8f59fd0)

- Use the SQLAlchemy automap_base() function to reflect your tables into classes

  ![image](https://github.com/CourtneyCole123/sqlalchemy-challenge/assets/162069113/d44bb70f-ea31-4839-94cc-c23e2945912d)

- Save references to the classes named station and measurement

  ![image](https://github.com/CourtneyCole123/sqlalchemy-challenge/assets/162069113/8f5540fd-708d-405b-a4c6-8ce92768deae)

- Link Python to the database by creating a SQLAlchemy session

  ![image](https://github.com/CourtneyCole123/sqlalchemy-challenge/assets/162069113/970be9b4-871e-4882-ad21-8b3b1c16f3e5)

- Close your session at the end of your notebook

  ![image](https://github.com/CourtneyCole123/sqlalchemy-challenge/assets/162069113/9cce117f-78e4-4cd1-8ac3-a1d78df85696)

  ## Precipitation Analysis 🌧️ ##

- Create a query that finds the most recent date in the dataset (8/23/2017)

  ![image](https://github.com/CourtneyCole123/sqlalchemy-challenge/assets/162069113/bf53c331-48f7-41b4-a8fb-be7fb48c3665)

- Create a query that collects only the date and precipitation for the last year of data without passing the date as a variable

  ![image](https://github.com/CourtneyCole123/sqlalchemy-challenge/assets/162069113/f47d95b3-0fc1-4522-b69d-1ce3d377a356)

- Save the query results to a Pandas DataFrame to create date and precipitation columns

  ![image](https://github.com/CourtneyCole123/sqlalchemy-challenge/assets/162069113/ace9ddb7-b275-474d-b2f4-4539736085e6)

- Sort the DataFrame by date

  ![image](https://github.com/CourtneyCole123/sqlalchemy-challenge/assets/162069113/42cbd84c-8737-4e76-83fb-7a8c3a6cdf9c)

- Plot the results by using the DataFrame plot method with date as the x and precipitation as the y variables

  ![image](https://github.com/CourtneyCole123/sqlalchemy-challenge/assets/162069113/01e586d6-29c4-4c10-a444-5f2e86d24741)

- Use Pandas to print the summary statistics for the precipitation data

  ![image](https://github.com/CourtneyCole123/sqlalchemy-challenge/assets/162069113/ad7551c5-c262-46b0-b864-3fac7c049325)

  ## Station Analysis 🌐 ##

- Design a query that correctly finds the number of stations in the dataset (9)

- Design a query that correctly lists the stations and observation counts in descending order and finds the most active station (USC00519281)

- Design a query that correctly finds the min, max, and average temperatures for the most active station (USC00519281)

- Design a query to get the previous 12 months of temperature observation (TOBS) data that filters by the station that has the greatest number of observations

- Save the query results to a Pandas DataFrame

- Correctly plot a histogram with bins=12 for the last year of data using tobs as the column to count.

  <pre> Special Note: I learned to sort tuples in a list using https://www.geeksforgeeks.org/sort-in-python/.</pre>

# Part 2: Design Your Climate App ☀️ #

- Correctly generate the engine to the correct sqlite file

- Use automap_base() and reflect the database schema

- Correctly save references to the tables in the sqlite file (measurement and station)

- Correctly create and binds the session between the python app and database

- Display the available routes on the landing page

<ins> API Static Routes: </ins> 

- A precipitation route that:

  - Returns json with the date as the key and the value as the precipitation

  - Only returns the jsonified precipitation data for the last year in the database

- A stations route that:

  - Returns jsonified data of all of the stations in the database

- A tobs route that:

  - Returns jsonified data for the most active station (USC00519281)

  - Only returns the jsonified data for the last year of data
    
<ins> API Dynamic Route </ins>

- A start route that:

  - Accepts the start date as a parameter from the URL

  - Returns the min, max, and average temperatures calculated from the given start date to the end of the dataset

- A start/end route that:

  - Accepts the start and end dates as parameters from the URL

  - Returns the min, max, and average temperatures calculated from the given start date to the given end date

