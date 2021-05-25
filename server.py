from flask import Flask, request, render_template, url_for, current_app,g
import json
from ext import *

app = Flask(__name__)


@app.route('/', methods = ['GET'])
def index():
    g.device = device
    static = url_for('static', filename = '')
    return render_template('index.html', **locals())

@app.route('/upload', methods = ['POST'])
def upload():
    pass

@app.route('/get-devices', methods = ['POST'])
def handle_get_all_devices():
    print json.dumps(device)
    return json.dumps(device)

@app.route('/info', methods = ['POST'])
def info():
    return json.dumps(get_all_info())

if __name__ == '__main__':
    init()
    app.debug = True
    # app.run(host='0.0.0.0')

    from gevent.wsgi import WSGIServer
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()

