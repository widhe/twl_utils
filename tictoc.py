from datetime import datetime


class TicToc:

    def __init__(self):
        self.__start_time = datetime.now()

    def toc(self, sw_return_string=False):
        run_time = datetime.now() - self.__start_time
        days = run_time.days
        hours = run_time.seconds//3600
        mins = (run_time.seconds//60) % 60
        secs = run_time.seconds % 60
        if days > 0:
            str_message = f"Execution time: {days} days {hours} hours {mins} minutes {secs} seconds"
        else:
            str_message = f"Execution time: {hours:02d}:{mins:02d}:{secs:02d}"
        if sw_return_string:
            return str_message
        else:
            print(str_message)
