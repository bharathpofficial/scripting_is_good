import requests, os
from dotenv import load_dotenv
def configure():
    load_dotenv()
configure()
    
url = "https://randomproxy.p.rapidapi.com/"

headers = {
	"X-RapidAPI-Key": os.getenv('api_key'),
	"X-RapidAPI-Host": "randomproxy.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())