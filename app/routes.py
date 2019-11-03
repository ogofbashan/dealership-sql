from app import app, db
from flask import render_template, url_for, redirect, flash
from app.forms import NameForm, MaintenanceForm, LoginForm
from app.models import Inventory, Car, Staff, Maintenance, Customer
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    #if user is already logged in, redirect them
    if current_user.is_authenticated:
        flash('You are already logged in!')
        return redirect(url_for('index', username=current_user.username))

    if form.validate_on_submit():

        # query the db for the user information, and log them in if everything is validators
        user = Staff.query.filter_by(email=form.email.data).first()

        # if user doesn't exist, reload page and flash message

        if user is None or not user.check_password(form.password.data):
            flash('Invalid Credentials.')
            return redirect(url_for('login'))

        #if the user does exist, and credentials are correct, log them in
        login_user(user)
        flash(f'You have been logged in!')
        return redirect(url_for('index', username=current_user.username))

    return render_template('form.html', form=form, title='Login')


@app.route('/index/<username>')
def index(username = ''):

     if not username:
        return redirect(url_for('login'))

     car = Car.query.all()

     inventory = Inventory.query.all()

     return render_template('index.html', inventory=inventory, car=car, username=username)

@app.route('/getcustomer', methods=['GET', 'POST'])
def GetCustomer():
    form = NameForm()

    if form.validate_on_submit():
        full_name= form.full_name.data
        customer = Customer.query.filter_by(full_name=full_name).first()
        search_cust_id = customer.cust_id
        return redirect(url_for('result', search_cust_id=search_cust_id))


    return render_template('form.html', title='Get Customer', form=form)

@app.route('/workorder', methods=['GET', 'POST'])
def WorkOrder():
    form = MaintenanceForm()

    work_order = Maintenance(payment_id = form.payment_id.data, staff_id = form.staff_id.data, date_started = form.date_started.data, date_finished=form.date_finished.data, description=form.description.data)

    if form.validate_on_submit():
        db.session.add(work_order)
        db. session.commit()
    return render_template('form.html', title='Work Order', form=form)

@app.route('/result/<search_cust_id>')
def result(search_cust_id):
    car = Car.query.all()
    search_cust_id = int(search_cust_id)

    customer= Customer.query.all()

    return render_template('result.html', title='Result', search_cust_id=search_cust_id, car=car, customer=customer)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
