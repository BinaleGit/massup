import json
import os

MY_DATA = 'cars.txt'
cars = []

def load_data():
    global cars
    with open(MY_DATA, 'r') as filehandle:
        cars = json.load(filehandle)

def save_to_file():
    with open(MY_DATA, 'w') as filehandle:
        json.dump(cars, filehandle)

def print_menu():
    print("Hi, Welcome to Bina's Garage! What would you like to do?")
    print("A - Add a Car to the Garage")
    print("P - Print All the Cars in the Garage")
    print("D - Delete All the Cars in the Garage")
    print("DL - Delete the Least Car")
    # print("D1 - Delete Specific Car You Chose")   # Didn't make it yet :(

def menu_actions(user_selection):
    if user_selection == 'A':
        cars.append({
            "Car_Module": input("Hi, Welcome to Bina's Garage. Please enter your car module: "),
            "T_Module": input("Great! Now the T Module: "),
            "Color": input("Now the Color: ")
        })
    elif user_selection == 'P':
        print(cars)
    elif user_selection == 'D':
        cars.clear()
    elif user_selection == 'DL':
        if cars:
            cars.pop()

def main():
    load_data()
    while True:
        print_menu()
        user_selection = input("Type the key for your choice: ")
        os.system('cls' if os.name == 'nt' else 'clear') #clear terminal
        menu_actions(user_selection)
        save_to_file()

main()
    
