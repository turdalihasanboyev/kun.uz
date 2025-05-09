from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


class LoginView(View):
    def get(self, request):
        return render(request, 'auth/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Siz muvaffaqiyatli login qildingiz!")
            return redirect('profile')
        else:
            messages.error(request, 'Login yoki parol xato!')
            return redirect('login')
