from django.shortcuts import render
from django.views.generic import TemplateView
from .models import ErrorCalculation

class HomeView(TemplateView):
    template_name = 'home.html'

class ErrorCalculatorView(TemplateView):
    template_name = 'error_calculator.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rows'] = range(6)  # Create 6 rows for the grid
        return context
