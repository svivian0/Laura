from flask import Flask, jsonify, request
import mysql.connector as mconn
from mysql.connector import Error

app=Flask(__name__)
##Configuring database connection
dbConfig={
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'Laura'
}

##CONNECT
def connect():
    try:
        conn=mconn.connect(dbConfig)
        return conn
    except Error as e:
        print(f"Error {e}")
        return None

class Laura: ##Only created to use self
    def __init__(self):
        self.conn=connect()

    ##GET ROUTE
    @app.route('/login', methods=['GET'])
    def getUser(self):
        users=[]
        if self.conn is None:
            return jsonify({"Error in connection with database"}), 500 ##MENSAGE IF CONNECTION FAILS
        cursor=self.conn.cursor(dictionary=True) ##DICTIONARY ORGANIZES THE ITENS
        cursor.execute('select id, nameu, email, passwordu from users')
        users=cursor.fetchall()
        cursor.close
        return jsonify(users) ##JSON WITH ALL USERS


    ##POST ROUTE
    @app.route('/login', methods=['POST'])
    def addUser(self):
        cursor=self.conn.cursor()
        newUser=request.json
        if not newUser or 'nameu' not in newUser or 'email' not in newUser or 'passwordu' not in newUser: ## VERIFY ALL ITENS IN NEW USER
            return jsonify({'error'}), 400 ##ERROR IF ONE ITEN IS NONE
        if self.conn is None:
            return jsonify({'error'}), 400 ##ERROR IF CONNECTION FAILS
        query='insert into users (nameu, email, passwordu) values (%s, %s, %s)' ## A DB COMMAND
        date=(newUser['nameu'], newUser['email'], newUser['passwordu'])
        try: ##TRY INSERT NEW USER
            cursor.execute(query, date)
            self.conn.commit
            newId=cursor.lastrowid
            createUser={
                'id': newId,
                'nameu':newUser['nameu'],
                'email': newUser['email'],
                'passwordu': newUser['passwordu']
            }
            return jsonify(createUser), 201 ##RETURN A JSON WITH ONLY NEW USER, NOT ALL
        except Error as e:
            return jsonify({"Error", e}), 500 

if __name__=='__main__':
    app.run(debug=True) 
