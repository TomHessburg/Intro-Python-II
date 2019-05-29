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
