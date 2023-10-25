from django_mongoengine import Document
from django_mongoengine.fields import StringField,ListField,ReferenceField,IntField,DateField,FileField,EmailField
from mongoengine import PULL

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class Category(Document):
    name = StringField(unique=True)
    def __str__(self):
        return self.name    
    
class Tags (Document):
    name = StringField(unique=True)
    def __str__(self):
        return self.name      
    
from django.db import models
    
class Post(Document) :
    title=StringField(max_length=200,blank=False)      
    content = StringField(blank=False)
    categories = ReferenceField(Category,default=Category.objects.first())
    tags= ListField(ReferenceField(Tags))    
    author = StringField(blank=True)
    created= DateField(default=datetime.today())
    photoname = StringField(max_length=255, blank=True)  # Store the photo filename
    
from tinymce.models import HTMLField    
class Page(models.Model):
    title = models.CharField(max_length=200)
    content = HTMLField()   
    def __str__(self):
        return self.title  
    
class SocialLink (Document):
    name = StringField(max_length=200)
    url = StringField(max_length=200)   
            
    def __str__(self):
        return self.id    
    
    
class Subscriber(Document):
    email = EmailField(unique=True,default='')

    def __str__(self):
        return self.email        
    
    
 