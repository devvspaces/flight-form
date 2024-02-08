from django.views.generic import CreateView
from django.http import JsonResponse


class FlightForm(CreateView):
    def form_valid(self, form):
        return JsonResponse({
            'message': 'Your form is submitted successfully!'})

    def form_invalid(self, form):
        return JsonResponse({'error': form.errors}, status=400)
