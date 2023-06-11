import requests
from send_email import send_email

api_key = "aec9b642525d4c9caee716b80e3b88c8"
url = "https://newsapi.org/v2/top-headlines?" \
      "country=in&category=business&apiKey=" \
      "aec9b642525d4c9caee716b80e3b88c8"
request = requests.get(url)
content = request.json()

for article in content["articles"]:
    try:
        print(article['url'])
        print(article['description'])
        message = article['title'].title() + "\n" + article['description']
        message = message.encode("utf-8")
        send_email(message)
    except TypeError:
        continue
