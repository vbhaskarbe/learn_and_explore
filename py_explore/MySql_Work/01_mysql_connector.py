import mysql.connector as mysql
## MySql connector
mydb = mysql.connect(
  host="localhost",
  user="root",
  passwd="welcome123",
#  database="lbc_db"
)


if __name__ == '__main__':
    ## Get cursor
    cursor = mydb.cursor()
    ## Check if our db exists
    for db in cursor:
        if ( list(set(db))[0]) == 'lbc_db':
            print( "Database %s exists." % (list(set(db))[0])) 

    cursor.execute("CREATE DATABASE IF NOT EXISTS lbc_db CHARACTER SET utf8;;")
    ## execute command to list DBs
    cursor.execute("SHOW DATABASES")
    databases = cursor.fetchall()
    print( databases)

