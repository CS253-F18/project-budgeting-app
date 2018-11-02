drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  'label' text,
  'category' category,
  'date' text,
  'incomeAmount' float not null,
  'expenseAmount' float
);
