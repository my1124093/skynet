# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, url_for, g
from ext import *

import json
import time
import redis
import TencentYoutuyun
import redis
import thread

appid = '10071022'
secret_id = 'AKIDH7yi1C6EalvAnKGqtpZAZ5mKhttgpMrD'
secret_key = 'LWmutkPuHUYaVEk3FE4rKezDF8tRn011'
userid= '1'
end_point = TencentYoutuyun.conf.API_YOUTU_END_POINT        #// 优图开放平台
r = redis.StrictRedis(host='localhost', port=6379, db = 0)

app = Flask(__name__)


@app.route('/', methods = ['GET'])
def index():
    g.device = device
    create_db()
    static = url_for('static', filename = '')
    return render_template('index.html', **locals())


def compare(id, image, deviceid):
    youtu = TencentYoutuyun.YouTu(appid, secret_id, secret_key, userid, end_point)
    ret = youtu.FaceCompare(image, './test' + str(deviceid) + '.jpeg')
    ret['personid'] = id
    print ret
    if ret['errorcode'] == 0:
        if ret['similarity'] > 70:
            value = {}
            value['device_id'] = deviceid
            value['time'] = time.time()
            r.set(id, value)



@app.route('/upload', methods = ['POST'])
def upload():
    deviceid = request.args.get('deviceid')
    file = request.files['file']
    file.save('./test' + str(deviceid) + '.jpeg')
    print './test' + str(deviceid) + '.jpeg'
    thread.start_new_thread(compare, (0, 'a.jpeg', deviceid))
    thread.start_new_thread(compare, (1, 'b.jpeg', deviceid))
    thread.start_new_thread(compare, (2, 'c.jpeg', deviceid))
    return "succ"


@app.route('/client')
def client():
    deviceid = request.args.get('deviceid')
    static = url_for('static', filename = '')
    return render_template('client.html', **locals())


@app.route('/get-devices', methods = ['POST'])
def handle_get_all_devices():
    # print json.dumps(device)
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

