import datetime


class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        time = datetime.time(self.hours, self.minutes, self.seconds)
        str_time = datetime.time.strftime(time, '%H:%M:%S')
        return str_time

    def next_second(self):
        self.seconds += 1
        if self.seconds > Time.max_seconds:
            self.seconds = 0
            self.minutes += 1
            if self.minutes > Time.max_minutes:
                self.minutes = 0
                self.hours += 1
                if self.hours > Time.max_hours:
                    self.hours = 0
        return Time.get_time(self)


time = Time(9, 30, 59)
print(time.next_second())

time = Time(23, 59, 59)
print(time.next_second())