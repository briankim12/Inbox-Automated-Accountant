import requests
import config

# curl -H "Authorization: Bearer <ACCESS_TOKEN>" https://api.youneedabudget.com/v1/budgets
# -H "Authorization: Bearer <ACCESS_TOKEN>"     -> This is the header for the Request sent to https://api.youneedabudget.com/v1/budgets


# Header -> Dictionary containing Authorization header.
headers = config.ynab['header']

# Obtain this info -> API endpoint is "https://api.youneedabudget.com/v1/budgets"
myBudgetID = config.ynab['BudgetID']


# Check Status Code of Response
def checkStatus(response):
    status_code = response.status_code
    return status_code


# returns dict (key: accountID, value: accountInfo)
def requestAllAccountData():
    accountListEndPoint = f"https://api.youneedabudget.com/v1/budgets/{myBudgetID}/accounts"
    response = requests.get(accountListEndPoint, headers=headers)

    # Check for Errors
    if checkStatus(response) != 200:
        return checkStatus(response)

    # Print the response.content (bytes) as JSON Object
    jsonResponse = response.json()

    # Access Data Inside YNAB (Parsing)
    return jsonResponse['data']['accounts']


# Returns Dict (key: account name, value: account balance)
def getAccountBalances():
    accountDict = {}
    accounts = requestAllAccountData()
    for account in accounts:
        accountDict[account['name']] = account['balance'] / 1000

    return accountDict


# Returns Dict( key: accountName, value: accountID)
def getAccountIDs():
    accountDict = {}
    accounts = requestAllAccountData()
    for account in accounts:
        accountDict[account['name']] = account['id']

    return accountDict


# Request Specific Account Info
def requestAccountData(accountID):
    accountEndPoint = f"https://api.youneedabudget.com/v1/budgets/{myBudgetID}/accounts/{accountID}"
    response = requests.get(accountEndPoint, headers=headers)

    # Check for Errors
    if checkStatus(response) != 200:
        return checkStatus(response)

    # Print the response.content (bytes) as JSON Object
    jsonResponse = response.json()

    # #Access Data Inside YNAB (Parsing)
    return jsonResponse['data']['account']


# Return's accountID's balance
def getAccountBalance(accountID):
    accountData = requestAccountData(accountID)
    return accountData['balance'] / 1000, "${:,.2f}".format(accountData['balance'] / 1000)


def getCategoryIDs():
    categoryDict = {}
    categoriesEndPoint = f"https://api.youneedabudget.com/v1/budgets/{myBudgetID}/categories"
    categoriesResponse = requests.get(categoriesEndPoint, headers=headers)

    # Check For Errors
    if checkStatus(categoriesResponse) != 200:
        return checkStatus(categoriesResponse)

    categoryGroups = categoriesResponse.json()['data']['category_groups']

    for categoryGroup in categoryGroups:
        for category in categoryGroup['categories']:
            categoryDict[category['name']] = category['id']

    return categoryDict


# category names will be transformed to allow it to be used as jinja tags for YNAB Template
def getCategoryBalances():
    categoryDict = {}
    categoriesEndPoint = f"https://api.youneedabudget.com/v1/budgets/{myBudgetID}/categories"
    categoriesResponse = requests.get(categoriesEndPoint, headers=headers)

    # Check For Errors
    if checkStatus(categoriesResponse) != 200:
        return checkStatus(categoriesResponse)

    categoryGroups = categoriesResponse.json()['data']['category_groups']

    for categoryGroup in categoryGroups:
        for category in categoryGroup['categories']:
            # Convert category name imported from YNAB suitable to jinja tags used in Template
            jinjaNameParts = category['name'].split('(')[0].split(' ')
            jinjaName = ""
            for jinjaNamePart in jinjaNameParts:
                jinjaName += jinjaNamePart

            categoryDict[jinjaName] = category['balance'] / 1000

    return categoryDict

def getCategoryActivities():
    categoryDict = {}
    categoriesEndPoint = f"https://api.youneedabudget.com/v1/budgets/{myBudgetID}/categories"
    categoriesResponse = requests.get(categoriesEndPoint, headers=headers)

    # Check For Errors
    if checkStatus(categoriesResponse) != 200:
        return checkStatus(categoriesResponse)

    categoryGroups = categoriesResponse.json()['data']['category_groups']

    for categoryGroup in categoryGroups:
        for category in categoryGroup['categories']:
            # Convert category name imported from YNAB suitable to jinja tags used in Template
            jinjaNameParts = category['name'].split('(')[0].split(' ')
            jinjaName = ""
            for jinjaNamePart in jinjaNameParts:
                jinjaName += jinjaNamePart

            categoryDict[jinjaName] = category['activity'] / 1000

    return categoryDict

def requestCategoryData(categoryID):
    # Return Dictionary of the Selected Category
    categoryEndPoint = f"https://api.youneedabudget.com/v1/budgets/{myBudgetID}/categories/{categoryID}"
    categoryResponse = requests.get(categoryEndPoint, headers=headers)

    # Check For Errors
    if checkStatus(categoryResponse) != 200:
        return checkStatus(categoryResponse)

    return categoryResponse.json()['data']['category']


def getCategoryBalance(categoryID):
    categoryData = requestCategoryData(categoryID)
    return categoryData['balance'] / 1000, "${:,.2f}".format(categoryData['balance'] / 1000)
