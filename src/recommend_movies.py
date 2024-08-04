import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_movie_data(json_file_path):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        if not data:
            print("O arquivo JSON está vazio ou não foi carregado corretamente.")
        return pd.DataFrame(data)

def prepare_features(movie_data):
    movie_data['combined_features'] = movie_data.apply(lambda x: x['genres'] + ' ' + x['description'], axis=1)
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(movie_data['combined_features'])
    return tfidf_matrix

def get_recommendations(title, movie_data, tfidf_matrix, num_recommendations=5):
    idx = movie_data[movie_data['title'] == title].index[0]

    cosine_similarities = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()
    
    similar_indices = cosine_similarities.argsort()[-(num_recommendations+1):-1][::-1]
    
    return movie_data['title'].iloc[similar_indices].tolist()

def read_user_searches(file_path):
    with open(file_path, 'r') as file:
        searches = file.readlines()
    return [search.strip() for search in searches]

if __name__ == "__main__":
    search_file_path = '../data/user_searches.txt'
    json_file_path = '../data/movie_genres.json'
    
    movie_data = load_movie_data(json_file_path)
    tfidf_matrix = prepare_features(movie_data)
    
    user_searches = read_user_searches(search_file_path)
    
    all_recommended_movies = []
    for search in user_searches:
        if search in movie_data['title'].values:
            recommendations = get_recommendations(search, movie_data, tfidf_matrix)
            all_recommended_movies.extend(recommendations)
    
    recommended_movies = list(set(all_recommended_movies))
    print("Filmes recomendados:", recommended_movies)
