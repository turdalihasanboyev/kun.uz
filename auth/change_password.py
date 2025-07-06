from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class ChangePasswordView(View):
    def get(self, request):
        return render(request, 'auth/change_password.html')

    def post(self, request):
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if not request.user.check_password(current_password):
            messages.error(request, "Joriy parol noto'g'ri.")
            return redirect('change_password')

        if new_password != confirm_password:
            messages.error(request, "Yangi parollar mos emas.")
            return redirect('change_password')

        request.user.set_password(new_password)
        request.user.save()
        update_session_auth_hash(request, request.user)
        messages.success(request, "Parolingiz muvaffaqiyatli tarzda yangilandi.")
        return redirect('profile')
