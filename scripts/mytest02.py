import csv 

from cats.models import Cat, Breed
def run():
    fhand = open('cats/meow.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header, so skip the first row
    for row in reader:
        print(row)
