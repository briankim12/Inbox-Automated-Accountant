import os
import sys
CWD = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(CWD, "venv/lib/python3.7/site-packages"))


import pyotp
import robin_stocks.robinhood as rs
import config

totp = pyotp.TOTP("OXUJ47CLO7XLLI67").now()
rs.login(username=config.robinhood['username'],
         password=config.robinhood['password'], mfa_code=totp)

def getPortfolioEquity():
    netWorth = float(rs.load_portfolio_profile()['equity'])
    return netWorth


