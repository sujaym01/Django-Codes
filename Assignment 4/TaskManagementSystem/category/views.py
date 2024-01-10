from django.shortcuts import render
from .forms import CategoryForm
# Create your views here.
def add_category(request):
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            print(category_form.cleaned_data)
    else:
        category_form = CategoryForm()
    return render(request, 'category/add_category.html', {'form': category_form})