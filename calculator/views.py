from django.shortcuts import render
from .forms import CalculatorForm
from .config import config

# Create your views here.


def HomeView(request):
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            data = config.calculate_salary(form.data['salary'])
            return render(request, 'home.html', data)
    else:
        form = CalculatorForm()
        
    return render(request, 'home.html', None)