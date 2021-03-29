## TEST CASE REPORT
**PROJECT: yfinance**<br>
March 28, 2021<br>

### General Information
**Test Stage:** Unit<br>
**Test Date:** 03/28/21<br>
**Tester:** Walker Peters, Ji Heon Kim, Scott Kavalinas<br>
**Test Case Number:** [test_case4](../test_cases/test_case4.md)<br>
**Test Case Description:** Test if yf.Ticker("SFL").info has a key and value for"shortName"<br>
**Result:** Pass<br>

### Introduction
**Requirements:** Does not require specific software<br>
**Roles and Responsibilities:** Every tester members listed above, have tested on their machines to ensure that the test is executed appropriately<br>
**Procedures and Results**<br>
| Step | Test Step/Input                                             |
|------|-------------------------------------------------------------|
| 1    | Navigate to the root directory and run Python               |
| 2.   | Instantiate a ticker with "SFL"                             |
| 3.   | Get info on ticker.info to test if value exists             |

### Environmental Needs
**Procedural Requirements:** Before executing the test cases, must have the right files in the proper directories<br>

### Test
**Expected Results and Actual Results**<br>
| Expected Results                      | Results        |
|---------------------------------------|----------------|
| Python shell runs                     | pass           |
| ticker is created successfully        | pass           |
| ticker type is successfully tested    | pass           |
