from flask import Flask, render_template, url_for
from NBA_Stats_Scraper import NBA_Stats_Scraper
from forms import account, LoginForm
from analysis import analysis
app = Flask(__name__)

nba = NBA_Stats_Scraper()
team = nba.get_all_stats()

# this is the serects numbers
app.config['SECRET_KEY'] = 'ea7b11f0714027a81e7f81404612d80d'

print (type(team))

# this is the home page
@app.route("/")
@app.route("/home")
# debug mode in flask:  export FLASK_DEBUG=1
def home():
    return render_template("home.html", team=team)

# this is the about page
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/register")
def register():
    form = account()
    return render_template('register.html', title = 'Register', form = form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form = form)


if __name__ == 'main':
    app.run(debug = True)