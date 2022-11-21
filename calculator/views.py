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
        
    return render(request, 'home.html', {
        "salary": 0,
        "net_payment": 0,
        "pension": 0,
        "health": 0,
        "transport_assistant": 0,
        "solidarity_fund": 0
    })