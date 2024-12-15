from collections import Counter
import json


def words(json, name):
    with open(json,'r') as file:
        data = json.load(file)
    word_counter = Counter()
    if name in data:
        for word in data[name]:
            x = word.split(word)
            word_counter.update(x)
    return word_counter