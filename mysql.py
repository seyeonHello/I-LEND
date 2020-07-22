from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'db_tasks'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)
CORS(app)


@app.route('/api/tasks', methods=['GET'])
def get_all_tasks():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM db_tasks.tasks")
    rv = cur.fetchall()
    #print(rv)
    return jsonify(rv)

@app.route('/api/seeks', methods=['GET'])
def get_all_seeks():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM db_tasks.seek")
    rv = cur.fetchall()
    #print(rv)
    return jsonify(rv)

@app.route('/api/signup', methods=['GET'])
def get_all_users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM db_tasks.users")
    rv = cur.fetchall()
    #print(rv)
    return jsonify(rv)

@app.route('/api/task', methods=['POST'])
def add_task():
    cur = mysql.connection.cursor()
    title = request.get_json()['title']
    endDate = request.get_json()['endDate']
    startDate = request.get_json()['startDate']
    price = request.get_json()['price']
    des = request.get_json()['description']
    image = request.get_json()['image']
    memberID=request.get_json()['memberID']
    cur.execute(
      "INSERT INTO db_tasks.tasks (title, price, startDate, endDate, des,image,memberID) VALUES('" + str(title) + "', '" + str(price) + "', '" + str(startDate) + "', '" + str(endDate) + "', '" + str(des) + "', '" + str(image) + "', '" + str(memberID) + "');")
    data = cur.fetchall()
    mysql.connection.commit()

    result = {'title': title}

    return jsonify({'result': result})

@app.route('/api/seeks', methods=['POST'])
def add_seek():
    print('why')
    cur = mysql.connection.cursor()
    print('why')
    seekName = request.get_json()['seekName']
    seekDes = request.get_json()['seekDes']
    seekStartDate = request.get_json()['seekStartDate']
    seekEndDate = request.get_json()['seekEndDate']
    today=request.get_json()['today']
    print(seekDes)
    cur.execute(
      "INSERT INTO db_tasks.seek (seekName, seekDes, seekStartDate, seekEndDate, today) VALUES('" + str(seekName) + "', '" + str(seekDes) + "', '" + str(seekStartDate) + "', '" + str(seekEndDate) + "', '" + str(today) + "');")
    data = cur.fetchall()
    mysql.connection.commit()

    result = {'seekName': seekName}

    return jsonify({'result': result})

@app.route('/api/signup', methods=['POST'])
def add_users():
    cur = mysql.connection.cursor()
    id = request.get_json()['signUpID']
    pwd = request.get_json()['signUpPWD']
    phoneNum = request.get_json()['phoneNum']
    email = request.get_json()['email']
    print(id)
    print(pwd)
    cur.execute(
      "INSERT INTO db_tasks.users (id, pwd, phoneNum, email) VALUES('" + str(id) + "', '" + str(pwd) + "', '" + str(phoneNum) + "', '" + str(email) + "');")
    data = cur.fetchall()
    mysql.connection.commit()

    result = {'id': id}

    return jsonify({'result': result})

@app.route('/api/task/<id>', methods=['PUT'])
def update_task(id):
    cur = mysql.connection.cursor()
    title = request.get_json()['title']

    cur.execute("UPDATE db_tasks.tasks SET title = '" + str(title) +
                "' where id = " + id)
    mysql.connection.commit()

    result = {'title': title}

    return jsonify({'result': result})


@app.route('/api/task/<id>', methods=['DELETE'])
def delete_task(id):
    cur = mysql.connection.cursor()
    response = cur.execute("DELETE FROM db_tasks.tasks where id = " + id)
    mysql.connection.commit()

    if response > 0:
        result = {'message': 'record deleted'}
    else:
        result = {'message': 'no record found'}

    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=True)
