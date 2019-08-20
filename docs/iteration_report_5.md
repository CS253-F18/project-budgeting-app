Iteration Report 5
-----------------------

What each person was responsible for accomplishing
-----------------------
(From iteration report 4)
 - Joe: Get user accounts to save data on different accounts.  Personalize accounts with greeting message. Add ability to filter by date.
 - Jonathan: Get user accounts to save data on different accounts.  Add "show More" and "show less" to income and expense tables
 - Johnny: Add buttons to hide and show specific graphs.  Add bar graph. Get rounding working for all values in all tables. 
 - Alex: Get graphs working properly.  Help Jonathan with show more/less
 - Everyone: get previous unit tests working so we can focus on the new ones


What was completed
-----------------------
 - Joe: Fixed issues with the login page from last week. Login page will no longer break due to incorrect username/password. Also, the
page will no longer login with an incorrect username and correct password.
 - Jonathan: Added logout feature. Added filter date feature. Worked with Joe to get login page funtional. Added a remove filter button 
so the user can go back and see their entire table after adding a filter. Started making the page look better.
 - Johnny: Fixed unit tests so they are now passing in PyCharm. Added a show/hide feature for each of the graphs. Added rounding to the incomes.
 - Alex: Created 6 different graphs. They are now functional and use the data from each table.


What was planned but not finished
-----------------------
The personalized greeting messages were never completed. This is dependent on the ability to save data which our group struggled with. The "show more" and "show less" to income and expense table. Group has
reevaluated and decided that the "show more/show less" feature for the tables is not necessary as the user already has multiple filter options. The save data for each user acount was never completed.
Our group sturggled with the concept. We now have an idea of how to do from office hours on Monday and will implement it in the following iteration.


What troubles/issues/roadblocks/difficulties you encountered
-----------------------
We had a few issues getting the login page working correctly so it only logged in with username/password combos added to the database. This was completed use paraprogramming and researching
the problem online. We struggled with the saving data for each user account. This was due to having to fix other bugs in the code and confusion on the understanding of the topic. 


What adjustments to your overall design you discovered
-----------------------
This week our group swithced some of our individual tasks in order to complete the iteration on time. For example, Alex was able to complete the pie charts so he was able
to do the bar graphs for Johnny.
I believe our overall design is looking good right now. We need to dedicate time in the future to ensuring there are no bugs in our program that allow users to login incorrectly. We need
to test all cases before the program in completed. 


One important thing you learned during this iteration
-----------------------
We need to spend time in the future looking for bugs so there will be no way to break our application. This week we found a bug that allowed the user to login with an incorrect username
but a correct password. Also, office hours/piazza are very helpful to getting questions clearified when confused.


Which user stories and tasks you plan to complete in the coming iteration and in the two iterations following it.
----------------------- 

Week 7
 - Create the ability the save data based the user account
 - Make the page look good using Bootstrap. Ensure that it will be good for mobile users, tablet users, etc.
 - Add all missing unit tests. Make sure they are all passing in GitHub and PyCharm.
 - Start searching for bugs and places where the program does not work as intended by testing all cases.
 - Check all Flask messages to ensure they are working. Add messages for any function where one is needed.
 - Ensure that you cannot log in by changing your url to show_entries
 - Add logic that ensures you will not be able add the same username to database twice. Print message to tell user.

Week 8 
 - Complete work from previous week.
 - Thorough search for all bugs and confirming that application works exactly as we want.
 - Finalize all unit tests and ensure they are all passing
 - Add comments as needed
 - Ensure the page is secure (we will learn about this in class)
 - Polish all code to ensure it is easily readible

Presentation Week
 - Prepare final presentation.
 - Continue search for bugs and errors by testing all cases and functionality. 

Who will be responsible for each user story planned for the next iteration, not the following two.
-----------------------

 - Joe:  Add logic that ensures you will not be able add the same username to database twice. Print message to tell user. Add missing unit tests for login
 - Jonathan: Ensure that you cannot log in by changing your url to show_entries. Check all Flask messages to ensure they are working. Add messages for any function where one is needed.
 - Johnny: Create the ability the save data based the user account. Add missing unit tests for filter date
 - Alex: Implement bootstrap. Group will discuss specifics on how the page will look. Alex will be responsible for those changes. Keep phone and tablet users in mind. Add missing unit tests for edit.
 - Everyone: Search for bugs and places where the program does not work as intended