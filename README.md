
Twitter ETL Pipeline

This is an ETL pipeline built using the Twitter API. This would extract a user's tweets, do some basic transformations and load the data into our SQLite DB.

1. Extract - Extracting one of my favourite user: Shibetoshi Nakamoto's last 100 tweets on Twitter
2. Transform - Basic transformations such as selecting a particular set of data we want and converting the data into a Pandas dataframe
3. Load - Loading our dataframe to a SQLite database using SQLAlchemy ORM


I used SQLite here as it is an experiment project and the data is not huge. Same with the tooling! I reason I preferred Pandas instead of Spark is that the data is small.
I created a developer account in Twitter and requested the elevated access to our account that would allow us to extract data from Twitter. The access will take upto a day to get granted.
