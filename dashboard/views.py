from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from customer.models import PaymentHistoryModel, OrderModel, CarModel,  CarRentalModel, CarImportModel, BuyCarOrderModel, InstallmentPayment
from decimal import Decimal
from django.contrib.auth.models import User
from accounts.models import UserProfile
from .forms import (BuyCarOrderForm, CarImportForm, CarimportOrderForm, CarModelForm, CarRentalForm,
                    InstallmentPaymentForm, InstallmentRequestForm, RentalOrderForm, UserEditForm, UserProfileEditForm)

# Create your views here.

def home(request):
    clients = User.objects.filter()
    cars = CarModel.objects.filter()
    for_sell_cars = CarModel.objects.filter(offered='1')
    for_rental_cars = CarModel.objects.filter(offered='2')
    for_installment_cars = CarModel.objects.filter(offered='3')

    payments = PaymentHistoryModel.objects.filter()
    pay_payments = PaymentHistoryModel.objects.filter(order_type='1')
    charge_payments = PaymentHistoryModel.objects.filter(order_type='2')
    amount_pay_payments = sum(payment.amount for payment in pay_payments) or 0
    amount_charge_payments = sum(payment.amount for payment in charge_payments) or 0
    balance_amount = sum(client.userprofile.balance for client in clients) or 0
    orders = OrderModel.objects.filter()

    return render(request, 'dashboard/home.html', {
        'clients':clients,
        'cars':cars,
        'for_sell_cars':for_sell_cars,
        'for_rental_cars':for_rental_cars,
        'for_installment_cars':for_installment_cars,
        'balance_amount': balance_amount,
        'payments': payments,
        'amount_pay_payments': amount_pay_payments,
        'amount_charge_payments': amount_charge_payments,
        'orders':orders
    })


def index(request):
    if request.user.is_authenticated:
        return home(request)
    else :
        return redirect('Login')


def view_buy_car_order(request, id):
    user = request.user
    order = OrderModel.objects.get(id=id)
    
    buy_car_form = BuyCarOrderForm(instance=order.buy_car_order)
    if request.method == 'POST':
        buy_car_form = BuyCarOrderForm(request.POST, instance=order.buy_car_order)
        if buy_car_form.is_valid():
            buy_car_form.save()
            return redirect('dashboard_view_buy_car_order', id)
        
    return render(request, 'dashboard/orders/view_buy_car_order.html', {'buy_car_form':buy_car_form})

def view_car_import_order(request, id):
    user = request.user
    order = OrderModel.objects.get(id=id)
    
    buy_car_form = BuyCarOrderForm(instance=order.buy_car_order)  # إذا كانت الطريقة GET، ننشئ النموذج فارغًا
    car_import_form = CarImportForm(instance=order.buy_car_order.car_import)  # إذا كانت الطريقة GET، ننشئ النموذج فارغًا

    if request.method == 'POST':
        buy_car_form = BuyCarOrderForm(request.POST, instance=order.buy_car_order)  # إذا كانت الطريقة GET، ننشئ النموذج فارغًا
        car_import_form = CarImportForm(request.POST, instance=order.buy_car_order.car_import) 
        
        if buy_car_form.is_valid() and car_import_form.is_valid():
            buy_car_form.save()
            car_import_form.save()
            return redirect('dashboard_view_car_import_order', id)
        
    return render(request, 'dashboard/orders/view_car_import_order.html', {'buy_car_form':buy_car_form, 'car_import_form':car_import_form})

def view_car_rental_order(request, id):
    user = request.user
    order = OrderModel.objects.get(id=id)
    
    buy_car_form = RentalOrderForm(instance=order.car_rental_order, car_rental=order.car_rental_order.car_rental)
    if request.method == 'POST':
        buy_car_form = RentalOrderForm(request.POST, instance=order.car_rental_order, car_rental=order.car_rental_order.car_rental)
        if buy_car_form.is_valid():
            buy_car_form.save()
            return redirect('dashboard_view_car_rental_order', id)
        
    return render(request, 'dashboard/orders/view_car_rental_order.html', {'buy_car_form':buy_car_form})

def view_car_installment_order(request, id):
    user = request.user
    order = OrderModel.objects.get(id=id)
    
    buy_car_form = InstallmentRequestForm(instance=order.car_installment_order)
    if request.method == 'POST':
        buy_car_form = InstallmentRequestForm(request.POST, instance=order.car_installment_order)
        if buy_car_form.is_valid():
            buy_car_form.save()
            return redirect('dashboard_view_car_installment_order', id)
    return render(request, 'dashboard/orders/view_car_installment_order.html', {'buy_car_form':buy_car_form})



def edit_for_sell_car(request, car_id):
    car = CarModel.objects.get(id=car_id)
    user = request.user
    form = CarModelForm(instance=car)  # إذا كانت الطريقة GET، ننشئ النموذج فارغًا
    if request.method == 'POST':
        form = CarModelForm(request.POST, request.FILES, instance=car)  # إضافة ملفات مثل الصورة (icon)
        if form.is_valid():
            cropped_main_image = request.FILES.get('cropped_main_image')
            price = request.POST.get('price')
            car = form.save(commit=False)  # حفظ البيانات في قاعدة البيانات
            if cropped_main_image:
                car.icon = cropped_main_image
            car.price = Decimal(price)
            car.save()
            return redirect('dashboard_for_sell_cars')  # توجيه المستخدم إلى صفحة النجاح بعد الحفظ

    return render(request, 'dashboard/cars/edit/edit_for_sell_car.html', {'form': form, 'car':car, 'delete_car_img_url':reverse('delete_car_img')})

def edit_for_installment_car(request, car_id):
    car = CarModel.objects.get(id=car_id)
    user = request.user
    form = CarModelForm(instance=car)  # إذا كانت الطريقة GET، ننشئ النموذج فارغًا
    if request.method == 'POST':
        form = CarModelForm(request.POST, request.FILES, instance=car)  # إضافة ملفات مثل الصورة (icon)
        if form.is_valid():
            price = request.POST.get('price')
            cropped_main_image = request.FILES.get('cropped_main_image')
            car = form.save(commit=False)  # حفظ البيانات في قاعدة البيانات
            if cropped_main_image:
                car.icon = cropped_main_image
            car.price = Decimal(price)
            car.save()
            return redirect('dashboard_for_installment_cars')  # توجيه المستخدم إلى صفحة النجاح بعد الحفظ

    return render(request, 'dashboard/cars/edit/edit_for_installment_car.html', {'form': form, 'car':car, 'delete_car_img_url':reverse('delete_car_img')})

def edit_car_for_rental(request, car_id):
    user = request.user
    rental_car = CarRentalModel.objects.get(id=car_id)
    form = CarModelForm(instance=rental_car.car)  # إذا كانت الطريقة GET، ننشئ النموذج فارغًا
    rental_form = CarRentalForm(instance=rental_car)  # إذا كانت الطريقة GET، ننشئ النموذج فارغًا
    if request.method == 'POST':
        form = CarModelForm(request.POST, request.FILES, instance=rental_car.car)  # إضافة ملفات مثل الصورة (icon)
        rental_form = CarRentalForm(request.POST, instance=rental_car)
        if form.is_valid() and rental_form.is_valid():
            cropped_main_image = request.FILES.get('cropped_main_image')
            car = form.save(commit=False)  # حفظ البيانات في قاعدة البيانات
            if cropped_main_image:
                car.icon = cropped_main_image
            car.save()

            rental_form.save()
            return redirect('dashboard_for_rental_cars')  # توجيه المستخدم إلى صفحة النجاح بعد الحفظ

    return render(request, 'dashboard/cars/edit/edit_car_for_rental.html', {'form': form, 'rental_form':rental_form, 'delete_car_img_url':reverse('delete_car_img')})



def for_sell_cars(request):
    cars = CarModel.objects.filter(offered='1')
    return render(request, 'dashboard/cars/for_sell_cars.html', {'cars':cars})

def for_rental_cars(request):
    cars = CarRentalModel.objects.filter(car__offered='2')
    return render(request, 'dashboard/cars/for_rental_cars.html', {'cars':cars})

def for_installment_cars(request):
    cars = CarModel.objects.filter(offered='3')
    return render(request, 'dashboard/cars/for_installment_cars.html', {'cars':cars})

def Clients(request):
    # clients = User.objects.exclude(is_superuser=True)
    clients = User.objects.all()
    return render(request, 'dashboard/clients/clients.html', {'clients':clients})

def installment_payment_requests(request):
    payments = InstallmentPayment.objects.filter()
    return render(request, 'dashboard/orders/installment_payment_requests.html', {'payments':payments})

def edit_installment_payment_request(request, id):
    payment = InstallmentPayment.objects.get(id=id)
    form = InstallmentPaymentForm(instance=payment)
    if request.method == "POST":
        form = InstallmentPaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect('dashboard_installment_payment_requests')  # Replace with the name of your success URL
    return render(request, 'dashboard/orders/edit_installment_payment_request.html', {'form': form})

def edit_client(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile = get_object_or_404(UserProfile, user=user)
    user_form = UserEditForm(instance=user)
    profile_form = UserProfileEditForm(instance=profile)\
    
    if request.method == "POST":
        user_form = UserEditForm(request.POST, instance=user)
        profile_form = UserProfileEditForm(request.POST, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('dashboard_clients')  # Redirect to the user table page

    return render(request, 'dashboard/clients/edit_client.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'user': user
    })


def orders(request):
    user = request.user

    order_type = request.GET.get('order_type', '')
    
    orders = OrderModel.objects.filter().order_by('-id')
    
    if order_type:orders=orders.filter(order_type=order_type)

    return render(request, 'dashboard/orders/orders.html', {'orders':orders})