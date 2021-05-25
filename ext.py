
import redis

device = []
r = redis.StrictRedis(host='localhost', db=0)

def init():
    device.append({'x': 114.504212, 'y': 30.487297 })
    device.append({'x': 114.461884, 'y': 30.512097 })

def get_all_info():
    res = []
    for key in r.scan_iter():
        print key, r.get(key)
        d = r.get(key)
        d['id'] = key
        res.append(d)
    return res

