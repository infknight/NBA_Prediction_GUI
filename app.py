from flask import Flask, render_template, url_for,  flash, redirect
from NBA_Stats_Scraper import NBA_Stats_Scraper
from analysis import analysis
app = Flask(__name__)

nba = NBA_Stats_Scraper()
team = nba.get_all_stats()

# this is the serects numbers
app.config['SECRET_KEY'] = 'ea7b11f0714027a81e7f81404612d80d'


# this is the home page
@app.route("/")
@app.route("/home")
# debug mode in flask:  export FLASK_DEBUG=1
def home(): 
    return render_template("layout.html", team=team)



if __name__ == 'main':
    app.run(debug = True)