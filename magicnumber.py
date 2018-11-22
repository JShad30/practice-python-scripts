scrabble_score = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4, "g": 2, "h": 4, "i": 1, "j": 8, "k": 5, "l": 1, "m": 3, "n": 1, "o": 1, "p": 3, "q": 10, "r": 1, "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8, "y": 4, "z": 10}

def your_magic_number():
    score = 0 
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    f = open("magicnumber.txt", "a")
    for letter in first_name.lower():
        if letter in scrabble_score:
            score += scrabble_score[letter]
    score *= len(last_name)
    print("Thanks for playing {}, your names magic number is {}.".format(first_name, score))
    f.write("\n{} {} - name score: {}".format(first_name, last_name, score))

your_magic_number()