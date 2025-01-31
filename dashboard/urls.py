from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="dashboard_index"),
    path("clients", views.Clients, name="dashboard_clients"),
    path("edit_client/<int:user_id>/", views.edit_client, name="dashboard_edit_client"),
    path("orders", views.orders, name="dashboard_orders"),
    

    path("for_sell_cars", views.for_sell_cars, name="dashboard_for_sell_cars"),
    path("for_rental_cars", views.for_rental_cars, name="dashboard_for_rental_cars"),
    path("for_installment_cars", views.for_installment_cars, name="dashboard_for_installment_cars"),
    path("installment_payment_requests", views.installment_payment_requests, name="dashboard_installment_payment_requests"),
    path("edit_installment_payment_request/<int:id>", views.edit_installment_payment_request, name="dashboard_edit_installment_payment_request"),
    
    path("edit_for_sell_car/<int:car_id>", views.edit_for_sell_car, name="dashboard_edit_for_sell_car"),
    path("edit_car_for_rental/<int:car_id>", views.edit_car_for_rental, name="dashboard_edit_car_for_rental"),
    path("edit_for_installment_car/<int:car_id>", views.edit_for_installment_car, name="dashboard_edit_for_installment_car"),

    path("view_buy_car_order/<int:id>", views.view_buy_car_order, name="dashboard_view_buy_car_order"),
    path("view_car_import_order/<int:id>", views.view_car_import_order, name="dashboard_view_car_import_order"),
    path("view_car_rental_order/<int:id>", views.view_car_rental_order, name="dashboard_view_car_rental_order"),
    path("view_car_installment_order/<int:id>", views.view_car_installment_order, name="dashboard_view_car_installment_order"),
    path("for_sell_cars/<int:id>", views.for_sell_cars, name="dashboard_for_sell_cars"),
]
