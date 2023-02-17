# Stock Exchange Notification App

## About Project

- This Python-based project monitors the closing price of yesterday and day before yesterday of a stock. If the difference percentage is greater than 5%, then the app sends NEWS to the user as a notification via SMS related to the stock.

- Execute the `index.py` file to run the application (Ensure that you change the type of STOCK as per your choice and your details as well)


## Requirements

- Python 3.10.6 <i>(recommended)</i>
- Account on <a target="_blank" href="https://newsapi.org/"><img src="https://img.shields.io/badge/-NEWS%20API-blue" /></a> and the key
- Account on <a target="_blank" href="https://www.twilio.com/"><img src="https://img.shields.io/badge/-Twilio-crimson" /></a> with accID, accKey, and phone number
- Account on <a target="_blank" href="https://www.alphavantage.co/"><img src="https://img.shields.io/badge/-Alpha%20Vantage-green" /></a> with key
- Basic knowledge about Stocks
- Request Handling
- Environment Variables



## APIs

<a target="_blank" href="https://newsapi.org/">
<img src="https://img.shields.io/badge/-NEWS%20API-blue" />
</a>

<a target="_blank" href="https://www.alphavantage.co/">
<img src="https://img.shields.io/badge/-Alpha%20Vantage-green" />
</a>

<a target="_blank" href="https://www.twilio.com/">
<img src="https://img.shields.io/badge/-Twilio-crimson" />
</a>

## For Users
- Change the STOCK name and COMPANY name as per your own wish.
- Activate all your keys and put them in the `.env` file to ensure security.
- Ensure that you are using the correct APIs and their respective KEYS with correct params.
- You can set the number of NEWS updates you want to receive via SMS, by default it will send 3 messages.
- You can change the threshold to notify you as well, by default it is 5% change in closing price.

###### Thank you for your time. Please contact me if you face any query or errors (visit my profile or webpage for contact details). I will be happy to help :smiley: :heart:




<hr />

>By Piyush Pant
