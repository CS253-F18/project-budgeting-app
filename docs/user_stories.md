Budgeting Application User Stories

Authors: Joe Ruppenthal, Johnny Whitfield, Jonathan Nocek, Alex O’Neill

The system for priorities and estimates are ranked by high, medium, and low priorities or estimates.  High priority is a user story that we want to accomplish first.  High estimate is a user story that will take a lot of work to accomplish.  

High Priority

Add an income
-----------------------
As a user, I want to be able to add an income to my account so that I can view my inflows of money.

 - Priority: high
 - Estimate: Low
 - Confirmation:

   1. Test step 1: enter a number in the income field
   2. Test step 2: check if the database is not empty
   3. Test step 3: check to see if the number entered is in the database

Add an expense
-----------------------
As a user, I want to be able to add an expense to my account so that I can view my outflows of money.

 - Priority: High
 - Estimate: Low
 - Confirmation:
   1. Test step 1: enter a number in the expense field
   2. Test step 2: check if the database is not empty
   3. Test step 3: check to see if the number entered is in the database

Remove an income
-----------------------
As a user, I want to be able to remove an income from my account so that my inflows of money are accurate.

 - Priority: High
 - Estimate: Low
 - Confirmation:

   1. Test step 1: add an income
   2. Test step 2: check to see that there is a value in the database
   3. Test step 3: run delete function
   4. Test step 4: check to see that the database is empty

Remove an expense
-----------------------
As a user, I want to be able to remove an expense from my account so that my outflows of money are accurate.

 - Priority: High
 - Estimate: Low
 - Confirmation:

   1. Test step 1: add an expense
   2. Test step 2: check to see that there is a value in the database
   3. Test step 3: run delete function
   4. Test step 4: check to see that the database is empty

Edit an income
-----------------------
As a user, I want to be able to edit an income from my account so that I can update my inflows of money when changes occur.

 - Priority: High
 - Estimate: Low
 - Confirmation:

   1. Test step 1: add an income
   2. Test step 2: check to see that a value is in the database
   3. Test step 3: run the edit function and change value of income
   4. Test step 4: check to see that the new value is in the database
   5. Test step 5: check to see that the initial value is not in the database

Edit an expense
-----------------------
As a user, I want to be able to edit an expense from my account so that I can update my outflows of money when changes occur.

 - Priority: High
 - Estimate: Low
 - Confirmation:

   1. Test step 1: add an expense
   2. Test step 2: check to see that a value is in the database
   3. Test step 3: run the edit function and change value of expense
   4. Test step 4: check to see that the new value is in the database
   5. Test step 5: check to see that the initial value is not in the database

Dates of expenses
-----------------------
As a user, I want to be able to view the date an expense was applied to my account so that I can budget with time in mind and verify/identify expenses based on time.

 - Priority: High
 - Estimate: Medium
 - Confirmation:

   1. Test step 1: Add the date of the expense
   2. Test step 2: check to see that database is not empty
   3. Test step 3: check to see that the date is in the database

Graphs
-----------------------
As a user, I want to be able to view my expenses in a graph so that I have a visual representation of all my expenses.

 - Priority: High
 - Estimate: High
 - Confirmation:

   1. Test step 1: See if a graph shows up at all in the User’s page
   2. Test step 2: See if the graph is populated with the User’s data
   3. Test step 3: See if the graph is correct based on that data

Net Income
-----------------------
As a user, I want to be able to view my total net income so that I can view how much money I have available after expenses.

 - Priority: High
 - Estimate: Low
 - Confirmation:

   1. Test step 1: Create a total net income function
   2. Test step 2: Make the total net income individual for each user
   3. Test step 3: Check that the right data shows up for each user

Medium Priority

Expense Alert
-----------------------
As a user, I want to receive an alert when I close to or have gone over a limit that I set for expenses so that my expenses do not exceed my income.

 - Priority: Medium
 - Estimate: Medium
 - Confirmation:

   1. Test step 1: add an income
   2. Test step 2: add an expense greater than income
   3. Test step 3: check if alert appears

Regular expenses
-----------------------
As a user, I want to be able to set regular expenses that will be applied to my account at a specified date so that monthly payments will be automatically applied to my account.

 - Priority: Medium
 - Estimate: Medium
 - Confirmation:

   1. Test step 1: Make regular expenses that show up as user input
   2. Test step 2: Test to make sure that they show up monthly
   3. Test step 3: Make sure that they do not show up any time but monthly

Limit on Expenses
-----------------------
As a user, I want set a max total expense to be applied to my account so that my expenses don’t exceed the specified amount.

 - Priority: Medium
 - Estimate: Medium
 - Confirmation:

   1. Test step 1: Have a max total expense option
   2. Test step 2: Make it a user input
   3. Test step 3: Be able to categorize max total expenses towards certain labels?

Label incomes and expenses 
-----------------------
As a user, I want to be able label incomes and expenses so that I can differentiate my entries.

 - Priority: Medium
 - Estimate: Low
 - Confirmation:

   1. Test step 1: Add a category option to income and expenses
   2. Test step 2: Make it a user input for the user to be able to name their own labels
   3. Test step 3: Check to see if the labels are showing up correctly

Filter function
-----------------------
As a user, I want to be able to filter which incomes and expenses are being displayed so that I can view incomes and expenses that belong to a specific category.

 - Priority: Medium
 - Estimate: Medium
 - Confirmation:

   1. Test step 1: Be able to add categories to the income and expenses
   2. Test step 2: Make it a user input
   3. Test step 3: View data based on the category

Low Priority

Sub-account
-----------------------
As a user, I want to be able to create a sub-account within my user-account so that I can isolate specific incomes and expenses to budget for specific events like a birthday or christmas.

 - Priority: Low
 - Estimate: High
 - Confirmation:

   1. Test step 1: Create a “Christmas” sub-account
   2. Test step 2: Add two different incomes to general and Christmas totals
   3. Test step 3: Login to user account
   4. Test step 4: Check if the general and Christmas totals are different
   5. Test step 5: Check if the totals are correct for the incomes inputted

User Activity
-----------------------
As an administrator, I want to be able to view how much activity user accounts have over time so that I can identify dormant accounts.

 - Priority: Low
 - Estimate: Medium
 - Confirmation:

   1. Test step 1: Add an income to a user’s account
   2. Test step 2: Login as an administrator
   3. Test step 3: See if the user’s income and total are visible
   4. Ensure that the information is correct to the user’s account

Delete account
-----------------------
As a user, I want to be able to delete my account so that my information is removed from the database.

 - Priority: Low
 - Estimate: Low
 - Confirmation:

   1. Test step 1: A a delete option
   2. Test step 2: Make sure that it shows up for the user
   3. Test step 3: Make sure that it deletes the users data from the database

Monthly history
-----------------------
As a user, I want to be able to view my activity in past months so that I can compare how I budgeted in past months to how I am budgeting in the current month.

 - Priority: Low
 - Estimate: Medium
 - Confirmation:

   1. Test step 1: Add a monthly history column to the home page to link to other pages with months
   2. Test step 2: Select the correct SQL data for each month
   3. Test step 3: Check that the months link to the right page and show the right information
