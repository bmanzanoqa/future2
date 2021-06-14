from flask import Flask,request
import random
from os import getenv
import random 
import datetime 
import calendar

app = Flask(__name__)

@app.route('/get_fortune/<day>/<int:number>', methods=['POST'])
def get_fortune(day, number):
    if number == 0:
        return f"On {day} YOU WILL LOOSE YOUR HOUSE AND FIANCE, IT'S A TOUGH LIFE!"
    elif number <= 3 :
        return f"On {day}  YOU WILL WIN £50 FROM THE LOTTERY, NOW NOW NO COMPLAINING, EVERY LITTLE HELPS!"
    elif number <= 6:
        return f"On {day}YOU WILL BE INVITED YO COUNTLESS PARTIES!!!"
    elif number <= 9:
            return f"On {day} you will become a millionaire, yeah, right!!!"
    else :
        return f"On {day} you will pass your assessment with flying colours"


if __name__ == "__main__": app.run(host="0.0.0.0", port=5000, debug=True)