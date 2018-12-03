Iteration Report 6
--------------------------

What each person was responsible for accomplishing
--------------------------
(from iteration report 5)
- Joe:  Add logic that ensures you will not be able add the same username to database twice. Print message to tell user. Add missing unit tests for login
 - Jonathan: Ensure that you cannot log in by changing your url to show_entries. Check all Flask messages to ensure they are working. Add messages for any function where one is needed.
 - Johnny: Create the ability the save data based the user account. Add missing unit tests for filter date
 - Alex: Implement bootstrap. Group will discuss specifics on how the page will look. Alex will be responsible for those changes. Keep phone and tablet users in mind. Add missing unit tests for edit.
 - Everyone: Search for bugs and places where the program does not work as intended

What was completed
----------------------------
- Joe: No two usernames can be the same, with corresponding flash messages
- Jonathan: Used session variable to prevent changing the url to get into show_entries or any other pages without logging in.
- Johnny: Incomes and expenses are now user-specific. Helped Alex with hiding/showing graphs
- Alex: Updated styling to implement bootstrap, make interface more user-friendly

What was planned and not completed
------------------------------
Any work intended on unit tests was not completed. Work was done to try and update them, but ultimately they mostly fail or worked prior to merging of our individual branches, only to now fail.

What troubles/issues/roadblocks/difficulties you encountered
-------------------------------
Our graphs now do not display at all after bootstrap was incorporated. This will be fixed in our next iteration. Additionally, with the included security measures, our unit tests now need to be updated to accommodate how the data is being added and handled.

One important thing you learned during this iteration
--------------------------------
Session variables are incredibly useful. Using it, we added two new security features in preventing manually typing in a URL, and making only the specific user’s data appear. Also, we need to be conscious of how our updates to existing functions will affect unit tests, in that they will probably break them

What are you working on this week
-------------------------------------------
- Joe; Update login function to use hash functions to increase security
- Jonathan: Combing through application, trying to break it/find bugs that we need to fix, as well as assisting anyone in their assigned tasks
- Johnny: Update old unit tests to work with the new functions and changes to old ones
- Alex: Makes the graphs appear again, style them to look good in the app interface

What we will do in the final week
---------------------------------
Collectively search for bugs in our code, finding different areas to error check for when something could go wrong. Make a plan of how to present our project, making sure to showcase all functionality of the program.
