from django.shortcuts import render,redirect
def index(request):
    return render(request, 'index.html')
def shop(request):
    return render(request, 'shop.html')
def product(request):
    return render(request, 'product.html')
