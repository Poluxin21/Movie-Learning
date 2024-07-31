import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



movies = pd.read_csv('ml-100k/u.item', sep='|', encoding='latin-1', names=['movie_id', 'title'], usecols=[0, 1])

print(movies.head())

def read_user_searches(file_path):
    with open(file_path, 'r') as file:
        searches = file.readlines()
    searches = [search.strip() for search in searches]
    return searches

user_searches = read_user_searches('user_searches.txt')
print("Pesquisas do usuário:", user_searches)


tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['title'])

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def recommend_movies_based_on_searches(searches, movies, cosine_sim, num_recommendations=5):
    search_indices = [movies[movies['title'].str.lower() == search.lower()].index[0] for search in searches if search.lower() in movies['title'].str.lower().values]
    
    sim_scores = cosine_sim[search_indices]
    
    total_sim_scores = sim_scores.sum(axis=0)
    
    movie_indices = total_sim_scores.argsort()[-num_recommendations:][::-1]
    
    recommended_movies = movies.iloc[movie_indices]['title'].values
    return recommended_movies

recommended_movies = recommend_movies_based_on_searches(user_searches, movies, cosine_sim)
print("Filmes recomendados:", recommended_movies)
