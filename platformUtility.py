
# Platform Connect API Example

import requests
import json
import credentials

print "Platform Connect API"

baseUrl = 'https://api.gpsengine.net/v1'
apiKey = credentials.apiKey
accountId = credentials.accountId
authHeader = {'Authorization': 'JWT ' + apiKey}

##################################################
# Function:    DisplayJson
# Description: Display the string in JSONN pretty 
#              print style.
def DisplayJson(str):
    jsonString = json.loads(str)
    print json.dumps(jsonString, indent=4)


##################################################
# Function:    GetListOfAccountsDevices
# Description: 
def GetListOfAccountsDevices(fieldset='simple'):
    print "Get list of account's devices:"
    r = requests.get(baseUrl + '/account/' + accountId + '/device?fieldset=' + fieldset, headers=authHeader)
    print '> ' + r.url
    print '> ' + str(r)
    DisplayJson(r.text)


##################################################
# Function:    GetListOfAccountsNotifications
# Description: 
def GetListOfAccountsNotifications(fieldset='simple'):
    print "Get a list of account's notifications:"
    r = requests.get(baseUrl + '/account/' + accountId + '/notification', headers=authHeader)
    print '> ' + r.url
    print '> ' + str(r)
    DisplayJson(r.text)


##################################################
# Function:    GetListOfMapProviders
# Description: 
def GetListOfMapProviders():
    print 'Get list of map providers:'
    r = requests.get(baseUrl + '/account/' + accountId + '/mapproviders', headers=authHeader)
    print '> ' + r.url
    print '> ' + str(r)
    DisplayJson(r.text)


##################################################
# Function:    GetListOfUsersAssociatedWithAccount
# Description: 
def GetListOfUsersAssociatedWithAccount():
    print 'Get list of users associated with an account:'
    r = requests.get(baseUrl + '/account/' + accountId + '/user?fieldset=simple', headers=authHeader)
    print '> ' + r.url
    print '> ' + str(r)
    DisplayJson(r.text)


##################################################
# Function:    GetAccountAssets
# Description: 
def GetAccountAssets(fieldset='simple'):
    print "Get account assets::"
    r = requests.get(baseUrl + '/account/' + accountId + '/asset', headers=authHeader)
    print '> ' + r.url
    print '> ' + str(r)
    DisplayJson(r.text)
    

##################################################
#
def main():
    print 'Platform Utility'
    
    GetListOfAccountsDevices('extended')
    GetListOfAccountsNotifications()
    GetListOfMapProviders()
    GetListOfUsersAssociatedWithAccount()
    GetAccountAssets()




if __name__ == '__main__':
	main()





