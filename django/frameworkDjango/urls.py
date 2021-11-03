from django.contrib import admin
from django.urls import path
from wordselector import views as dev
urlpatterns = [
    # DJANGO
    # path('django/', include(('frameworkDjango.urls', 'frameworkDjango'), namespace='frameworkDjango')),
    path('admin/', admin.site.urls),
]