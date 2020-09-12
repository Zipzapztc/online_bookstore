from django.shortcuts import render

# Create your views here.
def favorite(request):
    context = {}
    return render(request, 'favorite.html', context)