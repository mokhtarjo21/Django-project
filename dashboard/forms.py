from django import forms
from  customer.models import CarModel, BuyCarOrderModel, CarRentalModel, RentalOrderModel, InstallmentRequestModel, InstallmentPayment, CarImportModel
from django.contrib.auth.models import User
from accounts.models import UserProfile


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'gender', 'balance']



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
            
            'shipping_company',
            'tracking_number',
            'shipping_cost',
            'delivery_date',

            'status',
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم الكامل للمشتري'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'البريد الإلكتروني'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'رقم الهاتف'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'عنوان التسليم'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'ملاحظات إضافية', 'rows': 3}),
            'delivery_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type':'datetime-local', 'placeholder': 'ملاحظات إضافية', 'rows': 3}),
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
            'rental_days', 'address', 'notes', 'start_date', 'end_date',
            'status', 'total_cost'
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
            'customer_name', 'customer_email', 'customer_phone', 'notes',
            'financing_plan', 'status'
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
            'amount_paid', 'status'
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