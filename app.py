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
    cur = db.execute('select amount, category from incomes order by id desc')
    incomes = cur.fetchall()
    cur = db.execute('select amount, category from expenses order by id desc')
    expenses = cur.fetchall()
    return render_template('show_entries.html', incomes=incomes, expenses=expenses)


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

# Function to redirect the webpage to the edit_entires.html page
@app.route('/redirect_edit_income', methods=['GET'])
def redirect_edit_income():
    db = get_db()
    cur = db.execute('select id, amount, category from incomes where id=?', [request.args['edit_text']])
    # Created the redirect_edit() function. Used similar format as the functions above.
    incomes = cur.fetchall()
    return render_template('edit_incomes.html', incomes=incomes)

# Function to redirect the webpage to the edit_entires.html page
@app.route('/redirect_edit_expense', methods=['GET'])
def redirect_edit_expense():
    db = get_db()
    cur = db.execute('select id, amount, category from expenses where id=?', [request.args['edit_text']])
    # Created the redirect_edit() function. Used similar format as the functions above.
    expenses = cur.fetchall()
    return render_template('edit_expenses.html', expenses=expenses)

# Function that actually edits the posts. The function will load a new page with the selected text already preloaded.
@app.route('/edit_entries', methods=['POST'])
def edit_entries():
    db = get_db()
    # https://stackoverflow.com/questions/1307378/python-mysql-update-statement
    # Used the above link for the update. It helped me learn the syntax.
    db.execute("update incomes, expenses set amount = ?, category = ? where id = ?",
               [request.form['amount'], request.form['category'],request.form['edit_text']])
    db.commit()
    return show_entries()