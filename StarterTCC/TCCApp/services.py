import requests
import os

def get_mockupapi():
    url = "https://api.mediamodifier.com/mockups"
    
    headers = {
        "Content-Type": "application/json",
        "api_key": "4cb1d7d9-36d3-45f7-837e-2dd1358081d0"
    }
    
    response = requests.request("GET", url, headers=headers)
    
    print(response.text)