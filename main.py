#
class MyTime:
    def __init__(self, minutes, seconds):
        if 0 <= minutes < 60:
            self.minutes = minutes
        if 0 <= seconds < 60:
            self.seconds = seconds

    def __add__(self, other):
        m = self.minutes + other.minutes
        s = self.seconds + other.seconds
        m += s//60
        s = s % 60
        m = m % 60
        return MyTime(m, s)

    def __str__(self):
        return f"<Time {self.minutes:02}:{self.seconds:02}>"


t1 = MyTime(13,00)
t2 = MyTime(53,5)
print(t1 + t2)