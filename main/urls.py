
from django.urls import path

from main.views import ShowPerson

urlpatterns = [
    path('', ShowPerson.as_view(), name="show_person"),

]
