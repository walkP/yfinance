## TEST CASE REPORT
**PROJECT: yfinance**<br>
March 28, 2021<br>

### General Information
**Test Stage:** Unit<br>
**Test Date:** 03/28/21<br>
**Tester:** Walker Peters, Ji Heon Kim, Scott Kavalinas<br>
**Test Case Number:** [test_case1](../test_cases/test_case1.md)<br>
**Test Case Description:** Ensuring that the cleanup function doesn't fail when calling Ticker.info on certain stocks<br>
**Result:** Pass<br>

### Introduction
**Requirements:** Does not require specific software<br>
**Roles and Responsibilities:** Every tester members listed above, have tested on their machines to ensure that the test is executed appropriately<br>
**Procedures and Results**<br>
| Step | Test Step/Input                                             |
|------|-------------------------------------------------------------|
| 1    | Navigate to the root directory and run Python               |
| 2.   | Instantiate a ticker with either  "HTOO", "BNKO", or "MSFT" |
| 3.   | Get the stock info by typing `ticker.info'`                 |

### Environmental Needs
**Procedural Requirements:** Before executing the test cases, must have the right files in the proper directories<br>

### Test
**Expected Results and Actual Results**<br>
| Expected Results                      | Results        |
|---------------------------------------|----------------|
| Python shell runs                     | pass           |
| ticker is created successfully        | pass           |
| program crashes due to KeyError       | pass           |
