import psycopg

def get_connection():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg.connect(
            dbname="TestDB",
            host="localhost",
            port=5432,
            user="postgres",
            password="admin"
        );
        print("Conectado")
        return conn
    except (Exception, psycopg.DatabaseError) as error:
        print("Error al conectar:", error)
        if (conn is not None):
            conn.close()

def close_connection(conn: psycopg.Connection):
    if (conn is not None):
        print("Close Connection")
        conn.close()
    