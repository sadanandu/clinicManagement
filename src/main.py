# Main file for App 

import psycopg2
import os
from flask import Flask, request, render_template

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='3.86.9.220',
                            port=5432,
                            database='clinic_mgmt',
                            user='clinic',
                            password='password')
    return conn



@app.route('/users', methods=["GET"])
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users;')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', users=users)

