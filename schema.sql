drop table if exists incomes;
create table incomes (
  id integer primary key autoincrement,
  'label' text,
  'income_date' text,
  'amount' float,
  category text,
  'user_id' integer not null
);
drop table if exists expenses;
create table expenses (
  id integer primary key autoincrement,
  'label' text,
  'expense_date' text,
  'amount' float,
  category text,
  'user_id' integer not null
);
drop table if exists users;
create table users (
  id integer primary key autoincrement,
  'username' text,
  'password' text
);