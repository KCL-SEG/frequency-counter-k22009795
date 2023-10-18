"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here

    for i in items:
        if i in frequencies.keys():
            frequencies[i] = frequencies.get(i) + 1
        else:
            frequencies[i] = 1
    return frequencies
