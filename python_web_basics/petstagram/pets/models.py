from django.db import models


class Pet(models.Model):
    id = models.IntegerField(primary_key=True)
    cat = 'CAT'
    dog = 'DOG'
    parrot = 'PARROT'
    unknown = 'UNKNOWN'
    PET_TYPES = [(cat, 'cat'), (dog, 'dog'), (parrot, 'parrot'), (unknown, 'unknown')]
    type = models.CharField(max_length=7, choices=PET_TYPES, default=unknown)
    name = models.CharField(max_length=6)
    age = models.PositiveIntegerField()
    description = models.TextField(default=' ')
    image_url = models.ImageField(upload_to='images')

    def __str__(self):
        return f'{self.id}:{self.name}, {self.age} years old'


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    test = models.CharField(max_length=2)
