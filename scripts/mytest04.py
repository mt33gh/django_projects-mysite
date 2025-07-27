import csv 

from cats.models import Cat, Breed
def run():
    fhand = open('cats/meow.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header, so skip the first row
    for row in reader:
        print(row)
    print("Existing Cat and Breed entries:")
    for cat in Cat.objects.all():
        print(f"{cat.id}, {cat.nickname}, {cat.breed.name}, {cat.weight}")
    for br in Breed.objects.all():
        print(f"{br.id} | {br.name}")
    Cat.objects.all().delete()
    print("Existing Cat and Breed entries:")
    for cat in Cat.objects.all():
        print(f"{cat.id}, {cat.nickname}, {cat.breed.name}, {cat.weight}")
    for br in Breed.objects.all():
        print(f"{br.id} | {br.name}")
    # add an entry to Cat
    breed, created = Breed.objects.get_or_create(name="Siamese")
    if created:
        print(f"breed.name is newly created:{breed.id} {breed.name}")
    cat = Cat(nickname="Mimi", breed=breed, weight=5.2)
    cat.save()
    print("Cat added:", cat.nickname, cat.breed.name, cat.weight)
    print("Existing Cat and Breed entries:")
    for cat in Cat.objects.all():
        print(f"{cat.id}, {cat.nickname}, {cat.breed.name}, {cat.weight}")
    for br in Breed.objects.all():
        print(f"{br.id} | {br.name}") 
