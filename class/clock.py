class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        print(self.time)
boston_clock = Clock('5:30')
paris_clock = boston_clock
paris_clock.time = '10:30'
boston_clock.print_time()