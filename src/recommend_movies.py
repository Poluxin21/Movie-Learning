import json
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

def load_movie_genres(json_file_path):
    with open(json_file_path, 'r') as json_file:
        return json.load(json_file)

def recommend_movies_ml(searches, movie_genres, num_recommendations=5):
    df = pd.DataFrame(list(movie_genres.items()), columns=['title', 'genres'])

    df['genre_str'] = df['genres'].apply(lambda x: ' '.join(x))

    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(df['genre_str'])

    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    title_to_index = pd.Series(df.index, index=df['title'])

    search_indices = [title_to_index[title] for title in searches if title in title_to_index]

    sim_scores = np.mean(cosine_sim[search_indices], axis=0)

    sim_indices = np.argsort(-sim_scores)[:num_recommendations + len(searches)]

    recommended_indices = [i for i in sim_indices if i not in search_indices]

    recommended_titles = df['title'].iloc[recommended_indices].tolist()[:num_recommendations]

    return recommended_titles

def read_user_searches(file_path):
    with open(file_path, 'r') as file:
        searches = file.readlines()
    return [search.strip() for search in searches]

if __name__ == "__main__":
    search_file_path = '../data/user_searches.txt'
    json_file_path = '../data/movie_genres.json'

    movie_genres = load_movie_genres(json_file_path)

    user_searches = read_user_searches(search_file_path)

    recommended_movies = recommend_movies_ml(user_searches, movie_genres)
    print("Filmes recomendados:", recommended_movies)
