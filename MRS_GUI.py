import pandas as pd
import streamlit as st
import time

movie = []
movie = pd.DataFrame(movie)
data = []
data = pd.DataFrame(data)
final_data = []
final_data = pd.DataFrame(final_data)
movie_rating = []
movie_rating = pd.DataFrame(movie_rating)
year_check = False
genre_check = False

st.image('https://i.redd.it/4fxxbm4opjd31.jpg', use_column_width=True)

st.title("MOVIE RECOMMENDER SYSTEM")
load = st.checkbox('CHECK TO LOAD DATA')
time.sleep(1)
if load:
    @st.cache(allow_output_mutation=True)
    def load_data():
        time.sleep(2)
        dat = pd.read_csv("https://raw.githubusercontent.com/John-Alex07/MINI_PR0JECT/Datasets/movies.csv",
                          index_col='movieId')
        return dat


    data = load_data()
    if 'IF_FOUND' in data.columns:
        data = data.drop(columns=['IF_FOUND'])
    st.dataframe(data)
    'DATA LOADED SUCCESSFULLY'
    genres = st.selectbox("SELECT A GENRE",
                          ("Action", "Crime", "Fantasy", "Drama", "Animation", "Comedy", "Horror", "Romance",
                           "Thriller", "Mystery", "Adventure", "Sci-Fi", "IMAX", "War", "Children", "Documentary"))
    time.sleep(1)

    genre_check = st.checkbox('GENRE SELECTED')
    if load:
        if genre_check:
            @st.cache(allow_output_mutation=True)
            def filter_by_genre(data_filtered, genre_0):
                data_filtered['IF_FOUND'] = data_filtered['genres'].str.find(genre_0)
                data_filtered = data_filtered.loc[data_filtered['IF_FOUND'] != -1]
                return data_filtered


            data = filter_by_genre(data, genres)
    else:
        st.error('LOAD THE DATA')
    year = st.text_input('Preferable Year : ')
    year_check = st.checkbox('YEAR SELECTED')
    if load:
        if year_check:
            if year == '':
                st.warning("ENTER A VALID YEAR")


            @st.cache(allow_output_mutation=True)
            def filter_by_year(data_filtered, year_0):
                data_filtered['IF_FOUND'] = data_filtered['title'].str.find(year_0)
                data_filtered = data_filtered.loc[data_filtered['IF_FOUND'] != -1]
                return data_filtered


            data = filter_by_year(data, year)
            final_data = data.drop(columns=['IF_FOUND'])
    else:
        st.error('LOAD THE DATA')

    check_process = st.checkbox('Check To Recommend')
    if year_check & genre_check:
        if check_process:
            @st.cache(allow_output_mutation=True)
            def load_data0():
                ratings = 'https://raw.githubusercontent.com/John-Alex07/MINI_PR0JECT/Datasets/ratings.csv'
                movie_rat0 = pd.read_csv(ratings, index_col='movieId', usecols=['movieId', 'rating'])
                movie_rat0 = movie_rat0.sort_values(by='rating', ascending=False)
                return movie_rat0


            movie_rating = load_data0()


            @st.cache(allow_output_mutation=True)
            def movie_merge(movie_rating0, final_data0):
                movies = final_data0.merge(movie_rating0[['rating']], left_index=True, right_index=True)
                movies = movies.drop_duplicates(subset='title', keep='first')
                movies = movies.sort_values(by='rating', ascending=False)
                return movies


            movie = movie_merge(movie_rating, final_data)
            st.dataframe(movie.head(10))
    else:
        st.warning("CHECK PREVIOUS INPUTS")
    mId = int(st.number_input("Enter Movie ID :"))
    check_movie = st.checkbox('Movie Selected')
    if check_movie:
        if mId not in movie.index:
            st.error("ENTER A VALID MOVIE ID")
        else:
            movie_selected = movie.loc[[mId]]
            st.write('MOVIE SELECTED :', movie_selected)
            link = 'https://movielens.org/movies/' + str(mId)
            st.markdown(link, unsafe_allow_html=True)

    "\n\nMovie Recommender System \n"
    "BY : JOHN ALEXANDER"
