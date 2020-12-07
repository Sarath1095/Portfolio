from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="home-page"),
    path("home",views.home,name="home"),
    path("aboutme",views.about,name="aboutme-page"),
    path("mywork",views.works,name="mywork-page"),
    path("contact",views.contact,name="contact-page"),
]


