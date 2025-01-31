from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile, NotificationsModel
from .forms import UserSignUpModelForm, UserProfileSignUpModelForm, LoginForm, EditDealerProfileModelForm
from .libs import RandomDigitsGen
from django.contrib.auth import logout, login, authenticate
from django.http import JsonResponse
from customer.models import PaymentHistoryModel, CarModel, VehicleModel

# Create your views here.

def Relay(request):
    if request.user.is_authenticated:
        return redirect('buy_cars')
    else:
        return redirect('Login')
def Signup(request):
    user_form = UserSignUpModelForm()
    userprofile_form = UserProfileSignUpModelForm()

    if request.method == 'POST':
        user_form = UserSignUpModelForm(data=request.POST)
        userprofile_form = UserProfileSignUpModelForm(data=request.POST)
        if user_form.is_valid() and userprofile_form.is_valid():
            password = user_form.cleaned_data.get('password')

            user = user_form.save(commit=False)
            user.username = RandomDigitsGen()
            user.set_password(password)

            userprofile = userprofile_form.save(commit=False)
            userprofile.user = user

            user.save()
            userprofile.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('Login')
        else:messages.error(request, user_form.errors+userprofile_form.errors)
    return render(request, 'accounts/signup.html', {'user_form':user_form, "userprofile_form":userprofile_form})

def Login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            
            users = User.objects.filter(email=email)
            if users.exists():
                user = users.first()
                user = authenticate(username=user.username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Login Success')
                    return redirect('landingPage')
                else:messages.error(request, 'wrong email or password')
            else:messages.error(request, 'user dos not exists')
        else:messages.error(request, form.errors)
    return render(request, 'accounts/login.html', {'form':form})

def Logout(request):
    logout(request)
    return redirect('Login')


def Profile(request, id):
    return

def Balance(request):
    user = request.user
    userprofile = user.userprofile

    payments = PaymentHistoryModel.objects.filter()
    amount_payments = sum(payment.amount for payment in payments) or 0
    pay_payments = PaymentHistoryModel.objects.filter(order_type='1')
    charge_payments = PaymentHistoryModel.objects.filter(order_type='2')


    return render(request, 'accounts/balance.html', {'payments':payments, 'amount_payments':amount_payments})

def EditProfile(request):
    user = request.user
    userprofile = user.userprofile

    user_form = UserSignUpModelForm(instance=user)
    userprofile_form = UserProfileSignUpModelForm(instance=userprofile)
    if request.method == 'POST':
        profile_img = request.POST.get('profile_img')
        user_form = UserSignUpModelForm(data=request.POST, instance=user)
        user_form.fields.pop('password')
        userprofile_form = UserProfileSignUpModelForm(data=request.POST, instance=userprofile)
        if user_form.is_valid() and userprofile_form.is_valid():
            user_form.save()
            userprofile = userprofile_form.save(commit=False)
            userprofile.img_base64 = profile_img
            userprofile.save()
        else:
            if user_form.errors:
                messages.error(request, user_form.errors)
            if userprofile_form.errors:
                messages.error(request, userprofile_form.errors)
    return render(request, 'accounts/profile/EditProfile.html', {'user_form':user_form, 'userprofile_form':userprofile_form})


def EditDealerProfile(request):
    user = request.user
    try:dealerprofile = user.dealerprofile
    except:dealerprofile=None
    
    if dealerprofile:
        user_form = EditDealerProfileModelForm(instance=dealerprofile)
        if request.method == 'POST':
            profile_img = request.POST.get('profile_img')
            user_form = EditDealerProfileModelForm(data=request.POST, instance=dealerprofile)
            if user_form.is_valid():
                dealerprofile = user_form.save(commit=False)
                dealerprofile.user = user
                if profile_img:
                    dealerprofile.img_base64 = profile_img
                dealerprofile.save()
            else:
                if user_form.errors:
                    messages.error(request, user_form.errors)
        return render(request, 'accounts/profile/EditDealerProfile.html', {'user_form':user_form})
    else:
        user_form = EditDealerProfileModelForm()
        if request.method == 'POST':
            profile_img = request.POST.get('profile_img')
            user_form = EditDealerProfileModelForm(data=request.POST)
            if user_form.is_valid():
                dealerprofile = user_form.save(commit=False)
                dealerprofile.user = user
                if profile_img:
                    dealerprofile.img_base64 = profile_img
                dealerprofile.save()
            else:
                if user_form.errors:
                    messages.error(request, 'هناك اخطاء في المدخلات')
        return render(request, 'accounts/profile/EditDealerProfile.html', {'user_form':user_form})
    

def ViewProfile(request, user_id):
    provider = User.objects.get(id=user_id)
    provider_userprofile = provider.userprofile
    cars = CarModel.objects.filter(provider=provider)
    # reviews = Review.objects.filter(service_request__service__provider=provider)

    return render(request, 'accounts/profile/ViewProfile.html', {'provider':provider, 'provider_userprofile':provider_userprofile, 'cars':cars})
    

def ViewDealerProfile(request, user_id):
    provider = User.objects.get(id=user_id)
    provider_userprofile = provider.userprofile
    dealerprofile = provider.dealerprofile
    cars = CarModel.objects.filter(provider=provider, offered='1')
    vehicles = VehicleModel.objects.filter(owner=provider)
    # reviews = Review.objects.filter(service_request__service__provider=provider)

    return render(request, 'accounts/profile/ViewDealerProfile.html',
                    {'provider':provider, 'provider_userprofile':provider_userprofile, 'dealerprofile':dealerprofile,
                    'cars':cars, 'vehicles':vehicles})