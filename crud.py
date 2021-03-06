from model import db, User, Movie, Rating, connect_to_db

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


def get_movies():
    return Movie.query.all()


def get_movie_by_id(movie_id):
    return Movie.query.get(movie_id)


def get_movie_by_title(title):
    return Movie.query.filter(Movie.title==title).first()


def get_users():
    return User.query.all()


def get_user_by_id(user_id):
    return User.query.get(user_id)


def get_user_by_email(email):
    return User.query.filter(User.email==email).first()



if __name__ == '__main__':
    from server import app
    connect_to_db(app)