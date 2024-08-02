from bs4 import BeautifulSoup
import requests
response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
movies = response.text

soup = BeautifulSoup(movies, "html.parser")
list_of_movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")
movie_names = [movie.getText() for movie in list_of_movies]
movie_names.reverse()
with open("movie_names.txt", "w") as names:
    for movie_name in movie_names:
        names.write(movie_name+ '\n')

print()

# article_link = soup.get("href")

# print(article_link)
# score = soup.find(name="span", class_="score").getText()
# print(score)