from django import forms


class FlightForm(forms.Form):
    name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    address = forms.CharField(widget=forms.Textarea)
    booking_number = forms.CharField(max_length=100)
    flight_number = forms.CharField(max_length=100)
