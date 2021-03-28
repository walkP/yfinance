## System Test Case
**yfinance**<br><br>
**USER STORY:** Getting info on stocks by calling Ticker.info

**Purpose:** Calling Ticker.info on certain stocks results in `KeyError: "['maxAge'] not found in axis"`. We want to investigate the cause of this problem and uncover any bugs.<br>
**Tester Name(s):** Walker Peters, Ji Heon Kim<br>
**Date(s) of Test:** March 25-28<br><br>
**File Used to Test:** Test_yfinance.py

**TEST SCRIPT STEPS/RESULTS**
| Step | Test Step/Input                                             | Expected Results                      | Actual Results |
|------|-------------------------------------------------------------|---------------------------------------|----------------|
| 1    | Navigate to the root directory and run Python               | Python shell runs                     | pass           |
| 2.   | Instantiate a ticker with either "HTOO", "MSFT", or "BNKO"  | ticker is created successfully        | N/A            |
| 3.   | Get the stock info by typing `ticker.info'                  | ticker info is successfully displayed | pass           |
