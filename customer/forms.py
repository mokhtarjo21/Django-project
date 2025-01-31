from django import forms
from .models import (CarModel, BuyCarOrderModel, CarRentalModel, RentalOrderModel, InstallmentRequestModel,
                     InstallmentPayment, CarImportModel, VehicleService, VehicleModel, VehicleRentalOrder,
                     BuyVehicleOrderModel
                     )

class CarModelForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = [
            'title', 'brand', 'model', 'year', 'category', 
            'exterior_color', 'interior_color', 
            'origin', 'fuel_type', 'transmission_type', 
            'cylinder_count', 'condition', 'engine_capacity', 
            'drivetrain', 'keys_count', 'seat_count', 
            'engine_type', 'fuel_tank_capacity', 'horsepower', 
            'door_count', 'car_id',
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل عنوان السيارة'}),
            'brand': forms.Select(attrs={'class': 'form-control', 'placeholder': 'اختار الماركة'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل موديل السيارة'}),
            'year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل سنة صنع السيارة'}),
            'type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل نوع السيارة'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'اختار الفئة'}),
            
            'exterior_color': forms.Select(attrs={'class': 'form-control', 'placeholder': 'اختار اللون الخارجي'}),
            'interior_color': forms.Select(attrs={'class': 'form-control', 'placeholder': 'اختار اللون الداخلي'}),
            
            'origin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل بلد الوارد'}),
            'fuel_type': forms.Select(attrs={'class': 'form-control', 'placeholder': 'اختار نوع الوقود'}),
            'transmission_type': forms.Select(attrs={'class': 'form-control', 'placeholder': 'اختار نوع القير'}),
            
            'cylinder_count': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'أدخل عدد السلندرات'}),
            'condition': forms.Select(attrs={'class': 'form-control', 'placeholder': 'اختار الحالة'}),
            'engine_capacity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'أدخل حجم المحرك (باللتر)'}),
            'drivetrain': forms.Select(attrs={'class': 'form-control', 'placeholder': 'اختار نوع الدفع'}),
            
            'keys_count': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'أدخل عدد المفاتيح'}),
            'seat_count': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'أدخل عدد المقاعد'}),
            'engine_type': forms.Select(attrs={'class': 'form-control', 'placeholder': 'اختار نوع المحرك'}),
            
            'fuel_tank_capacity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'أدخل سعة خزان الوقود (لتر)'}),
            'horsepower': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'أدخل القدرة بالحصان'}),
            'door_count': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'أدخل عدد الأبواب'}),
            # 'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'سعر السيارة'}),
            
            # 'icon': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'car_id': forms.HiddenInput(),
        }
        
    # def __str__(self):
    #     return f"{self.brand} {self.model} ({self.type})"




class BuyCarOrderForm(forms.ModelForm):
    class Meta:
        model = BuyCarOrderModel
        fields = [
            'name',
            'email',
            'phone',
            'address',
            'notes',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم الكامل للمشتري'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'البريد الإلكتروني'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'رقم الهاتف'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'عنوان التسليم'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'ملاحظات إضافية', 'rows': 3}),
        }


class BuyVehicleOrderForm(forms.ModelForm):
    class Meta:
        model = BuyVehicleOrderModel
        fields = [
            'name',
            'email',
            'phone',
            'address',
            'notes',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم الكامل للمشتري'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'البريد الإلكتروني'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'رقم الهاتف'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'عنوان التسليم'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'ملاحظات إضافية', 'rows': 3}),
        }





class CarImportForm(forms.ModelForm):
    class Meta:
        model = CarImportModel
        fields = [
            'brand',
            'model',
            'year',
            'exterior_color',
            'interior_color',
            'icon',
            'price',
            'condition',
            'country_of_origin',
        ]
        widgets = {
            'brand': forms.Select(attrs={'class': 'form-control', 'placeholder': 'اختر ماركة'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل الموديل'}),
            'year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'أدخل سنة الصنع'}),
            'exterior_color': forms.Select(attrs={'class': 'form-control'}),
            'interior_color': forms.Select(attrs={'class': 'form-control'}),
            'icon': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'صورة للسيارة'}),
            # 'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'أدخل السعر'}),
            'condition': forms.Select(attrs={'class': 'form-control'}),
            'country_of_origin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل بلد المنشأ'}),
        }


class CarimportOrderForm(forms.ModelForm):
    class Meta:
        model = BuyCarOrderModel
        fields = [
            'name',
            'email',
            'phone',
            'address',
            'notes',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم العميل'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'البريد الإلكتروني'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'رقم الهاتف'}),

            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'عنوان التسليم'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'ملاحظات إضافية', 'rows': 3}),
        }


class CarRentalForm(forms.ModelForm):
    class Meta:
        model = CarRentalModel
        fields = ['daily_rate', 'weekly_rate', 'monthly_rate', 'availability']
        widgets = {
            'daily_rate': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'سعر الإيجار اليومي'}),
            'weekly_rate': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'سعر الإيجار الأسبوعي'}),
            'monthly_rate': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'سعر الإيجار الشهري'}),
            'availability': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }



class RentalOrderForm(forms.ModelForm):
    class Meta:
        model = RentalOrderModel
        fields = [
            'customer_name', 'customer_email', 'customer_phone', 
            'rental_days', 'address', 'notes'
        ]
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم العميل'}),
            'customer_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'البريد الإلكتروني'}),
            'customer_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'رقم الهاتف'}),
            'car_rental': forms.Select(attrs={'class': 'form-control'}),
            # 'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            # 'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'rental_days': forms.Select(attrs={'class': 'form-control'}),
            'total_cost': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'التكلفة الإجمالية'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'عنوان التسليم'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'ملاحظات إضافية', 'rows': 3}),
        }



    def __init__(self, *args, **kwargs):
        car_rental = kwargs.pop('car_rental', None)
        super().__init__(*args, **kwargs)

        if car_rental:
            # Set rate_type dynamically based on the selected car_rental
            rate_choices = []
            if car_rental.daily_rate:
                rate_choices.append(('1', f"يومي - {car_rental.daily_rate}"))
            if car_rental.weekly_rate:
                rate_choices.append(('7', f"أسبوعي - {car_rental.weekly_rate}"))
            if car_rental.monthly_rate:
                rate_choices.append(('30', f"شهري - {car_rental.monthly_rate}"))
            self.fields['rental_days'].choices = rate_choices
        else:
            self.fields['rental_days'].choices = []




class InstallmentRequestForm(forms.ModelForm):
    class Meta:
        model = InstallmentRequestModel
        fields = [
            'customer_name',
            'customer_email',
            'customer_phone',
            'notes',
        ]

        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'duration_months': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class InstallmentPaymentForm(forms.ModelForm):
    class Meta:
        model = InstallmentPayment
        fields = [
            'amount_paid'
        ]

        widgets = {
            'amount_paid': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ادخل مبلغ القسط'}),
        }

    def __init__(self, *args, **kwargs):
        # احصل على معلمات إضافية (مثلاً التمويل الذي يشير إلى الحد الأدنى)
        order = kwargs.pop('order', None)
        super().__init__(*args, **kwargs)

        if order:
            # افتراض أن الحد الأدنى موجود في financing_plan.min_down_payment
            min_down_payment = order.car_installment_order.calculate_down_payment()
            reminding_car_price = order.car_installment_order.get_reminding_car_price()
            self.fields['amount_paid'].widget.attrs['min'] = min_down_payment
            self.fields['amount_paid'].widget.attrs['max'] = int(reminding_car_price)
            self.fields['amount_paid'].widget.attrs['value'] = min_down_payment
            self.fields['amount_paid'].help_text = f"الحد الأدنى للدفع: {min_down_payment}"





class VehicleServiceForm(forms.ModelForm):
    class Meta:
        model = VehicleService
        fields = ['name', 'category', 'description', 'base_price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم الخدمة'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'وصف الخدمة'}),
            'base_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'السعر الأساسي'}),
        }

VehicleModelWidgets = {
            'owner': forms.Select(attrs={'class': 'form-control'}),
            'provider_type': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل نوع المركبة'}),
            'brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل ماركة المركبة'}),
            'year': forms.NumberInput(attrs={'class': 'form-control', 'min': 1900, 'max': 2100}),
            'model_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل موديل المركبة'}),
            'truck_category': forms.Select(attrs={'class': 'form-control'}),
            'energy_type': forms.Select(attrs={'class': 'form-control'}),
            'dimensions': forms.TextInput(attrs={'class': 'form-control'}),
            'empty_weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control', 'step': 0.1}),
            'max_power': forms.NumberInput(attrs={'class': 'form-control', 'step': 0.1}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'license_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل رقم الرخصة'}),
            'license_plate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل رقم اللوحة'}),
            'origin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل البلد'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'price_per_km': forms.NumberInput(attrs={'class': 'form-control', 'step': 0.01}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': 0.01}),
            'loading_cost': forms.NumberInput(attrs={'class': 'form-control', 'step': 0.01}),
            'unloading_cost': forms.NumberInput(attrs={'class': 'form-control', 'step': 0.01}),
            'vehicle_id': forms.HiddenInput(),
        }

class VehicleModelForm(forms.ModelForm):
    class Meta:
        model = VehicleModel
        fields = [
            # 'owner',
            # 'provider_type',
            'name',
            'brand',
            'model_number',
            'year',
            'truck_category',
            'energy_type',
            'capacity',
            'dimensions',
            'empty_weight',
            'capacity',
            'max_power',
            'description',
            'license_number',
            'license_plate',
            'origin',
            'price',
            # 'image',
            'vehicle_id',
        ]
        widgets = VehicleModelWidgets

    def clean_year(self):
        """تحقق من أن السنة بين 1900 و 2100."""
        year = self.cleaned_data.get('year')
        if year and (year < 1900 or year > 2100):
            raise forms.ValidationError("يجب أن تكون سنة الصنع بين 1900 و 2100.")
        return year

    def clean_capacity(self):
        """تحقق من أن الحمولة قيمة إيجابية."""
        capacity = self.cleaned_data.get('capacity')
        if capacity and capacity <= 0:
            raise forms.ValidationError("يجب أن تكون الحمولة قيمة موجبة.")
        return capacity

class VehicleRentalModelForm(forms.ModelForm):
    class Meta:
        model = VehicleModel
        fields = [
            # 'owner',
            'provider_type',
            'name',
            'brand',
            'model_number',
            'year',
            'truck_category',
            'energy_type',
            'capacity',
            'dimensions',
            'empty_weight',
            'capacity',
            'max_power',
            'description',
            'license_number',
            'license_plate',
            'origin',
            # 'image',
            'price_per_km',
            'loading_cost',
            'unloading_cost',
            'vehicle_id',
        ]
        widgets = VehicleModelWidgets

    def clean_year(self):
        """تحقق من أن السنة بين 1900 و 2100."""
        year = self.cleaned_data.get('year')
        if year and (year < 1900 or year > 2100):
            raise forms.ValidationError("يجب أن تكون سنة الصنع بين 1900 و 2100.")
        return year

    def clean_capacity(self):
        """تحقق من أن الحمولة قيمة إيجابية."""
        capacity = self.cleaned_data.get('capacity')
        if capacity and capacity <= 0:
            raise forms.ValidationError("يجب أن تكون الحمولة قيمة موجبة.")
        return capacity


class VehicleRentalOrderForm(forms.ModelForm):
    class Meta:
        model = VehicleRentalOrder
        fields = [
            'service',
            'km_count',
            # 'vehicle', 'start_location', 'end_location', 
            'date', 'time',
            # 'status'
            'start_address', 'end_address', 'customer_name', 'customer_email', 'customer_phone', 'notes']
        widgets = {
            'service': forms.Select(attrs={'class': 'form-control'}),
            'km_count': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'onchange':'on_km_change(this)'}),
            'vehicle': forms.Select(attrs={'class': 'form-control'}),
            'start_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نقطة البداية'}),
            'end_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نقطة الوصول'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'التكلفة الإجمالية'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'start_address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'عنوان التحميل'}),
            'end_address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'عنوان التفريغ'}),
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم العميل'}),
            'customer_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'البريد الإلكتروني'}),
            'customer_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'رقم الهاتف'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'ملاحظات إضافية', 'rows': 3}),

        }