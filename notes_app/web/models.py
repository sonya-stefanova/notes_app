from django.db import models

# Create your models here.
'''•	Profile
o	first_name - Character field with max length of 20 characters
o	last_name - Character field with max length of 20 characters
o	age - Integer field
o	image_url - URL field
•	Note
o	title - Character field with max length of 30 characters
o	image_url - URL field
o	content - Text field
'''
class Profile(models.Model):
    FIRST_NAME_MAX_LEN = 20
    LAST_NAME_MAX_LEN = 20

    first_name = models.CharField(max_length=FIRST_NAME_MAX_LEN,verbose_name='First Name')
    last_name = models.CharField(max_length=LAST_NAME_MAX_LEN, verbose_name='Last Name')
    age = models.IntegerField()
    image_url = models.URLField(verbose_name='Link to Profile Image',)

    def __str__(self):
        return self.first_name

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Note(models.Model):
    TITLE_MAX_LEN = 30
    title = models.CharField(max_length=TITLE_MAX_LEN,)
    image_url = models.URLField(verbose_name='Image URL',)
    content = models.TextField()

    def __str__(self):
        return self.title
