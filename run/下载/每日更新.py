from process.Download.DailyUpdate import DailyUpdate
from run.config import Path, Time, Token


if __name__ == '__main__':

    process = DailyUpdate(start_date='2022-05-20', end_date=Time.current_date)
    process.run()


