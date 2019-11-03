from app import app, db, login
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Address(db.Model):
    add_id = db.Column(db.Integer, primary_key=True)
    street_num = db.Column(db.String(10))
    street_1 = db.Column(db.String(50))
    street_2 = db.Column(db.String(50))
    city = db.Column(db.String(30))
    state = db.Column(db.String(3))
    zipcode = db.Column(db.String(11))

class Customer(db.Model):
    cust_id= db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(80))
    email = db.Column(db.String(120))
    phone = db.Column(db.String(13))
    add_id = db.Column(db.Integer, db.ForeignKey('address.add_id'))
    acct_id = db.Column(db.Integer, unique=True, index=True)
    date_created = db.Column(db.DateTime, default=datetime.now())

class Staff(db.Model):
    staff_id = db.Column(db.Integer, primary_key=True)
    job = db.Column(db.String(50))
    department = db.Column(db.String(50))
    full_name = db.Column(db.String(80))
    add_id = db.Column(db.Integer, db.ForeignKey('address.add_id'))
    date_hired = db.Column(db.DateTime, default=datetime.now())
    email= db.Column(db.String(120), unique=True, index=True)
    phone_num = db.Column(db.String(13))
    username = db.Column(db.String(30), unique=True)
    password_hash = db.Column(db.String(256))
    isadmin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Car(db.Model):
    car_id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(20))
    model = db.Column(db.String(20))
    color = db.Column(db.String(20))
    year = db.Column(db.String(4))
    vin = db.Column(db.String(20), unique=True)
    cust_id = db.Column(db.Integer, db.ForeignKey('customer.cust_id'))

class Payment(db.Model):
    payment_id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float)
    date = db.Column(db.DateTime, default=datetime.now())
    car_id = db.Column(db.Integer, db.ForeignKey('car.car_id'))
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.staff_id'))

class Inventory(db.Model):
    inventory_id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer, db.ForeignKey('car.car_id'))
    price = db.Column(db.Float)

class Maintenance(db.Model):
    maint_id = db.Column(db.Integer, primary_key=True)
    payment_id = db.Column(db.Integer, db.ForeignKey('payment.payment_id'))
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.staff_id'))
    date_started = db.Column(db.DateTime, default = datetime.now())
    date_finished = db.Column(db.DateTime, default = datetime.now())
    description = db.Column(db.String(200))

class Loan(db.Model):
    loan_id = db.Column(db.Integer, primary_key=True)
    payment_id = db.Column(db.Integer, db.ForeignKey('payment.payment_id'))
    credit_score = db.Column(db.Integer)
    loan_terms = db.Column(db.String(200))

class Insurance(db.Model):
    ins_id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer, db.ForeignKey('car.car_id'))
    provider = db.Column(db.String(80))
    montly_premium  = db.Column(db.Float)



@login.user_loader
def load_user(staff_id):
    return Staff.query.get(staff_id)
