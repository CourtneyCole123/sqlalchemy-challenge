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

  ![image](https://github.com/CourtneyCole123/sqlalchemy-challenge/assets/162069113/328cfcf5-75b5-4b80-bad5-0cbccb732f2d)

- Design a query that correctly lists the stations and observation counts in descending order and finds the most active station (USC00519281)

  ![image](https://github.com/CourtneyCole123/sqlalchemy-challenge/assets/162069113/ac59c33e-9b62-42df-ad06-e1503d7e4376)

- Design a query that correctly finds the min, max, and average temperatures for the most active station (USC00519281)

  ![image](https://github.com/CourtneyCole123/sqlalchemy-challenge/assets/162069113/35a2a287-fd64-4a63-b509-9d6dffa3f8f6)

- Design a query to get the previous 12 months of temperature observation (TOBS) data that filters by the station that has the greatest number of observations

  ![image](https://github.com/CourtneyCole123/sqlalchemy-challenge/assets/162069113/436e467a-eda9-4d24-abd0-1f529363c7eb)

- Save the query results to a Pandas DataFrame

  ![image](https://github.com/CourtneyCole123/sqlalchemy-challenge/assets/162069113/eca6fe2c-6f1e-4511-9691-e62a37cc6387)

- Correctly plot a histogram with bins=12 for the last year of data using tobs as the column to count.

  ![image](https://github.com/CourtneyCole123/sqlalchemy-challenge/assets/162069113/62acbcd2-4b2a-4f76-b4db-4a2e2e200620)

  <pre> Special Note: I learned to sort tuples in a list using https://www.geeksforgeeks.org/sort-in-python/.</pre>

# Part 2: Design Your Climate App ☀️ #

- Correctly generate the engine to the correct sqlite file

  ![image](https://github.com/CourtneyCole123/sqlalchemy-challenge/assets/162069113/78e709c8-a595-4a42-a601-38e1fd3ba9ea)

- Use automap_base() and reflect the database schema

  ![image](https://github.com/CourtneyCole123/sqlalchemy-challenge/assets/162069113/a50f4444-3662-4fcd-80de-2d34f7f47eb5)

- Correctly save references to the tables in the sqlite file (measurement and station)

  ![image](https://github.com/CourtneyCole123/sqlalchemy-challenge/assets/162069113/33767b3c-d98b-478a-b87a-100d899424bf)

- Correctly create and binds the session between the python app and database

  ![image](https://github.com/CourtneyCole123/sqlalchemy-challenge/assets/162069113/774d4848-0b7f-43b3-8735-5c01c5b396e0)

- Display the available routes on the landing page

  ![image](https://github.com/CourtneyCole123/sqlalchemy-challenge/assets/162069113/f865da5b-828f-4502-8abd-67a64474e49b)

<ins> API Static Routes: </ins> 

- A precipitation route that:

  - Returns json with the date as the key and the value as the precipitation

  - Only returns the jsonified precipitation data for the last year in the database
 
    ![image](https://github.com/CourtneyCole123/sqlalchemy-challenge/assets/162069113/ae432384-06f7-4534-87f4-7fb5d72225e6)

- A stations route that:

  - Returns jsonified data of all of the stations in the database
 
    ![image](https://github.com/CourtneyCole123/sqlalchemy-challenge/assets/162069113/94d37f21-6dfc-4977-b844-414c5af88d89)

- A tobs route that:

  - Returns jsonified data for the most active station (USC00519281)

  - Only returns the jsonified data for the last year of data
 
    ![image](https://github.com/CourtneyCole123/sqlalchemy-challenge/assets/162069113/e6f7e204-3c12-4bf1-a363-1e0161b40089)
    
<ins> API Dynamic Route </ins>

- A start route that:

  - Accepts the start date as a parameter from the URL

  - Returns the min, max, and average temperatures calculated from the given start date to the end of the dataset
 
    ![image](https://github.com/CourtneyCole123/sqlalchemy-challenge/assets/162069113/69702b7b-84a7-4d31-a908-7e9af0238795)

- A start/end route that:

  - Accepts the start and end dates as parameters from the URL

  - Returns the min, max, and average temperatures calculated from the given start date to the given end date
 
    ![image](https://github.com/CourtneyCole123/sqlalchemy-challenge/assets/162069113/bee8f37f-752d-45e4-a0b9-aced225b7cb7)


