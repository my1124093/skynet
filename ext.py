
import redis

device = []
r = redis.StrictRedis(host='localhost', db=0)

def init():
    device.append({'x': 114.504212, 'y': 30.487297 })
    device.append({'x': 114.461884, 'y': 30.512097 })
    device.append({'x': 114.481884, 'y': 30.498497 })

def get_all_info():
    res = []
    for key in range(0, 2):
        d = eval(r.get(key))
        d['id'] = key
        print d
        res.append(d)
    return res

def create_db():
    value0 = {
        'device_id': -1,
        'time': -1,
        'filename': 'a.jpeg'
    }
    r.set(0, value0)
    value1 = {
        'device_id': -1,
        'time': -1,
        'filename': 'b.jpeg'
    }
    r.set(1, value1)
    value2 = {
        'device_id': -1,
        'time': -1,
        'filename': 'c.jpeg'
    }
    r.set(2, value2)
    value3 = {
        'device_id': -1,
        'time': None,
        'filename': 'd.jpeg'
    }
    r.set(3, value3)
