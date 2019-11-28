from __future__ import print_function

import mysql.connector as mysql
from mysql.connector import errorcode

## Create a given DB.
def create_database(conn, cursor, db_name):
    print("Creating database and using it....")
    try:
        cursor.execute(
            "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(db_name))
    except mysql.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)
    else:
        cursor.execute("USE {}".format(db_name))
        print("Database {} created successfully.".format(db_name))
        conn.database = db_name

## Display records with fetch all
def display_records( cursor):
    try: 
        records = cursor.fetchall()
    except mysql.Error as err_msg:
        print("WARNING: {}".format(err_msg))
    else:
        for record in records:
            print( record)

## Execute given sql command, optionally commit, optionally display records.
def SQL_execute_one_statement( db, cursor, sql_cmd, commit = False, show_data = True):
    cursor.execute( sql_cmd)
    if commit:
        db.commit()
    if show_data:
        display_records( cursor) 


