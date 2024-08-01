import json
import requests

API_KEY = '800d7152787bb58d98304adbf121fce1'

def load_movie_genres(json_file_path):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        if not data:
            print("O arquivo JSON está vazio ou não foi carregado corretamente.")
        return data

def get_similar_movies(movie_id, api_key, num_similar=3):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}/similar'
    params = {
        'api_key': api_key,
        'language': 'pt-BR', # Aqui coloque seu idioma
        'page': 1
    }
    response = requests.get(url, params=params)
    results = response.json().get('results', [])
    similar_movies = [movie['title'] for movie in results[:num_similar]]
    return similar_movies

def recommend_movies(searches, movie_genres, api_key, num_recommendations=5):
    all_similar_movies = []

    for title in searches:
        if title in movie_genres:
            movie_id = movie_genres[title]['id']
            similar_movies = get_similar_movies(movie_id, api_key, num_similar=num_recommendations)
            all_similar_movies.extend(similar_movies)

    return list(set(all_similar_movies)) 

def read_user_searches(file_path):
    with open(file_path, 'r') as file:
        searches = file.readlines()
    return [search.strip() for search in searches]

if __name__ == "__main__":
    search_file_path = '../data/user_searches.txt'
    json_file_path = '../data/movie_genres.json'
    movie_genres = load_movie_genres(json_file_path)
    user_searches = read_user_searches(search_file_path)
    recommended_movies = recommend_movies(user_searches, movie_genres, API_KEY)
    print("Filmes recomendados:", recommended_movies)
