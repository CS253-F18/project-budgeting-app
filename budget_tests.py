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
        rv = self.app.get('/')
        assert b'No incomes entered' in rv.data
        assert b'No expenses entered' in rv.data

    def test_add_income(self):
        rv = self.app.post('/add_income', data=dict(
            add_income=50,
            incomeCategory="Salary"
        ), follow_redirects=True)
        assert b'No incomes entered' not in rv.data
        assert b'Category Salary' in rv.data
        assert b'Amount 50.0' in rv.data

    def test_add_expense(self):
        rv = self.app.post('/add_expense', data=dict(
            add_expense=50,
            expenseCategory="Housing"
        ), follow_redirects=True)
        assert b'No expenses entered' not in rv.data
        assert b'Category Housing' in rv.data
        assert b'Amount 50.0' in rv.data

    def test_filter_income(self):
        rv = self.app.post('/add_income', data=dict(
            add_income=50,
            incomeCategory="Salary"
        ), follow_redirects=True)
        rv = self.app.post('/add_income', data=dict(
            add_income=55,
            incomeCategory="Miscellaneous"
        ), follow_redirects=True)
        rv = self.app.post('/filter_income', data=dict(
            filter_income="Salary"
        ), follow_redirects=True)
        assert b'No incomes entered' not in rv.data
        assert b'Amount 55.0' not in rv.data
        assert b'Amount 50.0' in rv.data
        assert b'Category Salary' in rv.data

    def test_filter_expense(self):
        rv = self.app.post('/add_expense', data=dict(
            add_expense=50,
            expenseCategory="Housing"
        ), follow_redirects=True)
        rv = self.app.post('/add_expense', data=dict(
            add_expense=50,
            expenseCategory="Transportation"
        ), follow_redirects=True)
        rv = self.app.post('/filter_expense', data=dict(
            filter_expense="Housing"
        ), follow_redirects=True)
        assert b'No expenses entered' not in rv.data
        assert b'Amount 55.0' not in rv.data
        assert b'Amount 50.0' in rv.data
        assert b'Category Housing' in rv.data