import time
from Ex_6_Clock_Display.ClockDisplay import ClockDisplay


def clock_display(hour, minute, clock_limit=None):
    stop_clock = True
    display = ClockDisplay(hour, minute)

    while stop_clock:
        display.tick_time()

        if display.get_time() == clock_limit:
            stop_clock = False

        time.sleep(1)


clock_display(15, 59, clock_limit="16:10")
