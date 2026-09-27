valid_floors = ["F1", "F2", "F3", "F4", "F5"]
current_floor = 1


def cfg_check(user_input):
    parts = user_input.split(",")
    floors = []
    for p in parts:
        p = p.strip()
        if p not in valid_floors:
            return None
        floors.append(int(p[1:]))
    return floors


def tm_shortest_route(floors, start):
    remaining = floors[:]
    route = []
    position = start
    while remaining:
        nearest = min(remaining, key=lambda f: abs(f - position))
        route.append(nearest)
        remaining.remove(nearest)
        position = nearest
    return route


def dfa_move(current, target):
    if target > current:
        state = "moving_up"
    elif target < current:
        state = "moving_down"
    else:
        state = "idle"
    print(f"DFA: {state} -> arrived at floor {target}")
    return target


print("Smart Elevator (type 'exit' to quit)")

while True:
    user_input = input("\nEnter floor request (e.g. F1,F3): ")
    if user_input.lower() == "exit":
        break

    floors = cfg_check(user_input)
    if floors is None:
        print("CFG: invalid request")
        continue

    print("CFG: valid request")
    route = tm_shortest_route(floors, current_floor)
    print("TM: shortest route is", route)

    for floor in route:
        current_floor = dfa_move(current_floor, floor)

    print("Elevator is now idle at floor", current_floor)