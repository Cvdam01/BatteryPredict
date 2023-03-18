import requests
from datetime import datetime
from datetime import timedelta
import pandas as pd
import lxml
import re
import pdb
import matplotlib.pyplot as plt
def getPriceDocument(startDate,endDate):
    loadStartDate = datetime.strftime(startDate,'%Y%m%d')
    loadEndDate = datetime.strftime(endDate,'%Y%m%d')
    api_token = "07c466d7-15c7-4d40-a406-7772460331f6"
    urlwebsite='https://web-api.tp.entsoe.eu/api?'
    urltoken='securityToken='+api_token
    urldoctype='&documentType=A44'
    urldomain='&in_Domain=10YNL----------L&out_Domain=10YNL----------L'
    urlperiod='&periodStart='+loadStartDate+'0000&periodEnd='+loadEndDate+'2300'
    url=urlwebsite+urltoken+urldoctype+urldomain+urlperiod
    # creating HTTP response object from given url
    print(url)
    response = requests.get(url)
    f = open("pricedoc.xml","w")
    f.write(response.text)
    if response.status_code == 200:
        # saving the xml file
        return response.text
    else:
        print(response.status_code)
        print(response.content)
        return False

def getRangeData(startDate, endDate):
    pricedoc = getPriceDocument(startDate,endDate)
    print(pricedoc)
    
    pricedoc = re.sub(' xmlns="[^"]+"', '', pricedoc, count=1)

    df = pd.read_xml(pricedoc, parser="lxml", xpath="//Point")
    time_df = pd.read_xml(pricedoc, parser="lxml", xpath="//timeInterval")
    hours = range(0,24)
    col_names = ["hour_" + str(h) for h in hours]
    df2 = pd.DataFrame(columns = col_names)
    for i in hours:
        df2["hour_" + str(i)] = df[df["position"] == i+1].reset_index()['price.amount']
    df2['Date'] = time_df['start']
    df2.set_index('Date', inplace=True)
    return df2


def getTestData(days_past = 1):
    endDate = datetime.now()
    startDate = endDate - timedelta(days=days_past)
    pricedoc = getPriceDocument(startDate,endDate)
    print(pricedoc)
    
    pricedoc = re.sub(' xmlns="[^"]+"', '', pricedoc, count=1)

    df = pd.read_xml(pricedoc, parser="lxml", xpath="//Point")
    time_df = pd.read_xml(pricedoc, parser="lxml", xpath="//timeInterval")
    hours = range(0,24)
    col_names = ["hour_" + str(h) for h in hours]
    df2 = pd.DataFrame(columns = col_names)
    for i in hours:
        df2["hour_" + str(i)] = df[df["position"] == i+1].reset_index()['price.amount']
    df2['Date'] = time_df['start']
    df2.set_index('Date', inplace=True)
    return df2

def getColStats(df):
    df2 = df.mean(axis=0)
    return df2
    pass

def getRowStats():
    pass

if __name__ == "__main__":
    df = getTestData(30)
    df2 = getColStats(df)
    print(df2)

df = getPriceDocument
x = getTestData(30)
y = 
plt.plot(x, y)

high = max(y)
low = min(y)


print(f'Highest value: {high}')
print(f'Lowest value: {low}')


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
            setTextDevice(planningDisplayIDX,outputString)
    timestamp=datetime.strftime(datetime.now(),'%Y%m%d %H:%M:%S')
    setTextDevice(planningDisplayIDX,"**__date_______time_________price________action___change__%max_____total_____amount______PV___******")
    setTextDevice(planningDisplayIDX,"****** planning created "+timestamp+" for period "+startdate+" "+str(starthour)+" hr to "+enddate+" 24:00 hr ******")



def getUserInput():
    maxBatteryCapacity=int(input("Enter max capacity in Wh (default 5000) :") or 5000)
    maxChargeSpeed=int(input("Enter max charge speed in Watt (default 2000) :") or 2000)

    