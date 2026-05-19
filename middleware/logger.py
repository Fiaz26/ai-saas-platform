import time

from flask import request

def before_request():
    request.start_time = time.time()

def after_request(response):

    duration = time.time() - request.start_time

    print(
        request.path,
        response.status_code,
        duration
    )

    return response
