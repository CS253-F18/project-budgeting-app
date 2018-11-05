drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  'label' text,
  'date' text,
  'incomeAmount' float,
  'expenseAmount' float,
  incomeCategory text,
  expenseCategory text
);
