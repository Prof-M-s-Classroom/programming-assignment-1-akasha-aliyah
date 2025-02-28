import datetime
class Distance:     # a class representing a distance measurement with timestamp

    def __init__(self, distance):       # initializing distance object with distance, timestamp
        self.distance = distance
        self.time = datetime.datetime.now().time()

    def __str__(self):      # return formatted string representation of distance object
        return "Distance from wall is " + str(self.distance) + ""