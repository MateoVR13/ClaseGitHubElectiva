from django.shortcuts import render

def landing_page(request):
    return render(request, 'productos/landing_page.html')

def guitarra_esp_ltd(request):
    return render(request, 'productos/guitarra_esp_ltd.html')

def eii_eclipse(request):
    return render(request, 'productos/eii_eclipse.html')

def eii_tb7(request):
    return render(request, 'productos/eii_tb7.html')
