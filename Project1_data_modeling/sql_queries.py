# DROP TABLES

songplay_table_drop = "Drop table if exists songplays;"
user_table_drop = "Drop table if exists users;"
song_table_drop = "Drop table if exists songs;"
artist_table_drop = "Drop table if exists artists;"
time_table_drop = "Drop table if exists time;"

# CREATE TABLES

songplay_table_create = (""" create table if not exists songplays  
                                                      ( 
                                                      songplay_id int primary key,
                                                      start_time varchar, 
                                                      user_id int not null, 
                                                      level varchar, 
                                                      song_id varchar not null, 
                                                      artist_id varchar not null, 
                                                      session_id int not null, 
                                                      location varchar, 
                                                      user_agent varchar
                                                    );
                        """)

user_table_create = (""" create table if not exists users  
                                              ( 
                                              user_id int primary key,
                                              first_name varchar not null, 
                                              last_name varchar not null, 
                                              gender varchar, 
                                              level varchar not null
                                            );
                    """)

song_table_create = ("""create table if not exists songs 
                                             ( 
                                             song_id varchar primary key, 
                                             title varchar unique, 
                                             artist_id varchar not null, 
                                             year int, 
                                             duration numeric
                                             );
                     """)

artist_table_create = ("""create table if not exists artists  
                                                 ( 
                                                 artist_id varchar primary key,
                                                 name varchar not null, 
                                                 location varchar, 
                                                 latitude numeric, 
                                                 longitude numeric
                                                 );
                       """)

time_table_create = ("""create table if not exists time  
                                            ( 
                                            start_time varchar not null,
                                            hour int, 
                                            day varchar, 
                                            week int, 
                                            month int, 
                                            year int,
                                            weekday varchar
                                            );
                    """)

# INSERT RECORDS

songplay_table_insert = (""" INSERT INTO songplays 
                                ( 
                                songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent 
                                )
                                VALUES 
                                (
                                %s, %s, %s, %s, %s, %s, %s, %s, %s 
                                )
                        """)

user_table_insert = (""" INSERT INTO users 
                            (
                            user_id, first_name, last_name, gender, level
                            ) 
                            VALUES 
                            (
                            %s, %s, %s, %s, %s
                            )
                        ON CONFLICT ( user_id ) 
                        DO UPDATE
                        SET level  = EXCLUDED.level;
                     """)

song_table_insert = (""" INSERT INTO songs 
                            (
                            song_id, title, artist_id, year, duration
                            ) 
                            VALUES 
                            (
                            %s, %s, %s, %s, %s
                            )
                        ON CONFLICT (song_id) 
                        DO NOTHING;
                     """)

artist_table_insert = (""" INSERT INTO artists 
                             (
                             artist_id, name, location, latitude, longitude 
                             )  
                             VALUES 
                             (
                             %s, %s, %s, %s, %s
                             )
                            ON CONFLICT (artist_id) 
                            DO UPDATE
                            SET location  = EXCLUDED.location,
                            latitude  = EXCLUDED.latitude,
                            longitude  = EXCLUDED.longitude;
                       """)


time_table_insert = (""" INSERT INTO time 
                            (
                            start_time, hour, day, week, month, year, weekday
                            ) 
                            VALUES 
                            (
                            %s, %s, %s, %s, %s, %s, %s
                            )
                     """)

# FIND SONGS

song_select = ("""SELECT artists.artist_id, songs.song_id 
                  FROM artists 
                  JOIN songs 
                  ON artists.artist_id = songs.artist_id 
                  WHERE songs.title =%s 
                        and artists.name = %s 
                        and songs.duration = %s
              """)


# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]