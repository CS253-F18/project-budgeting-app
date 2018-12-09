
# -*- coding: utf-8 -*-
"""
    Budgeting Application
    ~~~~~~~~~~~~~~~~~~~~~~

    An application for users to enter incomes and
    expenses to effectively budget their money.

    Authors: Joe Ruppenthal, Jonathan Nocek, Johnny Whitfield,
             and Alex O'Neill

    Flaskr framework is utilized within this application
    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.

"""
import os
import werkzeug.security
import formatter
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, g, redirect, url_for, render_template, flash, session

# create our little application :)
app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'budget.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

# Connect_db: imported from Flask
def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

# Init_db: imported from Flask
def init_db():
    """Initializes the database."""
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

# Initdb_command: Imported from Flask
@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    init_db()
    print('Initialized the database.')

# get_db: Imported from Flask
def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

# close_db: Imported from Flask
@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

# login_page: This the default loading page for our application.
#             Will be called when first accessing the application, will render login.html
@app.route('/')
def login_page():
    flash('Welcome to our Budgeting Application', 'info')
    return render_template('login.html')

# login: Checks to see if the username and password are the same, if true, load show_entries
#        if false, then print error and reload login.
# Code found from the following website: http://flask.pocoo.org/docs/0.12/tutorial/views/
@app.route('/login', methods=['POST'])
def login():
    db = get_db()
    cur = db.execute('select username from users where username=?',
                     [request.form['login_username']])
    loginRow = cur.fetchone()
    # If loginRow = none, then selected username does not exist within the datebase.
    # give the user an error and reload login.html
    if loginRow == None:
        flash('Username and password do not match', "danger")
        return render_template('login.html')

    cur = db.execute('select password from users where username=?',
                     [request.form['login_username']])
    pwhash = cur.fetchone()[0]

    password = request.form['login_password']
    # Adds hashing to our password security. Adds SALT to password to create additional security.
    passwordCheck = werkzeug.security.check_password_hash(pwhash, password)
    # If passwordCheck == false, then there is no correct username/password combination.
    # give the user an error and reload login.html
    if passwordCheck == False:
        flash('Username and password do not match', "danger")
        return render_template('login.html')
    # If passing all of the above, then the username/password combination is correct. Set session to true.
    session['logged_in'] = True
    cur = db.execute('select id from users where username=?', [request.form['login_username']])
    user_id = cur.fetchone()[0]
    # Set the session's user_id to the user who has just logged in.
    session['user_id'] = int(user_id)
    cur = db.execute('select username from users where username=?', [request.form['login_username']])
    username = cur.fetchone()[0]
    # Personalized flash message
    flash('Welcome, ' + username + '!', "info")
    # User is now logged in, so load the url for show_entries
    return redirect(url_for('show_entries'))


# Code found from the following website http://flask.pocoo.org/docs/0.12/tutorial/views/
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('logged_in', None)
    flash('You were logged out', "info")
    return redirect(url_for('login_page'))


@app.route('/add_user', methods=['POST'])
def add_user():
    db = get_db()
    cur = db.execute('select username from users where username=?',
                     [request.form['add_username']])
    userRow = cur.fetchone()
    if userRow != None:
        flash('Username unavailable', "danger")
        return redirect(url_for('login_page'))
    user_password = request.form['add_password']
    db_password = werkzeug.security.generate_password_hash(user_password, method='pbkdf2:sha256', salt_length=8)
    db.execute('INSERT INTO users (username, password) VALUES (?, ?)',
               [request.form['add_username'], db_password])
    db.commit()
    flash('New user was successfully added', 'info')
    return redirect(url_for('login_page'))


@app.route('/show_entries')
def show_entries():
    db = get_db()
    cur = db.execute('select amount, category, id, income_date from incomes where user_id=? order by id desc', [session['user_id']])
    incomes = cur.fetchall()
    cur = db.execute('select amount, category, id, expense_date from expenses where user_id=? order by id desc',
                     [session['user_id']])
    expenses = cur.fetchall()

    cur = db.execute('SELECT TOTAL(amount) FROM incomes where user_id=?', [session['user_id']])
    incomeTotal = cur.fetchone()[0]
    cur = db.execute('SELECT TOTAL(amount) FROM expenses where user_id=?', [session['user_id']])
    expenseTotal = cur.fetchone()[0]
    cur = db.execute('SELECT TOTAL(amount) FROM incomes WHERE category = "Salary" and user_id=?', [session['user_id']])
    salaryTotal = cur.fetchone()[0]
    cur = db.execute('SELECT TOTAL(amount) FROM incomes WHERE category = "Miscellaneous" and user_id=?', [session['user_id']])
    miscellaneous1Total = cur.fetchone()[0]
    cur = db.execute('SELECT TOTAL(amount) FROM expenses WHERE category = "Housing" and user_id=?', [session['user_id']])
    housingTotal = cur.fetchone()[0]
    cur = db.execute('SELECT TOTAL(amount) FROM expenses WHERE category = "Transportation" and user_id=?', [session['user_id']])
    transportationTotal = cur.fetchone()[0]
    cur = db.execute('SELECT TOTAL(amount) FROM expenses WHERE category = "Food/Drink" and user_id=?', [session['user_id']])
    fooddrinkTotal = cur.fetchone()[0]
    cur = db.execute('SELECT TOTAL(amount) FROM expenses WHERE category = "Miscellaneous" and user_id=?', [session['user_id']])
    miscellaneous2Total = cur.fetchone()[0]

    if incomeTotal == "None" and expenseTotal == "None":
        net = 0.00
    elif incomeTotal != "None" and expenseTotal == "None":
        net = incomeTotal
    elif incomeTotal == "None" and expenseTotal != "None":
        net = 0.00 - expenseTotal
    else:
        net = incomeTotal - expenseTotal

    if net < 0:
        flash("Expenses outweigh incomes, needs re-budgeting", "danger")

    net = "{:.2f}".format(net)
    if 'logged_in' in session and session['logged_in']:
        return render_template('show_entries.html', incomes=incomes, expenses=expenses, net=net, salaryTotal=salaryTotal, miscellaneous1Total=miscellaneous1Total,
                               housingTotal=housingTotal, transportationTotal=transportationTotal, fooddrinkTotal=fooddrinkTotal, miscellaneous2Total=miscellaneous2Total,
                               incomeTotal=incomeTotal, expenseTotal=expenseTotal)
    flash('You are not logged in',  "danger")
    return redirect(url_for('login_page'))


@app.route('/add_income', methods=['POST'])
def add_income():
    db = get_db()
    db.execute('INSERT INTO incomes (amount, category, income_date, user_id) VALUES (?, ?, ?, ?)',
               [request.form['add_income'], request.form['incomeCategory'], request.form['income_date'], session['user_id']])
    db.commit()
    flash('New income was successfully added', "info")
    return redirect(url_for('show_entries'))


@app.route('/add_expense', methods=['POST'])
def add_expense():
    db = get_db()
    db.execute('INSERT INTO expenses (amount, category, expense_date, user_id) VALUES (?, ?, ?, ?)',
               [request.form['add_expense'], request.form['expenseCategory'], request.form['expense_date'],
                session['user_id']])
    db.commit()
    flash('New expense was successfully added', "info")
    return redirect(url_for('show_entries'))


@app.route('/edit_income_form', methods=['GET'])
def edit_income_form():
    db = get_db()
    cur = db.execute('select id, amount, category, income_date from incomes where id=?', [request.args['edit_incomes']])
    income = cur.fetchone()
    if 'logged_in' in session and session['logged_in']:
        return render_template('edit_incomes.html', income=income)
    flash('You are not logged in', "danger")
    return redirect(url_for('login_page'))


@app.route('/filter_income', methods=['POST'])
def filter_income():
    db = get_db()
    cur = db.execute("select amount, category, income_date from incomes where category=? order by id desc",[request.form['filter_income']])
    incomes = cur.fetchall()
    cur = db.execute("select amount, category, expense_date from expenses")
    expenses = cur.fetchall()
    flash('Incomes filtered', "info")
    return render_template('show_entries.html', incomes=incomes,  expenses=expenses)


@app.route('/filter_date', methods=['POST'])
def filter_date():
    db = get_db()
    cur = db.execute("select amount, category, expense_date from expenses where expense_date=? order by id desc",[request.form['filter_date']])
    expenses = cur.fetchall()
    cur = db.execute("select amount, category, income_date from incomes")
    incomes = cur.fetchall()
    flash('Dates filtered', "info")
    return render_template('show_entries.html', expenses=expenses, incomes=incomes)


@app.route('/filter_expense', methods=['POST'])
def filter_expense():
    db = get_db()
    cur = db.execute("select amount, category, expense_date from expenses where category=? order by id desc", [request.form['filter_expense']])
    expenses = cur.fetchall()
    cur = db.execute("select amount, category, income_date from incomes")
    incomes = cur.fetchall()
    flash('Expenses filtered', "info")
    return render_template('show_entries.html', expenses=expenses, incomes=incomes)


@app.route('/edit_expense_form', methods=['GET'])
def edit_expense_form():
    db = get_db()
    cur = db.execute('select id, amount, category, expense_date from expenses where id=?', [request.args['edit_expenses']])
    # Created the redirect_edit() function. Used similar format as the functions above.
    expense = cur.fetchone()
    if 'logged_in' in session and session['logged_in']:
        return render_template('edit_expenses.html', expense=expense)
    flash('You are not logged in', "danger")
    return redirect(url_for('login_page'))


@app.route('/edit_incomes', methods=['POST'])
def edit_incomes():
    db = get_db()
    db.execute("update incomes set amount = ?, category = ?, income_date = ? where id = ?",
               [request.form['amount'], request.form['category'], request.form['income_date'], request.form['edit_incomes']])
    db.commit()
    flash('Income edited', "info")
    return redirect(url_for("show_entries"))


@app.route('/edit_expenses', methods=['POST'])
def edit_expenses():
    db = get_db()
    db.execute("update expenses set amount = ?, category = ?, expense_date = ? where id = ?",
               [request.form['amount'], request.form['category'], request.form['expense_date'], request.form['edit_expenses']])
    db.commit()
    flash('Expense edited', "info")
    return redirect(url_for("show_entries"))

@app.route('/delete_income', methods=['POST'])
def delete_income():
    db = get_db()
    db.execute('DELETE FROM incomes WHERE id=?', [request.form['income_id']])
    db.commit()
    flash('Income deleted', "info")
    return redirect(url_for('show_entries'))


@app.route('/delete_expense', methods=['POST'])
def delete_expense():
    db = get_db()
    db.execute('DELETE FROM expenses WHERE id=?', [request.form['expense_id']])
    db.commit()
    flash('Expense deleted', "info")
    return redirect(url_for('show_entries'))


@app.route('/remove_filter', methods=['POST'])
def remove_filter():
    flash('Removed filter', "info")
    return redirect(url_for('show_entries'))
