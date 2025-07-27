import csv 

from cats.models import Cat, Breed
def run():
    fhand = open('cats/meow.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header, so skip the first row
    for row in reader:
        print(row)
    print("Existing Cat entries:")
    for cat in Cat.objects.all():
        print(f"{cat.nickname}, {cat.breed.name}, {cat.weight}")
    for br in Breed.objects.all():
        print(f"{br.id} | {br.name}")
