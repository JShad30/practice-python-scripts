def question():
    first_name = input("What is your first Name? ")
    last_name = input("What is your last name? ")
    print("Many thanks {}. Now... just a few questions...".format(first_name))
    favourite_animal = input("What is your favourite animal? ")
    print("So... is it fair that I can tell people that your name is {} {}, and your favourite animal is a {}...Yes or No".format(
        first_name, 
        last_name, 
        favourite_animal)
    )
    yes_or_no_answer = input("Type y or n: ")
    if yes_or_no_answer == "y":
        print("Many thanks... I will do that")
    elif yes_or_no_answer == "n":
        print("That's unfair... why did you answer my questions then!")
    else:
        print("That's not a valid answer, so I'm going to carry on regardless")
        reason_no = input("Please tell me: ")
    first_nmumber = input("Give me a number: ")
    second_number = input("Give me another number: ")
    magic_number = int(first_nmumber) + int(second_number)
    print("I'm going to say your magic number is " + str(magic_number))
    password = str(magic_number) + favourite_animal + str(len(last_name))
    print("Your password is: {} Make sure you remember it!".format(password))
    f = open("names.txt", "a")
    f.write("\n" + first_name + " " + last_name + ": " + password)
    
question()

fruits = ["apple", "banana", "strawberry"]

def juicy():
    for fruit in fruits:
        print(fruit)
        
juicy()
    
