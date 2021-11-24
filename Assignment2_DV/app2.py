import os
from flask import Flask, render_template
from google.cloud import storage
import pandas as pd
import csv
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
#from kafka import KafkaConsumer


app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/why/')
def hello_world():
 
  html = "<h3>Hello, Streaming Process</h3>"
  return html  

app.run(host='0.0.0.0', port=5000)