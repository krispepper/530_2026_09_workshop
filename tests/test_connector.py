#written by Ben Wesson

#import our testing libray
import pytest

#import the connector function from the file mysqlConnection.py in folder database
from database.mysqlConnection import connector

#I am using mys as an alias for mysql.connector 

#tests if a database connection can be established successfully
def test_connector():

    #attempt to establish a connection to the database
    conn = connector()

    #check if the connection is established successfully
    try:
        #assert that the connection is active with the is_connected() method
        assert conn.is_connected()
    finally:
        #close the database connection
        conn.close()