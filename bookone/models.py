from django.db import models

# Create your models here.

class Lang(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13)
    lang = models.ForeignKey('Lang', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        """String for representing the Model object."""
        return self.title

class Instance(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    due_back = models.DateField(null=True, blank=True)
    def __str__(self):
        """String for representing the Model object."""
        return str(self.book) + " " + str(self.due_back)
