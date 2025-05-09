from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib import messages


@method_decorator(login_required, name='dispatch')
class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'Siz muvaffaqiyatli chiqdingiz!')
        return redirect('home')
