import time


def timeit(func):
    def timed(*args, **kw):
        start = time.time()
        result = func(*args, **kw)
        end = time.time()
        print(f"Function -> {func.__name__} took {round(start - end,2)} seconds")
        return result

    return timed
