from urllib import response
import requests
class Rozewail :
    def get_unsent_msg(center_id=None):
        api_url="https://rozewail.com/api/get-unsent-messages?center_id="+str(center_id)
        response= requests.get(api_url)
        print(response.json())
        return response.json()
    
    get_unsent_msg(2022)
