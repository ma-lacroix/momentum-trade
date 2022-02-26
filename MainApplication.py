from src.Utils.functions import timeit
from src.Resources.UserInterfaceResource import MainUI


@timeit
def main():
    window = MainUI("StockMaster 2000")
    window.mainloop()


if __name__ == "__main__":
    main()
