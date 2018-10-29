Iteration Report 1
-----------------------

What each person was responsible for accomplishing
-----------------------
(From iteration plan 1)
 - Joe: Create a database for incomes and expenses. Create the add income and add expense functions
 - Jonathan: Start formatting the webpage. Create Skeleton
 - Alex: Create .html table for all incomes and expenses
 - Johnny: Create Schema table. Create unit tests for add income and add expense functions.

What was completed
-----------------------
 - Jonathan: Created the basic layout and formatting for layout.html and style.css. This
included: creating a title for the webpage, creating two columns for each side of the
webpage, creating setions for the income table, expense table, the add income function,
the add expense function, and graphs. Created the show_entries.html file as well. This included
the show functions for add_income and add_expense.
 - Joe: Transferred the framework from Flaskr into our application which included app.py. Then added the add income and add expenses functions.
Helped the group setup Flask configurations. This included the run and initdb tests. 
 - Johnny: Created the schema file. He made the unit tests for add_income and add_expense.
 - Alex: Created the html for the expense and income table. Included the columns for category, edit, delete, and amount.


One tool or process or approach you used that you felt was especially helpful, and why.
-----------------------

Group meetings were very helpful for us. We were able to accomplish a lot and whatever one of us was stuck on was quickly resovled by
another team member. We were able to discuss overall strategy that is difficult to talk about over GroupMe. We can also look at each
other's code for bugs as a new set of eyes can quickly catch errors.

What was planned but not finished
-----------------------



What troubles/issues/roadblocks/difficulties you encountered
-----------------------

We discovered that we did not correctly consider the scope of an add function. We did not distrubute work correctly. We should have
had each person write their respective html for their functions. Instead, we had two people work on all the html while
two other people worked on the unit tests and python. This resulted in our group not being able to test out functions individually
since the people writing the python code did not have the html and visa versa. We did not account for the time taken to setup PyCharm. 

What adjustments to your overall design you discovered
-----------------------

We will now have everyone write the html for what they add into python so they can test it before merging. We will think out
all dependencies as we had the overarching dependencies correct but there little things that we did not consider that led to 
problems. Our group worked very well together when meeting so we plan to meet at least 3 times a week and have these meetings scheduled
out periodcally thoughout the week instead of meeting the days before the due date.

Which user stories and tasks you plan to complete in the coming iteration and in the two iterations following it.
-----------------------

Week 2:
 - The first priority will be to test show_entries and the income/expense table.
 - Once that is complete, we will add a categories feature and test it. These appear next the the add entry function and give the
user an option to give each entry a predetermined category.
 - Create filter categories feature and test it. This will appear below the table and give the user the option to sort the table
by one of the predetermined categories
 - Create net income display. This should be show the income remaining after each income and expense is added. This will
be displayed above the table in the top right corner of the page. Test it.

Week 3:
 - Continue the work from the previous week if we do not finish everything.
 - Create the remove an expense and remove an income functions. Work on associated .html files
so the delete/remove button appears next to each entry within the table. Test it.
 - Create the edit expense/income functions and associated html. This should be displayed next
to each entry within the table. Test it.

Week 4:
 - Continue the work that was not completed from the previous week.
 - Create a "Create User Account" page and make associated html. Test it.
 - Create a database that stores usernames and passwords.  Test it. 

Who will be responsible for each user story planned for the next iteration, not the following two.
-----------------------

Week 2:
 - Joe:
 - Jonathan:
 - Johnny:
 - Alex: 