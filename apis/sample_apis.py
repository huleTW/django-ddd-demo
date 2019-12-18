from django.urls import path

from application.sample_user_case import sample

urlpatterns = [
    path('samples/', sample)
]