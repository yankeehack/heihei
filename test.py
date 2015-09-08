from functools import wraps
def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print 'Calling decorated function'
        return f(*args, **kwds)
    return wrapper

def example():
    """Docstring"""
    print 'Called example function'
