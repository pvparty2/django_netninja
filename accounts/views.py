from django.shortcuts import render, HttpResponse

# Create your views here.
def sign_up(request):
    return render(request, 'accounts/signup.html')