## TEST CASE REPORT
**PROJECT: yfinance**<br>
March 28, 2021<br>

### General Information
**Test Stage:** Unit<br>
**Test Date:** 03/28/21<br>
**Tester:** Walker Peters, Ji Heon Kim, Scott Kavalinas<br>
**Test Case Number:** test_case5<br>
**Test Case Description:** Testing the functionality related to empty stock dataframes. User should be notified of an error rather than receiving empty data.<br>
**Result:** Fail<br>

### Introduction
**Requirements:** Does not require specific software<br>
**Roles and Responsibilities:** Every tester members listed above, have tested on their machines to ensure that the test is executed appropriately<br>
**Procedures and Results**<br>
| Step | Test Step/Input                                                      |
|------|----------------------------------------------------------------------|
| 1    | Navigate to the root directory and run python yfinance/emptyTest.py  |
| 2.   | allow code to run for 2 tickers "MSFT" and 'ENE'(delisted)           |


### Environmental Needs
**Procedural Requirements:** Before executing the test cases, must have the right files in the proper directories<br>

### Test
**Expected Results and Actual Results**<br>
| Expected Results                                          | Results        |
|-----------------------------------------------------------|----------------|
| Python shell runs                                         | pass           |
| allow code to run for 2 tickers "MSFT" and 'ENE'(delisted)| fail           |

