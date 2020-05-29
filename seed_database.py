import os
import json
from random import choice, randint
from datetime import datetime
import crud, model, server

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

movies_in_db = []
for movie in movie_data:
    release_date_str = movie['release_date']
    format = '%Y-%m-%d'
    release_date = datetime.strptime(release_date_str, format)
    movie = crud.create_movie(movie['title'], 
                 movie['overview'], 
                 release_date, 
                 movie['poster_path'])
    movies_in_db.append(movie)

for n in range(10):
    email = f'user{n}@test.com'
    password = 'test'

    user = crud.create_user(email, password)

    for r in range(10):
        movie = choice(movies_in_db)
        score = randint(1, 5)
        crud.create_rating(user, movie, score)