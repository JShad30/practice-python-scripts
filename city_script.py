import json

city_data = []
with open("city_score.json", "r") as json_data:
    city_data = json.load(json_data)

print(city_data)
    
"""def city_display(city_data):
    print("Let us know what you're interested in. Type y for yes or n for no, to find the cities that are right for you.")
    architecture = input("Architecture: ")
    if architecture.lower() == "y":
        print("What type of architecture are you interested in? Type y or n: ")
        for architecture_choice in city_data.architecture:
            print(architecture_choice)"""
