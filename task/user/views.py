from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from rest_framework import viewsets
from user.serializers import MoneySerializer, ConvertionSerializer
from user.models import Money, Convertion

# view for the api to show lists of all the dait currency
class MoneyViewSet(viewsets.ModelViewSet):
    queryset = Money.objects.all().order_by('code')
    serializer_class = MoneySerializer

# view for the api to show rate convertion of currency
class ConvertionViewSet(viewsets.ModelViewSet):
    queryset = Convertion.objects.all()
    serializer_class = ConvertionSerializer

# this is the sign up 
def Sign_up(request):
    form  = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            user = authenticate(username=username, password = password1)
            login(request, user)
            return redirect('api/')

    return render(request, 'sign_up.html', {'form':form})