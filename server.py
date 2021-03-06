"""Server for movie ratings app."""

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db
import crud
from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = 'blahdiblah'
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def show_homepage():
    return render_template('homepage.html')


@app.route('/movies')
def all_movies():
    movies = crud.get_movies()
    return render_template('all_movies.html', movies=movies)


@app.route('/movies/<movie_id>')
def show_movie(movie_id):
    movie = crud.get_movie_by_id(int(movie_id))
    return render_template('movie_details.html', movie=movie)


@app.route('/users')
def all_users():
    users = crud.get_users()
    return render_template('all_users.html', users=users)


@app.route('/users', methods=['POST'])
def register_user():
    email = request.form.get('email')
    password = request.form.get('password')
    user = crud.get_user_by_email(email)
    if user:
        flash('A user with that email address already exists. Please try again.')
    else:
        crud.create_user(email, password)
        flash('Account created. Please log in.')
    return redirect('/')


@app.route('/users/<user_id>')
def show_user(user_id):
    user = crud.get_user_by_id(user_id)
    return render_template('user_details.html', user=user)


@app.route('/login', methods=['POST'])
def process_login():
    email = request.form.get('email')
    password = request.form.get('password')
    user = crud.get_user_by_email(email)
    if not user:
        flash('There is no user with that email address. Please create an account.')
    elif password == user.password:
        session['logged_in_customer_email'] = email
        flash('You have successfully logged in.')
        return render_template('index.html')
    else:
        flash('Incorrect password. Please try again.')
    return redirect('/')


@app.route('/add_rating', methods=['POST'])
def add_rating():
    score = int(request.form.get('score'))
    movie_title = request.form.get('movie')
    email = session['logged_in_customer_email']
    user = crud.get_user_by_email(email)
    movie = crud.get_movie_by_title(movie_title)
    crud.create_rating(user, movie, score)
    flash('Rating added')
    return redirect(f'/movies/{movie.movie_id}')


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
