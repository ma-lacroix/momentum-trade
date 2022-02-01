import datetime as dt
import math
import time
import os


def timeit(func):
    def timed(*args, **kw):
        start = time.time()
        result = func(*args, **kw)
        end = time.time()
        print(f"Function -> {func.__name__} took {round(start - end, 2)} seconds")
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


def compile_cpp(libName='src/Utils/cpp_sharpe', sourceFile='src/Utils/sharpe'):
    os.system("g++ --std=c++17 -shared -Wl,-install_name,{n}.so -o {n}.so -fPIC {s}.cpp " \
              "-I/Library/Frameworks/Python.framework/Versions/3.9/include/python3.9" \
              .format(n=libName, s=sourceFile))
