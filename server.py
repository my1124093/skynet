from flask import Flask, request, render_template, url_for
import redis
from ext import *

app = Flask(__name__)


@app.route('/', methods = ['GET'])
def index():
    static = url_for('static', filename = '')
    return render_template('index.html', **locals())

@app.route('/upload', methods = ['POST'])
def upload():
    pass

@app.route('/get-devices', methods = ['POST'])
def handle_get_all_devices():
    return json.dumps(Device.get_all_devices())

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
    '''
    from gevent.wsgi import WSGIServer
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
    '''
