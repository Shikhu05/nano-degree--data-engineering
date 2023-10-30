Project description
Sparkify is a music streaming startup with a growing user base and song database.

Their user activity and songs metadata data resides in json files in S3. The goal of the current project is to build an ETL pipeline that extracts their data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team to continue finding insights in what songs their users are listening to.


Database schema design-

State and justify your database schema design and ETL pipeline.

1. Staging Tables
    staging_events
    staging_songs
2. Fact Table
    songplays - records in event data associated with song plays i.e. records with page NextSong - songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

3. Dimension Tables
   users - users in the app - user_id, first_name, last_name, gender, level
   songs - songs in music database - song_id, title, artist_id, year, duration
   artists - artists in music database - artist_id, name, location, lattitude, longitude
   time - timestamps of records in songplays broken down into specific units - start_time, hour, day, week, month, year, weekday



Steps followed on this project-

Update dwh.cfg-
1. Add Host and AWS details. (removed after executing the scripts)

Create Table Schemas
2. Design schemas for your fact and dimension tables
3. Write a SQL CREATE statement for each of these tables in sql_queries.py
4. Complete the logic in create_tables.py to connect to the database and create these tables
5. Write SQL DROP statements to drop tables in the beginning of - create_tables.py if the tables already exist. This way, you can run create_tables.py whenever you want to reset your database and test your ETL pipeline.

6. Launch a redshift cluster and create an IAM role that has read access to S3.
7. Add redshift database and IAM role info to dwh.cfg.
8. Test by running create_tables.py and checking the table schemas in your redshift database. You can use Query Editor in the AWS Redshift console for this.

Build ETL Pipeline
9. Implement the logic in etl.py to load data from S3 to staging tables on Redshift.
10. Implement the logic in etl.py to load data from staging tables to analytics tables on Redshift.
11. Test by running etl.py after running create_tables.py and running the analytic queries on your Redshift database to compare your results with the expected results.

12. Delete your redshift cluster when finished.