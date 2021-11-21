import os
import pandas as pd
import requests
from flask import Flask, Response,jsonify

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/visualizationass2/', methods=['GET'])
def Visualization(age, clss):
    #Set up returning text
    html = "<h3>Hello, This is how you performed over the past week</h3>"  

    #Retrieve the score that indicates 'live' or 'die'
    Prediction_api = 'http://predict_service:5000/predict/Age:{}/class:{}'.format(age, clss)
    Request = requests.get(Prediction_api)
    value = float(Request.text)
    
    if value >= 0.5:
        result = "live"
        return html.format(liveOrDie = result)
    else:
        result = "die"
        return html.format(liveOrDie = result)

app.run(host='0.0.0.0', port=5000)