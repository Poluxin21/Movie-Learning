# Sistema de Recomendação de Filmes Baseado em Pesquisas

Este projeto demonstra um sistema de recomendação de filmes que utiliza um arquivo de texto com as pesquisas dos usuários para gerar recomendações.

## Dependências

- DataSet MovieLens-100K (https://grouplens.org/datasets/movielens/100k/)
- pandas
- numpy
- scikit-learn

## Como rodar

1. Clone o repositório.
2. Baixe o conjunto de dados MovieLens 100k e extraia-o na pasta do projeto.
3. Instale as dependências: `pip install -r requirements.txt`
4. Crie um arquivo `user_searches.txt` com as pesquisas do usuário, uma por linha.
5. Execute o script: `python index.py`
