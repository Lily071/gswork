from contextlib import redirect_stderr
import json
import os
from flask import Flask
from flask import render_template, request, url_for, redirect
import facemesh

app = Flask(__name__, template_folder='template')
UPLOAD_FOLDER = './static/imgfile/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=('GET', 'POST'))

def index():

  if request.method == 'POST':
    filename = "tess.mov"
    file = request.files.get('file')
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    filepass = './static/imgfile/tess.mov'
    ans = facemesh.face(filepass)
    print(ans)
    return redirect(url_for('answer'))

  return render_template('index.html')

@app.route('/answer')
def answer():
  imgpass = './static/imgfile/graph.png'
  return render_template('answer.html', imgpass1=imgpass)

if __name__ == "__main__":
  app.run(debug = True)