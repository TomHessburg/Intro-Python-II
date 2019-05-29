# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, items):
        self.name = name
        self.current_room = current_room
        self.items = items
    def tell_items(self):
        if len(self.items) > 0:
            print("\nyoure currently carrying:\n")
            for i in self.items:
                print(f"    {i.name} {i.description}")
        else:
            print("\nyou arent currently carrying any items")
    
    def on_take(self, item_name):
        print(f"\n{self.name} picked up {item_name}")


    # example of inheritence if needed
# class Waypoint(LatLon):
#     def __init__(self, name, lat, lon):
#         LatLon.__init__(self, lat, lon) #having trouble getting super() to work for whatever reason... will come back to it tomorrow since i believe well be talking about ovjects/inheritence
#         self.name = name
#     def __str__(self):
#         return ', '.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])