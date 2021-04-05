from flask import Flask, render_template, url_for,  flash, redirect, request
import flask
from NBA_Stats_Scraper import NBA_Stats_Scraper
from analysis import analysis, get_name, team_name
app = Flask(__name__)
# debug mode in flask:  export FLASK_DEBUG=1
# export FLASK_APP=app
# export FLASK_ENV=development
# flask run

nba = NBA_Stats_Scraper()
team = team_name()
# team_name = get_name()
# print (type(team_name))

# this is the serects numbers
app.config['SECRET_KEY'] = 'ea7b11f0714027a81e7f81404612d80d'


# this is the home page
@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home(): 
    if request.method == "POST":
        teamone = request.form.get("teamApic", None)
        if teamone!=None:
            return render_template("home.html", teamone = teamone, team = team)  
# ready to create 2 submit button and a predict button for POST. Submit button would use dynamic image, and the predict button will POST
    return render_template("home.html", team = team)



if __name__ == 'main':
    app.run(debug = True)