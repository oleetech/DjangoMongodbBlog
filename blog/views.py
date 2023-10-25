from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Category
from .forms import CategoryForm

from .models import Post
from .forms import PostForm
from django.http import HttpResponseBadRequest

from mongoengine.errors import NotUniqueError
from .forms import SubscriberForm
from .models import Subscriber
def home(request):
    if request.method == 'POST':
        subform = SubscriberForm(request.POST)
        if subform.is_valid():
            try:
                subform.save()
                messages.success(request, "Success")
            except NotUniqueError:
                messages.error(request, "Email already exists.")


        else:
            messages.error(request, "Error message goes here.")
        return redirect('home')    
    else:
        subform = SubscriberForm() 
        posts= Post.objects.all().order_by('_created')

        return render(request,'home.html',{'posts':posts,'subform':subform})


def category_list(request):

    return render(request,'category/list.html')

def create_category(request):

 
     
    if request.method=='POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            
            form.save()
            return redirect('home')
    else:
        form = CategoryForm()   
    return render(request,'category/form.html',{'form':form}) 


def edit_category(request,name) :
    category = get_object_or_404(Category,name=name)
    if request.method=='POST':
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form= CategoryForm(instance=category)       
        
    return render(request,'category/form.html',{'form':form})


def delete_category(request,name):
    category = get_object_or_404(Category,name=name)
    if request.method=='POST':
        category.delete()
        return redirect('home')
    else :
        return render(request,'category/delete_confirm.html',{'category':category})
 
from .models import Tags
from .forms import TagsForm
def create_tags(request):
    if request.method=='POST':
        form = TagsForm(request.POST)
        if form.is_valid():
            
            form.save()
            return redirect('home')
    else:
        form = TagsForm()   
    return render(request,'tags/form.html',{'form':form})  


import os
from django.conf import settings
@login_required
def create_post(request) :
    if request.method=='POST':
        form   = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a new Post instance and set the author to the current user
            post = form.save(commit=False)
            post.author = request.user.username  # Set the author to the currently logged-in user        
            
            # Save the image file
            photo_file = form.cleaned_data['photo']
            with open(os.path.join(settings.MEDIA_ROOT, photo_file.name), 'wb') as f:
                for chunk in photo_file.chunks():
                    f.write(chunk)  
                    
            post.photoname ='assets/media/'+ photo_file.name                 
            post.save()
            return redirect('home')
    else:
        form = PostForm()
        return render(request,'post/form.html',{'form':form}) 
    
    
def post_view(request,post_title) :
    post = get_object_or_404(Post,title=post_title)         
    return render(request,'post/postdetails.html',{'post':post})     


def edit_post(request,post_title) :
    post = get_object_or_404(Post,title=post_title)
    if request.method=='POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form= PostForm(instance=post)       
        
    return render(request,'post/form.html',{'form':form})


def post_based_on_category(request,name) :
    # Get the Category object for the specified category name.
    category = Category.objects.get(name=name)    
    posts = Post.objects.filter(categories=category) 
    
     

   
    return render(request,'post/archive.html',{'posts':posts})   


def post_based_on_tag(request,name) :
    # Get the Category object for the specified category name.
    tag = Tags.objects.get(name=name)    
    posts = Post.objects.filter(tags=tag) 
    
     

    
        
    return render(request,'post/archive.html',{'posts':posts}) 


def post_based_on_author(request,name) :
    # Get the Category object for the specified category name.  
    posts = Post.objects.filter(author=name) 
    
     

            
    return render(request,'post/archive.html',{'posts':posts,}) 

from mongoengine.queryset.visitor import Q

def search_post(request):
    search_term = request.GET.get('title', '')

    # Create a query using the Q object for case-insensitive search
    post_filter = Post.objects(Q(title__icontains=search_term) | Q(content__icontains=search_term))

    return render(request, 'post/search_post_list.html', {'filter': post_filter})



from .models import Page
def page_content(request,title):
    page = Page.objects.get(title=title)
    return render(request,'page.html',{'page':page})

from .models import SocialLink
from .forms import SocialLinkForm
def create_social_link(request):

  
     
    if request.method=='POST':
        form = SocialLinkForm(request.POST)
        if form.is_valid():
            
            form.save()
            return redirect('home')
    else:
        form = SocialLinkForm()   
    return render(request,'social/form.html',{'form':form}) 


def subscribe(request):

    
    return render(request, 'home.html', {'subform': subform})


