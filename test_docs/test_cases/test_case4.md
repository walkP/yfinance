## System Test Case
**yfinance**<br><br>
**USER STORY:** Getting info on whether yf.Ticker("SFL") has info on "shortName"

**Purpose:** Calling yf.Ticker("SFL") to test if yf.Ticker("SFL").info has a key "shortName" and a value for it `Error when using ticker.info`. We want to investigate the cause of this problem and uncover any bugs.<br>
**Tester Name(s):** Walker Peters, Ji Heon Kim, Scott Kavalinas<br>
**Date(s) of Test:** March 25-28<br>
**File Used to Test:** Test_yfinance.py<br><br>

**TEST SCRIPT STEPS/RESULTS**
| Step | Test Step/Input                                             | Expected Results                      | Results        |
|------|-------------------------------------------------------------|---------------------------------------|----------------|
| 1    | Navigate to the root directory and run Python               | Python shell runs                     | pass           |
| 2.   | Instantiate a ticker with "MSFT"                            | ticker is created successfully        | pass           |
| 3.   | Get info on ticker.info to test if value exists             | ticker type is successfully tested    | pass           |
