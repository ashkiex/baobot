from datetime import datetime

class Logger:
    def __init__(self, line):
        self.__line = line

    def set_line(self, line):
        self.__line = line

    def get_line(self):
        return self.__line

    def log(self, line):
        self.set_line(line)
        today = "logs/" + datetime.today().strftime('%d-%m-%Y') + ".txt"
        time = datetime.today().strftime('%H:%M:%S | ')
        f = open(today, 'a')
        f.write(time + self.get_line())
        f.write("\n")
        f.close()
