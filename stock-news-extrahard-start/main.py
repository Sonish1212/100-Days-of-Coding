import requests
from newsapi import NewsApiClient
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
my_api_stock = "F5NO610ORTI93ON2"
newsapi = 'e650256722f84cbd93198869d96b74e4'
account_sid = 'ACbb1904b33ebaec888a6c6426deb8f29c'
auth_token = '29072fa0f1580edbf3b90eee376d9acb'

stock_parameter = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": my_api_stock,
}

response = requests.get(url="https://www.alphavantage.co/query", params=stock_parameter)
response.raise_for_status()

stock_data = response.json()['Time Series (Daily)']
daily_data = [value for (key,value) in stock_data.items()]
yesterday = float(daily_data[0]['4. close'])
day_yesterday = float(daily_data[1]['4. close'])
percentage = ((day_yesterday - yesterday)/day_yesterday)*100

if percentage <= 1:
    news_params = {
        "apiKey": newsapi,
        "qInTitle": 'tesla'
    }
    news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()['articles'][:3]
    formatted_news_data = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in news_data]
    print(formatted_news_data)

    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=formatted_news_data,
        from_="+1 646 461 4749",
        to="+9779866126473"
    )
# elif percentage > -1:
#     news_params = {
#         "apiKey": newsapi,
#         "qInTitle": 'tesla'
#     }
#     news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_params)
#     news_response.raise_for_status()
#     news_data = news_response.json()['articles'][:3]
#     print(news_data)
#
#     client = Client(account_sid, auth_token)
#     message = client.messages \
#         .create(
#         body=f"{COMPANY_NAME} ▼ {int(percentage)}%\n"
#              f"Headline:{news_data[0]['title']}\n"
#              f"Brief: {news_data[0]['description']}",
#         from_="+1 646 461 4749",
#         to="+9779866126473"
#     )
#
#
#

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

