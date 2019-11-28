from db_lib_methods import display_records, SQL_execute_one_statement

## Method to create books static table
def SQL_create_books_table( db, cursor):
    cursor.execute("DROP TABLE IF EXISTS books")
    cursor.execute("CREATE TABLE books ( \
                                    id          INT(11) NOT NULL AUTO_INCREMENT, \
                                    title       VARCHAR(255), \
                                    description VARCHAR(255), \
                                    author      VARCHAR(255) NOT NULL, \
                                    price       float(10,2), \
                                    currency    VARCHAR(20), \
                                    language    VARCHAR(25), \
                                    category    VARCHAR(40) NOT NULL, \
                                    PRIMARY KEY (id), \
                                    CONSTRAINT uc_id_title UNIQUE( id, title))" )
    cursor.execute("DESC books")
    print(cursor.fetchall())
    ## Defining the SQL command
    sql_cmd = "INSERT INTO books (title, description, author, price, currency, language, category) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    ## storing values in a variable
    values  = [
        ("Word Power Made Easy", "Useful for competitive exams.", "Lewis Norman", '124.0', 'rs', 'English', 'Vocabulory' ),
        ("The Alchemist", "Feel good, Enchanting novel.", "Paulo Coelho", '245.0', 'rs', 'English', 'Fiction' ),
        ("Learning Python", "Programming languages. computers.", "Lutz Mark", '1520', 'rs', 'English', 'Educational' ), 
        ("Asamardhuni Jeeva Yathra", "Telugu fiction novel.", "Gopi Chand", "100.0", "rs", "Telugu", "Fiction"), 
        ("Chanakya Neeti", "Hindi self help book.", "Parashar Ashwini", "90", 'rs', 'Hindi', 'Selfhelp')
    ]
    ## executing the query with values
    cursor.executemany( sql_cmd, values)
    ## to make final output we have to run the 'commit()' method of the database object
    db.commit()
    print(cursor.rowcount, "records inserted")
    print("INFO: All entries from table 'books'")
    SQL_execute_one_statement( db, cursor, "SELECT * FROM books")
    print("INFO: ORDER BY title")
    SQL_execute_one_statement( db, cursor, "SELECT * FROM books ORDER BY title")
    print("INFO: ORDER BY title DESC")
    SQL_execute_one_statement( db, cursor, "SELECT * FROM books ORDER BY title DESC")
    print("INFO: Deleting entry with 'id' as 4")
    SQL_execute_one_statement( db, cursor, "DELETE FROM books WHERE id = 4", True, False)
    SQL_execute_one_statement( db, cursor, "SELECT * FROM books")
    print("INFO: Update price for entry with 'id' as 3")
    SQL_execute_one_statement( db, cursor, "UPDATE books SET price = '1280' WHERE id = 3", True, False)
    SQL_execute_one_statement( db, cursor, "SELECT * FROM books")

if __name__ == '__main__':
    import mysql.connector as mysql
    ## MySql connector - change to create db if not exists.
    mydb = mysql.connect(
            host="localhost",
            user="root",
            passwd="welcome123",
            database="lbc_db"
    )

    ## Get cursor
    cursor = mydb.cursor()

    print("INFO: Create the Products type table")
    SQL_create_books_table(mydb, cursor)
    
    #print( dir( mydb))


