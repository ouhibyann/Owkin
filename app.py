from flask import Flask, request
#from utils import allowed_file
#from werkzeug import secure_filename


UPLOAD_FOLDER = ''
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'csv'}


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():

  if request.method == 'POST':
      f = request.files['file']
      f.save(f.filename)
      return 'file uploaded successfully'


if __name__ == "__main__":               
    app.run(host='127.0.0.1',port = 5000) 