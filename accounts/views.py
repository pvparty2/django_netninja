from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def sign_up(request):
    form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})