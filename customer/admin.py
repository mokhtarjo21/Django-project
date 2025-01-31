from django.contrib import admin
from .models import (CarModel, CarImagesModel, OrderModel, BuyCarOrderModel, ShippingCompanyModel,
                     CarImportModel, RentalOrderModel, FinancingPlanModel, InstallmentRequestModel,
                     InstallmentPayment, PaymentHistoryModel, VehicleImagesModel, VehicleService)
# Register your models here.
admin.site.register(CarModel)
admin.site.register(CarImagesModel)
admin.site.register(VehicleImagesModel)
admin.site.register(ShippingCompanyModel)
admin.site.register(CarImportModel)
admin.site.register(OrderModel)
admin.site.register(BuyCarOrderModel)
admin.site.register(RentalOrderModel)
admin.site.register(FinancingPlanModel)
admin.site.register(InstallmentRequestModel)
admin.site.register(InstallmentPayment)
admin.site.register(PaymentHistoryModel)
admin.site.register(VehicleService)