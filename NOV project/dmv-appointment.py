import json
import time

# Michael Muniz DMV appointment scheduling application
# opens the customer data json file and then parses it
customerFileObject = open('../novProject/data-set/CustomerData.json')
customerDataJSON = customerFileObject.read()

customerData = json.loads(customerDataJSON)

# opens the teller data json and then parses it
tellerFileObject = open('../novProject/data-set/TellerData.json')
tellerDataJSON = tellerFileObject.read()

tellerData = json.loads(tellerDataJSON)

# function to identify the teller


def identifyTeller(tellerId):
    for teller in tellerData["Teller"]:
        if (teller['ID'] == tellerId):
            print('Teller Found', teller)

# function to assign customer to teller


def assignCustomer():
    # loops through all the customers in the data set
    for customer in customerData['Customer']:
        # checks if customer is currently assigned or has been seen and skips them
        if (customer['seen'] == True | customer['assigned'] == True):
            continue

        # checks if customer hasn't been serviced and assigns them to a teller
        if (customer['seen'] == False & customer['assigned'] == False):

            # loops through the tellers, find the first available one, assigns them a customer
            for teller in tellerData["Teller"]:
                if teller['available'] == True:
                    teller['available'] = False

                    # assigns the customer to a teller
                    teller['customerId'] = customer['Id']
                    customer['assigned'] = True

                    # checks if the specialty of the teller matches the customer
                    if (customer['type'] == teller['SpecialtyType']):
                        time.sleep(int(customer['duration'])
                                   * teller['SpecialtyType'])
                    else:
                        time.sleep(int(customer['duration']))

                    # frees up the teller and makes the customer ineligible to be seen again
                    teller['available'] = True
                    customer['seen'] = True
                    customer['assigned'] = False
                    break
        break


if __name__ == '__main__':

    # loop through the list of tellers and adds bool 'available' property to it
    # also adds customerId as the customer currently being serviced
    for teller in tellerData['Teller']:
        teller['available'] = True
        teller['customerId'] = 0

    # loop through the list of customers and adds bool 'assigned' property to let us know customers is assigned
    # also adds 'seen' property to customer so we don't assign them more than once
    for customer in customerData['Customer']:
        customer['assigned'] = False
        customer['seen'] = False

    assignCustomer()
