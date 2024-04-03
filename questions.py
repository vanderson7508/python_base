"""
print("Welcome to the test.")
input("When you are ready press enter: ")

name = input("name:")
print(f"It is nice to meet you {name}")

color = input("What is your favorite color?")
print(f"{color} is a freat color! ")

input("Descibe yourself: ")
print("admirable!")

print("Goodbye.")
"""
def welcome():
    print("Welcome to the test.")
    input("When you are ready press enter: ")

def ask_questions():
    name = input("name:")
    print(f"It is nice to meet you {name}")

    color = input("What is your favorite color?")
    print(f"{color} is a freat color! ")

    input("Descibe yourself: ")
    print("admirable!")

def goodbye():
    print("Goodbye.")

welcome()
ask_questions()
goodbye()
