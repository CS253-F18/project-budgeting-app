Iteration Report 4
-----------------------

What each person was responsible for accomplishing
-----------------------
(From iteration report 3)
 - Joe: Joe was responsible for creating the login/Create User Account page, which included input tags for inputting username and passwords.
 - Jonathan: Johnathan worked with Joe on the schema, login.html, and app.py for the Login page, and making sure the functionality for logging in works. 
 - Johnny: Create a flash message for when the expenses exceed the amount of income that you have. This will eventually include the regular expenses that we would like to implement, but not for next week. 
 - Alex: Alex was responsible for starting on the implementation for the graphs. The goal for this week will be to have one kind of graph working. In the future we plan to have multiple types of graphs working. 


What was completed
-----------------------
 - Jonathan & Joe:  Through pair programming, completed the login/create new user page
 - Johnny: Johnny completed the alert messages for when total expenses exceed incomes. Got rounding working for net income
 - Alex: Added a pie chart and line graph.


What was planned but not finished
-----------------------
The graphs show up on the page, however, they are not functional.  Rounding for individual values in the table is not functional.


What troubles/issues/roadblocks/difficulties you encountered
-----------------------
We encountered issues trying get the functionality of the login page working.  The first big road block was figuring out that we were selecting a row object rather than the actual value contained in the row object.  After we solved this issue, the problem we ran into next was trying to put all of the python code for login in a single function within a single handler.  We then separated the code into different handlers and different functions to finally get the login page working. We ran into trouble trying to get the graphs to utilize the data in our tables.  Last, we had difficulties getting incomes and expenses to be rounded and displayed to the nearest hundredth place within the tables.


What adjustments to your overall design you discovered
-----------------------
Changes to the overall design that we would like to implement soon will be personalization with user accounts such a "Welcome [username] " message that appears at the top of the page when a user logs in to their account.  In addition, we want to be able to hide/show different graphs so all of the graphs are not displayed at once

One important thing you learned during this iteration
-----------------------
One important thing we learned this iteration is how helpful the debugger in PyCharm is when it is utilized properly.  We ran our code in debug mode and added a break-point before login to identify where the errors in our login function were occurring.


Which user stories and tasks you plan to complete in the coming iteration and in the two iterations following it.
----------------------- 
Week 6:
 - Continue the work that was not completed from the previous week.
 - Date and time of incomes and expenses being added to the table
 - Finish the impletation of the graphs, we believe that this will be a two week job. 
 
Week 7:
 - Continue the work that was not completed from the previous week.
 - Finish all user stories and unit tests that have not been completed up unto this point. The program should be done at this point. 
 
Who will be responsible for each user story planned for the next iteration, not the following two.
-----------------------

Week 6:
 - Joe: Get user accounts to save data on different accounts.  Personalize accounts with greeting message. Add ability to filter by date.
 - Jonathan: Get user accounts to save data on different accounts.  Add "show More" and "show less" to income and expense tables
 - Johnny: Add buttons to hide and show specific graphs.  Add bar graph. Get rounding working for all values in all tables. 
 - Alex: Get graphs working properly.  Help Jonathan with show more/less
 - Everyone: get previous unit tests working so we can focus on the new ones