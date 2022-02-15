from urllib import response
import requests
api_url="https://rozewail.com/api/get-unsent-messages?center_id=2022"
response= requests.get(api_url)
print(response.json())