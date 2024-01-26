import pandas as pd
import difflib as df

# Reading CSV files
data = pd.read_csv("E:\\Python\\Demo_CSV\\movies.csv", index_col='movieId')
# print(data.head())

genre_list = ["Action", "Crime", "Fantasy", "Drama", "Animation", "Comedy", "Horror", "Romance", "Thriller", "Mystery",
              "Adventure", "Sci-Fi", "IMAX", "War"]
# INPUT for PREFERRED MOVIE GENRE
genres = input("Enter the preferred genre : ")
if genres not in genre_list:
    genres = df.get_close_matches(genres, genre_list)


def list_to_string(s):
    cstr = ""
    return cstr.join(s)


genres = list_to_string(genres)
# print(genres)
data['IF_FOUND'] = data['genres'].str.find(genres)

# Processed DATAFRAME from which movies will be recommended
data = data.loc[data['IF_FOUND'] != -1]
# print(data.head(20))

# Further Processed DATAFRAME
year = input("Enter the preferred year : ")
data['IF_FOUND'] = data['title'].str.find(year)
data = data.loc[data['IF_FOUND'] != -1]

# FINAL DATAFRAME
final_data = data.drop(columns=['IF_FOUND'])
# print(final_data.head(10))


ratings = 'E:\\Python\\DATASETS\\ml-latest-small\\ratings.csv'
movie_rating = pd.read_csv(ratings, index_col='movieId', usecols=['movieId', 'rating'])
movie_rating = movie_rating.sort_values(by='rating', ascending=False)
# print(movie_rating.head(10))


movie = final_data.merge(movie_rating[['rating']], left_index=True, right_index=True)
movie = movie.drop_duplicates(subset='title', keep='first')
movie = movie.sort_values(by='rating', ascending=False)
print(movie.head(10))

mId = int(input("Enter the MOVIE ID to Select the Movie : "))
movie_selected = movie.loc[[mId]]
print("\n\nMOVIE SELECTED :\n", movie_selected.to_string(index=False))

