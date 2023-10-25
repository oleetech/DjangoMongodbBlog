from django.urls import path
from . import views
from . import context_processors
urlpatterns = [
    path('',views.home,name='home'),
    path('create_category/',views.create_category,name='create_category'),   
    path('edit_category/<str:name>',views.edit_category,name='edit_category'),    
    path('delete_category/<str:name>',views.delete_category,name='delete_category'),
    path('create_tags/',views.create_tags,name='create_tags'),      
    path('create_post/',views.create_post,name='create_post'),
    path('post_view/<str:post_title>',views.post_view,name='post_view'), 
    path('edit_post/<str:post_title>',views.edit_post,name='edit_post'),       
    path('post_based_on_category/<str:name>',views.post_based_on_category,name='post_based_on_category'),      
    path('post_based_on_tag/<str:name>',views.post_based_on_tag,name='post_based_on_tag'),    
    path('post_based_on_author/<str:name>',views.post_based_on_author,name='post_based_on_author'),    
    path('page_content/<str:title>',views.page_content,name='page_content'),    
    path('create_social_link/',views.create_social_link,name='create_social_link'),   
    path('search_post/',views.search_post,name='search_post'),     
    path('subscribe/',views.subscribe,name='subscribe'),            
     
]