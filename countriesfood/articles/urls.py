from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:country_id>/', get_category),
    path('article/<int:article_id>/', article),
]
