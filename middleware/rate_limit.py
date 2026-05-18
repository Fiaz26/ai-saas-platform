from flask import request
import time

RATE_STORE = {}

def rate_limit(limit=10):
    def decorator(fn):
        def wrapper(*args, **kwargs):

            ip = request.remote_addr
            now = time.time()

            calls = RATE_STORE.get(ip, [])

            calls = [c for c in calls if now - c < 60]

            if len(calls) >= limit:
                return {"error": "Rate limit exceeded"}, 429

            calls.append(now)
            RATE_STORE[ip] = calls

            return fn(*args, **kwargs)

        return wrapper
    return decorator
