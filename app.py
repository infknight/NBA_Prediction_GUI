from flask import Flask, render_template, url_for
from NBA_Stats_Scraper import NBA_Stats_Scraper
from analysis import analysis
app = Flask(__name__)

nba = NBA_Stats_Scraper()
team = nba.get_all_stats()


print (type(team))

@app.route("/")
@app.route("/home")
# debug mode in flask: export FLASK_DEBUG=1
def home():
    return render_template("home.html", team=team)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == 'main':
    app.run(debug = True)