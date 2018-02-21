import redis

r = redis.StrictRedis(host='redis-server', port=6379, db=0)
r.set('foo', 'bar')
print(r.get('foo'))
