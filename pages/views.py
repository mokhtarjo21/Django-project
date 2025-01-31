from django.shortcuts import render, redirect

# Create your views here.

def landingPage(request):
    if request.user.is_authenticated:
        return redirect('buy_cars')
    return render(request, 'pages\index.html')