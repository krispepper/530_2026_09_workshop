import mysql.connector as mys

def connector():
    conn = mys.connect(
        host="localhost",
        user="benjaminwesson",
        database="benjaminwesson",
        ssl_disabled=True
    )

    return conn

    

