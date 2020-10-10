from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('examplepost/', views.post_example),
    path('examplepost2/', views.post_example_2),
    path('exampleget/', views.get_example)
]
