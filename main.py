import os
import cx_Oracle
from flask import Flask, render_template, request, redirect, url_for, flash

db_user = os.environ.get('DBAAS_USER_NAME', 'system')
db_password = os.environ.get('DBAAS_USER_PASSWORD', 'system')
db_connect = os.environ.get('DBAAS_DEFAULT_CONNECT_DESCRIPTOR', "localhost:1521/XE")
service_port = port=os.environ.get('PORT', '8080')

app= Flask(__name__)

@app.route ('/') 
def index():
    connection = cx_Oracle.connect(db_user, db_password, db_connect)
    cur = connection.cursor()
    cur.execute("SELECT 'Hello, World from Oracle DB!' FROM DUAL")
    col = cur.fetchone()[0]
    cur.close()
    connection.close()
    return render_template('index.html')

@app.route ('/evaluation') 
def evaluation():
    return render_template('evaluation.html')

@app.route ('/registeruser') 
def registeruser():
    window_open = True
    return render_template('registeruser.html')

@app.route ('/auth') 
def auth():
    window_open = True
    return render_template('auth.html')

if __name__== "__main__":
    app.run (debug=True)