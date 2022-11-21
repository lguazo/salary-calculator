from django import forms

class CalculatorForm(forms.Form):
    salary = forms.FloatField(label='Your Salary')