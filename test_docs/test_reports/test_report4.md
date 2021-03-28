## System Test Case
**yfinance**<br><br>
**USER STORY:** Getting info on whether yf.Ticker("SFL") has info on "shortName"

**Purpose:** Calling yf.Ticker("SFL") to test if yf.Ticker("SFL").info has a key "shortName" and a value for it `Error when using ticker.info`. We want to investigate the cause of this problem and uncover any bugs.<br>
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
| 2.   | Instantiate a ticker with "MSFT"                            |
| 3.   | Get info on ticker.info to test if value exists             |

## Environmental Needs
**Procedural Requirements:** Before executing the test cases, must have the right files in the proper directories<br>

## Test
**Expected Results and Actual Results**<br>
| Expected Results                      | Results        |
|---------------------------------------|----------------|
| Python shell runs                     | pass           |
| ticker is created successfully        | pass           |
| ticker type is successfully tested    | pass           |
