import yfinance as yf

symbols = ['MSFT', 'IWO', 'VFINX', '^GSPC', 'BTC-USD']
tickers = [yf.Ticker(symbol) for symbol in symbols]

class TestTicker:
    def test_info_history(self):
        for ticker in tickers:
            # always should have info and history for valid symbols
            assert(ticker.info is not None and ticker.info != {})
            assert(ticker.history(period="max").empty is False)

    def test_attributes(self):
        for ticker in tickers:
            # following should always gracefully handled, no crashes
            ticker.cashflow
            ticker.balance_sheet
            ticker.financials
            ticker.sustainability
            ticker.major_holders
            ticker.institutional_holders
            ticker.mutualfund_holders

    def test_holders(self):
        for ticker in tickers:
            assert(ticker.info is not None and ticker.info != {})
            assert(ticker.major_holders is not None)
            assert(ticker.institutional_holders is not None)


msft = yf.Ticker("MSFT")

# get stock info
msft.info
#print(msft.info)

# get historical market data
hist = msft.history(period="max")


# show actions (dividends, splits)
msft.actions

# show dividends
msft.dividends

# show splits
msft.splits

# show financials
msft.financials
msft.quarterly_financials
# show major holders
msft.major_holders
# show institutional holders
msft.institutional_holders
# show balance sheet
msft.balance_sheet
msft.quarterly_balance_sheet
# show cashflow
msft.cashflow
msft.quarterly_cashflow
print(msft.quarterly_cashflow)
# show earnings
msft.earnings
msft.quarterly_earnings
# show sustainability
msft.sustainability
# show analysts recommendations
msft.recommendations
# show next event (earnings, etc)
msft.calendar
# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
msft.isin
# show options expirations
msft.options

# get option chain for specific expiration
#opt = msft.option_chain('YYYY-MM-DD')
# data available via: opt.calls, opt.puts