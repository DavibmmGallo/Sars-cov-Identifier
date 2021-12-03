from flask import Flask, render_template,request
import os
from werkzeug.utils import secure_filename

app = Flask(__name__,template_folder=os.getcwd() + "\\Html",
static_folder=os.getcwd() + "\\static",
instance_path=os.getcwd() + "\\upload")


@app.route("/")
def homepage():
    return (
        render_template('mainpage.html')
    ) 

@app.route("/analizar")
def analizer():
    return (
        render_template('Analizer.html')
    ) 
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(os.path.join(app.instance_path, secure_filename(f.filename)))
      return 'file uploaded successfully'
if __name__ == '__main__':
    app.run(debug=True)