import unittest
import base
import utils


finList=['MSFT',  'ENE']

# stocks that are currently listed return empty containers rather than a message to the user.


class TestGenericPatterns(unittest.TestCase):
            
      
            #msg += "Empty DataFrame"
            #self.assertTrue(msg == "Empty DataFrame")
    # testing if for non empty financial records

    def test_empty(self):
        for i in finList:
            self.stock = base.TickerBase(i)        
            data = {}
            alist = []
            _financials = {
                "yearly": self.stock.get_financials(),
                "quarterly": self.stock.get_financials(freq='quarterly')}
            self.assertTrue(_financials['yearly'].empty ==False or  _financials['quarterly'].empty == False,"Cannot have empty financial statements")
            _balancesheet = {
                "yearly": self.stock.get_balance_sheet(),
                "quarterly": self.stock.get_balance_sheet(freq='quarterly')}
            self.assertTrue(_balancesheet['yearly'].empty ==False or  _balancesheet['quarterly'].empty == False,"Cannot have empty financial statements")
            
            _cashflow = {
                "yearly": self.stock.get_cashflow(),
                "quarterly": self.stock.get_cashflow(freq='quarterly')}

            self.assertTrue(_cashflow['yearly'].empty ==False or  _cashflow['quarterly'].empty == False,"Cannot have empty financial statements")
            


if __name__ == "__main__":

    unittest.main() 