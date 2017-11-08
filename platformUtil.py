
# Platform Connect API Example

import requests
import json
import credentials

print "Platform Connect API"

baseUrl = 'https://api.gpsengine.net/v1'
apiKey = credentials.apiKey
accountId = credentials.accountId

##################################################
# Function:    DisplayJson
# Description: Display the string in JSONN pretty 
#              print style.
def DisplayJson(str):
    jsonString = json.loads(str)
    print json.dumps(jsonString, indent=4)


##################################################
# Function:    GetListOfMapProviders
# Description: 
def GetListOfMapProviders():
    print 'Get list of map providers:'
    r = requests.get(baseUrl + '/account/' + accountId + '/mapproviders', headers={'Authorization': 'JWT ' + apiKey})
    print '> ' + r.url
    print '> ' + str(r)
    DisplayJson(r.text)

##################################################
# Function:    GetListOfAccountsDevices
# Description: 
def GetListOfAccountsDevices(fieldset='simple'):
    print "Get list of account's devices:"
    r = requests.get(baseUrl + '/account/' + accountId + '/device?fieldset=' + fieldset, headers={'Authorization': 'JWT ' + apiKey})
    print '> ' + r.url
    print '> ' + str(r)
    DisplayJson(r.text)

##################################################
# Function:    GetListOfUsersAssociatedWithAccount
# Description: 
def GetListOfUsersAssociatedWithAccount():
    print 'Get list of users associated with an account:'
    r = requests.get(baseUrl + '/account/' + accountId + '/user?fieldset=simple', headers={'Authorization': 'JWT ' + apiKey})
    print '> ' + r.url
    print '> ' + str(r)
    DisplayJson(r.text)
    

##################################################
#
def main():
    GetListOfAccountsDevices('extended')
    GetListOfMapProviders()
    GetListOfUsersAssociatedWithAccount()




if __name__ == '__main__':
	main()





