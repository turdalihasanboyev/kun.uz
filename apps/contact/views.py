from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View

from .models import Contact


class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        file = request.FILES.get('file')

        if name and email and phone_number and message and file:
            contact = Contact()
            contact.name = name
            contact.email = email
            contact.phone_number = phone_number
            contact.subject = subject
            contact.message = message
            contact.file = file
            contact.save()
            messages.success(request, 'Sizning xabaringiz qabul qilindi!')
            return redirect('contact')
        else:
            messages.error(request, "Barcha ma'lumotlarni to'ldiring")
            return redirect('contact')
