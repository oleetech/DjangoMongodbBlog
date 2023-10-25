from django_mongoengine import Document
from django_mongoengine.forms import DocumentForm

from .models import Category
class CategoryForm(DocumentForm):
    class Meta:
        model=Category
        fields='__all__'
        
    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control form-control-sm',
                'id': f"{field_name}",
            })    
        
        
from .models import Tags

class TagsForm(DocumentForm)   :
    class Meta:
        model=  Tags
        fields='__all__'         
        
    def __init__(self, *args, **kwargs):
        super(TagsForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control form-control-sm',
                'id': f"{field_name}",
            })            
            
from mongoengine.fields import StringField
from django import forms
# from tinymce.widgets import TinyMCE

            
from .models import Post            
class PostForm(DocumentForm)   :
    content = StringField()
    photo = forms.ImageField(required=False)  # Add the photo field

    class Meta:
        model=  Post
        exclude=['author','photoname','created']             
        
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control form-control-sm',
                'id': f"{field_name}",
            })           
            
            
from .models import SocialLink
class SocialLinkForm(DocumentForm):
    class Meta:
        model=SocialLink
        fields='__all__'   
        
    def __init__(self, *args, **kwargs):
        super(SocialLinkForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control form-control-sm',
                'id': f"{field_name}",
            })      
            
            
from .models import Subscriber

class SubscriberForm(DocumentForm):
    class Meta:
        model = Subscriber
        fields = ['email']                                
        labels = {
            'email': '',  # Set the label to an empty string to remove it
        }
        
    def __init__(self, *args, **kwargs):
        super(SubscriberForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'id': f"{field_name}",
            })      
                    