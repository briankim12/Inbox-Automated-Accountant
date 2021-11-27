from requestEndPoint import *
import modifyWord
import rhAPI
import gmail
import config

# Make this more modular in the future

# Get all Account + Category Balances from YNAB
# Names have been reconfigured to match Jinja Tag in YNAB
accountBalances = getAccountBalances()
categoryBalances = getCategoryBalances()

allBalances = {}
allBalances.update(categoryBalances)
allBalances.update(accountBalances)

# Jinja Tag for Robinhood + additional calculations
allBalances['RH'] = rhAPI.getPortfolioEquity()
allBalances['totalCash'] = allBalances['Checking'] + allBalances['Savings'] + allBalances['Paypal'] + allBalances[
    'Cash']
allBalances['totalInvestment'] = allBalances['RH'] + allBalances['Webull'] + allBalances['KatieWebull']
allBalances['assets'] = allBalances['totalCash'] + allBalances['totalInvestment']

allBalances['totalMama'] = -allBalances["MamaQueenSavings"] - allBalances["MamaQueen"]
allBalances['liabilities'] = allBalances['Freedom'] + allBalances['Sapphire'] + allBalances['totalMama']

allBalances['nw'] = allBalances["assets"] + allBalances["liabilities"]

allBalances['inflow'] = allBalances['Income'] + allBalances['Other']
allBalances['outflow'] = allBalances['Bills'] + allBalances['PersonalCare'] + allBalances['Recreation'] + allBalances[
    'DiningOut'] + allBalances['OtherExpense']
allBalances['netCashFlow'] = allBalances['inflow'] - allBalances['outflow']
allBalances['capitalGain'] = 0


# Convert Balance to Currency Format
for item in allBalances.items():
    if item[1] >= 0:
        allBalances[item[0]] = '${:,.2f}'.format(item[1])
    else:
        allBalances[item[0]] = '-${:,.2f}'.format(-item[1])


# Get Current Month Year
from datetime import date

todays_date = date.today()
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
currMonth = months[todays_date.month - 1]
currYear = todays_date.year
currDate = todays_date

#Set Jinja tag for date
allBalances['mnth'] = currMonth
allBalances['yr'] = currYear
allBalances['date'] = currDate

# YNAB Practices:
# Don't have same name from account and category
# For the Jinja Tags in Word Template use same category/account names listed in YNAB
modifyWord.createStatement("ynabTemplate.docx", allBalances, allBalances['mnth'], allBalances['yr'])
gmail.sendEmail(config.gmail['fromAddr'], config.gmail['toAddr'], config.gmail['password'], f'Automized Accountant: {currMonth} {currYear} Statement', "Work Hard", ['/Users/briankim/Documents/YNAB_API/November2021YNAB.docx'])


