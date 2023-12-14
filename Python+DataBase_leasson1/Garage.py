import json
import os

MY_DATA = 'cars.txt'
cars = []
x=True

def load_data():
    global cars
    try:
        with open(MY_DATA, 'r') as filehandle:
            cars = json.load(filehandle)
    except FileNotFoundError:
        # Handle the case where the file does not exist
        pass

def save_to_file():
    with open(MY_DATA, 'w') as filehandle:
        json.dump(cars, filehandle)

def print_menu():
    print("Hi, Welcome to Bina's Garage! What would you like to do?")
    print("A - Add a Car to the Garage")
    print("P - Print All the Cars in the Garage")
    print("D - Delete All the Cars in the Garage")
    print("DL - Delete the Least Car")
    print("X - Exit")
    # print("D1 - Delete Specific Car You Chose")   # Didn't make it yet :(

def menu_actions(user_selection):
    global x
    if user_selection == 'A':
        add_car()
    elif user_selection == 'P':
        print_cars()
    elif user_selection == 'D':
        delete_all_cars()
    elif user_selection == 'DL':
        delete_least_car()
    elif user_selection == 'X':
        os.system('cls' if os.name == 'nt' else 'clear')  # clear terminal
        save_to_file()
        x=False
        print("Bye Bye!")

def add_car():
    cars.append({
        "Car_Module": input("Hi, Welcome to Bina's Garage. Please enter your car module: "),
        "T_Module": input("Great! Now the T Module: "),
        "Color": input("Now the Color: ")
    })

def print_cars():
    if not cars:
        print("No Cars In The Garage")
    else:
        print(cars)

def delete_all_cars():
    cars.clear()

def delete_least_car():
    if cars:
        cars.pop()

def main():
    global x
    os.system('cls' if os.name == 'nt' else 'clear')  # clear terminal
    load_data()
    
    while  x==True:
        print_menu()
        user_selection = input("Type the key for your choice: ").upper()
        os.system('cls' if os.name == 'nt' else 'clear')  # clear terminal
        menu_actions(user_selection)

if __name__ == "__main__":
    main()
