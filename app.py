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
    cur = db.execute('select incomeAmount, expenseAmount from entries order by id desc')
    entries = cur.fetchall()
    return render_template('show_entries.html', entries=entries)


@app.route('/add_income', methods=['POST'])
def add_income():
    db = get_db()
    db.execute('INSERT INTO entries (incomeAmount) VALUES (?)',
               [request.form['incomeAmount']])
    db.commit()
    flash('New income was successfully added')
    return redirect(url_for('show_entries'))

@app.route('/add_expense', methods=['POST'])
def add_expense():
    db = get_db()
    db.execute('INSERT INTO entries (expenseAmount) VALUES (?)',
               [request.form['expenseAmount']])
    db.commit()
    flash('New expense was successfully added')
    return redirect(url_for('show_entries'))
