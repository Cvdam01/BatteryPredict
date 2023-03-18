import requests
from datetime import datetime
from datetime import timedelta
import pandas as pd
import lxml
import re
import pdb
import matplotlib.pyplot as plt
from entsoe_api import *

if __name__ == "__main__":
    df = getTestData(30)
    #print(df)
    # pak de eerste row:
    #df_row = df.head(1)
    #print(df_row)
    maxValues = df.max(axis=1)
    #df.mean(axis=1)

    print("Maximaal")
    print(maxValues)   

    minValues = df.min(axis=1)
    print("Minimaal")
    print(minValues)    
    amount_of_days = maxValues.count()
    x = range(1, amount_of_days+1)
    print(x)
    y_1 = list(maxValues)
    y_2 = list(minValues)
    print(y_1)
    print(y_2)
    diffValues = maxValues - minValues
    print(diffValues)
    plt.plot(x, y_1)
    plt.plot(x, y_2)
    diffValues = diffValues / 1000  * 10 #
    print("Dit is de cumsum")
    diffValues = diffValues.cumsum()
    print(diffValues)
    
    plt.plot(x, diffValues)
    print(max(diffValues))
    #plt.plot(x, diffValues)
    plt.show()
    # x = 
    # y = 
    # 

    # high = max(y)
    # low = min(y)


    # print(f'Highest value: {high}')
    # print(f'Lowest value: {low}')
    #maak een functie van wat we hebben. 
    # met als variable/parameter (x10) de capaciteit van de batterij. 
    #return een dataframe, met als rijen, de dagen,
    #kolommen, datum, min, max, difference, cumulatieve difference, hoeveelheid stroom (capaciteit * aantaal trades), cumulatieve hoeveelheid stroom, gemiddelde, std, min_tijd, max_tijd   



def outputToDevice(displayList,starthour,writeMode):

    if writeMode=='w': 
        clearTextDevice(planningDisplayIDX)
    unclassifiedList=markTopLowPrices(displayList,starthour)
    for i in reversed(displayList):
        if int(i[2][11:13])>=starthour or i[2][0:10]>todayLongString:
            outputString="%2d  %s  %+4.5f  %12s  %+7.0f  %+4.0f   %+7.0f   %+5.5f   %+5.0f" %(i[0],i[2],(i[1]/1000),i[4],i[5],i[7],i[3],i[6],i[8])
            if i[4]=="unclassified":
                for u in unclassifiedList:
                    if i[0]==u[0]: 
                        outputString=outputString+u[2]
            outputString=outputString.replace(' ','_')  # JSON processing removes all duplicate spaces, so use underscore to get table format
    timestamp=datetime.strftime(datetime.now(),'%Y%m%d %H:%M:%S')
   
# string = "Hoi, ik ben hassen"
# str = "hoi"
# split_string = string.split(" ") 
# split_string[0] == 
# string[0] = "H"

def getUserInput():
    maxBatteryCapacity=int(input("Enter max capacity in Wh (default 5000) :") or 5000)
    maxChargeSpeed=int(input("Enter max charge speed in Watt (default 2000) :") or 2000)
