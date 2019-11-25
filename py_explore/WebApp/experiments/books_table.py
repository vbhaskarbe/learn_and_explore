

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
    ## defining the Query
    query = "INSERT INTO books (title, description, author, price, currency, language, category) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    ## storing values in a variable
    values = [
        ("Word Power Made Easy", "Useful for competitive exams.", "Lewis Norman", '124.0', 'rs', 'English', 'Vocabulory' ),
        ("The Alchemist", "Feel good, Enchanting novel.", "Paulo Coelho", '245.0', 'rs', 'English', 'Fiction' ),
        ("Learning Python", "Programming languages. computers.", "Lutz Mark", '1520', 'rs', 'English', 'Educational' ) 
    ]
    ## executing the query with values
    cursor.executemany(query, values)
    ## to make final output we have to run the 'commit()' method of the database object
    db.commit()
    print(cursor.rowcount, "records inserted")
    ## defining the Query
    query = "SELECT * FROM books ORDER BY title"
    ## getting records from the table
    cursor.execute(query)
    ## fetching all records from the 'cursor' object
    records = cursor.fetchall()
    ## Showing the data
    for record in records:
        print(record)
    
    


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



