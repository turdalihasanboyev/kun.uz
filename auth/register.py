from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login


class RegisterView(View):
    def get(self, request):
        return render(request, 'auth/register.html')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Parollar bir hil emas')
            return redirect('register')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username allaqachon mavjud')
            return redirect('register')
        
        user = User.objects.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.save()
        messages.success(request, "Profil muvaffaqiyatli yaratildi!")
        login(request, user)
        return redirect('profile')
