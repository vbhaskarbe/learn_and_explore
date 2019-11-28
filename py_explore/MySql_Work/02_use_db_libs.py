import mysql.connector as mysql

from db_lib_methods import create_database
from db_lib_tables import TABLES


if __name__ == '__main__':
    conn = mysql.connect( user = 'root', passwd = 'welcome123')
    cursor = conn.cursor()

    DB_NAME = 'my_test_db'
    create_database( conn, cursor, 'my_test_db')
    #create_database( conn, cursor, 'lbc_db')

    print( conn.database)
    cursor.execute("USE {};".format( DB_NAME))
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    for x in tables:
        print(x) 

    

