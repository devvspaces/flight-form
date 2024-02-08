from django.urls import path

from . import views


app_name = 'main'
urlpatterns = [
    path('submit-flight/', views.FlightForm.as_view(), name='flight-form'),
]
