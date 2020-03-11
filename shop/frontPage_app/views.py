from django.shortcuts import render
from django.shortcuts import HttpResponse
from .forms import addressForm

# Create your views here.

def frontPageView(request):
    form  = addressForm()
    context = dict()

    if request.method == 'POST':
        form = addressForm(request.POST or None)
        if form.is_valid():
            print('this form is valid')
            print(form.cleaned_data)
            print('cleaned data end')
            if form.cleaned_data['postnr'] == 2400: # In real production, we will be looking up on an internal dictionary for a match
                context['postcode_delivery'] = 'Vi leverer til dit postnummer!'
                context['form'] = form 
            else:
                context['postcode_delivery'] = 'Vi leverer desværre ikke til dit postnummer, men du kan afhente dimsum box hos Hidden Dimsum Nytorv 19, 1450 København K'
                context['form'] = form
        
    else:
        context['form'] = form 
        context['postcode_delivery'] = ''

    return render(request, 'index.html', context = context)

