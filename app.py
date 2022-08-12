from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# import os
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:147root@localhost:3306/project"
app.config['SECRET_KEY'] = "secret"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Employer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    company_name = db.Column(db.String(50), nullable=False)
    employees = db.relationship('Employee', backref='employer')

    def __repr__(self):
        return f'<Company "{self.company_name}">'


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    employer_id = db.Column(db.Integer, db.ForeignKey('employer.id'))


db.create_all()


@app.route('/')
def index():
    employers = Employer.query.all()
    return render_template('index.html', employers=employers)


@app.route('/<int:employer_id>/', methods=('GET', 'POST'))
def employer(employer_id):
    employer = Employer.query.get_or_404(employer_id)
    if request.method == 'POST':
        employee = Employee(name=request.form['content'], employer=employer)
        db.session.add(employee)
        db.session.commit()
        return redirect(url_for('employer', employer_id=employer.id))
    return render_template('employer.html', employer=employer)


@app.route('/employees')
def employees():
    employees = Employee.query.order_by(Employee.id.desc()).all()
    return render_template('employee.html', employees=employees)


@app.route('/employees/<int:employee_id>/delete')
def delete_employee(employee_id):
    employee = Employee.query.get_or_404(employee_id)
    employer_id = employee.employer.id
    db.session.delete(employee)
    db.session.commit()
    return redirect(url_for('employer', employer_id=employer_id))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')




