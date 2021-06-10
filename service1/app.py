from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import desc
import requests 
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

db = SQLAlchemy(app)

class Fortunes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fortune = db.Column(db.String(1000), nullable=False)


@app.route('/')
# @app.route("/home")
def home():
    number = requests.get('http://number_api:5000/get_number').json()['number']
    day = requests.get('http://day_api:5000/get_day')
    fortune = requests.post(f'http://fortune_api:5000/get_fortune/{day.text}/{number}')
    # print(fortune.text)

    last_five_fortune = Fortunes.query.order_by(desc(Fortunes.id)).limit(5).all()
    db.session.add(Fortunes(fortune = fortune.text))
    db.session.commit()
    
    return render_template('home.html', number=number, day=day.text, fortune=fortune.text, all_fortune = last_five_fortune)

    
if __name__ == "__main__": app.run(host="0.0.0.0", port=5000, debug=True)