from django.shortcuts import render,redirect,get_object_or_404


from .models import SocialLink
def footer_data(request):
    social = SocialLink.objects.all()  # Fetch the data
    return {'footer_pages': social}


from .models import Category
def category_data(request):
    categories = Category.objects.all()  # Fetch the data
    return {'categories': categories}

from .models import Tags
def tag_data(request):
    tags = Tags.objects.all()  # Fetch the data
    return {'tags': tags}


from .models import Page
def page_data(request):
    pages = Page.objects.all()  # Fetch the data
    return {'pages': pages}

