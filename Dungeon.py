import nltk
import random
from nltk.corpus import wordnet as wn


def start():
    # Welcome the player to our game
    print("Welcome to the dungeon")
    name = input("Please enter your name for research purposes: ")

    print(name + "... you find yourself in a dark room\n your lying on the ground in a wet puddle...\n you have no "
                 "recollection of how you got here.\n Warrily, you rise. \nYou look around, and see " + str(
        doorNum()) + "doors.")


# get the number of doors. Will later be rng
def doorNum():
    doorNum = [1, 2, 3, 4, 5]
    return doorNum


def chooseDoor():
    door = int(input("Which one shall you enter?"))
    return door


def door_badness():
    shuffle_doors = doorNum()
    print("unshuffled: " + str(shuffle_doors))
    random.shuffle(shuffle_doors)
    print("shuffled: " + str(shuffle_doors))
    badness = shuffle_doors.index(chooseDoor())
    print("badness: " + str(badness))
    return badness


def generate_keywords():
    syn = list()
    words = ['Amazing', 'Good', 'Mediocre', 'Bad', 'Horrible']
    descriptor = words[door_badness()]
    print(str(descriptor))
    for synset in wn.synsets(descriptor):
        for lemma in synset.lemmas():
            syn.append(lemma.name())

    print('Synonyms: ' + str(syn))

# now we need to randomly generate a story

# start()
generate_keywords()
