import os
from flask import Flask
from google.cloud import storage
import pandas as pd


app = Flask(__name__)
app.config["DEBUG"] = True


#import gcsfs # type: ignore


#@app.route('/visualization/week:<week>', methods=['GET'])
@app.route('/visualization/')
def hello_world():


  # fs = gcsfs.GCSFileSystem(project='prefab-clover-330908')
  # fs.ls('output_batch_ass2')
  # with fs.open('output_batch_ass2/out_ass2_batch', 'rb') as f:
  #   df = pd.read_csv(f)
  #   return fs.ls('output_batch_ass2')


  storage_client = storage.Client()
  file_data = 'out_ass2_batch'
  bucket_name = 'output_batch_ass2'
  temp_file_name = 'batch_output'
  bucket = storage_client.get_bucket(bucket_name)
  blob = bucket.get_blob(file_data)
  blob.download_to_filename(temp_file_name)

  #df = pd.read_csv('gs://output_batch_ass2/out_ass2_batch')
  temp_str=''
  with open (temp_file_name, "r") as myfile:
    temp_str = myfile.readline()
    
  return temp_str 
  #return df.head()

#if __name__ == "__main__":
#    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 5000))) 


##
app.run(host='0.0.0.0', port=5000)
##