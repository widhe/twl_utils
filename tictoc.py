from datetime import datetime
from datetime import timedelta

class TicToc:

    def __init__(self):
        self.__start_time = datetime.now()

    def toc(self):
        run_time = datetime.now() - self.__start_time
        #run_time = datetime.now() + timedelta(seconds=390000) - self.__start_time
        days = run_time.days
        hours = run_time.seconds//3600
        mins = (run_time.seconds//60) % 60
        secs = run_time.seconds % 60
        if days > 0:
            print(f"Execution time: {days} days {hours} hours {mins} minutes {secs} seconds")
        else:
            print(f"Execution time: {hours:02d}:{mins:02d}:{secs:02d}")
