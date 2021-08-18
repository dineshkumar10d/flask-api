from flask import Flask, request, redirect
from sqlalchemy.orm import session

from model import db, StudentModel

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:password@localhost/students'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
db.init_app(app)


@app.route('/student/create', methods=['POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        age = request.form['age']
        try:
            student = StudentModel(name=name, gender=gender, age=age)
            db.session.add(student)
            db.session.commit()
            return 'Ok'
        except Exception as e:
            return 'Unable to create student, Please contact support:' + str(e)


@app.route('/student/get', methods=['GET'])
def get_student():
    student_id = request.args.get('id')
    try:
        # sql = f"SELECT * FROM students WHERE ID = {student_id}"
        student = StudentModel.query.filter_by(ID=student_id).first()
        result = student.to_dict()
        if result:
            return result
    except Exception as e:
        return 'Unable to fetch student, Please contact support:' + str(e)


@app.route('/student/update', methods=['PUT'])
def update_student():
    student_id = request.form['id']
    name = request.form['name']
    age = request.form['age']
    try:
        # sql = "UPDATE students SET NAME = %s, AGE = %s WHERE ID = %s"
        # val = (name, age, student_id)
        student = StudentModel.query.filter_by(ID=student_id).first()
        if student:
            student.NAME = name
            student.AGE = age
            db.session.merge(student)
            db.session.commit()
        return 'Student Data Updated Successfully!'
    except Exception as e:
        return 'Unable to update the student, Please contact support:' + str(e)


@app.route('/student/delete', methods=['DELETE'])
def delete():
    student_id = request.args.get('id')
    try:
        student = StudentModel.query.filter_by(ID=student_id).first()
        if student:
            db.session.delete(student)
            db.session.commit()
            return 'Student Data deleted successfully'
    except Exception as e:
        return 'Unable to delete data, Please contact support:' + str(e)


app.run(port=8000, debug=True)
