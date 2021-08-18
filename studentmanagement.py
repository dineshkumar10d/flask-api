import mysql.connector
from flask import Flask, request

myDb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="students"
)
myCursor = myDb.cursor(dictionary=True)

app = Flask(__name__)


@app.route('/student/create', methods=['POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        age = request.form['age']
        try:
            sql = "INSERT INTO students(NAME,GENDER,AGE) VALUES(%s,%s,%s)"
            val = (name, gender, age)
            myCursor.execute(sql, val)
            myDb.commit()
            return 'Ok'
        except Exception as e:
            return 'Unable to create student, Please contact support:' + str(e)


@app.route('/student/get', methods=['GET'])
def get_student():
    student_id = request.args.get('id')
    try:
        sql = f"SELECT * FROM students WHERE ID = {student_id}"
        myCursor.execute(sql)
        my_result = myCursor.fetchone()
        return my_result
    except Exception as e:
        return 'Unable to fetch student, Please contact support:' + str(e)


@app.route('/student/update', methods=['PUT'])
def update_student():
    student_id = request.form['id']
    name = request.form['name']
    age = request.form['age']
    try:
        sql = "UPDATE students SET NAME = %s, AGE = %s WHERE ID = %s"
        val = (name, age, student_id)
        myCursor.execute(sql, val)
        myDb.commit()
        return 'Student Data Updated Successfully!'
    except Exception as e:
        return 'Unable to update the student, Please contact support:' + str(e)


@app.route('/student/delete/<int:student_id>', methods=['DELETE'])
def delete_student():
    student_id = request.form['id']
    sql = f"DELETE FROM students WHERE ID = {student_id}"
    try:
        myCursor.execute(sql)
        myDb.commit()
        return "Student Data deleted Successfully!"
    except Exception as e:
        return "Unable to delete student:" + str(e)


app.run(port=8000, debug=True)
