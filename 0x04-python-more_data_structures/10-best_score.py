#!/usr/bin/python3
def best_score(a_dictionary):
    best = 0
    best_key = ""
    if a_dictionary is None or len(a_dictionary) == 0:
        return (None)
    for key in a_dictionary:
        if a_dictionary[key] > best:
            best = a_dictionary[key]
            best_key = key
    return best_key

my_dict = {}
best_key = best_score(my_dict)
print("Best score: {}".format(best_key))