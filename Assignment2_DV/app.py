import os
from flask import Flask
from google.cloud import storage
import pandas as pd
import csv

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/visualization/')
def hello_world():

  storage_client = storage.Client()
  file_data = 'out_ass2_batch'
  bucket_name = 'output_batch_ass2'
  temp_file_name = 'batch_output'
  bucket = storage_client.get_bucket(bucket_name)
  blob = bucket.get_blob(file_data)
  blob.download_to_filename(temp_file_name)

  temp_str=''
  #header = ''
  with open (temp_file_name, "r") as myfile:
    #header = myfile.readline()
    temp_str = myfile.read()  
    
  return temp_str 


 
#@app.route('/best_performing/week:<week>', methods=['GET'])
@app.route('/best_performing/')
def best_performing():
  storage_client = storage.Client()
  file_data = 'best_performing_NAS.csv'
  bucket_name = 'airplane_chris_ass2'
  temp_file_name = 'best_performing_table'
  bucket = storage_client.get_bucket(bucket_name)
  blob = bucket.get_blob(file_data)
  blob.download_to_filename(temp_file_name)

  df_input = pd.read_csv(temp_file_name)
  #df_output_week = df_input[df_input["Week_number"] == '{}'].format(week)
  df_output_week1 = df_input[df_input["Week_number"] == 1]
  html = "<h3>Hello, these are the best performing NAS of this week</h3>"
  return html, df_output_week1


     





  
app.run(host='0.0.0.0', port=5000)
