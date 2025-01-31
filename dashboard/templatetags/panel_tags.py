from django import template
from django.template.defaultfilters import stringfilter
from customer.models import CarImagesModel, CarModel
from django.conf import settings
import random, json

register = template.Library()

# @register.simple_tag
# @stringfilter
# def get_car_images(car_id):
#     images = CarImagesModel.objects.filter(car_id=car_id)
#     return images
