import requests
import cloudmersive_currency_api_client
from flask import Flask, render_template

# Configure API key authorization: Apikey
URL = 'https://testapi.cloudmersive.com/currency/exchange-rates/list-available'
APIKEY = 'a40d3c0e-1fad-4d8d-88ee-cb07a373b4e1'
headers = {
    'Apikey': APIKEY
}

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
    response = requests.post(url=URL, headers=headers)
    data = response.json()
    currency = data['Currencies']
    currency_item = [item['ISOCurrencyCode'] for item in currency]
    print(currency_item)

    source_code = input("Enter the code of the country: ")
    destination_code = input('Enter the code of the country: ')
    amount_to_convert = float(input("Enter the amount of money you want to convert: "))

    if source_code in currency_item:
        if destination_code in currency_item:
            URL2 = 'https://testapi.cloudmersive.com/currency/exchange-rates/get/{source}/to/{destination}'
            params = {
                'source': source_code,
                'destination': destination_code,
            }

            response2 = requests.post(url=URL2, params=params, headers=headers)
            response2.raise_for_status()
            data2 = response2.json()
            exchange_rate = data2['ExchangeRate']
            print(exchange_rate)
            print(f"Total amount of money is: {exchange_rate * amount_to_convert}")
        return render_template("index.html", currencies=currency_item)


if __name__ == "__main__":
    app.run(debug=True)







