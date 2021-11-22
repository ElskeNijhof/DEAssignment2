import os
from flask import Flask
from google.cloud import storage
import pandas as pd


app = Flask(__name__)
app.config["DEBUG"] = True

#@app.route('/visualization/week:<week>', methods=['GET'])
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
  header = ''
  with open (temp_file_name, "r") as myfile:
    header = myfile.readline()
    temp_str = myfile.read()  # moet nog gefixt worden
    
  return header, temp_str 


 
@app.route('/best_performing/week:<week>', methods=['GET'])
def best_performing(week):
  storage_client = storage.Client()
  file_data = 'best_performing_NAS'
  bucket_name = 'airplane_chris_ass2'
  temp_file_name = 'best_performing_table'
  bucket = storage_client.get_bucket(bucket_name)
  blob = bucket.get_blob(file_data)
  blob.download_to_filename(temp_file_name)


app.run(host='0.0.0.0', port=5000)
