"""tutorial_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from people.views import hello_world, PersonDetailView, PeopleView, PeopleCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world),
    path('person/<slug:pk>', PersonDetailView.as_view(), name='person_details'),
    path('create/person', PeopleCreateView.as_view(), name='create_person'),
    path('', PeopleView.as_view(), name='list_people')
]
