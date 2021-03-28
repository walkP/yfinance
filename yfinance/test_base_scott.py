import unittest
import base
import utils
import yfinance as yf

testNULL = False

finList=['MSFT', 'IWO', 'VFINX', '^GSPC', 'BTC-USD',"ENE"]
tick = yf.Ticker(finList[0])

if testNULL:
    testFinancials = {
        "yearly": tick.cashflow,
        "quarterly": utils.empty_df()}
    testBalancesheet = {
        "yearly": utils.empty_df(),
        "quarterly": utils.empty_df()}
    testCashflow = {
        "yearly": utils.empty_df(),
        "quarterly": utils.empty_df()}

else:
    testFinancials = {
        "yearly": tick.financials,
        "quarterly": tick.quarterly_financials}
    testBalancesheet = {
        "yearly": tick.balance_sheet,
        "quarterly": tick.balance_sheet}
    testCashflow = {
        "yearly": tick.cashflow,
        "quarterly": tick.quarterly_cashflow}


class TestGenericPatterns(unittest.TestCase):


       
    # testing if data is a dict type
    def test_is_dict(self):
        finList=['MSFT', 'IWO', 'VFINX', '^GSPC', 'BTC-USD',"ENE"]
        self.stock = base.TickerBase('MSFT')
        empty_dict = dict()
        data = self.stock.generic_patterns(dict())
        self.assertTrue(isinstance(data, dict))
        self.hist = self.stock.history(period="max")
       
    # testing if loop is being handled properly
    def test_loop(self):
        
        data = {}
        alist = []
        _financials =testFinancials
        _balancesheet = testBalancesheet
        _cashflow =testCashflow
        for key in (
            (_cashflow, 'cashflowStatement', 'cashflowStatements'),
            (_balancesheet, 'balanceSheet', 'balanceSheetStatements'),
            (_financials, 'incomeStatement', 'incomeStatementHistory')
        ):
            item = key[1] + 'History'
            alist.append(item)
        for i in range(len(alist)):
            if i == 0:
                self.assertTrue(alist[i] == "cashflowStatementHistory")
            elif i == 1:
                self.assertTrue(alist[i] == "balanceSheetHistory")
            elif i == 2:
                self.assertTrue(alist[i] == "incomeStatementHistory")

    # testing if item doesn't exist in the data dictionary
    def test_switch_statement(self):
        data = {}
        msg = ""
        _financials =testFinancials
        _balancesheet = testBalancesheet
        _cashflow =testCashflow
        for key in (
            (_cashflow, 'cashflowStatement', 'cashflowStatements'),
            (_balancesheet, 'balanceSheet', 'balanceSheetStatements'),
            (_financials, 'incomeStatement', 'incomeStatementHistory')
        ):
            item = key[1] + 'History'
            if isinstance(data.get(item), dict):
                try:
                    msg += base.cleanup('yearly')
                except Exception as e:
                    pass

            item = key[1]+'HistoryQuarterly'
            if isinstance(data.get(item), dict):
                try:
                    msg += base.cleanup('quarterly')
                except Exception as e:
                    pass

        if (not isinstance(data.get(item), dict)):
            msg += "Empty DataFrame"
        self.assertTrue(msg == "Empty DataFrame")

if __name__ == "__main__":
    unittest.main() 