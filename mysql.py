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
    args = request.args.get('major')
    strBefore=str(args)
    strArg="'"+str(args)+"'"
    if(strBefore=="전체"):
      cur.execute("SELECT * FROM db_tasks.tasks")
    else:
      cur.execute("SELECT * FROM db_tasks.tasks WHERE major="+strArg)
    rv = cur.fetchall()
    #print(rv)
    return jsonify(rv)

@app.route('/api/seeks', methods=['GET'])
def get_all_seeks():
    cur = mysql.connection.cursor()
    args = request.args.get('major')
    strBefore = str(args)
    strArg = "'" + str(args) + "'"
    if (strBefore == "전체"):
      cur.execute("SELECT * FROM db_tasks.seek")
    else:
      cur.execute("SELECT * FROM db_tasks.seek WHERE major=" + strArg)
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

@app.route('/api/rent', methods=['GET'])
def get_all_rent():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM db_tasks.rent")
    rv = cur.fetchall()
    #print(rv)
    return jsonify(rv)

@app.route('/api/users', methods=['GET'])
def get_msg():
    cur = mysql.connection.cursor()
    args = request.args.get('hostName')
    print(args)
    hostname=str(args)
    cur.execute("SELECT * FROM db_tasks."+hostname)
    rv = cur.fetchall()
    return jsonify(rv)

@app.route('/api/reviews', methods=['GET'])
def get_reviews():
    cur = mysql.connection.cursor()
    name = request.args.get('ID')
    print('hello')
    name=str(name)
    strName="'"+name+"'"
    cur.execute("SELECT * FROM db_tasks.reviews WHERE name="+strName)
    rv = cur.fetchall()
    return jsonify(rv)

@app.route('/api/rent', methods=['POST'])
def add_rent():
    cur = mysql.connection.cursor()
    lender = request.get_json()['lender']
    borrower = request.get_json()['borrower']
    rentTitle = request.get_json()['rentTitle']
    dueDate = request.get_json()['dueDate']
    dueTime = request.get_json()['dueTime']
    meetPlace = request.get_json()['meetPlace']
    cur.execute(
      "INSERT INTO db_tasks.rent (lender, borrower, rentTitle, dueDate, dueTime,meetPlace) VALUES('" + str(lender) + "', '" + str(borrower) + "', '" + str(rentTitle) + "', '" + str(dueDate) + "', '" + str(dueTime) + "', '" + str(meetPlace) + "');")
    data = cur.fetchall()
    mysql.connection.commit()

    result = {'lender': lender}

    return jsonify({'result': result})

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
    selectedState = request.get_json()['selectedState']
    cur.execute(
      "INSERT INTO db_tasks.tasks (title, price, startDate, endDate, des,image,memberID,major) VALUES('" + str(title) + "', '" + str(price) + "', '" + str(startDate) + "', '" + str(endDate) + "', '" + str(des) + "', '" + str(image) + "', '" + str(memberID) + "', '" + str(selectedState) + "');")
    data = cur.fetchall()
    mysql.connection.commit()

    result = {'title': title}

    return jsonify({'result': result})

@app.route('/api/seeks', methods=['POST'])
def add_seek():
    cur = mysql.connection.cursor()
    seekName = request.get_json()['seekName']
    seekDes = request.get_json()['seekDes']
    seekStartDate = request.get_json()['seekStartDate']
    seekEndDate = request.get_json()['seekEndDate']
    today=request.get_json()['today']
    memberID=request.get_json()['memberID']
    selectedState = request.get_json()['selectedState']
    print(seekDes)
    cur.execute(
      "INSERT INTO db_tasks.seek (seekName, seekDes, seekStartDate, seekEndDate, today, memberID,major) VALUES('" + str(seekName) + "', '" + str(seekDes) + "', '" + str(seekStartDate) + "', '" + str(seekEndDate) + "', '" + str(today) + "', '" + str(memberID) + "', '" + str(selectedState) + "');")
    data = cur.fetchall()
    mysql.connection.commit()

    result = {'seekName': seekName}

    return jsonify({'result': result})

@app.route('/api/users', methods=['POST'])
def add_msg():
    cur = mysql.connection.cursor()
    receiver = request.get_json()['receiver']
    sender = request.get_json()['sender']
    message = request.get_json()['message']
    title = request.get_json()['title']
    #title(receiver+" "+sender+" "+message)

    firstWord = "INSERT INTO "
    secondWord=" (sender, message,title) VALUES("
    strSender= '"'+str(sender)+'"'+", "
    strMessage = '"' + str(message) + '"' + ", "
    strTitle = '"'+str(title)+'"' + ");"
    strReceiver = str(receiver)
    print(firstWord+strReceiver+secondWord+strSender+strMessage)
    cur.execute(firstWord+strReceiver+secondWord+strSender+strMessage+strTitle)
    data = cur.fetchall()
    mysql.connection.commit()

    result = {'receiver': receiver}

    return jsonify({'result': result})

@app.route('/api/signup', methods=['POST'])
def add_users():
    cur = mysql.connection.cursor()
    id = request.get_json()['signUpID']
    pwd = request.get_json()['signUpPWD']
    phoneNum = request.get_json()['phoneNum']
    email = request.get_json()['email']

    cur.execute(
      "INSERT INTO db_tasks.users (id, pwd, phoneNum, email, score) VALUES('" + str(id) + "', '" + str(pwd) + "', '" + str(phoneNum) + "', '" + str(email) + "');")
    data = cur.fetchall()
    mysql.connection.commit()
    cur = mysql.connection.cursor()
    firstWord="CREATE TABLE "
    secondWord="(sender VARCHAR(40), message TEXT, title VARCHAR(50));"
    strID=str(id)
    cur.execute(firstWord +strID+secondWord)
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
