## System Test Case
**yfinance**<br><br>
**USER STORY:** Income Statement, Balance Sheet and Cashflows are coming up as an empty dataframe (issue #191)

**Purpose:** if a user is looking for information on a particular company and either: 1) the company does not exist 2) the company is not publicly traded or 3) the use input an incorrect ticker,
 the user should be notified of an error rather than receiving empty data.<br>
**Tester Name(s):** Walker Peters, Ji Heon Kim, Scott Kavalinas<br>
**Date(s) of Test:** March 25-28<br>
**File Used to Test:** emptyTest.py<br><br>

**TEST SCRIPT STEPS/RESULTS**
| Step | Test Step/Input                                             | Expected Results                      | Results        |
|------|-------------------------------------------------------------|---------------------------------------|----------------|
| 1    | Navigate to the root directory and run python emptyTest.py  | Python shell runs                     | pass           |
| 2.   | allow code to run for 2 tickers "MSFT" and 'ENE'(delisted)  | Financial statements are not empty.   | fail           |

