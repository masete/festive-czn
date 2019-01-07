"""my database file, creating tables and a database connection"""
import psycopg2
import os
from psycopg2.extras import RealDictCursor
from werkzeug.security import generate_password_hash


class DatabaseConnection:
    """
    Initializing my database
    """
    def __init__(self):
        self.commands = (
            """
            CREATE TABLE IF NOT EXISTS users(
                    user_id SERIAL PRIMARY KEY,
                    first_name VARCHAR(100) NOT NULL,
                    last_name VARCHAR(100) NOT NULL,
                    other_names VARCHAR(100) NOT NULL,
                    email VARCHAR(100) NOT NULL,
                    phone_number INTEGER NOT NULL,
                    user_name VARCHAR(100) NOT NULL,
                    registered_on TIMESTAMP DEFAULT NOW(),
                    password VARCHAR(200) NOT NULL,
                    is_admin BOOLEAN DEFAULT FALSE NOT NULL
                    )
            """,
            """
            CREATE TABLE IF NOT EXISTS redflags (                    
                    flag_id SERIAL PRIMARY KEY,
                    created_by VARCHAR(100) NOT NULL,
                    flag_title VARCHAR(100) NOT NULL,
                    flag_location VARCHAR(100) NOT NULL,
                    flag_comment VARCHAR(20) NOT NULL,
                    created_on TIMESTAMP DEFAULT NOW(),
                    flag_status VARCHAR(50) NOT NULL,
                    flag_image VARCHAR(50) NOT NULL,
                    flag_video VARCHAR(50) NOT NULL
                    )
            """
        )
        try:
            self.attributes = dict(dbname='ireporter',
                                   user='postgres',
                                   password='masete',
                                   host='localhost',
                                   port='5432')
            self.connection = psycopg2.connect(**self.attributes, cursor_factory=RealDictCursor)
            if os.getenv("FLASK_ENV") == "production":
                self.connection = psycopg2.connect(os.getenv("DATABASE_URL"), cursor_factory=RealDictCursor)

            elif os.getenv("FLASK_ENV") == "TESTING":
                print('Connecting to test db')
                self.connection = psycopg2.connect(dbname='test_db',
                                                   user='postgres',
                                                   password='masete',
                                                   host='localhost',
                                                   port='5432', cursor_factory=RealDictCursor)
            else:
                print('Connecting development db')
                self.connection = psycopg2.connect(dbname='ireporter',
                                                   user='postgres',
                                                   password='masete',
                                                   host='localhost',
                                                   port='5432', cursor_factory=RealDictCursor)
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()

            for command in self.commands:
                self.cursor.execute(command)
        except Exception as error:
            print(f"error: {error}")


    """
    method to drop tables being used in my tests
    """
    def drop_tables(self):
        query = "DROP TABLE IF EXISTS {} CASCADE"
        tabl_names = ["redflags, users"]
        for name in tabl_names:
            self.cursor.execute(query.format(name))

    def create_tables(self):
        for command in self.commands:
            self.cursor.execute(command)
