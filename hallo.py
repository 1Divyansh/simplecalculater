def greet():
    name = input("What's your name? ")
    a = 45
    b = 68
    if name.strip():
        print(f"Hello, {name}!")
    else:
        print("Hello, World!")

greet()

