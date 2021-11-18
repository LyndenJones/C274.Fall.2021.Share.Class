# NOTE:  JSON *not* needed for Assignment #2
# https://realpython.com/python-json/
# https://www.w3schools.com/python/python_json.asp
# https://docs.python.org/3/library/json.html
import json
# import pickle

d = dict()
d[ "cat" ] = 2
d[ "dog" ] = 7

print("Dump:", d)
with open("cd.json", "w") as fout:
    json.dump(d, fout)

with open("cd.json", "r") as fin:
    e = json.load(fin)
print(e)
