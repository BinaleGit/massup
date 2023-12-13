def name():
    print("Roee")

def time30():
    for x in range(30):
        print("Roee Bina")

def bigger3 (one,two,three):
    if one > two:
        if one > three:
            print(one)
    else:
        if two>three:
            print(two)
        else:
            print(three)

            #    print(max(one, two, three))
def smaller3():
    one = float(input("Enter the first number: "))
    two = float(input("Enter the second number: "))
    three = float(input("Enter the third number: "))
    
    smallest = min(one, two, three)
    
    print("The smallest number is:", smallest)

smaller3()


