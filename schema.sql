drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  'label' text not null,
  'category' category not null,
  'date' text not null,
  'incomeAmount' float not null,
  'expenseAmount' float not null
);
