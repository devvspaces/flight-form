from django.views.generic import CreateView, FormView
from django.http import JsonResponse
from .models import FlightForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.conf import settings
from .forms import FlightForm as FlightFormForm
import requests


@method_decorator(csrf_exempt, name='dispatch')
class GetSignature(FormView):
    form_class = FlightFormForm

    def form_valid(self, form):
        base_url = 'https://api.sandbox.signaturit.com/v3/signatures.json'
        headers = {
            'Authorization': f'Bearer {settings.SIGNATURIT_TOKEN}'
        }
        data = {
            "recipients": [
                {
                    "name": form.cleaned_data.get('name'),
                    "email": form.cleaned_data.get('email')
                }
            ],
            "templates": ["#test"],
            "data": {
                "name": form.cleaned_data.get('name'),
                "surname": form.cleaned_data.get('surname')
            },
            "delivery_type": "url"
        }
        response = requests.post(base_url, headers=headers, json=data)

        try:
            data = response.json()
        except Exception:
            return JsonResponse(
                {'error': 'An error occurred while sending the signature!'},
                status=400)

        if response.status_code != 200:
            return JsonResponse(response.json(), status=400)

        return JsonResponse({
            'id': data.get('id'),
            'url': data.get('url')
        })

    def form_invalid(self, form):
        return JsonResponse({'error': form.errors}, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class FlightForm(CreateView):
    model = FlightForm
    fields = '__all__'

    def form_valid(self, form):
        form.save()
        return JsonResponse({
            'message': 'Your form is submitted successfully!'})

    def form_invalid(self, form):
        return JsonResponse({'error': form.errors}, status=400)
