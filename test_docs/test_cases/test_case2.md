## System Test Case
**yfinance**<br><br>
**USER STORY:** Getting info on stocks by calling Ticker.info

**Purpose:** Calling Ticker.info on certain stocks results in `KeyError: 'cashflowStatements'`. We want to investigate the cause of this problem and uncover any bugs.<br>
**Tester Name(s):** Walker Peters, Ji Heon Kim, Scott Kavalinas<br>
**Date(s) of Test:** March 25-28<br>
**File Used to Test:** test_yfinance.py<br><br>

**TEST SCRIPT STEPS/RESULTS**
| Step | Test Step/Input                                  | Expected Results                      | Results        |
|------|--------------------------------------------------|---------------------------------------|----------------|
| 1    | Navigate to the root directory and run Python    | Python shell runs                     | pass           |
| 2.   | Instantiate a ticker with either "ACGL" or "SFL" | ticker is created successfully        | pass           |
| 3.   | Get the stock info by typing `ticker.info'`      | ticker info is successfully displayed | pass           |
