# Movie Recommender System

![Movie Recommender System](https://i.redd.it/4fxxbm4opjd31.jpg)

## Overview

This Movie Recommender System is a Streamlit app designed to help users discover and explore movies based on genre, release year, and user ratings. The system utilizes movie data loaded from a CSV file and movie ratings from another CSV file to provide personalized recommendations.

## Features

- **Data Loading**: Easily load movie data from a CSV file.
- **Genre Filtering**: Choose a preferred movie genre to filter the recommendations.
- **Year Filtering**: Specify a preferable release year to narrow down movie options.
- **Movie Recommendations**: Get top movie recommendations based on user ratings.
- **Movie Details**: Select a movie by ID to view its details and a link to MovieLens.

## Code Explanation

### Data Loading

The app uses the `load_data` function to load movie data from a CSV file (`movies.csv`). The loaded data is then displayed using Streamlit's `st.dataframe` function.

```python
# Function to load movie data
@st.cache(allow_output_mutation=True)
def load_data():
    time.sleep(2)
    dat = pd.read_csv("./movies.csv", index_col='movieId')
    return dat

# Load data into 'data' DataFrame
data = load_data()

# Display the loaded data
st.dataframe(data)
```
### Genre Filtering
Users can select a preferred genre using the dropdown menu. The filter_by_genre function filters the loaded data based on the selected genre, and the results are displayed in real-time.

```python
# Function to filter data by selected genre
@st.cache(allow_output_mutation=True)
def filter_by_genre(data_filtered, genre_0):
    data_filtered['IF_FOUND'] = data_filtered['genres'].str.find(genre_0)
    data_filtered = data_filtered.loc[data_filtered['IF_FOUND'] != -1]
    return data_filtered

# Apply genre filter
data = filter_by_genre(data, genres)
```
### Year Filtering
Users can input a preferable release year, and the filter_by_year function filters the data accordingly. An optional warning is displayed if an invalid year is entered.
```python
# Function to filter data by selected year
@st.cache(allow_output_mutation=True)
def filter_by_year(data_filtered, year_0):
    data_filtered['IF_FOUND'] = data_filtered['title'].str.find(year_0)
    data_filtered = data_filtered.loc[data_filtered['IF_FOUND'] != -1]
    return data_filtered

# Apply year filter
data = filter_by_year(data, year)
```
### Movie Recommendations
The app provides a checkbox to trigger the recommendation process. User ratings data is loaded using the load_data0 function, and the movie_merge function merges movie ratings with the filtered data to create a list of recommended movies. The top 10 recommendations are displayed in a dataframe.

```python
# Function to load movie ratings data with caching
@st.cache(allow_output_mutation=True)
def load_data0():
    ratings = './ratings.csv'
    movie_rat0 = pd.read_csv(ratings, index_col='movieId', usecols=['movieId', 'rating'])
    movie_rat0 = movie_rat0.sort_values by='rating', ascending=False)
    return movie_rat0

# Load movie ratings data
movie_rating = load_data0()

# Function to merge movie ratings and final data
@st.cache(allow_output_mutation=True)
def movie_merge(movie_rating0, final_data0):
    movies = final_data0.merge(movie_rating0[['rating']], left_index=True, right_index=True)
    movies = movies.drop_duplicates(subset='title', keep='first')
    movies = movies.sort_values(by='rating', ascending=False)
    return movies

# Merge movie ratings and final data
movie = movie_merge(movie_rating, final_data)

# Display the recommended movies
st.dataframe(movie.head(10))
```
### Movie Details
Users can input a movie ID to view details about a specific movie. If the entered ID is valid, details about the selected movie are displayed, along with a link to MovieLens for more information.

```python
# Input for entering a movie ID
mId = int(st.number_input("Enter Movie ID :"))

# Checkbox for selecting a movie
check_movie = st.checkbox('Movie Selected')

# If a movie is selected
if check_movie:
    # If the movie ID is not in the index of 'movie'
    if mId not in movie.index:
        st.error("ENTER A VALID MOVIE ID")
    else:
        # Display the selected movie
        movie_selected = movie.loc[[mId]]
        st.write('MOVIE SELECTED :', movie_selected)
        
        # Display a link to the selected movie on movielens.org
        link = 'https://movielens.org/movies/' + str(mId)
        st.markdown(link, unsafe_allow_html=True)
```
Usage
Clone the repository:

```bash
git clone https://github.com/your-username/movie-recommender-system.git
cd movie-recommender-system
```
Install dependencies:
```bash
pip install -r requirements.txt
```
Run the Streamlit app:
```bash
streamlit run app.py
```
Interact with the app through the provided widgets and enjoy exploring movie recommendations!

## License

This project is licensed under the [MIT License](LICENSE).

[MIT License](https://opensource.org/licenses/MIT)

