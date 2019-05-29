# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = None



    # example of inheritence if needed
# class Waypoint(LatLon):
#     def __init__(self, name, lat, lon):
#         LatLon.__init__(self, lat, lon) #having trouble getting super() to work for whatever reason... will come back to it tomorrow since i believe well be talking about ovjects/inheritence
#         self.name = name
#     def __str__(self):
#         return ', '.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])