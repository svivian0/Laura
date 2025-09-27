from flask import Flask, jsonify, request
app=Flask(__name__)
##WITHOUT DB
users=[
    {
        "id":1,
        "name": "test",
        "email": "test@gmail.com",
    }
]
nextId=2

##GET
@app.route('/login', methods=['GET'])
def getUser():
    return jsonify(users)

##POST
@app.route('/login', methods=['POST'])
def addUser():
    global nextId
    newUser=request.json
    if not newUser or 'name' not in newUser or 'email' not in newUser:
        return jsonify({'error'}), 400
    
    newUserLogin=[
        {
            'id':nextId,
            'name': "testnewname",
            'email': "testnewemail@gmail.com",
        }
    ]
    users.append(newUserLogin)
    nextId+=1
    return jsonify(users), 201

if __name__=='__main__':
    app.run(debug=True)
