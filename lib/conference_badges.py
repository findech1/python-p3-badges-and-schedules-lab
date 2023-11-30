def badge_maker(name):
    message = "Hello, my name is " + name + "."
    return message

def batch_badge_creator(names):
    badges = []
    for name in names:
        badge = badge_maker(name)
        badges.append(badge)
    return badges
def assign_rooms(names):
    
    new_list = [f"Hello, {name}! You'll be assigned to room {names.index(name) + 1}!" for name in names]
    return new_list


def printer(names):
    badges = batch_badge_creator(names)
    for badge in badges:
        print(badge)

    room_assignments = assign_rooms(names)
    for assignment in room_assignments:
        print(assignment)