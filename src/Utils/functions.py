import time


def timeit(func):
    def timed(*args, **kw):
        start = time.time()
        result = func(*args, **kw)
        end = time.time()
        print(f"{func.__name__} took %2.4f {start - end} seconds")
        return result

    return timed
