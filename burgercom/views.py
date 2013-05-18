from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from django.core.mail import send_mail

email_template = """
Email Received from burgercom.co.za

Name: %(name)s
Email: %(email_address)s
Message:
%(message)s
"""

email_subject = "Mail from burgercom.co.za"
to_email_address = "adi@burgercom.co.za"

class ContactForm(forms.Form):
    name = forms.CharField()
    email_address = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

def handle_contact(request, template="contactus.html", extra_context=None):
    form_class = ContactForm
    extra_context = extra_context or {}
    if request.method == "POST":
        form = form_class(request.POST, request.FILES)  
        if form.is_valid():
            email = email_template % form.cleaned_data
            extra_context["sent_message"] = "Thanks, we'll get back to you as soon as possible"
            form = form_class()
            send_mail(email_subject, email, "site@burgercom.co.za", [to_email_address])
    else:
        form = form_class()
        
    extra_context["form"] = form
    extra_context["section"] = "contact"
    return render(request, template, extra_context)
    
