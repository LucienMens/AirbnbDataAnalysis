'''
Data Visualization Practice Project
Created by @LucienMens
This project is a refinement of a final exam I had for a programming class.

The program takes in airbnb csv files and processes the hosting info, room info,
the price, and the types of rooms.

I am experimenting with pandas for processing the data and matlab plotting
for displaying the data. Currently, the displays are not interactive, but I
would like to add that in eventually.
'''
import statistics
import pandas as pd
import matplotlib.pyplot as plt

#this reads the file and puts it into a dataset
x = input("Enter a file name: ")
dataset = pd.read_csv(x)
def dataCreate(x):
#used for verification to make sure there are enough rows & columns
    y = dataset.shape
    print(y)
def listingsInfo(x):
    multi =  dataset['host_id'].value_counts()
    #this gives you the total number of hostids
    print("Total number of listings is:",len(multi))
    print("Maximum number of listings per hosts:", max(multi))
    return multi
#Percentage of hosts that have more than one listing
def multiHosts(x):
    v = dataset['host_id'].value_counts()
    atwo = dataset[dataset['host_id'].isin(v.index[v.gt(2)])]
#percentage of hosts
    perhos = int(((round((len(atwo) / len(v)), 2))*100))
    print("The percentage of hosts with more than one listing is",
      perhos,"percent.")
#Total price of all listings in the city/region for one night
def listPrices(x):
    dataset['price'] = pd.to_numeric(dataset['price'])
    print("The total price of all listings in the city for one night are", 
      int(dataset['price'].sum()),"dollars, USD.")
#Median listing price
def medList(x):
    tot = int(statistics.median(dataset['price']))
    print("The median room price is",tot,"dollars, USD.")
#The shares of private rooms, shared rooms, and entire home/apartments
def roomShares(x):
    rooms = dataset['room_type'].value_counts(normalize=True).iloc[:3].round(decimals=2)
    room = rooms[0:3]
    global per
    for x in dataset.iteritems():
        per = room * 100
        print("The percentages of entire rooms are",int(per[0]),
      "percent, private rooms are",int(per[1]),
      "percent, and shared rooms are,",int(per[2]),"percent.")
        break
#func calls
dataCreate(x)
listingsInfo(x)
multiHosts(x)
listPrices(x)
medList(x)
roomShares(x)

#Data Vis- Visual Display of the Rooms and their hosts
#Eventually would like to enable a zoom feature, also show full numbers
'''

'''