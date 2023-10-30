Discuss the purpose of this database in the context of the startup, Sparkify, and their analytical goals.
State and justify your database schema design and ETL pipeline.
[Optional] Provide example queries and results for song play analysis.

Project Data Sets(given): JSON files
    Song Dataset : to get song and artist information
    Log Dataset : to get the user, time information and create the fact tables

Purpose of the database:
     To analyze the data for Sparkify for understanding the user behavior such as what songs users are listening to, easily query the database for any ad-hoc analysis. For this, Data need to be maintained in an optimized way.

Approach:
    We will be using Postgres database and designing the table structures in such a way that task of data analysis and ad-hoc queries become easier.
    For maintaining the database, we are creating the ETL pipeline to load the data in optimized manner.



Database schema design:

    We are creating the relational database and creating the Start schema and we will be having one fact table i.e. Sonplay and other tables are dimension tables.
    
    SongPlay table: 
        Data source: Log files
        Data format: JSON
        
        "SongPlay" table will be having user_activity data and below are the field details for this table:
            songplay_id is a primary key column and is the index (surrogate) column, 
            user_id (reference from Users table), song_id (reference from Songs table), artist_id (reference from Artist table) and are the not null columns
            start_time, 
            level, 
            session_id is a "not null" column, 
            location, 
            user_agent
    
    User Table:
        Data source: Log files
        Data format: JSON
        
        "Users" table will be having user information and below are the field details for this table:
            user_id is the primary key,
            first_name and last_name fields have "not null" Constraints, 
            gender
            level is also not null field and tells the status of users if that is paid or free.
     
    Artist Table:
        Data source: Song files
        Data format: JSON
        
        "Artists" table will be having artist information and below are the field details for this table:
            artist_id is the primary key,
            name fields has "not null" Constraints, 
            location, latitude anf longitude are the other information available from the logs.
    
    Song Table:
        Data source: Song files
        Data format: JSON
        
        "Songs" table will be having song information and below are the field details for this table:
            song_id is the primary key,
            title fields has "unique" Constraints, 
            artist_id is the not null field
            other fields- year & duration
    
    Time Table:
        Data source: Log files
        Data format: JSON
        
        "Time" table will be having the information related to the duration and time for the song specifically only for "Next Song" page and below are the field details for this table:
           start_time, hour, day, week, month, year, weekday
 

ETL Pipeline-
    process:
    1. connect database and load the path information where data source resides. for us it is Json.
    2. Load the dimension tables; those are- Songs, Artists, Users and Time.
    3. Load the fact table i.e. SongPlay, and it will be having the Song_id and Artist Id information from the dimension table. Other information will be loaded from the Logs.


Run Script (process):

1. Run create_tables.py file on the terminal using "python create_tables.py". this file has the Table creation and insertion operation written that will be used by ETL pipleline.
2. Run etl.py on terminal using "python etl.py". This file will load the data in the table.
3. Use Test.ipynb file to verify data from the table. 
    Ex-
    
    Query
    %sql SELECT * FROM songplays LIMIT 5;
    
    Data
    
    songplay_id	start_time	user_id	level	song_id	artist_id	session_id	location	user_agent
    483	1542837407796	15	paid	AR5KOSW1187FB35FF4	SOZCTXZ12AB0182364	818	Chicago-Naperville-Elgin, IL-IN-WI	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/36.0.1985.125 Chrome/36.0.1985.125 Safari/537.36"


Sources- Udacity material, Knowledge and Google for the postgres. Mentor has helped in defining 