############################################################
# Platform API Example Utility

import requests
import json
import credentials


baseUrl = 'https://api.gpsengine.net/v1'
apiKey = credentials.apiKey
accountId = credentials.accountId
deviceId = credentials.deviceId
authHeader = {'Authorization': 'JWT ' + apiKey}

############################################################
# Function:    DisplayJson
# Description: Display the string in JSONN pretty 
#              print style.
def DisplayJson(str):
    jsonString = json.loads(str)
    print json.dumps(jsonString, indent=4)


############################################################
# Function:    GetListOfAccountsDevices
# Description: 
def GetListOfAccountsDevices(fieldset='simple'):
    print "Get list of account's devices:"
    r = requests.get(baseUrl + '/account/' + accountId + '/device?fieldset=' + fieldset, headers=authHeader)
    print '> ' + r.url
    print '> ' + str(r)
    DisplayJson(r.text)


############################################################
# Function:    GetListOfAccountsNotifications
# Description: 
def GetListOfAccountsNotifications(fieldset='simple'):
    print "Get a list of account's notifications:"
    r = requests.get(baseUrl + '/account/' + accountId + '/notification', headers=authHeader)
    print '> ' + r.url
    print '> ' + str(r)
    DisplayJson(r.text)


############################################################
# Function:    GetListOfMapProviders
# Description: 
def GetListOfMapProviders():
    print 'Get list of map providers:'
    r = requests.get(baseUrl + '/account/' + accountId + '/mapproviders', headers=authHeader)
    print '> ' + r.url
    print '> ' + str(r)
    DisplayJson(r.text)


############################################################
# Function:    GetListOfUsersAssociatedWithAccount
# Description: 
def GetListOfUsersAssociatedWithAccount():
    print 'Get list of users associated with an account:'
    r = requests.get(baseUrl + '/account/' + accountId + '/user?fieldset=simple', headers=authHeader)
    print '> ' + r.url
    print '> ' + str(r)
    DisplayJson(r.text)


############################################################
# Function:    GetAccountAssets
# Description: 
def GetAccountAssets(fieldset='simple'):
    print "Get account assets:"
    r = requests.get(baseUrl + '/account/' + accountId + '/asset', headers=authHeader)
    print '> ' + r.url
    print '> ' + str(r)
    DisplayJson(r.text)
    

############################################################
# Function:    GetAccountInfo
# Description: 
def GetAccountInfo(fieldset='simple'):
    print "Get account info:"
    r = requests.get(baseUrl + '/account/' + accountId + '?fieldset=' + fieldset, headers=authHeader)
    print '> ' + r.url
    print '> ' + str(r)
    DisplayJson(r.text)
    

############################################################
# Function:    GetListOfDeviceNotifications
# Description: 
def GetListOfDeviceNotifications():
    print "Get a list of device notifications:"
    r = requests.get(baseUrl + '/device/' + deviceId + '/notification', headers=authHeader)
    print '> ' + r.url
    print '> ' + str(r)
    DisplayJson(r.text)
    

############################################################
# Function:    GetListOfSupportedDeviceVendorsAndModels
# Description: 
def GetListOfSupportedDeviceVendorsAndModels(fieldset='simple'):
    print "Get a list of supported device vendors and models:"
    r = requests.get(baseUrl + '/vendors' + '?fieldset=' + fieldset, headers=authHeader)
    print '> ' + r.url
    print '> ' + str(r)
    DisplayJson(r.text)
    

############################################################
# Function:    GetProvisioningState
# Description: 
def GetProvisioningState():
    print "Get provisioning state:"
    r = requests.get(baseUrl + '/device/' + deviceId + '/provision', headers=authHeader)
    print '> ' + r.url
    print '> ' + str(r)
    DisplayJson(r.text)


############################################################
# Function:    GetSentCommands
# Description: 
def GetSentCommands():
    print "Get sent commands:"
    r = requests.get(baseUrl + '/device/' + deviceId + '/command', headers=authHeader)
    print '> ' + r.url
    print '> ' + str(r)
    DisplayJson(r.text)
    
    
############################################################
# Function:    GetSentCommands
# Description: 
def ReadDeviceRecord():
    print "Read device record:"
    r = requests.get(baseUrl + '/device/' + deviceId, headers=authHeader)
    print '> ' + r.url
    print '> ' + str(r)
    DisplayJson(r.text)


############################################################
# Function:    RetrieveDataMessagesForTheDevice
# Description: 
def RetrieveDataMessagesForTheDevice(timeFrom, timeTo, fieldset='simple'):
    print "Retrieve data messages for the device:"
    r = requests.get(baseUrl + '/device/' + deviceId + '/samples?from=' + str(timeFrom) + '&to=' + str(timeTo) + '&fieldset=' + fieldset, headers=authHeader)
    print '> ' + r.url
    print '> ' + str(r)
    DisplayJson(r.text)


############################################################
# Function:    RetrieveLatestDataMessagesForTheDevice
# Description: 
def RetrieveLatestDataMessagesForTheDevice(fieldset='simple'):
    print "Retrieve latest data messages for the device:"
    r = requests.get(baseUrl + '/device/' + deviceId + '/samples/last?fieldset=' + fieldset, headers=authHeader)
    print '> ' + r.url
    print '> ' + str(r)
    DisplayJson(r.text)

class cPosition:
    longitude = 0
    latitude = 0



def GetLocation():
    print "Get location:"
    fieldset = 'simple'
    r = requests.get(baseUrl + '/device/' + deviceId + '/samples/last?fieldset=' + fieldset, headers=authHeader)
    jsonString = json.loads(r.text)
    print jsonString
    myPosition = cPosition()
    
    myPosition.longitude = jsonString['records'][0]['longitude']
    myPosition.latitude  = jsonString['records'][0]['latitude']
    return myPosition

    
############################################################
# Function:    RetrieveTimestampOfFirstReportedDataMessage
# Description: 
def RetrieveTimestampOfFirstReportedDataMessage():
    print "Retrieve timestamp of the first reported data message:"
    r = requests.get(baseUrl + '/device/' + deviceId + '/samples/firstdate', headers=authHeader)
    print '> ' + r.url
    print '> ' + str(r)
    DisplayJson(r.text)


############################################################
# Function:    ReverseGeocodeAddress
# Description: 
def ReverseGeocodeAddress(latitude, longitude, locale):
    print "Reverse geocode an address:"
    r = requests.get(baseUrl + '/reverse_geocode?lat=' + str(latitude) + '&long=' + str(longitude) + '&locale=' + str(locale), headers=authHeader)
    print '> ' + r.url
    print '> ' + str(r)
    DisplayJson(r.text)


############################################################
# Function:    GetListOfNotificationEvents
# Description: 
def GetListOfNotificationEvents():
    print "Get list of notification events:"
    r = requests.get(baseUrl + '/notification/event', headers=authHeader)
    print '> ' + r.url
    print '> ' + str(r)
    DisplayJson(r.text)


############################################################
#
def main():
    print 'My Tracker'

    # Accounts
    #GetListOfAccountsDevices('extended')
    #GetListOfAccountsNotifications()
    #GetListOfMapProviders()
    #GetListOfUsersAssociatedWithAccount()
    #GetAccountAssets()
    #GetAccountInfo()

    # Devices
    #GetListOfDeviceNotifications()
    #GetListOfSupportedDeviceVendorsAndModels()
    #GetProvisioningState()
    #GetSentCommands()
    #ReadDeviceRecord()
    #RetrieveDataMessagesForTheDevice('1510110935', '1510115935')
    ##RetrieveLatestDataMessagesForTheDevice('extended')
    #RetrieveTimestampOfFirstReportedDataMessage()

    position = cPosition() 

    position = GetLocation()
    print 'longitude = ' + str(position.longitude)
    print 'latitude = ' + str(position.latitude)

    # Geocoding
    ReverseGeocodeAddress(position.latitude, position.longitude, 'en')
    #ReverseGeocodeAddress(51.510357, -0.116773, 'en')

    # Notifications
    #GetListOfNotificationEvents()

    


if __name__ == '__main__':
	main()






