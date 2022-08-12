from app import Employer, Employee, db

employer1 = Employer(name='Fran', company_name='Star plus')
employer2 = Employer(name='Mark', company_name='Mark n Spencers')
employer3 = Employer(name='Steven', company_name='Marvel')
employer4 = Employer(name='Stacy', company_name='Stacys wheels')

employee1 = Employee(name='Linda', employer=employer1)
employee2 = Employee(name='Joan', employer=employer2)
employee3 = Employee(name='Frank', employer_id=1)
employee4 = Employee(name='Tim', employer_id=2)

db.session.add_all([employer1, employer2, employer3, employer4])
db.session.add_all([employee1, employee2])

db.session.commit()
