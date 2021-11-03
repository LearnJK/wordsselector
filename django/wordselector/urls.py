from django.contrib import admin
from django.urls import path , include

from wordselector import views as dev
from post import views as post
from mduser import views as users

urlpatterns = [
    # DJANGO
    path('django/', include(('frameworkDjango.urls', 'frameworkDjango'), namespace='frameworkDjango')),

    # DEV
    path('', dev.testReq),
    path('dev/<str:page>', dev.dev),
    
    # app post
    path('posts/', post.list_posts),
    
    # app persona
    path('users/login', users.login),

]