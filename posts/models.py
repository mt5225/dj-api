from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    sex = models.CharField(
        max_length=6,
        choices=[('male', 'male'), ('female', 'female')],
        default='',
    )

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
