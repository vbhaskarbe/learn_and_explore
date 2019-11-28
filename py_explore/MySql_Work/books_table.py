from db_lib_methods import display_records, SQL_execute_one_statement

## Method to create books static table
def SQL_create_books_table( db, cursor):
    cursor.execute("DROP TABLE IF EXISTS books")
    cursor.execute("CREATE TABLE books ( \
                                    id          MEDIUMINT(11) NOT NULL AUTO_INCREMENT, \
                                    title       VARCHAR(255), \
                                    description VARCHAR(255), \
                                    author      VARCHAR(255) NOT NULL, \
                                    price       float(10,2), \
                                    currency    VARCHAR(20), \
                                    language    VARCHAR(25), \
                                    category    ENUM('Vocabulory', 'Fiction', 'Academic', 'Selfhelp') NOT NULL, \
                                    PRIMARY KEY (id), \
                                    CONSTRAINT uc_id_title UNIQUE( id, title))" )
    cursor.execute("ALTER TABLE books AUTO_INCREMENT = 10")
    cursor.execute("DESC books")
    print(cursor.fetchall())
    ## Defining the SQL command
    sql_cmd = "INSERT INTO books (title, description, author, price, currency, language, category) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    ## storing values in a variable
    values  = [
        ("Word Power Made Easy", "Useful for competitive exams.", "Lewis Norman", '124.0', 'rs', 'English', 'Vocabulory' ),
        ("The Alchemist", "Feel good, Enchanting novel.", "Paulo Coelho", '245.0', 'rs', 'English', 'Fiction' ),
        ("Learning Python", "Programming languages. computers.", "Lutz Mark", '1520', 'rs', 'English', 'Academic' ), 
        ("Asamardhuni Jeeva Yathra", "Telugu fiction novel.", "Gopi Chand", "100.0", "rs", "Telugu", "Fiction"), 
        ("Chanakya Neeti", "Hindi self help book.", "Parashar Ashwini", "90", 'rs', 'Hindi', 'Selfhelp'),
        ("Effective Python", "To write better python code.", "Brett Slatkin", '328.0', 'rs', 'English', 'Academic'),
        ("Python Tricks", "Python tips and tricks.", "Dan Bader", "480", 'rs', 'English', 'Academic')
    ]
    ## executing the query with values
    cursor.executemany( sql_cmd, values)
    ## to make final output we have to run the 'commit()' method of the database object
    db.commit()
    print(cursor.rowcount, "records inserted")
    print("***** INFO: All entries from table 'books'")
    SQL_execute_one_statement( db, cursor, "SELECT * FROM books")
    print("***** INFO: Display only 3 entries from table 'books'")
    SQL_execute_one_statement( db, cursor, "SELECT * FROM books LIMIT 3")
    print("***** INFO: Display only 3 entries from table 'books' starting from 2nd")
    SQL_execute_one_statement( db, cursor, "SELECT * FROM books LIMIT 3 OFFSET 2")
    print("***** INFO: Show the max priced book details")
    SQL_execute_one_statement( db, cursor, "SELECT title, author, price FROM books WHERE price=(select MAX(price) FROM books);")
    print("***** INFO: ORDER BY title")
    SQL_execute_one_statement( db, cursor, "SELECT id, title, books.author, price, language FROM books ORDER BY title")
    print("***** INFO: ORDER BY title DESC")
    SQL_execute_one_statement( db, cursor, "SELECT id, title, books.author, price, category FROM books ORDER BY title DESC")
    print("***** INFO: WHERE 'title' LIKE 'python'")
    SQL_execute_one_statement( db, cursor, "SELECT id, title, books.author, price FROM books WHERE title LIKE '%Python%'")
    print("***** INFO: Deleting entry with 'id' as 4")
    SQL_execute_one_statement( db, cursor, "DELETE FROM books WHERE id = 4", True, False)
    SQL_execute_one_statement( db, cursor, "SELECT id, books.author, price FROM books")
    print("***** INFO: Update price for entry with 'id' = 3")
    SQL_execute_one_statement( db, cursor, "UPDATE books SET price = '1280' WHERE id = 3", True, False)
    SQL_execute_one_statement( db, cursor, "SELECT * FROM books")
    print("***** INFO: Drop the table 'books'")
    SQL_execute_one_statement( db, cursor, "DROP TABLE IF EXISTS books;", True, True)

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

    print("***** INFO: Create the Products type table")
    SQL_create_books_table(mydb, cursor)
    
    #print( dir( mydb))


