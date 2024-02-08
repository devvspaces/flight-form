from django.views.generic import CreateView
from django.http import JsonResponse
from .models import FlightForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class FlightForm(CreateView):
    model = FlightForm
    fields = '__all__'

    def form_valid(self, form):
        return JsonResponse({
            'message': 'Your form is submitted successfully!'})

    def form_invalid(self, form):
        return JsonResponse({'error': form.errors}, status=400)
