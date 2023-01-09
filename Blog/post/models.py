from django.db import models
from autoslug import AutoSlugField


# Create your models here.
from froala_editor.fields import FroalaField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = FroalaField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)
    image = models.ImageField(null=True, blank=True, upload_to='media/')
    slug = AutoSlugField(populate_from='title',unique=True,null=True,default=None)

    CATEGORY_CHOICES = ( 
        ("1", "Programming/Technology"), 
        ("2", "Health/Fitness"), 
        ("3", "Entertainment"), 
        ("4", "Fashion"), 
        ("5", "Food"), 
        ("7", "Business"), 
        ("6", "Sports"), 
        ("8", "Health"),
        ("9", "Education"), 
        ("10", "Others"),
    ) 
    
    category = models.CharField( 
        max_length = 20, 
        choices = CATEGORY_CHOICES, 
        default = '1'
        ) 
