from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from slack_op import parcel_notice, image_to_slack, image_to_slack2 
app = Flask(__name__)

@app.route('/')
def index():
        return 'Slack Bot Index Page'

@app.route('/user/<username>')
def show_user_name(username):
    parcel_notice(username)
    return 'Slack user: {}'.format(username)

@app.route('/upload', endpoint='upload_file1')
def upload_file1():
   return render_template('upload.html')

@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('/tmp/' + secure_filename(f.filename))
        image='/tmp/'+f.filename
        image_to_slack(image)
        return 'file: {} uploaded'.format(f.filename)

@app.route('/slack', methods=['GET', 'POST'])
def slack_notify():
    if request.method == 'POST':
        f = request.files['file']
        user = request.form['username']
        print "slack_notify: {}".format(user)
        f.save('/tmp/' + secure_filename(f.filename))
        image='/tmp/'+f.filename
        image_to_slack2(image, user)
        try:
          os.remove(image)
        except:
          pass
        return 'file: {} uploaded'.format(f.filename)

if __name__ == '__main__':
    app.run('0.0.0.0', '5000', True)