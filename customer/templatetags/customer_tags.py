from django import template
from django.template.defaultfilters import stringfilter
from customer.models import CarImagesModel, CarModel, OrderModel, VehicleImagesModel
from django.conf import settings
import random, json

register = template.Library()

@register.simple_tag
@stringfilter
def get_car_images(car_id):
    images = CarImagesModel.objects.filter(car_id=car_id)
    return images

@register.simple_tag
@stringfilter
def get_vehicle_images(vehicle_id):
    images = VehicleImagesModel.objects.filter(vehicle_id=vehicle_id)
    return images

@register.simple_tag
@stringfilter
def get_installment_down_payment(car_id, financing_plan_id):
    car = CarModel.objects.get(id=car_id)
    down_payment = car.calculate_down_payment_by_financing_plan(financing_plan_id)
    return down_payment

@register.simple_tag
@stringfilter
def get_full_car_price_by_financing_plan(car_id, financing_plan_id):
    car = CarModel.objects.get(id=car_id)
    down_payment = car.get_full_car_price_by_financing_plan(financing_plan_id)
    return down_payment

@register.simple_tag
@stringfilter
def get_user_orders(user_id):
    orders = OrderModel.objects.filter(customer__id=user_id)
    return orders
