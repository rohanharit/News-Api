import requests
query=input("what type of news you want: ")
api=input("Write YOUR NEWS API here: ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2025-12-14&sortBy=publishedAt&apiKey={api}"
print(url)
r=requests.get(url)
data=r.json()
articles=data["articles"]
for index,article in enumerate(articles):
    print(index+1,article["title"],article["url"],article["content"],sep="\n")
    print("\n")
