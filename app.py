from flask import Flask, render_template
from NBA_Stats_Scraper import NBA_Stats_Scraper
from analysis import analysis
app = Flask(__name__)

nba = NBA_Stats_Scraper()
post = nba.get_all_stats()

@app.route("/")
@app.route("/home")

def home():
    return render_template('home.html', posts=post)


if __name__ == 'main':
    app.run(debug = True)