from django.contrib.auth.models import User
from django.db import models


class TimeAbstractModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


def image_upload_to( filename):
    return f'images/{filename}'


class Post(TimeAbstractModel):

    PEGI_EASY = 1
    PEGI_MEDIUM = 2
    PEGI_HARD = 3
    PEGI_CHOICES = (
        (PEGI_EASY, 'Easy'),
        (PEGI_MEDIUM, 'Medium'),
        (PEGI_HARD, 'Hard')
    )

    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    developer = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    image = models.ImageField(upload_to=image_upload_to, blank=True, null=True)
    difficulty = models.PositiveSmallIntegerField(choices=PEGI_CHOICES)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.pk:
            print('update')
        else:
            print('create')
        return super(Post, self).save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):

        return super(Post, self).delete(using, keep_parents)


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
