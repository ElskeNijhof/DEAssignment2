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
from kafka import KafkaConsumer
from jinja2 import Environment


app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def home_page():
  return render_template("home_page.html")





@app.route('/visualization/stream/')
def hello_world():

  
  return render_template("stream_good.html", result = read_from_topic())

def read_from_topic():
      kafka_consumer = KafkaConsumer(bootstrap_servers='34.135.2.155:9092',  # use your VM's external IP Here!
      auto_offset_reset='latest',
      consumer_timeout_ms=1000000)          # latest reads only latest values
      kafka_consumer.subscribe(topics=["output_stream"])
      
      dicts = {}
      j = 0
      for msg in kafka_consumer:      # build a list/dict and append. return up to 100 
        j = j + 1 
        dicts[msg.key.decode("utf-8")] = msg.value.decode("utf-8")
        if j == 30:
          break

      return dicts  

      
@app.route('/best_performing/week:<week>', methods=['GET'])
#@app.route('/best_performing/')
def best_performing(week):
 
  
  storage_client = storage.Client()
  file_data = 'worst_performing.csv'
  bucket_name = 'batch_worst_seconds'
  temp_file_name = 'worst_performing_table'
  bucket = storage_client.get_bucket(bucket_name)
  blob = bucket.get_blob(file_data)
  blob.download_to_filename(temp_file_name)

  
  df_input = pd.read_csv(temp_file_name)
  week_in = int(week)
  df_output_week = df_input[df_input["Week_number"] == week_in]
  #df_output_week1 = df_input[df_input["Week_number"] == 1]
  city_avgNASDelay = df_output_week.drop(columns=["Month", "Week_number", "Worst_performing_cities"])
  
  fig, ax = plt.subplots(figsize=(10,8), facecolor='white', dpi= 80)
  ax.vlines(x=city_avgNASDelay.index, ymin=0, ymax=city_avgNASDelay.avg_NASDelay_sec, color='firebrick', alpha=0.7, linewidth=20)



  # Title, Label, Ticks and Ylim
  ax.set_title('Worst performing NAS', fontdict={'size':18})
  ax.set(ylabel='Average NAS Delay (s)', ylim=(0, 100))
  plt.xticks(city_avgNASDelay.index, city_avgNASDelay.City.str.upper(), rotation=10, horizontalalignment='right', fontsize=10)


  # Convert plot to PNG image
  pngImage = io.BytesIO()
  FigureCanvas(fig).print_png(pngImage)
    
  # Encode PNG image to base64 string
  pngImageB64String = "data:image/png;base64,"
  pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    
  return render_template("complete.html", image=pngImageB64String)

     
  
app.run(host='0.0.0.0', port=5050)
