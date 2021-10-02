from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
f = soup.find_all(name="a", class_="storylink")
print(f)
article_link = []
article_tag = []
for article in f:
    tag = article.getText()
    article_tag.append(tag)
    link = article.get("href")
    article_link.append(link)

article_upvote = [int((score.getText().split()[0]))for score in soup.find_all(name="span", class_="score")]
print(article_upvote)

largest_number = max(article_upvote)
largest_index = article_upvote.index(largest_number)
print(largest_index)
print(article_link[largest_index])
print(article_tag[largest_index])