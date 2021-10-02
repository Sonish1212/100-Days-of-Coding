from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///best-Anime-collection.db"
# Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

API_KEY = "bdb86326f2ca01b2c4de26dc02a2804d"
ANIME_URL = "https://api.themoviedb.org/3/search/tv"
ANIME_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"


class RateAnimeForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")


class AddAnimeForm(FlaskForm):
    add_anime = StringField("Anime Name", validators=[DataRequired()])
    submit = SubmitField("Done")


class Anime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


db.create_all()

# new_anime = Anime(id=2, title="Jujustu Kaisen", year=2020,
#                   description="It is about a boy named naruto who was disliked by everyone in the village but"
#                   "inspite of that want to become a Hokageotsutsuki with their friends", rating=7.9, ranking=1,
#                   review="Ain't got nothing to say just wonderful",
#                   img_url="https://m.media-amazon.com/images/M/MV5BZmQ5NGFiNWEtMmMyMC00MDdiLTg4YjktOGY5Yzc2MDUxMTE1XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_.jpg")
# db.session.add(new_anime)
# db.session.commit()


@app.route("/")
def home():
    all_anime = Anime.query.order_by(Anime.rating).all()
    for i in range(len(all_anime)):
        all_anime[i].ranking = len(all_anime) - i
        db.session.commit()
    return render_template("index.html", animes=all_anime)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = RateAnimeForm()
    anime_id = request.args.get("id")
    anime_selected = Anime.query.get(anime_id)
    if form.validate_on_submit():
        anime_selected.review = form.review.data
        anime_selected.rating = float(form.rating.data)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", anime=anime_selected, form=form)


@app.route('/delete')
def delete():
    anime_id = request.args.get('id')
    anime_selected = Anime.query.get(anime_id)
    db.session.delete(anime_selected)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddAnimeForm()
    if form.validate_on_submit():
        movie_title = form.add_anime.data
        response = requests.get(url=ANIME_URL,
                                params={"api_key": API_KEY, "query": movie_title})
        data = response.json()["results"]
        return render_template("select.html", options=data)
    return render_template("add.html", form=form)


@app.route('/find')
def find_anime():
    anime_id = request.args.get("id")
    if anime_id:
        anime_api_url = f"https://api.themoviedb.org/3/tv/{anime_id}"
        response = requests.get(anime_api_url,
                                params={"api_key": API_KEY, "tv_id": anime_id})
        data = response.json()
        new_anime = Anime(title=data['original_name'], year=data["first_air_date"].split("-")[0],
                          img_url=f"{ANIME_DB_IMAGE_URL}{data['poster_path']}",
                          description=data["overview"])
        db.session.add(new_anime)
        db.session.commit()
        return redirect(url_for("edit", id=new_anime.id))


if __name__ == '__main__':
    app.run(debug=True)
