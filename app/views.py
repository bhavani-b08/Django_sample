from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserLogin
from django.views.generic.edit import CreateView 
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

def success(request) :
    # return HttpResponse("Data added successfully")
    return render(request , 'app/success.html')


class Add_data(CreateView) :
    model = UserLogin
    fields = ['username' , 'password']
    template_name = 'app/index.html'
    success_url = reverse_lazy('app:success')

    def form_valid(self, form):
        # Hash the password before saving
        form.instance.set_password(form.instance.password)
        return super().form_valid(form)

@login_required
def secret_page(request) :
    return render(request , 'app/secret.html')


