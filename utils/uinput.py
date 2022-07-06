def askint(text="Integer: "):
    while True:
        try:
            return int(input(text))
        except ValueError:
            print("That's not an integer!")

def askfloat(text="Float: "):
    while True:
        try:
            return float(input(text))
        except ValueError:
            print("That's not a float!")

def askstring(text="String: "):
    return input(text)
