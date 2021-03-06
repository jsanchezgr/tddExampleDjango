from django.shortcuts import render, redirect

from lists.models import Item


def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST.get('text', ''))
        return redirect('/')

    return render(request, 'home.html', {'item_list': Item.objects.all()})
