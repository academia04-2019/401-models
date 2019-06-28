from django.shortcuts import render

# Create your views here.
def mostrar_main(request):
    return render(request, 'main.html')