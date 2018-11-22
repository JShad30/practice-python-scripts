fruits = ["an apple", "a banana", "a strawberry", "broccoli", "cabbage", "grapes", "pomegranite", "an avocado", "pineapple", "melon", "grapefruit", "watermelon", "Dragon Fruit", "lettuce", "a pepper", "a kiwi fruit", "some summer fruits", "mango", "an orange", "a tangerine", "a tomato"]

def fruit_and_veg():
    score = 0
    for fruit in fruits:
        print("have you eaten {} today?".format(fruit))
        has_fruit_been_eaten = input("Type y for yes or n for no: ")
        if has_fruit_been_eaten == "y":
            score += 1
    
    first_name = input("Type your first name: ")
    last_name = input("Type your last name: ")
    f = open("fruitnames.txt", "a")
    if score >= 5:
        print("Well done {}. You've eaten {} fruits today which is very good! Well done keep it up!".format(first_name, str(score)))
        f.write("\n" + first_name + " " + last_name + ": " + str(score) + " fruits eaten today. Very good!")
    else:
        print("Sorry {}, you've only eaten {} fruits today. That's not your 5 a day... very naughty!".format(first_name, str(score)))
        f.write("\n" + first_name + " " + last_name + ": " + str(score) + " fruits eaten today. Keep an eye on them!!")
        
fruit_and_veg()
        