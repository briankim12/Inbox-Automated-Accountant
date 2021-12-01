import ynab
import modifyWord
import rhAPI
import gmail
import config
import json


def lambda_handler(event=None, context=None):
    # ETL trade data from Robinhood’s API to YNAB for downstream consumption
    # print( ynab.getAccountIDs()["Robinhood"])
    # transaction = {
    #     "transaction": {
    #         "account_id": "26ecaa4a-35bb-4230-9f26-4936d16cdc63",
    #         "date": "2021-11-30",
    #         "amount": -100000,
    #         "payee_id": "57974cd1-e3b2-4650-ae74-043be2c76c1d",
    #         "payee_name": "Gain/Loss",
    #         "category_id": None,
    #         "memo": "November",
    #         "cleared": "cleared",
    #         "approved": True,
    #         "flag_color": None,
    #         "import_id": None,
    #         "subtransactions": []
    #     },
    #     "transactions": []
    # }
    # print(ynab.addTransaction(transaction))


    # Get all Account + Category Balances from YNAB
    # Names have been reconfigured to match Jinja Tag in YNAB
    accountBalances = ynab.getAccountBalances()
    categoryBalances = ynab.getCategoryActivities()

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
    allBalances['outflow'] = allBalances['Bills'] + allBalances['PersonalCare'] + allBalances['Recreation'] + \
                             allBalances[
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
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    currMonth = months[todays_date.month - 1]
    currYear = todays_date.year
    currDate = todays_date

    # Set Jinja tag for date
    allBalances['mnth'] = currMonth
    allBalances['yr'] = currYear
    allBalances['date'] = currDate

    # YNAB Practices:
    # Don't have same name from account and category
    # For the Jinja Tags in Word Template use same category/account names listed in YNAB
    filename = modifyWord.createStatement("ynabTemplate.docx", allBalances, allBalances['mnth'], allBalances['yr'])
    gmail.sendEmail(config.gmail['fromAddr'], config.gmail['toAddr'], config.gmail['password'],
                    f'Automized Accountant: {currMonth} {currYear} Statement', "Work Hard", [filename])

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


lambda_handler()
