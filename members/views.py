from django.shortcuts import render, redirect
from .models import Trainer, Membership, ClassSchedule
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import ContactForm
from .forms import JoinNowForm
from django.conf import settings
import razorpay
from .models import Membership, Payment


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def trainers(request):
    trainers = Trainer.objects.all()
    return render(request, 'trainers.html', {'trainers': trainers})

def plans(request):
    return render(request, 'plans.html', {'plans': plans})

def schedule(request):
    classes = ClassSchedule.objects.all()
    return render(request, 'schedule.html', {'classes': classes})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def join_now(request, plan_name):
    payment = None  # default
    amount = None
    if request.method == 'POST':
        form = JoinNowForm(request.POST)
        if form.is_valid():
            # ✅ Membership ko variable mein save karo
            membership = Membership.objects.create(
                full_name=form.cleaned_data['full_name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                plan=form.cleaned_data['plan']
            )

            # ✅ Plan amount mapping
            plan_amounts = {'Standard': 1500, 'Premium': 2500, 'VIP': 5000}
            amount = plan_amounts.get(plan_name, 500) * 100  # Razorpay mein paisa mein bhejte hain

            # ✅ Razorpay Order create karo
            client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
            payment = client.order.create({
                'amount': amount,
                'currency': 'INR',
                'payment_capture': '1'
            })

            # ✅ Payment record save karo
            Payment.objects.create(
                full_name=membership.full_name,
                email=membership.email,
                phone=membership.phone,
                amount=amount / 100,  # Rupees mein
                payment_id=payment['id'],
                paid=False  # Webhook se TRUE karenge
            )

            # ✅ Checkout page pe bhejo
            context = {
                'form': form,
                'plan_name': plan_name,
                'payment': payment,
                'amount': amount,
                'key_id': settings.RAZORPAY_KEY_ID,
                'membership': membership
            }
            return render(request, 'join_now_form.html', context)

    else:
        form = JoinNowForm(initial={'plan': plan_name})

    return render(request, 'join_now_form.html', {
        'form': form,
        'plan_name': plan_name,
        'payment': payment,
        'amount': amount,
        'key_id': settings.RAZORPAY_KEY_ID,
    })

    
def join_success(request):
    return render(request, 'join_success.html')

def payment_success(request):
    return render(request, 'payment_success.html')
