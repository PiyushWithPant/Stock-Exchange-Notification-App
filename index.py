# Importing modules
import os
import requests as req
from dotenv import *
from twilio.rest import Client


# Loading the environment variables
load_dotenv()


# Required objects

stockName = "TSLA"
companyName = "Tesla Inc"



# API endpoints

newsEndpoint = "https://newsapi.org/v2/everything"
stockEndpoint = "https://www.alphavantage.co/query"



# Importing the envs
stockAPI_KEY = os.getenv("STOCK_API")
newsAPI_KEY = os.getenv("NEWS_API")
smsAPI_KEY = os.getenv("SMS_API")
smsAPI_ACCOUNT = os.getenv("SMS_ACC")



# Yesterday's closing stock price

stockParams = {
    'function': "TIME_SERIES_DAILY_ADJUSTED",
    'symbol': stockName,
    'apikey': stockAPI_KEY,
}

stockData = req.get(stockEndpoint, params=stockParams)
# Out of the huge data, we need the closing stock data so we will query it out
stockInfo = stockData.json()["Time Series (Daily)"]

# Now we will use List comprehension to turn the dict into a list 
dataList = [value for (key,value) in stockInfo.items()]

# Since we need closing data of yesterday, so just tap into the first object of the list
yesterdayData = dataList[0] 

# closing data of yesterday
yesterdayClosingData = yesterdayData["4. close"]

# print(yesterdayClosingData)


# now we will get closing data of day before yesterday so

dayBeforeYesterdayClosingData = dataList[1]["4. close"]

# print(dayBeforeYesterdayClosingData)


# Now we will find the POSITIVE DIFFERENCE between the yesterday's closing price and day before yesterday's closing price

diff = float(yesterdayClosingData) - float(dayBeforeYesterdayClosingData)

positiveDiff = round(abs(diff),2)

# print(positiveDiff)

# Now we will find the percentage difference

percentDiff = round((positiveDiff / float(yesterdayClosingData)) * 100, 2)
print(f'Difference percent: {percentDiff}%')


# if the percent difference is more than 5%, means noticing loss or profit in the stocks, so why is the case?? then we will get news to find it out

if percentDiff > 5:
    
    # Now we will get the news
    
    newsParams = {
        'qInTitle': companyName,
        
        'apiKey': newsAPI_KEY
    }
    
    newsData = req.get(newsEndpoint, newsParams)
    
    # we just need the news so
    theNEWS = newsData.json()["articles"]
    
    # Getting the first 3 news
    # we will slice the dictionary
    firstThreeNEWS = theNEWS[:3]    # [start:stop] => [:stop], where stop = stop-1 so if we want 3 news, the index should be 3, cuz 3-1 = 2 which are news index 0,1 and 2
    
    print("Found NEWS!")
    
    # making the list of the news description
    
    newsToBeSentList = [f"\n\nHeadline: {news['title']}. \nDescription: {news['description']}" for news in firstThreeNEWS]
    
    
    # Now after getting the news, we will send it to the user via sms
    client = Client(smsAPI_ACCOUNT, smsAPI_KEY)
    
    for news in newsToBeSentList:
        
        msg = client.messages.create( 
            body= news, 
            from_='+12316133953', 
            to='+919834642387'
        )
        print("Notification sent successfully!")
    
    
    
    
    
    

