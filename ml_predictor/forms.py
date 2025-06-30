from django import forms

class TeslaPredictionForm(forms.Form):
    # Use EXACT encoder classes from your Jupyter output
    MODEL_CHOICES = [
        ('Model S', 'Tesla Model S'),
        ('Model X', 'Tesla Model X'),
    ]
    
    COUNTRY_CHOICES = [
        ('Australia', 'Australia'),
        ('Germany', 'Germany'),
        ('US', 'United States'),
    ]
    
    PURCHASE_CHOICES = [
        ('Cash purchase', 'Cash Purchase'),
        ('Deposit', 'Deposit'),
    ]
    
    QUARTER_CHOICES = [
        (1, 'Q1'), (2, 'Q2'), (3, 'Q3'), (4, 'Q4')
    ]
    
    tesla_model = forms.ChoiceField(
        choices=MODEL_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Tesla Model'
    )
    
    country = forms.ChoiceField(
        choices=COUNTRY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Country'
    )
    
    purchase_type = forms.ChoiceField(
        choices=PURCHASE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Purchase Type'
    )
    
    year = forms.IntegerField(
        initial=2017,
        min_value=2016,
        max_value=2017,
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        label='Year'
    )
    
    quarter = forms.ChoiceField(
        choices=QUARTER_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Quarter'
    )
