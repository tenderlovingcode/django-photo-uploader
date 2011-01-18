from django.db import models

from random import random
from hashlib import md5

def random_key():
    return md5(str(random())).hexdigest()

class Photo(models.Model):
	image       = models.FileField(upload_to='photos')
	title       = models.CharField(max_length=255,null=True)
	time        = models.DateTimeField(auto_now=True)
	# for geotagging
	longitude   = models.DecimalField(max_digits=9,decimal_places=7,null=True)
	latitude    = models.DecimalField(max_digits=9,decimal_places=7,null=True)
	# for obfuscated URLs, etc.
	receipt     = models.SlugField(max_length=32,default=random_key)
