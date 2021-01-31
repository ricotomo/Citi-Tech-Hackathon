import random
import json

def random_generator():

    randomlist = []
    majors = ["Computer science", "Finance"]
    colleges = ["University of Florida", "Carnegie Mellon"]
    for i in range(0,50):
        tuition = random.randint(10000, 1000000)
        major = random.choices(majors)[0]
        college = random.choices(colleges)[0]
        randomlist.append([tuition, major, college])
    return randomlist

if __name__ == "__main__":
    random_generator()
