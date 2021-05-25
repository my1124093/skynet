import redis

device = []

r = redis.StrictRedis(host='localhost', port=6379, db = 0)

def init():
    device.append({'x': 114.504212, 'y': 30.487297 })
    device.append({'x': 114.461884, 'y': 30.512097 })

def get_all_info():
    res = []
    for key in r.scan_iter():
        print key, r.get(key)
        res.append({key: r.get(key)})

def create_db():
    value0 = {
        'device_id': None,
        'time': None,
        'filename': 'a.jpeg'
    }
    r.set(0, value0)
    value1 = {
        'device_id': None,
        'time': None,
        'filename': 'b.jpeg'
    }
    r.set(1, value1)
    value2 = {
        'device_id': None,
        'time': None,
        'filename': 'c.jpeg'
    }
    r.set(2, value2)
    value3 = {
        'device_id': None,
        'time': None,
        'filename': 'd.jpeg'
    }
    r.set(3, value3)