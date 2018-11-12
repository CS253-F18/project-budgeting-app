drop table if exists incomes;
create table incomes (
  id integer primary key autoincrement,
  'label' text,
  'income_date' text,
  'amount' float,
  category text
);
drop table if exists expenses;
create table expenses (
  id integer primary key autoincrement,
  'label' text,
  'expense_date' text,
  'amount' float,
  category text
);