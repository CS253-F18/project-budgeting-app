import os
import tempfile
import unittest
import flask

import app as budget


class BudgetTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, budget.app.config['DATABASE'] = tempfile.mkstemp()
        budget.app.testing = True
        self.app = budget.app.test_client()
        with budget.app.app_context():
            budget.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(budget.app.config['DATABASE'])

    def test_empty_db(self):
        rv = self.app.get('/show_entries')
        assert b'No incomes entered' in rv.data
        assert b'No expenses entered' in rv.data

    def test_add_income(self):
        rv = self.app.post('/add_income', data=dict(
            income_date="2018-11-16",
            add_income=50,
            incomeCategory="Salary"
        ), follow_redirects=True)
        assert b'No incomes entered' not in rv.data
        assert b'50.00' in rv.data

    def test_add_expense(self):
        rv = self.app.post('/add_expense', data=dict(
            expense_date="2018-11-16",
            add_expense=50,
            expenseCategory="Housing"
        ), follow_redirects=True)
        assert b'No expenses entered' not in rv.data
        assert b'50.00' in rv.data

    def test_filter_income(self):
        rv = self.app.post('/add_income', data=dict(
            income_date="2018-11-16",
            add_income=50,
            incomeCategory="Salary"
        ), follow_redirects=True)
        rv = self.app.post('/add_income', data=dict(
            income_date="2018-11-17",
            add_income=55,
            incomeCategory="Miscellaneous"
        ), follow_redirects=True)
        rv = self.app.post('/filter_income', data=dict(
            filter_income="Salary"
        ), follow_redirects=True)
        assert b'No incomes entered' not in rv.data
        assert b'55.00' not in rv.data
        assert b'50.00' in rv.data

    def test_filter_expense(self):
        rv = self.app.post('/add_expense', data=dict(
            expense_date="2018-11-16",
            add_expense=50,
            expenseCategory="Housing"
        ), follow_redirects=True)
        rv = self.app.post('/add_expense', data=dict(
            expense_date="2018-11-17",
            add_expense=55,
            expenseCategory="Transportation"
        ), follow_redirects=True)
        rv = self.app.post('/filter_expense', data=dict(
            filter_expense="Housing"
        ), follow_redirects=True)
        assert b'No expenses entered' not in rv.data
        assert b'55.00' not in rv.data
        assert b'50.00' in rv.data

    def test_delete_income(self):
        rv = self.app.post('/add_income', data=dict(
            income_date="2018-11-16",
            add_income=50,
            incomeCategory="Salary"
        ), follow_redirects=True)
        rv = self.app.post('/add_income', data=dict(
            income_date="2018-11-16",
            add_income=55,
            incomeCategory="Miscellaneous"
        ), follow_redirects=True)
        rv = self.app.post('/delete_income', data=dict(
            income_id=1
        ), follow_redirects=True)
        assert b'No incomes entered' not in rv.data
        assert b'50.00' not in rv.data
        assert b'55.00' in rv.data

    def test_delete_expense(self):
        rv = self.app.post('/add_expense', data=dict(
            expense_date="2018-11-16",
            add_expense=50,
            expenseCategory="Housing"
        ), follow_redirects=True)
        rv = self.app.post('/add_expense', data=dict(
            expense_date="2018-11-17",
            add_expense=55,
            expenseCategory="Transportation"
        ), follow_redirects=True)
        rv = self.app.post('/delete_expense', data=dict(
            expense_id=1
        ), follow_redirects=True)
        assert b'No expenses entered' not in rv.data
        assert b'50.0' not in rv.data
        assert b'55.0' in rv.data

    def test_add_user(self):
        rv = self.app.post('/add_user', data=dict(
            username="admin",
            password="default"
        ), follow_redirects=True)
        assert b'admin' not in rv.data
        assert b'admin' in rv.data
        assert b'default' in rv.data

    def test_login(self):
        rv = self.app.post('/add_user', data=dict(
            username="admin",
            password="default"
        ), follow_redirects=True)
        rv = self.app.post('/login', data=dict(
            username="admin",
            password="default"
        ), follow_redirects=True)
        assert b'admin' not in rv.data
        assert b'admin' in rv.data
        assert b'default' in rv.data
        assert b'You were logged in' in rv.data
