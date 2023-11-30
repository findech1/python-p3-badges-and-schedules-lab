def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [badge_maker(name) for name in names]
#Usage
names_list = ["Felix", "Ochieng", "Linder"]
badge_messages = batch_badge_creator(names_list)
print(badge_messages)


def assign_rooms(speakers):
    rooms = [f"Room {i}" for i in range(1, 8)]  # Creating a list of room numbers

    if len(speakers) > len(rooms):
    raise ValueError("There are more speakers than available rooms.")

    room_assignments = list(zip(speakers, rooms))
    return [f"{speaker} is assigned to {room}" for speaker, room in room_assignments]

def printer(names):
    return None
