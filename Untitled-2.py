def update_light(current):
    # Your code here.
    try:
        name = input()
    except EOFError:
        name = "default_name"
        print(f"Hello, {name}!")

    if current=="yellow":
        return "red"
    if current=="red":
        return "green"
    if current=="green":
        return "yellow"
    a=update_light(current)
    print(a)