from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from .forms import (CarModelForm, BuyCarOrderForm, CarImportForm, CarRentalForm, RentalOrderForm, InstallmentRequestForm,
                    InstallmentPaymentForm, VehicleModelForm, VehicleRentalOrderForm, VehicleServiceForm, VehicleRentalModelForm,
                    BuyVehicleOrderForm)

from .models import (CarImagesModel, CarModel, BuyCarOrderModel, OrderModel, CarImportModel, CarRentalModel,
                    FinancingPlanModel, InstallmentPayment, VehicleModel, VehicleRentalOrder, VehicleImagesModel,
                    )
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import json, datetime
from decimal import Decimal
from django.contrib.auth.models import User
# Create your views here.

def Home(request):
    return render(request, 'customer/home.html')

def buy_cars(request):
    cars = CarModel.objects.filter(offered='1')
    return render(request, 'customer/cars/buy_cars.html', {'cars':cars})

def for_sell_vehicles(request):
    vehicles = VehicleModel.objects.filter()
    return render(request, 'customer/vehicles/vehicles/vehicles.html', {'vehicles':vehicles})

def your_for_sell_vehicles(request):
    user = request.user

    vehicles = VehicleModel.objects.filter(owner=user)
    return render(request, 'customer/vehicles/vehicles/your_vehicles.html', {'vehicles':vehicles})

def view_for_sell_vehicle(request, id):
    user = request.user
    car = VehicleModel.objects.get(id=id)
    buy_car_form = BuyVehicleOrderForm()
    buy_car_form.initial = {
        'name': f'{user.first_name} {user.last_name}',
        'email': user.email,
        'phone': user.userprofile.phone_number,
    }
    return render(request, 'customer/vehicles/vehicles/view_vehicle.html', {'car':car, 'buy_car_form':buy_car_form})


def add_for_sell_vehicle(request):
    user = request.user
    form = VehicleModelForm()  # إذا كانت الطريقة GET، ننشئ النموذج فارغًا
    if request.method == 'POST':
        form = VehicleModelForm(request.POST, request.FILES)  # إضافة ملفات مثل الصورة (icon)
        if form.is_valid():
            cropped_main_image = request.FILES.get('cropped_main_image')
            car = form.save(commit=False)  # حفظ البيانات في قاعدة البيانات
            if cropped_main_image:
                car.image = cropped_main_image
            car.owner = user
            car.save()
            return redirect('your_rental_vehicles')  # توجيه المستخدم إلى صفحة النجاح بعد الحفظ

    return render(request, 'customer/vehicles/vehicles/add_vehicle.html', {'form': form, 'delete_car_img_url':reverse('delete_car_img')})

def edit_for_sell_vehicle(request, vehicle_id):
    user = request.user
    car = VehicleModel.objects.get(id=vehicle_id)
    form = VehicleModelForm(instance=car)  # إذا كانت الطريقة GET، ننشئ النموذج فارغًا
    if request.method == 'POST':
        form = VehicleModelForm(request.POST, request.FILES, instance=car)  # إضافة ملفات مثل الصورة (icon)
        if form.is_valid():
            cropped_main_image = request.FILES.get('cropped_main_image')
            car = form.save(commit=False)  # حفظ البيانات في قاعدة البيانات
            if cropped_main_image:
                car.image = cropped_main_image
            car.save()
            return redirect('your_rental_vehicles')  # توجيه المستخدم إلى صفحة النجاح بعد الحفظ

    return render(request, 'customer/vehicles/vehicles/edit_vehicle.html', {'form': form, 'car':car, 'delete_car_img_url':reverse('delete_car_img')})



def rental_vehicles(request):
    vehicles = VehicleModel.objects.filter()
    return render(request, 'customer/vehicles/rental/vehicles.html', {'vehicles':vehicles})

def your_rental_vehicles(request):
    user = request.user

    vehicles = VehicleModel.objects.filter(owner=user)
    return render(request, 'customer/vehicles/rental/your_vehicles.html', {'vehicles':vehicles})


def view_rental_vehicle(request, id):
    user = request.user
    car = VehicleModel.objects.get(id=id)
    buy_car_form = VehicleRentalOrderForm()
    buy_car_form.initial = {
        'customer_name': f'{user.first_name} {user.last_name}',
        'customer_email': user.email,
        'customer_phone': user.userprofile.phone_number,
    }
    return render(request, 'customer/vehicles/rental/view_vehicle.html', {'car':car, 'buy_car_form':buy_car_form})

def installment_cars(request):
    cars = CarModel.objects.filter(offered='3')
    return render(request, 'customer/cars/installment/buy_cars.html', {'cars':cars})

def rental_cars(request):
    cars = CarRentalModel.objects.filter(car__offered='2')
    return render(request, 'customer/cars/rental/rental_cars.html', {'cars':cars})

def view_car(request, id):
    user = request.user
    car = CarModel.objects.get(id=id)
    buy_car_form = BuyCarOrderForm()
    buy_car_form.initial = {
        'name': f'{user.first_name} {user.last_name}',
        'email': user.email,
        'phone': user.userprofile.phone_number,
    }
    return render(request, 'customer/cars/view_car.html', {'car':car, 'buy_car_form':buy_car_form})

def installment_view_car(request, id):
    user = request.user
    car = CarModel.objects.get(id=id)
    financing_plans = FinancingPlanModel.objects.filter().order_by('years')
    buy_car_form = InstallmentRequestForm()
    return render(request, 'customer/cars/installment/view_car.html', {'car':car, 'financing_plans':financing_plans, 'buy_car_form':buy_car_form})

def view_rental_car(request, id):
    user = request.user
    car = CarRentalModel.objects.get(id=id)
    buy_car_form = RentalOrderForm(car_rental=car)
    buy_car_form.initial = {
        'customer_name': f'{user.first_name} {user.last_name}',
        'customer_email': user.email,
        'customer_phone': user.userprofile.phone_number,
    }
    return render(request, 'customer/cars/rental/view_car.html', {'car':car, 'buy_car_form':buy_car_form})

def view_buy_car_order(request, order_id):
    user = request.user
    order = OrderModel.objects.get(id=order_id)
    buy_car_order = order.buy_car_order
    return render(request, 'customer/orders/view_buy_car_order.html', {'order':order, 'buy_car_order':buy_car_order})

def view_buy_vehicle_order(request, order_id):
    user = request.user
    order = OrderModel.objects.get(id=order_id)
    buy_car_order = order.buy_vehicle_order
    return render(request, 'customer/orders/view_buy_vehicle_order.html', {'order':order, 'buy_car_order':buy_car_order})

def view_vehicle_rental_order(request, order_id):
    user = request.user
    order = OrderModel.objects.get(id=order_id)
    buy_car_order = order.vehicle_rental_order
    
    return render(request, 'customer/orders/view_vehicle_rental_order.html', {'order':order, 'buy_car_order':buy_car_order})

def view_rental_car_order(request, order_id):
    user = request.user
    order = OrderModel.objects.get(id=order_id)
    buy_car_order = order.car_rental_order
    return render(request, 'customer/orders/view_rental_car_order.html', {'order':order, 'buy_car_order':buy_car_order})

def view_installment_car_order(request, order_id):
    user = request.user
    order = OrderModel.objects.get(id=order_id)
    car_installment_order = order.car_installment_order
    Installment_payment_form = InstallmentPaymentForm(order=order)
    Installment_payments = InstallmentPayment.objects.filter(installment_request__ordermodel=order).order_by('-id')
    if request.method == 'POST':
        Installment_payment_form = InstallmentPaymentForm(request.POST, order=order)
        if Installment_payment_form.is_valid():
            Installment_payment = Installment_payment_form.save(commit=False)
            Installment_payment.installment_request = car_installment_order
            Installment_payment.status = 'paid'
            Installment_payment.save()
            return redirect('view_installment_car_order', order_id)
    return render(request, 'customer/orders/view_installment_car_order.html', {'order':order, 'buy_car_order':car_installment_order, 'Installment_payment_form':Installment_payment_form, 'Installment_payments':Installment_payments})

def add_car_for_sell(request):
    user = request.user
    form = CarModelForm()  # إذا كانت الطريقة GET، ننشئ النموذج فارغًا
    if request.method == 'POST':
        form = CarModelForm(request.POST, request.FILES)  # إضافة ملفات مثل الصورة (icon)
        if form.is_valid():
            price = request.POST.get('price')
            cropped_main_image = request.FILES.get('cropped_main_image')
            car = form.save(commit=False)  # حفظ البيانات في قاعدة البيانات
            if cropped_main_image:
                car.icon = cropped_main_image
            car.provider = user
            car.offered = '1'
            car.price = price
            car.save()
            return redirect('your_cars')  # توجيه المستخدم إلى صفحة النجاح بعد الحفظ

    return render(request, 'customer/cars/add_car.html', {'form': form, 'delete_car_img_url':reverse('delete_car_img')})

def add_your_rental_vehicle(request):
    user = request.user
    form = VehicleRentalModelForm()  # إذا كانت الطريقة GET، ننشئ النموذج فارغًا
    if request.method == 'POST':
        form = VehicleRentalModelForm(request.POST, request.FILES)  # إضافة ملفات مثل الصورة (icon)
        if form.is_valid():
            cropped_main_image = request.FILES.get('cropped_main_image')
            car = form.save(commit=False)  # حفظ البيانات في قاعدة البيانات
            if cropped_main_image:
                car.image = cropped_main_image
            car.owner = user
            car.save()
            return redirect('your_rental_vehicles')  # توجيه المستخدم إلى صفحة النجاح بعد الحفظ

    return render(request, 'customer/vehicles/rental/add_vehicle.html', {'form': form, 'delete_car_img_url':reverse('delete_car_img')})

def add_car_for_rental(request):
    user = request.user
    form = CarModelForm()  # إذا كانت الطريقة GET، ننشئ النموذج فارغًا
    rental_form = CarRentalForm()  # إذا كانت الطريقة GET، ننشئ النموذج فارغًا
    if request.method == 'POST':
        form = CarModelForm(request.POST, request.FILES)  # إضافة ملفات مثل الصورة (icon)
        rental_form = CarRentalForm(request.POST)
        if form.is_valid() and rental_form.is_valid():
            cropped_main_image = request.FILES.get('cropped_main_image')
            car = form.save(commit=False)  # حفظ البيانات في قاعدة البيانات
            if cropped_main_image:
                car.icon = cropped_main_image
            car.provider = user
            car.offered = '2'
            car.save()

            rental_form = rental_form.save(commit=False)
            rental_form.car = car
            rental_form.save()
            return redirect('your_rental_cars')  # توجيه المستخدم إلى صفحة النجاح بعد الحفظ

    return render(request, 'customer/cars/rental/add_car.html', {'form': form, 'rental_form':rental_form, 'delete_car_img_url':reverse('delete_car_img')})

def edit_car(request, car_id):
    car = CarModel.objects.get(id=car_id)
    user = request.user
    form = CarModelForm(instance=car)  # إذا كانت الطريقة GET، ننشئ النموذج فارغًا
    if request.method == 'POST':
        form = CarModelForm(request.POST, request.FILES, instance=car)  # إضافة ملفات مثل الصورة (icon)
        if form.is_valid():
            cropped_main_image = request.FILES.get('cropped_main_image')
            print(cropped_main_image)
            car = form.save(commit=False)  # حفظ البيانات في قاعدة البيانات
            if cropped_main_image:
                car.icon = cropped_main_image
            car.provider = user
            car.save()
            return redirect('your_cars')  # توجيه المستخدم إلى صفحة النجاح بعد الحفظ

    return render(request, 'customer/cars/edit_car.html', {'form': form, 'car':car, 'delete_car_img_url':reverse('delete_car_img')})

def edit_rental_vehicle(request, vehicle_id):
    user = request.user
    car = VehicleModel.objects.get(id=vehicle_id)
    form = VehicleRentalModelForm(instance=car)  # إذا كانت الطريقة GET، ننشئ النموذج فارغًا
    if request.method == 'POST':
        form = VehicleRentalModelForm(request.POST, request.FILES, instance=car)  # إضافة ملفات مثل الصورة (icon)
        if form.is_valid():
            cropped_main_image = request.FILES.get('cropped_main_image')
            car = form.save(commit=False)  # حفظ البيانات في قاعدة البيانات
            if cropped_main_image:
                car.image = cropped_main_image
            car.save()
            return redirect('your_rental_vehicles')  # توجيه المستخدم إلى صفحة النجاح بعد الحفظ

    return render(request, 'customer/vehicles/rental/edit_vehicle.html', {'form': form, 'car':car, 'delete_car_img_url':reverse('delete_car_img')})



def your_cars(request):
    provider = request.user
    cars = CarModel.objects.filter(provider=provider, offered='1')
    return render(request, 'customer/cars/your_cars.html', {'cars':cars})

def your_rental_cars(request):
    provider = request.user
    cars = CarRentalModel.objects.filter(car__provider=provider, car__offered='2')
    return render(request, 'customer/cars/rental/your_cars.html', {'cars':cars})

def order_buy_car(request, id):
    user = request.user
    buy_car_form = BuyCarOrderForm()  # إذا كانت الطريقة GET، ننشئ النموذج فارغًا
    car = CarModel.objects.get(id=id)
    if request.method == 'POST':
        buy_car_form = BuyCarOrderForm(request.POST, request.FILES)  # إضافة ملفات مثل الصورة (icon)
        if buy_car_form.is_valid():
            car_import = CarImportModel.objects.create(brand=car.brand, model=car.model, year=car.year, exterior_color=car.exterior_color, interior_color=car.interior_color, price=car.price)
            car_import.icon = car.icon
            car_import.save()
            buy_car_order = buy_car_form.save(commit=False)  # حفظ البيانات في قاعدة البيانات
            buy_car_order.car = car
            buy_car_order.car_import = car_import
            buy_car_order.save()
            order = OrderModel.objects.create(customer=user, order_type='buy_car', buy_car_order=buy_car_order)
            order.save()
            return redirect('your_orders')  # توجيه المستخدم إلى صفحة النجاح بعد 

def order_buy_vehicle(request, id):
    user = request.user
    buy_car_form = BuyVehicleOrderForm()  # إذا كانت الطريقة GET، ننشئ النموذج فارغًا
    car = VehicleModel.objects.get(vehicle_id=id)
    if request.method == 'POST':
        buy_car_form = BuyVehicleOrderForm(request.POST, request.FILES)  # إضافة ملفات مثل الصورة (icon)
        if buy_car_form.is_valid():
            buy_car_order = buy_car_form.save(commit=False)  # حفظ البيانات في قاعدة البيانات
            buy_car_order.vehicle = car
            buy_car_order.save()
            order = OrderModel.objects.create(customer=user, order_type='buy_vehicle', buy_vehicle_order=buy_car_order)
            order.save()
            return redirect('your_orders')  # توجيه المستخدم إلى صفحة النجاح بعد 

def order_car_rental(request, id):
    user = request.user
    car_rental = CarRentalModel.objects.get(id=id)
    buy_car_form = RentalOrderForm(car_rental=car_rental)  # إذا كانت الطريقة GET، ننشئ النموذج فارغًا
    if request.method == 'POST':
        buy_car_form = RentalOrderForm(request.POST, request.FILES, car_rental=car_rental)  # إضافة ملفات مثل الصورة (icon)
        if buy_car_form.is_valid():
            buy_car_order = buy_car_form.save(commit=False)  # حفظ البيانات في قاعدة البيانات
            buy_car_order.car_rental = car_rental
            buy_car_order.cost = buy_car_order.get_cost
            buy_car_order.start_date = timezone.now().date()
            buy_car_order.end_date = (datetime.timedelta(days=int(buy_car_order.rental_days))+ timezone.now()).date()
            buy_car_order.save()
            order = OrderModel.objects.create(customer=user, order_type='car_rental', car_rental_order=buy_car_order)
            order.save()
            return redirect('your_orders')  # توجيه المستخدم إلى صفحة النجاح بعد 

def order_car_installment(request, id):
    user = request.user
    car = CarModel.objects.get(id=id)
    buy_car_form = InstallmentRequestForm()  # إذا كانت الطريقة GET، ننشئ النموذج فارغًا
    if request.method == 'POST':
        buy_car_form = InstallmentRequestForm(request.POST, request.FILES)  # إضافة ملفات مثل الصورة (icon)
        if buy_car_form.is_valid():
            financing_plan_id = request.POST.get('financing_plan')
            financing_plan = FinancingPlanModel.objects.get(id=financing_plan_id)
            buy_car_order = buy_car_form.save(commit=False)  # حفظ البيانات في قاعدة البيانات
            buy_car_order.car = car
            buy_car_order.financing_plan = financing_plan
            buy_car_order.save()
            order = OrderModel.objects.create(customer=user, order_type='car_installment', car_installment_order=buy_car_order)
            order.save()
            return redirect('your_orders')  # توجيه المستخدم إلى صفحة النجاح بعد 

def order_vehicle_rental(request, vehicle_id):
    user = request.user
    car = VehicleModel.objects.get(vehicle_id=vehicle_id)
    buy_car_form = VehicleRentalOrderForm()  # إذا كانت الطريقة GET، ننشئ النموذج فارغًا
    
    if request.method == 'POST':
        buy_car_form = VehicleRentalOrderForm(request.POST, request.FILES)  # إضافة ملفات مثل الصورة (icon)
        if buy_car_form.is_valid():
            buy_car_order = buy_car_form.save(commit=False)  # حفظ البيانات في قاعدة البيانات
            buy_car_order.vehicle = car
            buy_car_order.save()
            order = OrderModel.objects.create(customer=user, order_type='vehicle_rental_order', vehicle_rental_order=buy_car_order)
            order.save()
            return redirect('your_orders')  # توجيه المستخدم إلى صفحة النجاح بعد 

def order_car_import(request):
    user = request.user
    buy_car_form = BuyCarOrderForm()  # إذا كانت الطريقة GET، ننشئ النموذج فارغًا
    car_import_form = CarImportForm()  # إذا كانت الطريقة GET، ننشئ النموذج فارغًا
    if request.method == 'POST':
        buy_car_form = BuyCarOrderForm(request.POST, request.FILES)  # إضافة ملفات مثل الصورة (icon)
        car_import_form = CarImportForm(request.POST, request.FILES)  # إضافة ملفات مثل الصورة (icon)
        if buy_car_form.is_valid() and car_import_form.is_valid():
            car_import = car_import_form.save()
            buy_car_order = buy_car_form.save(commit=False)  # حفظ البيانات في قاعدة البيانات
            buy_car_order.car_import = car_import
            buy_car_order.save()
            order = OrderModel.objects.create(customer=user, order_type='car_import', buy_car_order=buy_car_order)
            order.save()
            return redirect('your_orders')  # توجيه المستخدم إلى صفحة النجاح بعد 

def your_orders(request):
    user = request.user
    buy_car_form = BuyCarOrderForm()  # إذا كانت الطريقة GET، ننشئ النموذج فارغًا
    car_import_form = CarImportForm()  # إذا كانت الطريقة GET، ننشئ النموذج فارغًا
    buy_car_form.initial = {
        'name': f'{user.first_name} {user.last_name}',
        'email': user.email,
        'phone': user.userprofile.phone_number,
    }
    show_car_import = request.GET.get('show_car_import', '')
    user = request.user
    orders = OrderModel.objects.filter(customer=user).order_by('-id')
    return render(request, 'customer/orders/your_orders.html', 
                  {'orders':orders, 'show_car_import':show_car_import,
                   'buy_car_form':buy_car_form,'car_import_form':car_import_form
                   })

@csrf_exempt
def GetVehicleRentalPrice(request, vehicle_id):
    if request.method == 'POST':
        body_json = json.loads(request.body)
        km_count = body_json.get('km_count', '')

        if km_count:
            vehicle = VehicleModel.objects.get(vehicle_id=vehicle_id)
            price_per_km = vehicle.price_per_km  # يمكن تخصيصه بناءً على نوع المركبة
            loading_cost = vehicle.loading_cost  # رسوم التحميل
            unloading_cost = vehicle.unloading_cost  # رسوم التفريغ
            price = (Decimal(km_count) * price_per_km) + loading_cost + unloading_cost
            return JsonResponse({"success":True, 'price':price})
    
    return JsonResponse({"success":False})

@csrf_exempt
def UploadCarImage(request, car_id):
    if request.method == 'POST':
        img = request.FILES.get('uploads[]', '')

        if img:
            car_img = CarImagesModel.objects.create(car_id=car_id, img=img)
            car_img.save()
            return JsonResponse({"success":True, 'id':car_img.id})
    
    return JsonResponse({"success":False})

@csrf_exempt
def UploadVehicleImage(request, vehicle_id):
    if request.method == 'POST':
        img = request.FILES.get('uploads[]', '')

        if img:
            car_img = VehicleImagesModel.objects.create(vehicle_id=vehicle_id, img=img)
            car_img.save()
            return JsonResponse({"success":True, 'id':car_img.id})
    
    return JsonResponse({"success":False})

@csrf_exempt
def delete_car_img(request):
    if request.method == 'POST':
        json_res = json.loads(request.body)
        img_id = json_res.get('img_id', '')
        if img_id:
            car_img = CarImagesModel.objects.get(id=img_id)
            car_img.delete()
            return JsonResponse({"success":True, 'id':img_id})
    return JsonResponse({"success":False})




