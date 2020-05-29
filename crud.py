from model import *
import json

def create_user(email, password):
    new_user = User(email=email, password=password)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def create_movie(title, overview, release_date, poster_path):
    new_movie = Movie(title=title, 
                     overview=overview, 
                     release_date=release_date,
                     poster_path=poster_path)
    db.session.add(new_movie)
    db.session.commit()
    return new_movie

def create_rating(user, movie, score):
    new_rating = Rating(user=user, movie=movie, score=score)
    db.session.add(new_rating)
    db.session.commit()
    return new_rating

# def enter_movies():
#     movies = json.load(open('data/movies.json'))
#     for movie in movies:
#         create_movie(movie['title'], 
#                      movie['overview'], 
#                      movie['release_date'], 
#                      movie['poster_path'])


if __name__ == '__main__':
    from server import app
    connect_to_db(app)