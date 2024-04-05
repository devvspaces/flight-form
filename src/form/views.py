from django.views.generic import CreateView, FormView
from django.http import JsonResponse
from .models import FlightForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from signaturit_sdk.signaturit_client import SignaturitClient
from django.conf import settings
from .forms import FlightForm as FlightFormForm


@method_decorator(csrf_exempt, name='dispatch')
class GetSignature(FormView):
    form_class = FlightFormForm

    def form_valid(self, form):
        client = SignaturitClient(
            settings.SIGNATURIT_TOKEN)
        response = client.create_signature([], {
            'name': 'John',
            'email': 'john.doe@gmail.com'
        }, {
            'delivery_type': 'url',
            'templates': ['89dca1ff-e048-4227-a07e-cb3667eba2a3'],
            'data': {
                'name': form.cleaned_data['name'],
                'surname': form.cleaned_data['surname'],
            }
        })
        print(response)
        return JsonResponse({
            'message': 'Signature was sent successfully!',
            'signature_id': response['id']
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
