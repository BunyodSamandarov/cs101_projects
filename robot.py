route = ["forward", "left", "forward"]

def make_route(route, position, instruction):
    a = route[:]
    a.append("stop")
    a[instruction] = position
    return a

def reset_route():
    empty = []
    return empty

num = int(input("Enter instruction number: "))
position = input("Enter item: ")
revised = make_route(route,position, num-1)
print(f"Original route: {route}")
print(f"Revised route: {revised}")
revised = reset_route()
print(f"After reset: {revised}")



    