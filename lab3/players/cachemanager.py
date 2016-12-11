import redis
import json

class Cache:
    def __init__(self):
        self.r = redis.Redis(host='localhost', port=6379)
        self.current_index = 0
        self.r.flushall()


