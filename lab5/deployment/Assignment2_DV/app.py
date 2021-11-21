import os
from flask import Flask
from google.cloud import storage

app = Flask(__name__)

##
app.config["DEBUG"] = True
##


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
  with open (temp_file_name, "r") as myfile:
     temp_str = myfile.read().replace('\n', '')

  return temp_str

#if __name__ == "__main__":
#    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 5000))) 


##
app.run(host='0.0.0.0', port=5000)
##