#!/usr/bin/python3
def multiple_returns(sentence):
    multi_return = ()
    if sentence is None or sentence == "":
        multi_return = (0, None)
    else:
        multi_return = (len(sentence), sentence[0])
    return multi_return
