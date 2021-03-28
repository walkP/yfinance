## System Test Case
**yfinance**<br><br>
**USER STORY:** Getting info on stocks by calling Ticker.info

**Purpose:** Calling Ticker.info on certain stocks results in `KeyError: "['maxAge'] not found in axis"`. We want to investigate the cause of this problem and uncover any bugs.<br>
**Tester Name(s):** Walker Peters, Ji Heon Kim, Scott Kavalinas<br>
**Date(s) of Test:** March 25-28<br>
**File Used to Test:** Test_yfinance.py<br><br>

## Introduction
**Requirements:** Does not require specific software<br>
**Roles and Responsibilities:** Every tester members listed above, have tested on their machines to ensure that the test is executed appropriately<br>
**Procedures and Results**<br>
| Step | Test Step/Input                                             |
|------|-------------------------------------------------------------|
| 1    | Navigate to the root directory and run Python               |
| 2.   | Instantiate a ticker with either "HTOO", "MSFT", or "BNKO"  |
| 3.   | Get the stock info by typing `ticker.info'                  |

## Environmental Needs
**Procedural Requirements:** Before executing the test cases, must have the right files in the proper directories<br>

## Test
**Expected Results and Actual Results**<br>
| Expected Results                      | Results        |
|---------------------------------------|----------------|
| Python shell runs                     | pass           |
| ticker is created successfully        | pass           |
| ticker info is successfully displayed | pass           |
