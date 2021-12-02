import ynab
import modifyWord
import rhAPI
import gmail
import config
import json
from datetime import date


# Update Robinhood's Equity to YNAB's Equity, return equity gain/loss
def etlRobinhoodToYnab():
    robinhoodID = ynab.getAccountIDs()["Robinhood"]
    newEquity = rhAPI.getPortfolioEquity()
    oldEquity = ynab.getAccountBalance(robinhoodID)
    equityDiff = newEquity - oldEquity

    todays_date = date.today()
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    strDate = str(todays_date)

    ynab.updateRobinhoodAccount(robinhoodID, strDate, equityDiff, months[todays_date.month - 1])
    return equityDiff


def jinjaTagCategoryAndAccountBalances(allBalances):
    accountBalances = ynab.getAccountBalances()
    categoryBalances = ynab.getCategoryActivities()
    allBalances.update(categoryBalances)
    allBalances.update(accountBalances)
    return allBalances


def jinjaTagNewCalculations(allBalances):
    allBalances['totalCash'] = allBalances['Checking'] + allBalances['Savings'] + allBalances['Paypal'] + allBalances[
        'Cash']
    allBalances['totalInvestment'] = allBalances['Robinhood'] + allBalances['Webull'] + allBalances['KatieWebull']
    allBalances['assets'] = allBalances['totalCash'] + allBalances['totalInvestment']

    allBalances['totalMama'] = -allBalances["MamaQueenSavings"] - allBalances["MamaQueen"]
    allBalances['liabilities'] = allBalances['Freedom'] + allBalances['Sapphire'] + allBalances['totalMama']

    allBalances['nw'] = allBalances["assets"] + allBalances["liabilities"]

    allBalances['inflow'] = allBalances['Income'] + allBalances['Other']
    allBalances['outflow'] = allBalances['Bills'] + allBalances['PersonalCare'] + allBalances['Recreation'] + \
                             allBalances[
                                 'DiningOut'] + allBalances['OtherExpense']
    allBalances['netCashFlow'] = allBalances['inflow'] - allBalances['outflow']
    allBalances['capitalGain'] = 0


def convertBalanceToCurrencyFormat(tagToBalancesDict):
    for item in tagToBalancesDict.items():
        if item[1] >= 0:
            tagToBalancesDict[item[0]] = '${:,.2f}'.format(item[1])
        else:
            tagToBalancesDict[item[0]] = '-${:,.2f}'.format(-item[1])


def jinjaTagDate(jinjaTagDict):
    # Get Current Month Year
    todays_date = date.today()
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    currMonth = months[todays_date.month - 1]
    currYear = todays_date.year
    currDate = todays_date

    # Set Jinja tag for date
    jinjaTagDict['mnth'] = currMonth
    jinjaTagDict['yr'] = currYear
    jinjaTagDict['date'] = currDate


def lambda_handler(event=None, context=None):
    jinjaTagDict = dict()

    # ETL trade data from Robinhood’s API to YNAB for downstream consumption + update jinjaTag
    jinjaTagDict['capitalGain'] = etlRobinhoodToYnab()

    # Get all Account + Category Balances from YNAB
    # AccountName have been reconfigured to match Jinja Tag in YNAB
    jinjaTagCategoryAndAccountBalances(jinjaTagDict)

    # Jinja Tag for Robinhood + additional calculations
    jinjaTagNewCalculations(jinjaTagDict)

    # Convert Balance to Currency Format in tagToBalanceDict
    convertBalanceToCurrencyFormat(jinjaTagDict)

    jinjaTagDate(jinjaTagDict)

    # YNAB Practices: Don't have same name from account and category
    # For the Jinja Tags in Word Template use same category/account names listed in YNAB
    filename = modifyWord.createStatement("ynabTemplate.docx", jinjaTagDict, jinjaTagDict['mnth'], jinjaTagDict['yr'])

    gmail.sendEmail(config.gmail['fromAddr'], config.gmail['toAddr'], config.gmail['password'],
                    f'Automized Accountant: {jinjaTagDict["mnth"]} {jinjaTagDict["yr"]} Statement', "Work Hard",
                    [filename])

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


if __name__ == "__main__":
    lambda_handler()
