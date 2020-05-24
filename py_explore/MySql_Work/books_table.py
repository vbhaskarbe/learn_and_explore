from db_lib_methods import display_records, SQL_execute_one_statement

## Method to create books static table
def SQL_create_books_table( db, cursor, tab_name = 'book'):
    cursor.execute("DROP TABLE IF EXISTS orders")
    cursor.execute("DROP TABLE IF EXISTS books")
    cursor.execute("CREATE TABLE {tab_name} ( \
                                    id          MEDIUMINT(11) NOT NULL UNIQUE AUTO_INCREMENT, \
                                    title       VARCHAR(255), \
                                    description VARCHAR(255), \
                                    author      VARCHAR(255) NOT NULL, \
                                    price       float(10,2), \
                                    currency    VARCHAR(20), \
                                    language    VARCHAR(25), \
                                    in_store    TINYINT(1) NOT NULL, \
                                    category    ENUM('Vocabulory', 'Fiction', 'Academic', 'Selfhelp') NOT NULL, \
                                    PRIMARY KEY (id), \
                                    CONSTRAINT uc_id_title UNIQUE( id, title))".format(tab_name = tab_name) )
    cursor.execute("ALTER TABLE books AUTO_INCREMENT = 100")
    print("***** INFO: The schema of the table 'books'")
    cursor.execute("DESC {tab_name}".format( tab_name = tab_name))
    print(cursor.fetchall())
    ## Defining the SQL command
    sql_cmd = "INSERT INTO {tab_name} (title, description, author, price, currency, language, in_store, category) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)".format(tab_name = tab_name)
    ## storing values in a variable
    values  = [
        ("Word Power Made Easy", "Useful for competitive exams.", "Lewis Norman", '124.0', 'rs', 'English', '1', 'Vocabulory' ),
        ("The Alchemist", "Feel good, Enchanting novel.", "Paulo Coelho", '245.0', 'rs', 'English', '1', 'Fiction' ),
        ("Learning Python", "Programming languages. computers.", "Lutz Mark", '1520', 'rs', 'English', '1', 'Academic' ), 
        ("Asamardhuni Jeeva Yathra", "Telugu fiction novel.", "Gopi Chand", "100.0", "rs", "Telugu", '1', "Fiction"), 
        ("Chanakya Neeti", "Hindi self help book.", "Parashar Ashwini", "90", 'rs', 'Hindi', '1', 'Selfhelp'),
        ("Effective Python", "To write better python code.", "Brett Slatkin", '328.0', 'rs', 'English', '1', 'Academic'),
        ("Python Tricks", "Python tips and tricks.", "Dan Bader", "480", 'rs', 'English', '1', 'Academic'),
        ("The Theory of Everything", "Good read about world.", "Stephen Hawking", "90", 'rs', "English", '1', "Fiction")
    ]
    ## executing the query with values
    cursor.executemany( sql_cmd, values)
    ## to make final output we have to run the 'commit()' method of the database object
    db.commit()
    print(cursor.rowcount, "records inserted")
    print("***** INFO: All entries from table 'books'")
    SQL_execute_one_statement( db, cursor, "SELECT * FROM {tab_name}".format(tab_name = tab_name))

def SQL_create_orders_table( db, cursor):
    cursor.execute("DROP TABLE IF EXISTS orders")
    cursor.execute("CREATE TABLE orders (\
                            id          MEDIUMINT(11) NOT NULL AUTO_INCREMENT, \
                            buyer_name  VARCHAR(255) NOT NULL, \
                            quantity    INT(5) NOT NULL, \
                            amount      FLOAT(11,2) NOT NULL, \
                            book_id     MEDIUMINT(11) NOT NULL, \
                            ordered_on  DATETIME NOT NULL, \
                            PRIMARY KEY (id), \
                            FOREIGN KEY (book_id) REFERENCES books(id))")
    print("***** INFO: The schema of the table 'orders'")
    cursor.execute("DESC orders;")
    print(cursor.fetchall())
    sql_cmd = "INSERT INTO orders (buyer_name, quantity, amount, book_id, ordered_on) VALUES(%s, %s, %s, %s, %s)"
    values  = [
                ("Bhaskar", "1", "480.0", "106", '2019-11-24 08:15:10'),
                ("Bhaskar", "20", "4900", "101", '2019-11-25 08:30:29'),
                ("Vishwa","2","180", "104", '2019-11-28 11:15:00'),
                ("Lehit","1", "124.0", "100", '2019-12-01 09:10:06'),
                ("Bhaskar", "2", "180", "107", '2019-12-02 06:30:19'),
                ("Vishwa", "1", "90", "104", '2019-12-02 10:45:54'),
                ("Bhaskar", "1", "480.0", "106", '2019-12-03 10:58:13'),
              ]
    cursor.executemany( sql_cmd, values)
    db.commit()
    print(cursor.rowcount, "records inserted")
    print("***** INFO: All entries from table 'orders'")
    SQL_execute_one_statement( db, cursor, "SELECT * FROM orders")
    print("***** INFO: Drop the table 'orders'")
    SQL_execute_one_statement( db, cursor, "DROP TABLE IF EXISTS orderss;", True, True)

def SQL_learn_commands(db, cursor):
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
    #print("***** INFO: Drop the table 'books'")
    #SQL_execute_one_statement( db, cursor, "DROP TABLE IF EXISTS books;", True, True)

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

    print("***** INFO: Create the 'books' table")
    SQL_create_books_table( mydb, cursor, 'books')
    SQL_learn_commands(mydb, cursor)
    print("***** INFO: --------------- orders -------------------")
    SQL_create_orders_table( mydb, cursor)
    #print( dir( mydb))


