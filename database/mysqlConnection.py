import mysql.connector as mys

def connector():
    conn = mys.connect(
        host="localhost",
        user="benjaminwesson",
        database="fall2026_530_workshop",
        ssl_disabled=True
    )

    return conn

    

