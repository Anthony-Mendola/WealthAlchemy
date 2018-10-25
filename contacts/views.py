from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
  if request.method == 'POST':
    offering_id = request.POST['offering_id']
    offering = request.POST['offering']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']
    affiliate_email = request.POST['affiliate_email']

    #  Check if user has made inquiry already
    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = Contact.objects.all().filter(offering_id=offering_id, user_id=user_id)
      if has_contacted:
        messages.error(request, 'You have already made an inquiry for this offering')
        return redirect('/offerings/'+offering_id)

    contact = Contact(offering=offering, offering_id=offering_id, name=name, email=email, phone=phone, message=message, user_id=user_id )

    contact.save()

    #send email
    send_mail(
      'Investment Offering Inquiry',
      'There has been an inquiry for ' + offering + '. Sign into the admin panel for more info.'
      'wealthyalchemy@gmail.com'
      ['affiliate_email'],
      fail_silently=False
    )

    messages.success(request, 'Your request has been submitted, a affiliate will get back to you soon')
    return redirect('/offerings/'+offering_id)