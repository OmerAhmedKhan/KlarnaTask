import time
from functools import wraps

def hawk_eye(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        response = {}
        start_time = time.time()
        result = f(*args, **kwds)

        if isinstance(result, int):
            response['result'] = result
        else:
            response['error'] = result

        execution_time =  time.time() - start_time
        response['execution_time'] = execution_time
        return response
    return wrapper