# Main file for App 

import psycopg2
import os
from flask import Flask, request, render_template, jsonify

app = Flask(__name__, static_url_path='/static')
conn = None
def get_db_connection():
    global conn
    if not conn:
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
    cur.execute('SELECT username FROM users;')
    users = cur.fetchall()
    cur.close()
    return render_template('index.html', users=users)

@app.route('/user/<username>', methods=['GET', 'PUT'])
def get_user_details(username):
    conn = get_db_connection()
    cur = conn.cursor()
    if request.method == 'GET':
        cur.execute(f"SELECT name, email, mobile FROM users WHERE username = '{username}';")
        user_details = cur.fetchall()
        cur.close()
        return jsonify(user_details)
    if request.method == 'PUT':
        data = request.json
        cur.execute(f'''UPDATE users set name='{data["name"]}', mobile='{data["mobile"]}', email='{data["email"]}' where username='{username}';''')
        cur.close()
        return jsonify({"message": "User details updated successfully"})
