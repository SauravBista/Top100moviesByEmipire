from bs4 import BeautifulSoup
import requests
response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
movies = response.text

soup = BeautifulSoup(movies, "html.parser")
list_of_movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")
movie_names = [movie.getText() for movie in list_of_movies]
link_of_movies = soup.find_all("p")

# Extract the href and text from each anchor tag
movie_links = [(a['href'], a.text) for p in link_of_movies for a in p.find_all('a')]




movie_names.reverse()
with open("movie_names.txt", "w") as names:
    for movie_name in movie_names:
        names.write(movie_name+ '\n')


with open("movie_names.txt", "r") as movies:
    movie = movies.read()
    print(movie)
article_link = soup.get("href")
with open("movie_link.txt", "w") as links:
    for link in movie_links:
        links.write(f"{link[0]} \n")

# print(article_link)
# score = soup.find(name="span", class_="score").getText()
# print(score)