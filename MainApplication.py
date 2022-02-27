from src.Utils.functions import timeit
from UserInterface import MainUI
import datetime as dt


@timeit
def main():
    print(f"Starting project {dt.datetime.today().strftime('%Y-%m-%d')}")
    window = MainUI("Momentum Trader")  # Name is a silly reference to all those tools from the 1990s
    window.mainloop()


if __name__ == "__main__":
    main()
