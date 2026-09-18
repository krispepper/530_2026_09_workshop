from flask import Flask
from markupsafe import escape 
import mysql.connector as mys
app = Flask(__name__)


@app.route("/")
def hello_world():
    name = "World"
    return f"<p>Hello, {escape(name)}</p>"


@app.route("/tahreem")
def tahreem_world():
    name = "Tahreem"
    return f"<p>Hello, {escape(name)}</p>"

@app.route("/bye")
def goodbye_world():
    name = "Goodbye"
    return f"<p>Goodbye, {escape(name)}</p>"

@app.route("/mysql",methods=["GET"])
def mysql_test():
    conn = mys.connect(
        host="localhost",
        user="tahreemshah",
        database="fall2026_530_workshop"
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM wesson")
    
    myresult = cursor.fetchall()


    return f"<p>Successfully executed query on table 'wesson' and found {escape(myresult)}</p>"