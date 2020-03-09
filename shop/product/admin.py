from django.contrib import admin

# Register your models here.

from .models import Product

class productAdmin(admin.ModelAdmin):
    #search_fields is a standard method. The strings in the list must match the model. These fields becomes searchable
    search_fields = ['title', 'description', 'price']
    #list_display is a method, all parameters given as a string in the list can be displayed in the admin site
    list_display = ['title', 'description', 'active', 'price']
    #Make the table in admin list editable
    list_editable = ['description', 'price','active']
    #Allow to sort 
    list_filter = ['price', 'title']

    class Meta:
        model = Product

admin.site.register(Product, productAdmin)