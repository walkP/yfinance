## System Test Case
**yfinance**<br><br>
**USER STORY:** Income Statement, Balance Sheet and Cashflows are coming up as an empty dataframe (issue #191)

**Purpose:** if a user is looking for information on a particular company and either: 1) the company does not exist 2) the company is not publicly traded or 3) the use input an incorrect ticker,
 the user should be notified of an error rather than receiving empty data.<br>
**Tester Name(s):** Walker Peters, Ji Heon Kim, Scott Kavalinas<br>
**Date(s) of Test:** March 25-28<br>
**File Used to Test:** yfinance/emptyTest.py<br><br>

## Introduction
**Requirements:** Does not require specific software<br>
**Roles and Responsibilities:** Every tester members listed above, have tested on their machines to ensure that the test is executed appropriately<br>
**Procedures and Results**<br>
| Step | Test Step/Input                                                      |
|------|----------------------------------------------------------------------|
| 1    | Navigate to the root directory and run python yfinance/emptyTest.py  |
| 2.   | allow code to run for 2 tickers "MSFT" and 'ENE'(delisted)           |


## Environmental Needs
**Procedural Requirements:** Before executing the test cases, must have the right files in the proper directories<br>

## Test
**Expected Results and Actual Results**<br>
| Expected Results                                          | Results        |
|-----------------------------------------------------------|----------------|
| Python shell runs                                         | pass           |
| allow code to run for 2 tickers "MSFT" and 'ENE'(delisted)| fail           |

