from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.imdb.com/list/ls025862144/")
data = response.text

soup = BeautifulSoup(data, "html.parser")

movies = soup.find_all(name="h3", class_="lister-item-header")
# print(movies)
for item in movies:
    all_movie = [(movie.getText())for movie in item.find_all(name="a")]
    movie_number = [(movie.getText())for movie in item.find_all(name="span")]
    c = 0
    with open("movies.txt", 'w') as movies_file:
        for movie in all_movie:

            movies_file.write(f"{movie_number}.{movie}")





