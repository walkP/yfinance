## System Test Case
**yfinance**<br><br>
**USER STORY:** Getting info on whether the type yf.Ticker("MSFT") is dict or not

**Purpose:** Calling yf.Ticker to compare the type of Ticker and an empty dict `Attributes in yf.Ticker("MSFT") as dict`. We want to investigate the cause of this problem and uncover any bugs.<br>
**Tester Name(s):** Walker Peters, Ji Heon Kim, Scott Kavalinas<br>
**Date(s) of Test:** March 25-28<br>
**File Used to Test:** Test_yfinance.py<br><br>

**TEST SCRIPT STEPS/RESULTS**
| Step | Test Step/Input                                             | Expected Results                      | Actual Results |
|------|-------------------------------------------------------------|---------------------------------------|----------------|
| 1    | Navigate to the root directory and run Python               | Python shell runs                     | pass           |
| 2.   | Instantiate a ticker with "MSFT"                            | ticker is created successfully        | pass           |
| 3.   | Get info on the type of Ticker attribute                    | ticker info is successfully displayed | pass           |
