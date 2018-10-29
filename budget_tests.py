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
        assert b'No entries here so far' in rv.data

    def test_add_income(self):
        rv = self.app.post('/add', data=dict(
            incomeAmount=50
        ), follow_redirects=True)
        assert b'No entries here so far' not in rv.data
        assert b'New income was successfully added' in rv.data

        def test_add_expense(self):
            rv = self.app.post('/add', data=dict(
                expenseAmount=50
            ), follow_redirects=True)
            assert b'No entries here so far' not in rv.data
            assert b'New expense was successfully added' in rv.data