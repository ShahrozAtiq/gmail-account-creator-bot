from csv import writer
import json
import random

def get_random_name():
    with open("names.json") as f:
        names = json.load(f)
    return random.choice(names)

def get_random_dob():
    months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    year = str(random.randint(1970, 2001))
    month = random.choice(months)
    day = str(random.randint(1, 28))
    return f"{day}/{month}/{year}"

def writeCred(filename,data):
    with open(filename, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(data)