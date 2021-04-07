from django.urls import path
from app2 import views

app_name='app2'

urlpatterns = [
    path('sample1/',views.sample1,name='map2'),
]
