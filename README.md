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
