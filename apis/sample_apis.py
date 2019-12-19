from django.urls import path

from applications.sample_user_case import sample

urlpatterns = [
    path('samples/', sample)
]