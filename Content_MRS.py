import pandas as pd
import Ratings_Preprocessing

user_movie = Ratings_Preprocessing.movie_selected
tags = pd.read_csv("E:\\Python\\DATASETS\\ml-latest-small\\tags.csv", index_col='movieId', usecols=['movieId', 'tag'])

user_movie = Ratings_Preprocessing.movie_selected

genre_similar = user_movie.genres
genre_similar = genre_similar.split('|')


def movie_similar(movie_gen):
    movies = Ratings_Preprocessing.movies.loc[Ratings_Preprocessing.movies['genres'].str.find(movie_gen) != -1]
    return movies


movie_content = []
for gen in genre_similar:
    if gen != Ratings_Preprocessing.genre:
        print(gen)
        movie_content.append(movie_similar(gen))

movies_rec = pd.concat(movie_content).drop_duplicates()
movies_rec = pd.merge(movies_rec, Ratings_Preprocessing.movie_ratings, left_index=True, right_index=True)
movies_rec.sort_values(by='rating', inplace=True, ascending=False)
movies_rec.drop(index=movies_rec.index[0], inplace=True)
print(movies_rec.head(10))
