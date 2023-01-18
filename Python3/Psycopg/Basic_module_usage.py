import psycopg

hostaddr = ""
port = 5432
dbname = ""
user = ""
password = ""
connect_timeout = 10

# Wrapper for a connection to the database.
# connect()
# autocommit=True
with psycopg.connect("hostaddr={} port={} dbname={} user={} password={} connect_timeout={}".format(
    hostaddr, port, dbname, user, password, connect_timeout),autocommit=True) as conn:

    # Return a new cursor to send commands and queries to the connection.
    # The connection this cursor is using.
    with conn.cursor() as cur:
        # Execute a query or command to the database.
        cur.execute("CREATE TABLE test()")

        # Number of records affected by the precedent operation.
        print(cur.rowcount)

        # Read record
        for i in cur:
            print(i)

        # Return the next record from the current recordset.
        # Return None the recordset is finished.
        # cur.fetchone()

        # Return all the remaining records from the current recordset.
        # cur.fetchall()

        # Close the current cursor and free associated resources.
        # cur.close()

        # You can use:
        # with conn.cursor() as cur:
        #   ...
        # to close the cursor automatically when the block is exited.
        

    # Roll back to the start of any pending transaction.
    # conn.rollback()

    # Commit any pending transaction to the database.
    # conn.commit()

    # Close the database connection.
    # conn.close()

    # You can use:
    # with psycopg.connect() as conn:
    #   ...
    # to close the connect automatically when the block is exited.
