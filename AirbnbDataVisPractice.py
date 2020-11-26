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
    global multi
    multi =  dataset['host_id'].value_counts()
    #this gives you the total number of hostids
    print("Total number of listings is:",len(multi))
    print("Maximum number of listings per hosts:", max(multi))

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


#Data Vis- Visual Display of the room IDs and their hosts
#Eventually would like to enable a zoom feature, also show full numbers
plt.scatter(dataset["host_id"],dataset["room_id"], color = "purple")
plt.title("Host and Room Ids")
plt.xlabel("Host ID")
plt.ylabel("Room ID")
plt.show()

#Data Vis- Histogram of hosts having multiple IDs. Probably would be best shown with a bar graph.
plt.hist(multi, bins = 30)
plt.title("Distribution of Host IDs")
plt.xlabel("Number of Hosts with Multiple Listings")
plt.ylabel("Frequency")
plt.show()

#Data Vis- Pie Graph of percentages of types of rooms
#Would like it to show the actual numbers
labels = ["Entire","Private","Shared"]
sizes = [per[0],per[1],per[2]]
plt.pie(sizes, labels=labels,explode= (0.01,0.01,0.01))
plt.axis('equal')
plt.show()

#Data Vis- Gives host IDs with how many rooms they have
plt.hist(dataset["host_id"], bins = 500) #bins can be edited, to show the full number of hosts, which is where the shape comes into play
plt.title("Distribution of Host IDs")
plt.xlabel("Host ID")
plt.ylabel("Frequency")
plt.show()