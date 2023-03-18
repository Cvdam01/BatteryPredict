import requests
from datetime import datetime, timedelta
import pandas as pd
import lxml
import re
import pdb

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
    #print(pricedoc)
    
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