import random
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from datetime import timedelta, date
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.models import CustomUser

User = get_user_model()


def register_view(request):
    if request.method == "POST":
        first = request.POST['firstname']
        last = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        otp = str(random.randint(100000, 999999))

        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            first_name=first,
            last_name=last,
            phone_number=phone,
            password=password,
            is_active=False,
            otp_code=otp
        )

        send_mail(
            subject="Your OTP Code",
            message=f"Your OTP verification code is: {otp}",
            from_email="yourapp@example.com",
            recipient_list=[email]
        )

        request.session['email'] = email
        return redirect('verify_code')

    return render(request, 'register.html')




def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Account is not active. Please verify your email.")
        else:
            messages.error(request, "Invalid credentials.")

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')



def verify_code_view(request):
    if request.method == "POST":
        entered_code = request.POST['otp']
        email = request.session.get('email')
        try:
            user = CustomUser.objects.get(email=email)
            if user.otp_code == entered_code:
                user.is_active = True
                user.is_verified = True
                user.otp_code = ''
                user.save()
                messages.success(request, "Account verified! You can now log in.")
                return redirect('')
            else:
                messages.error(request, "Incorrect OTP code.")
        except CustomUser.DoesNotExist:
            messages.error(request, "User not found.")

    return render(request, 'verify.html')



@login_required
def account_view(request):
    user = request.user
    if request.method == "POST":
        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']
        user.phone_number = request.POST['phone']
        user.save()
        messages.success(request, "Profile updated.")
        return redirect('account')

    return render(request, 'account.html', {"user": user})


@login_required
def change_password_view(request):
    if request.method == "POST":
        current = request.POST['current_password']
        new1 = request.POST['new_password1']
        new2 = request.POST['new_password2']

        if not request.user.check_password(current):
            messages.error(request, "Current password is incorrect.")
        elif new1 != new2:
            messages.error(request, "New passwords do not match.")
        else:
            request.user.set_password(new1)
            request.user.save()
            messages.success(request, "Password changed successfully.")
            return redirect('login')

    return redirect('account')




@login_required
def profile_update(request):
    user = request.user

    if request.method == 'POST':
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        phone = request.POST.get('phone')

        user.first_name = first_name
        user.last_name = last_name
        user.phone_number = phone
        user.save()

        messages.success(request, '✅ Profile updated successfully.')
        return redirect('home')

    return render(request, 'account.html', {'user': user})







def filter_by_period(queryset, period):
    today = date.today()

    if period == 'weekly':
        start_date = today - timedelta(days=7)
    elif period == 'monthly':
        start_date = today.replace(day=1)
    elif period == 'yearly':
        start_date = today.replace(month=1, day=1)
    else:
        return queryset

    return queryset.filter(date__gte=start_date)


