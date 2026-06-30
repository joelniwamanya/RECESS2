import csv
import json
#from json.decoder import JSONDecodeError
with open  ("students.csv", "w") as file:
    file.write("I love python programming\n")

#with open("students.csv", "a") as file:
    #file.
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

