import unittest
import base
import utils
import yfinance as yf



finList=['MSFT', 'shgsajnszxjmsrkjsrk','msft', 'ENE', 'AAPL', 'BTC-USD','AC']
#list contains stocks that are currently listed, companies that do not exist,TSX Stocks,
# ***'shgsajnszxjmsrkjsrk' does not cause an error, stocks like this that do not exist or
# are not currently listed return empty containers rather than a message to the user.


class TestGenericPatterns(unittest.TestCase):

    # testing if data is a dict type
    def test_is_dict(self):
        for i in finList:
            self.stock = base.TickerBase(i)
            print("Test: Dictionary type\n "+ "Stock: "+i)
            empty_dict = dict()
            data = self.stock.generic_patterns(dict())
            self.assertTrue(isinstance(data, dict))
            
       
    # testing if loop is being handled properly
    def test_loop(self):
        for i in finList:
            self.stock = base.TickerBase(i)
            print("Test: Loop\n "+ "Stock: "+i)        
            data = {}
            alist = []
            _financials = {
                "yearly": self.stock.get_financials(),
                "quarterly": self.stock.get_financials(freq='quarterly')}
            print(_financials)
            _balancesheet = {
                "yearly": self.stock.get_balance_sheet(),
                "quarterly": self.stock.get_balance_sheet(freq='quarterly')}
            print(_balancesheet)
            _cashflow = {
                "yearly": self.stock.get_cashflow(),
                "quarterly": self.stock.get_cashflow(freq='quarterly')}
            print(_cashflow)
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

        for i in finList:
            self.stock = base.TickerBase(i)
            print("Test: test_switch_statement\n "+ "Stock: "+i) 
            data = {}
            msg = ""
            _financials = {
                "yearly": self.stock.get_financials(),
                "quarterly": self.stock.get_financials(freq='quarterly')}
            _balancesheet = {
                "yearly": self.stock.get_balance_sheet(),
                "quarterly": self.stock.get_balance_sheet(freq='quarterly')}
            _cashflow = {
                "yearly": self.stock.get_cashflow(),
                "quarterly": self.stock.get_cashflow(freq='quarterly')}
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