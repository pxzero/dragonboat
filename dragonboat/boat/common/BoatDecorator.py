
def post_req(func):
    def wrapper(*args, **kw):
        return func(*args, **kw)

    return wrapper
