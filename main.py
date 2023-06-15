import requests
from send_email import send_email

topic = input("Please enter topic for the day")
api_key = "aec9b642525d4c9caee716b80e3b88c8"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic} " \
      "&from=2023-05-15" \
      "&sortBy=publishedAt" \
      "&apiKey=aec9b642525d4c9caee716b80e3b88c8" \
      "&language=en"

request = requests.get(url)
content = request.json()

for article in content["articles"][:20]:
    try:
        print(article['url'])
        print(article['description'])
        message = "Subject: Today's News" + "\n" + \
                  article['title'].title() + "\n" + \
                  article['description'] + "\n" + \
                  article["url"] + 2*"\n"
        message = message.encode("utf-8")
    except TypeError:
        continue
    send_email(message)

