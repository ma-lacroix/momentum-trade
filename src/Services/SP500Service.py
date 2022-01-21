from src.Models.SP500Model import SP500
from src.Utils.functions import timeit


@timeit
def get_sp500():
    return SP500()


