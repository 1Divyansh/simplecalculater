def greet():
    name = input("What's your name? ")
    if name.strip():
        print(f"Hello, {name}!")
    else:
        print("Hello, World!")

greet()

