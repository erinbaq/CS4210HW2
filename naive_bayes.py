#-------------------------------------------------------------------------
# AUTHOR: Russ Erin Baquiran
# FILENAME: naive_bayes.py
# SPECIFICATION: output class of each instance
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv

db=[]
dbTest=[]

#reading the training data
#--> add your Python code here
with open("weather_training.csv", 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                db.append (row)

#transform the original training features to numbers and add to the 4D array X. For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
#--> add your Python code here
X =[]
tempX=[0]*5 
for info in db:
    for i in range(5):
        if info[i]== "Sunny" or info[i]=="Hot" or info[i]=="High" or info[i]=="Strong":
            tempX[i]=1
        elif info[i]== "Overcast" or info[i]=="Mild" or info[i]=="Normal" or info[i]=="Weak":
            tempX[i]=2
        elif info[i]== "Rain" or info[i]=="Cool":
            tempX[i]=3
        else:
            tempX[i]=0

#transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
Y =[]
for i in db:
    if i[5]=="Yes":
        Y.append(1)
    elif i[5]=="No":
        Y.append(2)

#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

#reading the data in a csv file
#--> add your Python code here
with open("weather_training.csv", 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTest.append (row)
                
testData=[]
displayData=[]
tempX=[]*5
for info in dbTest:
    displayData.append(info[0:5])
    for i in range(5):
        if info[i]== "Sunny" or info[i]=="Hot" or info[i]=="High" or info[i]=="Strong":
            tempX[i]=1
        elif info[i]== "Overcast" or info[i]=="Mild" or info[i]=="Normal" or info[i]=="Weak":
            tempX[i]=2
        elif info[i]== "Rain" or info[i]=="Cool":
            tempX[i]=3
        else:
            tempX[i]=0
    testData.append(tempX[1:5])     



#printing the header os the solution
print ("Day".ljust(15) + "Outlook".ljust(15) + "Temperature".ljust(15) + "Humidity".ljust(15) + "Wind".ljust(15) + "PlayTennis".ljust(15) + "Confidence".ljust(15))

#use your test samples to make probabilistic predictions.
#--> add your Python code here
#-->predicted = clf.predict_proba([[3, 1, 2, 1]])[0]

for(data, display) in zip(testData, displayData):
    predicted = clf.predict_proba([data])[0]
    if predicted[0]>=.75:
        temp=""
        for i in display:
            temp+= i.ljust(15)
        print("Yes".ljust(15),"{:.2f}".format(predicted[0]), temp)
    elif predicted[1]>=.75:
        temp=""
        for i in display:
            temp+= i.ljust(15)
        print("No".ljust(15),"{:.2f}".format(predicted[0]), temp)
        


