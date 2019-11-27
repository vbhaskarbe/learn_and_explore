
## Method to create product_types static table
def SQL_create_product_types( db, cursor):
    cursor.execute("DROP TABLE IF EXISTS product_types")
    cursor.execute("CREATE TABLE product_types ( \
                                    id INT(11) NOT NULL AUTO_INCREMENT, \
                                    prod_type VARCHAR(40) NOT NULL, \
                                    prod_desc VARCHAR(255), \
                                    prod_unit VARCHAR(20), \
                                    max_price float(10,2), \
                                    PRIMARY KEY ( id), \
                                    CONSTRAINT uc_id_prod_type UNIQUE( id, prod_type))" )
    cursor.execute("DESC product_types")
    print(cursor.fetchall())
    ## defining the Query
    query = "INSERT INTO product_types (prod_type, prod_desc, prod_unit, max_price) VALUES (%s, %s, %s, %s)"
    ## storing values in a variable
    values = [
        ("fruits", "Eatables like apple, mango, banana etc", "KG", 199.99 ),
        ("clothes","Wearables like shirt, pant etc", 'NA', 2500.0),
        ("toys", "Playing stuff like cars, blocks etc", 'NA', 500.0),
        ("books","All types of books for reading", 'NA', 1249.99),
        ("shoes","All types of wearables for feet", 'NA', 2000.0)
    ]
    ## executing the query with values
    cursor.executemany(query, values)
    ## to make final output we have to run the 'commit()' method of the database object
    db.commit()
    print(cursor.rowcount, "records inserted")
    ## defining the Query
    query = "SELECT * FROM product_types"
    ## getting records from the table
    cursor.execute(query)
    ## fetching all records from the 'cursor' object
    records = cursor.fetchall()
    ## Showing the data
    for record in records:
        print(record)
    
def SQL_query_product_types(cursor, r_order = None):
    if r_order is None:
        query = "SELECT prod_type from product_types"
    else:
        query = "SELECT * FROM product_types ORDER BY %s" % r_order
    cursor.execute(query)
    prod_types = cursor.fetchall()
    for ptype in prod_types:
        print( ptype)


def SQL_query_product_type( cursor, prod_type):
    query = "SELECT * FROM product_types WHERE prod_type = '%s'" % prod_type
    cursor.execute(query)
    records = cursor.fetchall()
    for record in records:
        print(record)

if __name__ == '__main__':
    import mysql.connector as mysql
    ## MySql connector
    mydb = mysql.connect(
            host="localhost",
            user="root",
            passwd="welcome123",
            database="lbc_db"
    )

    print("INFO: Create all required initial tables")
    ## Get cursor
    cursor = mydb.cursor()
    ## execute command to list DBs
    cursor.execute("SHOW DATABASES")
    databases = cursor.fetchall()
    print( databases)

    print("INFO: Create the Products type table")
    SQL_create_product_types(mydb, cursor)
    print("INFO: Query the table")
    SQL_query_product_types( cursor)
    print("INFO: Query the table with WHERE clause")
    SQL_query_product_type( cursor, 'toys')
    print("INFO: Query the table, with ORDER BY max_price")
    SQL_query_product_types( cursor, 'max_price')


    

