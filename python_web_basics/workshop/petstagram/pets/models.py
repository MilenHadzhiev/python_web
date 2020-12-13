from django.db import models


class Pet(models.Model):
    CAT = 'Cat'
    DOG = 'Dog'
    PARROT = 'Parrot'
    UNKNOWN = 'Unknown'
    PET_CHOICES = [
        (CAT, 'Cat'),
        (DOG, 'Dog'),
        (PARROT, 'Parrot'),
        (UNKNOWN, 'Unknown'),
    ]

    type = models.CharField(
        max_length=7,
        choices=PET_CHOICES,
        default=UNKNOWN,
    )
    name = models.CharField(max_length=6)
    age = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(
        upload_to='images',
    )

    def __str__(self):
        return f'{self.type} {self.name}'


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    test = models.CharField(max_length=2)

    def __str__(self):
        return f'A like for {self.pet.name}'


class Comment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return self.comment
