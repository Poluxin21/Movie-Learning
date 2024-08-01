import requests
import json
import os


API_KEY = '800d7152787bb58d98304adbf121fce1'

def get_movie_id(title, api_key):
    url = f'https://api.themoviedb.org/3/search/movie'
    params = {
        'api_key': api_key,
        'query': title
    }
    response = requests.get(url, params=params)
    results = response.json().get('results')
    if results:
        return results[0]['id']
    return None

def get_movie_info(movie_id, api_key):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}'
    params = {'api_key': api_key}
    response = requests.get(url, params=params)
    return response.json()

def get_similar_movies(movie_id, api_key, num_similar=3):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}/similar'
    params = {
        'api_key': api_key,
        'language': 'en-US',
        'page': 1
    }
    response = requests.get(url, params=params)
    results = response.json().get('results', [])
    similar_movies = [(movie['title'], movie['id']) for movie in results[:num_similar]]
    return similar_movies

def fetch_and_save_movie_data(movie_titles, api_key, json_file_path):
    movie_data = {}
    for title in movie_titles:
        movie_id = get_movie_id(title, api_key)
        if movie_id:
            movie_info = get_movie_info(movie_id, api_key)
            genres = [genre['name'] for genre in movie_info.get('genres', [])]
            movie_data[title] = {'genres': genres, 'id': movie_id}

    with open(json_file_path, 'w') as json_file:
        json.dump(movie_data, json_file, indent=4)

def read_user_searches(file_path):
    with open(file_path, 'r') as file:
        searches = file.readlines()
    return [search.strip() for search in searches]

if __name__ == "__main__":

    search_file_path = '../data/user_searches.txt'
    json_file_path = '../data/movie_genres.json'


    user_searches = read_user_searches(search_file_path)

    fetch_and_save_movie_data(user_searches, API_KEY, json_file_path)

    print(f"Dados de filmes salvos em {json_file_path}")
