## System Test Case
**yfinance**<br><br>
**USER STORY:** Getting info on stocks by calling Ticker.info

**Purpose:** Calling Ticker.info on certain stocks results in `KeyError: "['maxAge'] not found in axis"`. We want to investigate the cause of this problem and uncover any bugs (related to issues #599, #163, #167).<br>
**Tester Name(s):** Walker Peters, Ji Heon Kim, Scott Kavalinas<br>
**Date(s) of Test:** March 25-28<br>
**File Used to Test:** Test_yfinance.py<br><br>

**TEST SCRIPT STEPS/RESULTS**
| Step | Test Step/Input                               | Expected Results                | Results                       |
|------|-----------------------------------------------|---------------------------------|-------------------------------|
| 1    | Navigate to the root directory and run Python | Python shell runs               | pass                          |
| 2.   | Instantiate a ticker with either "HTOO"       | ticker is created successfully  | pass                          |
| 3.   | Get the stock info by typing `ticker.info`    | program crashes due to KeyError | info work successfully (pass) |

**Alternative Flow 1: Test with BNKO**
| Step | Test Step/Input                               | Expected Results                | Results                       |
|------|-----------------------------------------------|---------------------------------|-------------------------------|
| 1    | Navigate to the root directory and run Python | Python shell runs               | pass                          |
| 2.   | Instantiate a ticker with either "BNKO"       | ticker is created successfully  | pass                          |
| 3.   | Get the stock info by typing `ticker.info`    | program crashes due to KeyError | info work successfully (pass) |

**Alternative Flow 2: Test with MSFT**
| Step | Test Step/Input                               | Expected Results                | Results                       |
|------|-----------------------------------------------|---------------------------------|-------------------------------|
| 1    | Navigate to the root directory and run Python | Python shell runs               | pass                          |
| 2.   | Instantiate a ticker with either "MSFT"       | ticker is created successfully  | pass                          |
| 3.   | Get the stock info by typing `ticker.info`    | program crashes due to KeyError | info work successfully (pass) |
