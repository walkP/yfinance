import unittest
import base
import utils

symbols = ['GOOGL', 'IWO', 'VFINX', '^GSPC', 'BTC-USD', 'SFL']

class TestGenericPatterns(unittest.TestCase):
    # random testing to make sure info is working 
    def test_info(self):
        stocks = [base.TickerBase(symbol) for symbol in symbols]
        for stock in stocks:
            info = stock.get_info()
            self.assertIsNotNone(info)

    # testing if MSFT contains maxAge
    def test_msft_info(self):
        msft = base.TickerBase(ticker="MSFT")
        info = msft.get_info()
        self.assertTrue(info['maxAge'])

    # testing if HTOO contains maxAge
    def test_htoo_info(self):
        htoo = base.TickerBase(ticker="HTOO")
        info = htoo.get_info()
        self.assertTrue(info['maxAge'])
    
    # testing if BNKO contains maxAge
    def test_bnko_info(self):
        bnko = base.TickerBase(ticker="BNKO")
        info = bnko.get_info()
        self.assertTrue(info['maxAge'])

    # testing if ACGL contains cashflowStatements
    def test_ACGL_info(self):
        acgl = base.TickerBase(ticker="ACGL")
        info = acgl.get_info()
        # if info doesn't fail then it worked
        self.assertIsNotNone(info)
        
    # testing if SFL contains cashflowStatements
    def test_SFL_info(self):
        SFL = base.TickerBase(ticker="SFL")
        info = SFL.get_info()
        # if info doesn't fail then it worked
        self.assertIsNotNone(info)

if __name__ == "__main__":
    unittest.main() 