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
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, g, redirect, url_for, render_template, flash


# create our little application :)
app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'budget.db'),
    DEBUG=True,
    SECRET_KEY='development key',
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
def show_entries():
    db = get_db()
    cur = db.execute('select id, amount, category from incomes order by id desc')
    incomes = cur.fetchall()
    cur = db.execute('select id, amount, category from expenses order by id desc')
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

    return render_template('show_entries.html', incomes=incomes, expenses=expenses, net=net)


@app.route('/add_income', methods=['POST'])
def add_income():
    db = get_db()
    db.execute('INSERT INTO incomes (amount, category) VALUES (?, ?)',
               [request.form['add_income'], request.form['incomeCategory']])
    db.commit()
    flash('New income was successfully added')
    return redirect(url_for('show_entries'))


@app.route('/add_expense', methods=['POST'])
def add_expense():
    db = get_db()
    db.execute('INSERT INTO expenses (amount, category) VALUES (?, ?)',
               [request.form['add_expense'], request.form['expenseCategory']])
    db.commit()
    flash('New expense was successfully added')
    return redirect(url_for('show_entries'))


@app.route('/filter_income', methods=['POST'])
def filter_income():
    db = get_db()
    cur = db.execute("select amount, category from incomes where category=? order by id desc",[request.form['filter_income']])
    incomes = cur.fetchall()
    return render_template('show_entries.html', incomes=incomes)


@app.route('/filter_expense', methods=['POST'])
def filter_expense():
    db = get_db()
    cur = db.execute("select amount, category from expenses where category=? order by id desc", [request.form['filter_expense']])
    expenses = cur.fetchall()
    return render_template('show_entries.html', expenses=expenses)


@app.route('/delete_income', methods=['POST'])
def delete_income():
    db = get_db()
    db.execute('DELETE FROM incomes WHERE id=?', [request.form['income-id']])
    db.commit()
    flash('Income deleted')
    return redirect(url_for('show_entries'))


@app.route('/delete_expense', methods=['POST'])
def delete_expense():
    db = get_db()
    db.execute('DELETE FROM expenses WHERE id=?', [request.form['expense-id']])
    db.commit()
    flash('Expense deleted')
    return redirect(url_for('show_entries'))

