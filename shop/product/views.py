from django.shortcuts import render
from .forms import ProductForm

# Create your views here.

def productCreateView(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        print('form is valid now to saving')
        print(request.POST['title'])
        print('\n\n')
        form.save()
        form = ProductForm() #clear the fields after saving

    context = {'form' : form}
    
    return render(request, '../templates/product_create.html', context=context)

