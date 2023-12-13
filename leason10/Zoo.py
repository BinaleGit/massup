import json
import os

MY_DATA = 'animals.txt'
animals = []

def load_data():
    global animals
    with open(MY_DATA, 'r') as filehandle:
        animals = json.load(filehandle)

def save_to_file():
    with open(MY_DATA, 'w') as filehandle:
        json.dump(animals, filehandle)

def print_menu():
    print("Hi, Welcome to Bina's Zoo! What would you like to do?")
    print("A - Add An Animal to the Zoo")
    print("P - Print All the Animal's in the Zoo")
    print("D - K*ll All the Animal's in the Zoo")
    print("DL - K*ll the Least Animal")
    # print("D1 - Delete Specific Car You Chose")   # Didn't make it yet :(

def menu_actions(user_selection):
    if user_selection == 'A':
        animals.append({
            "Animal_Type": input("Hi, Welcome to Bina's Zoo. Please enter your Animal Type: "),
            "Name": input("Great! Now The Name: "),
            "Age": input("Now the Age: ")
        })
    elif user_selection == 'P':
        print(animals)
    elif user_selection == 'D':
        animals.clear()
    elif user_selection == 'DL':
        if animals:
            animals.pop()

def main():
    load_data()
    while True:
        print_menu()
        user_selection = input("Type the key for your choice: ")
        os.system('cls' if os.name == 'nt' else 'clear') #clear terminal
        menu_actions(user_selection)
        save_to_file()

main()
    
