import requests
import json

api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=4&convert=USD&CMC_PRO_API_KEY=44240872-6952-4dd7-997c-b4b8a64f43e0")

api=json.loads(api_request.content)



print(api)
