import random

def getAsteroidColor():
    prob = random.randint(0,100)
    if prob > 90:
        return "ice"
    elif prob > 80:
        return "red"
    else:
        return "gray"