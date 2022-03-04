import nltk
import random
from nltk.corpus import wordnet as wn

print("Welcome to the dungeon")
name = input("Please enter your name for research purposes: ")

doorNum = [1, 2, 3, 4, 5]
print(name + "... you find yourself in a dark room\n your lying on the ground in a wet puddle...\n you have no "
             "recollection of how you got here.\n Warrily, you rise. \nYou look around, and see " + str(
    doorNum) + "doors.")
door = input("Which one shall you enter?")


def door_badness():
    shuffle_doors = list(doorNum)
    random.shuffle(shuffle_doors)
    print(shuffle_doors)


door_badness()
syn = list()
words = ['Horrible', 'Bad', 'Mediocre', 'Good', 'Amazing']
for synset in wn.synsets(words[0]):
    for lemma in synset.lemmas():
        syn.append(lemma.name())

print('Synonyms: ' + str(syn))
