import datetime
class Temperature:      # class representing a temperature reading with humidity and timestamp

    def __init__(self, temperature, humidity):      #initialize temperature object with temp, humidity, timestamp
        self.temp = temperature
        self.humid = humidity
        self.time = datetime.datetime.now().time()

    def __str__(self):      # return formatted string representation of temperature object
        return ("Temperature at time " + str(self.time) +
                " is " + str(self.temp) + " degrees with "
                + str(self.humid) + " humidity.")