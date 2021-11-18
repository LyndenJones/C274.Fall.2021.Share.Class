# NOTE:  JSON *not* needed for Assignment #2
# https://realpython.com/python-json/
# https://www.w3schools.com/python/python_json.asp
# https://docs.python.org/3/library/json.html
import json
# import pickle

d = dict()
d[ "0" ] = "a"
d[ "01" ] = "b"

print("Dump:", d)
with open("cd.json", "w") as fout:
    json.dump(d,fout,indent=4)

with open("cd.json", "r") as fin:
    e = json.load(fin)
print("Load:", e)

encrypted = "0 01 01 0"
for f in encrypted.split():
    print(e[f],end='')
print()
