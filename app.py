
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


def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    """Initializes the database."""
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    init_db()
    print('Initialized the database.')


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/')
def login_page():
    flash('Welcome to our Budgeting Application')
    return render_template('login.html')


# Code found from the following website: http://flask.pocoo.org/docs/0.12/tutorial/views/
@app.route('/login', methods=['GET', 'POST'])
def login():
    db = get_db()
    cur = db.execute('select username from login where username=?', [request.form['login_username']])
    loginUsername = cur.fetchone()[0]
    cur1 = db.execute('select password from login where password=?', [request.form['login_password']])
    loginPassword = cur1.fetchone()[0]
    error = None
    if request.method == 'POST':
        if request.form['login_username'] != loginUsername:
            error = 'Invalid username'
        elif request.form['login_password'] != loginPassword:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

# Code found from the following website http://flask.pocoo.org/docs/0.12/tutorial/views/
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('login_page'))


@app.route('/add_user', methods=['POST'])
def add_user():
    db = get_db()
    db.execute('INSERT INTO login (username, password) VALUES (?, ?)',
               [request.form['add_username'],request.form['add_password']])
    db.commit()
    flash('New user was successfully added')
    return redirect(url_for('login_page'))


@app.route('/show_entries')
def show_entries():
    db = get_db()
    cur = db.execute('select amount, category, id, income_date from incomes order by id desc')
    incomes = cur.fetchall()
    cur = db.execute('select amount, category, id, expense_date from expenses order by id desc')
    expenses = cur.fetchall()
    
    cur = db.execute('SELECT TOTAL(amount) FROM incomes')
    incomeTotal = cur.fetchone()[0]
    cur = db.execute('SELECT TOTAL(amount) FROM expenses')
    expenseTotal = cur.fetchone()[0]

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

    return render_template('show_entries.html', incomes=incomes, expenses=expenses, net=net)


@app.route('/add_income', methods=['POST'])
def add_income():
    db = get_db()
    db.execute('INSERT INTO incomes (amount, category, income_date) VALUES (?, ?, ?)',
               [request.form['add_income'], request.form['incomeCategory'], request.form['income_date']])
    db.commit()
    flash('New income was successfully added', "info")
    return redirect(url_for('show_entries'))


@app.route('/add_expense', methods=['POST'])
def add_expense():
    db = get_db()
    db.execute('INSERT INTO expenses (amount, category, expense_date) VALUES (?, ?, ?)',
               [request.form['add_expense'], request.form['expenseCategory'], request.form['expense_date']])
    db.commit()
    flash('New expense was successfully added', "info")
    return redirect(url_for('show_entries'))


@app.route('/edit_income_form', methods=['GET'])
def edit_income_form():
    db = get_db()
    cur = db.execute('select id, amount, category from incomes where id=?', [request.args['edit_incomes']])
    income = cur.fetchone()
    return render_template('edit_incomes.html', income=income)

                
@app.route('/filter_income', methods=['POST'])
def filter_income():
    db = get_db()
    cur = db.execute("select amount, category from incomes where category=? order by id desc",[request.form['filter_income']])
    incomes = cur.fetchall()
    flash('Incomes filtered', "info")
    return render_template('show_entries.html', incomes=incomes)
                

@app.route('/filter_date', methods=['POST'])
def filter_date():
    db = get_db()
    cur = db.execute("select amount, expense_date from expenses where expense_date=? order by id desc",[request.form['filter_date']])
    expenses = cur.fetchall()
    flash('Dates filtered', "info")
    return render_template('show_entries.html', expenses=expenses)


@app.route('/filter_expense', methods=['POST'])
def filter_expense():
    db = get_db()
    cur = db.execute("select amount, category from expenses where category=? order by id desc", [request.form['filter_expense']])
    expenses = cur.fetchall()
    flash('Expenses filtered', "info")
    return render_template('show_entries.html', expenses=expenses)

                
@app.route('/edit_expense_form', methods=['GET'])
def edit_expense_form():
    db = get_db()
    cur = db.execute('select id, amount, category from expenses where id=?', [request.args['edit_expenses']])
    # Created the redirect_edit() function. Used similar format as the functions above.
    expense = cur.fetchone()
    return render_template('edit_expenses.html', expense=expense)


@app.route('/edit_incomes', methods=['POST'])
def edit_incomes():
    db = get_db()
    db.execute("update incomes set amount = ?, category = ? where id = ?",
               [request.form['amount'], request.form['category'],request.form['edit_incomes']])
    db.commit()
    flash('Income edited', "info")
    return redirect(url_for("show_entries"))


@app.route('/edit_expenses', methods=['POST'])
def edit_expenses():
    db = get_db()
    db.execute("update expenses set amount = ?, category = ? where id = ?",
               [request.form['amount'], request.form['category'],request.form['edit_expenses']])
    db.commit()
    flash('Expense edited', "info")
    return redirect(url_for("show_entries"))
  
@app.route('/delete_income', methods=['POST'])
def delete_income():
    db = get_db()
    db.execute('DELETE FROM incomes WHERE id=?', [request.form['income-id']])
    db.commit()
    flash('Income deleted', "info")
    return redirect(url_for('show_entries'))


@app.route('/delete_expense', methods=['POST'])
def delete_expense():
    db = get_db()
    db.execute('DELETE FROM expenses WHERE id=?', [request.form['expense-id']])
    db.commit()
    flash('Expense deleted', "info")
    return redirect(url_for('show_entries'))
  
