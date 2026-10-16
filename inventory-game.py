# Phase 0: Inventory Game
# Goal: learn classes, __init__, self, methods, __str__, lists and dicts.
# Paste this whole file into ONE Colab cell and run it.


# ---------- CLASS 1: Item ----------
# A class is a blueprint. Each Item we create is an "object" made from it.
class Item:
    def __init__(self, name, weight, value):
        # __init__ runs automatically when you write Item(...).
        # "self" means "this particular object".
        self.name = name        # attributes: data stored inside the object
        self.weight = weight
        self.value = value

    def __str__(self):
        # __str__ controls what print(item) shows.
        return f"{self.name} (weight {self.weight}, value {self.value})"


# ---------- CLASS 2: Inventory ----------
# This class OWNS a list of Items and knows the rules for changing it.
class Inventory:
    def __init__(self, max_weight):
        self.items = []             # a list of Item objects
        self.max_weight = max_weight

    def total_weight(self):
        return sum(item.weight for item in self.items)

    def add(self, item):
        # Methods can enforce rules. Returns True/False so the caller knows what happened.
        if self.total_weight() + item.weight > self.max_weight:
            return False
        self.items.append(item)
        return True

    def remove(self, name):
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                return item         # hand the removed item back
        return None                 # not found

    def __str__(self):
        if not self.items:
            return "Your bag is empty."
        lines = [f"  - {item}" for item in self.items]
        return "\n".join(lines) + f"\nCarrying {self.total_weight()}/{self.max_weight}"


# ---------- THE GAME ----------
class Game:
    def __init__(self):
        self.bag = Inventory(max_weight=10)
        # A dict maps a name (key) to an Item (value) for fast lookup.
        self.room = {
            "sword": Item("sword", 5, 50),
            "shield": Item("shield", 6, 40),
            "potion": Item("potion", 1, 20),
            "coin": Item("coin", 1, 5),
            "anvil": Item("anvil", 12, 15),
        }

    def look(self):
        if not self.room:
            print("The room is empty.")
        for item in self.room.values():
            print(f"  You see: {item}")

    def take(self, name):
        if name not in self.room:            # "in" on a dict checks keys
            print(f"There is no {name} here.")
        elif self.bag.add(self.room[name]):
            del self.room[name]              # remove from room once taken
            print(f"Picked up {name}.")
        else:
            print(f"Too heavy! You can't carry the {name}.")

    def drop(self, name):
        item = self.bag.remove(name)
        if item is None:
            print(f"You don't have a {name}.")
        else:
            self.room[name] = item           # put it back in the room
            print(f"Dropped {name}.")

    def run(self):
        print("Commands: look, take <item>, drop <item>, bag, quit")
        while True:
            command = input("\n> ").strip().lower().split()
            if not command:
                continue
            action = command[0]
            target = command[1] if len(command) > 1 else ""
            if action == "look":
                self.look()
            elif action == "take":
                self.take(target)
            elif action == "drop":
                self.drop(target)
            elif action == "bag":
                print(self.bag)              # calls Inventory.__str__
            elif action == "quit":
                print("Thanks for playing!")
                break
            else:
                print("Unknown command.")


Game().run()
