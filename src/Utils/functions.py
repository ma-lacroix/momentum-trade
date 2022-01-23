import datetime as dt
import math
import time


def timeit(func):
    def timed(*args, **kw):
        start = time.time()
        result = func(*args, **kw)
        end = time.time()
        print(f"Function -> {func.__name__} took {round(start - end,2)} seconds")
        return result
    return timed


def get_date(window, end_date):
    date = dt.datetime.strptime(end_date, '%Y-%m-%d') - dt.timedelta(days=window)
    # weekend
    if date.date().weekday() > 4:
        date -= dt.timedelta(days=6 - date.weekday())
    return date.strftime('%Y-%m-%d')


def division(val1, val2):
    # some stock data might be null
    if val2 <= 0:
        return 0
    else:
        return round((val1 / val2 - 1) * 100, 3)


def log10(val1):
    if abs(val1) == 0:
        return 0
    else:
        return math.log10(abs(val1))