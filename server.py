# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, url_for
from ext import *

import requests
import json
import time
import TencentYoutuyun

appid = '10071022'
secret_id = 'AKIDH7yi1C6EalvAnKGqtpZAZ5mKhttgpMrD'
secret_key = 'LWmutkPuHUYaVEk3FE4rKezDF8tRn011'
userid= '1'

end_point = TencentYoutuyun.conf.API_YOUTU_END_POINT        #// 优图开放平台

app = Flask(__name__)


@app.route('/', methods = ['GET'])
def index():
    g.device = device
    static = url_for('static', filename = '')
    return render_template('index.html', **locals())

@app.route('/upload', methods = ['POST'])
def upload():
    file = request.files['file']
    file.save('./test.jpeg')
    youtu = TencentYoutuyun.YouTu(appid, secret_id, secret_key, userid, end_point)
    ret = youtu.FaceCompare('./a.jpeg','./test.jpeg')
    print ret
    return "succ"


@app.route('/client')
def client():
    static = url_for('static', filename = '')
    return render_template('client.html', **locals())


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

