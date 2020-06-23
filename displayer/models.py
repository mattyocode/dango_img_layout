from django.db import models

# Create your models here.
class InstaImage(models.Model):
    '''An instance of displaying scraped images.'''

    date_added = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='/MEDIA_ROOT/insta_img')