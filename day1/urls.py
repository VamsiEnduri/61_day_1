
from django.urls import path
from .views import about,contact,login
urlpatterns=[
    path("about/",about), # link/route, view
    path("contact/",contact),
    path("login/",login),
]