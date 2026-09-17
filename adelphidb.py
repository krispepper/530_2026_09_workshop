# https://flask.palletsprojects.com/en/stable/quickstart/
# https://www.w3schools.com/python/python_mysql_getstarted.asp
from flask import Flask, render_template, request, redirect, url_for
from markupsafe import escape
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    process_url = url_for("process")
    return f"""<html>
    <head>
    <title>Flask Demo</title>
    </head>
    <body>
        <h1>Welcome to Flask Demo</h1>
        <p>This is a simple demonstration of a Flask application.</p>
        <div><form action="{process_url}" method="post">
        <input type="text" widgth="80" name="userinput">  
        <input type="submit" value="Submit">
        </form></div>
    </body>
    </html>"""
    ''' you can instead put this html template into templates/welcome.html and change to 
         return render_template("welcome.html") 
         welcome.html will contain the same text <html> to </html> except
           the action will be { url_for("process") }}
              giving: "<div><form action={{ url_for("process") }} method="post">
        so templates/welcome.html will contain: 
        <html>
            <head>
                <title>Flask Demo</title>
            </head>
            <body>
                <h1>Welcome to Flask4 Demo</h1>
                <p>This is a simple demonstration of a Flask application.</p>
                <div><form action={{ url_for("process") }} method="post">
                <input type="text" widgth="80" name="userinput">  
                <input type="submit" value="Submit">
                </form></div>
            </body>
        </html>
    '''

@app.route('/process', methods=['GET'])
def process():
    user_input = request.form['userinput']
    out="Continent "
    # connect to the MySQL database
    mydb = mysql.connector.connect(
        host="localhost",
        user="benjaminwesson", #replace with your username for compsci
        database="world"  
    )
    mycursor = mydb.cursor()
    query = "SELECT continent FROM country where name = '%s' limit 1" % (escape(user_input))
    print("Query is", query)
    mycursor.execute(query)
    # Equivalent query: 
    # mycursor.execute("SELECT continent FROM country where name = %s limit 1", (user_input,)) 
    # Angola is a good input when you test
    myresult = mycursor.fetchall()
    if myresult:
        return out + escape(myresult[0][0])
    else:
        return "Country Not found - you entered" + escape(user_input)