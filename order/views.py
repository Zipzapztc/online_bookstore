from django.shortcuts import render

# Create your views here.
def order(request):
    context = {}
    return render(request, 'order.html', context)