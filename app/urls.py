from django.urls import path
from app.views import phrase_of_the_day

urlpatterns = [
    path('', phrase_of_the_day, name='phrase_of_the_day'),
]