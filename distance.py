import datetime
class Distance:     # a class representing a distance measurement with timestamp

    def __init__(self, distance):       # initializing distance object with distance, timestamp
        self.distance = float(distance)
        self.time = datetime.datetime.now().time().strftime('%H:%M:%S')     # stores HH:MM:SS format

    def __str__(self):      # return formatted string representation of distance object
        return f"Distance from wall is {self.distance:.3f}cm at time {self.time}."