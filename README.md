# Sistema de Recomendação de Filmes Baseado em Pesquisas

Este projeto é um sistema de recomendação de filmes que utiliza a API do TMDB para buscar informações sobre filmes e seus gêneros, e gera recomendações usando aprendizado de máquina para encontrar filmes similares com base nas pesquisas do usuário.

## Estrutura do Projeto

```
movie-recommendation/
│
├── data/
│ ├── user_searches.txt
│ └── movie_genres.json
│
├── src/
│ ├── fetch_movie_data.py
│ ├── recommend_movies.py
│
├── requirements.txt
└── README.md
```


- **data/user_searches.txt**: Contém os títulos dos filmes pesquisados pelo usuário, um por linha.
- **data/movie_genres.json**: Será gerado para armazenar informações sobre os gêneros dos filmes.
- **src/fetch_movie_data.py**: Script para buscar informações dos filmes usando a API do TMDB.
- **src/recommend_movies.py**: Script para gerar recomendações de filmes com base nas pesquisas do usuário.
- **requirements.txt**: Lista de bibliotecas necessárias para executar o projeto.

## Configuração

1. Crie uma conta e obtenha uma chave de API do [TMDB](https://www.themoviedb.org/).
2. Clone este repositório:
    ```bash
    git clone https://github.com/Poluxin21/ML-Recommender
    cd ML-Recommender
    ```
3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
4. Substitua `SUA_CHAVE_API` no arquivo `src/fetch_movie_data.py` pela sua chave de API.

## Como Executar

1. Certifique-se de que o arquivo `data/user_searches.txt` contém as pesquisas de filmes, um por linha.
2. Execute o script para buscar informações dos filmes:
    ```bash
    python src/fetch_movie_data.py
    ```
3. Execute o script para gerar recomendações:
    ```bash
    python src/recommend_movies.py
    ```

## Funcionamento do Sistema

- **Coleta de Dados**: Utiliza a API do TMDB para buscar gêneros de filmes pesquisados e armazena esses dados em um arquivo JSON.
- **Recomendação com Machine Learning**: Emprega a técnica de filtragem colaborativa, calculando a similaridade coseno dos gêneros dos filmes para recomendar aqueles mais similares às pesquisas do usuário.

## Melhorias Futuras

- Integração de dados de avaliações dos usuários para uma filtragem colaborativa mais precisa.
- Expansão para incluir dados de sinopses dos filmes para melhorar a vetorização e a precisão das recomendações.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
