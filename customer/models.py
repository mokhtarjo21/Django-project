from django.db import models
from .fields import (BRANDS, FUEL_TYPES, TRANSMISSION_TYPES, CONDITIONS, DRIVETRAINS, ENGINE_TYPES,
                    CATEGORIES, EXTERIOR_COLORS, INTERIOR_COLORS, RENTAL_DAYS_TYPES, TRUCK_CATEGORIES)
import random, string, datetime
from dateutil.relativedelta import relativedelta
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal

def RandomCarIDGen(N = 4):
    res = ''.join(random.choices(string.digits, k=N))
    car = CarModel.objects.filter(car_id=res)
    car_images = CarImagesModel.objects.filter(car_id=res)
    if car.exists() or car_images.exists():
        return RandomCarIDGen(N+1)
    return res

def RandomVehicleIDGen(N = 4):
    res = ''.join(random.choices(string.digits, k=N))
    car = VehicleModel.objects.filter(vehicle_id=res)
    car_images = VehicleImagesModel.objects.filter(vehicle_id=res)
    if car.exists() or car_images.exists():
        return RandomCarIDGen(N+1)
    return res

def RandomOrderIDGen(N = 6):
    res = ''.join(random.choices(string.digits, k=N))
    car = OrderModel.objects.filter(order_id=res)
    if car.exists():
        return RandomCarIDGen(N+1)
    return res

CAR_OFFERED_FOR = [
    ('1', 'للبيع'),
    ('2', 'للايجار'),
    ('3', 'للتقسيط'),
]

# Create your models here.
class CarModel(models.Model):
    title = models.CharField(max_length=80, verbose_name="العنوان", help_text="عنوان قصير للسيارة", null=True)
    provider = models.ForeignKey('auth.User', on_delete=models.CASCADE, help_text="صاحب السيارة", null=True)
    # Basic Information
    offered = models.CharField(
        max_length=20, 
        choices=CAR_OFFERED_FOR, 
        verbose_name="معروض", 
        help_text="اختر نوع عرض السيارة من الخيارات المتاحة.",
        default='1'
    )

    brand = models.CharField(
        max_length=20, 
        choices=BRANDS, 
        verbose_name="الماركة", 
        help_text="اختر ماركة السيارة من الخيارات المتاحة."
    )

    model = models.CharField(max_length=50, verbose_name="موديل السيارة", help_text="أدخل موديل السيارة بشكل دقيق.")
    year = models.PositiveIntegerField(verbose_name="سنة الصنع", help_text="أدخل سنة الصنع السيارة.", null=True)
    type = models.CharField(
        max_length=50, 
        verbose_name="النوع", 
        help_text="أدخل نوع السيارة (مثل: سيدان، هاتشباك، إلخ)."
    )
    category = models.CharField(
        max_length=20, 
        choices=CATEGORIES, 
        verbose_name="الفئة", 
        help_text="اختر الفئة التي تنتمي إليها السيارة (مثل: رياضية، عائلية، إلخ)."
    )
    
    # Colors
    exterior_color = models.CharField(
        max_length=20, 
        choices=EXTERIOR_COLORS, 
        verbose_name="اللون الخارجي", 
        help_text="اختر اللون الخارجي للسيارة."
    )
    interior_color = models.CharField(
        max_length=20, 
        choices=INTERIOR_COLORS, 
        verbose_name="اللون الداخلي", 
        help_text="اختر اللون الداخلي للسيارة."
    )

    # Specifications
    origin = models.CharField(
        max_length=50, 
        verbose_name="الوارد", 
        help_text="أدخل البلد الذي وردت منه السيارة."
    )
    fuel_type = models.CharField(
        max_length=20, 
        choices=FUEL_TYPES, 
        verbose_name="نوع الوقود", 
        help_text="اختر نوع الوقود المستخدم في السيارة (بنزين، ديزل، إلخ)."
    )
    transmission_type = models.CharField(
        max_length=20, 
        choices=TRANSMISSION_TYPES, 
        verbose_name="نوع القير", 
        help_text="اختر نوع القير (يدوي، أوتوماتيك، إلخ)."
    )
    cylinder_count = models.PositiveIntegerField(
        verbose_name="عدد السلندرات", 
        help_text="أدخل عدد السلندرات في المحرك."
    )
    condition = models.CharField(
        max_length=10, 
        choices=CONDITIONS, 
        verbose_name="الحالة", 
        help_text="اختر حالة السيارة (جديدة، مستعملة، إلخ)."
    )
    engine_capacity = models.DecimalField(
        max_digits=4, 
        decimal_places=1, 
        verbose_name="حجم المحرك", 
        help_text="أدخل حجم المحرك باللتر (مثال: 2.0)."
    )
    drivetrain = models.CharField(
        max_length=20, 
        choices=DRIVETRAINS, 
        verbose_name="نوع الدفع", 
        help_text="اختر نوع الدفع (دفع أمامي، دفع خلفي، دفع رباعي)."
    )
    keys_count = models.PositiveIntegerField(
        verbose_name="عدد مفاتيح السيارة", 
        help_text="أدخل عدد المفاتيح المتاحة للسيارة."
    )
    seat_count = models.PositiveIntegerField(
        verbose_name="عدد المقاعد", 
        help_text="أدخل عدد المقاعد في السيارة."
    )
    engine_type = models.CharField(
        max_length=20, 
        choices=ENGINE_TYPES, 
        verbose_name="نوع المحرك", 
        help_text="اختر نوع المحرك (بنزين، كهربائي، هجين)."
    )
    fuel_tank_capacity = models.PositiveIntegerField(
        verbose_name="سعة خزان الوقود (لتر)", 
        help_text="أدخل سعة خزان الوقود باللتر."
    )
    horsepower = models.PositiveIntegerField(
        verbose_name="القدرة بالحصان", 
        help_text="أدخل قدرة المحرك بالحصان."
    )
    door_count = models.PositiveIntegerField(
        verbose_name="عدد الابواب", 
        help_text="أدخل عدد الأبواب في السيارة."
    )

    # Additional Attributes
    icon = models.ImageField(
        upload_to='car_icons/', 
        verbose_name="الصورة الرئيسية", 
        blank=True, null=True, 
        help_text="اختر صورة الرئيسية التي ستظهر للسيارة (اختياري)."
    )

    price = models.DecimalField(max_digits=10, decimal_places=3, help_text="سعر السيارة", verbose_name="السعر", null=True)

    car_id = models.CharField(max_length=50, default=RandomCarIDGen, null=True)



    def get_financing_plan(self):
        financing_plans = FinancingPlanModel.objects.filter().order_by('-years')
        if financing_plans:
            financing_plan = financing_plans.first()
            return financing_plan
        return None
    
    def get_full_car_price_by_financing_plan(self, financing_plan_id):
        car_price = self.price
        financing_plan = FinancingPlanModel.objects.get(id=financing_plan_id)
        if financing_plan:
            interest_rate = car_price * Decimal(financing_plan.interest_rate / 100)
            full_car_price = interest_rate + car_price
            return int(full_car_price)
        return 999999
    
    def calculate_down_payment_by_financing_plan(self, financing_plan_id):
        full_car_price = Decimal(self.get_full_car_price)
        financing_plan = FinancingPlanModel.objects.get(id=financing_plan_id)
        if financing_plan:
            months = financing_plan.years * 12
            down_payment = full_car_price / months
            return int(down_payment)
        return None
    

    @property
    def get_full_car_price(self):
        financing_plan = self.get_financing_plan()
        full_car_price = self.get_full_car_price_by_financing_plan(financing_plan.id)
        return full_car_price
    
    @property
    def calculate_down_payment(self):
        financing_plan = self.get_financing_plan()
        down_payment = self.calculate_down_payment_by_financing_plan(financing_plan.id)
        return down_payment

    def __str__(self):
        return f"{self.brand} {self.type} ({self.model})"


class CarImportModel(models.Model):
    brand = models.CharField(
        max_length=20, 
        choices=BRANDS, 
        verbose_name="الماركة", 
        help_text="اختر ماركة السيارة من الخيارات المتاحة."
    )

    model = models.CharField(max_length=50, verbose_name="موديل السيارة", help_text="أدخل موديل السيارة بشكل دقيق.")
    year = models.PositiveIntegerField(verbose_name="سنة الصنع", help_text="أدخل سنة الصنع السيارة.", null=True)
    # Colors
    exterior_color = models.CharField(
        max_length=20, 
        choices=EXTERIOR_COLORS, 
        verbose_name="اللون الخارجي", 
        help_text="اختر اللون الخارجي للسيارة.",
        null=True
    )
    interior_color = models.CharField(
        max_length=20, 
        choices=INTERIOR_COLORS, 
        verbose_name="اللون الداخلي", 
        help_text="اختر اللون الداخلي للسيارة.",
        null=True
    )

    # Additional Attributes
    icon = models.ImageField(
        upload_to='car_icons/', 
        verbose_name="الصورة الرئيسية", 
        blank=True, null=True, 
        help_text="اختر صورة الرئيسية التي ستظهر للسيارة (اختياري)."
    )
    price = models.DecimalField(max_digits=10, decimal_places=3, help_text="سعر السيارة", verbose_name="السعر", null=True)

    condition = models.CharField(
        max_length=10, 
        choices=CONDITIONS, 
        verbose_name="الحالة", 
        help_text="اختر حالة السيارة (جديدة، مستعملة، إلخ).",
        null=True
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="سعر السيارة", null=True)
    country_of_origin = models.CharField(max_length=50, verbose_name="بلد المنشأ")

    class Meta:
        verbose_name = "سيارة للاستيراد"
        verbose_name_plural = "سيارات للاستيراد"

    def __str__(self):
        return f"{self.get_brand_display()} {self.model} ({self.year})"


class CarImagesModel(models.Model):
    car_id = models.CharField(max_length=50, null=True)
    img = models.FileField(upload_to='cars/images/%Y/%m/%d/', max_length=100)

    creation_date = models.DateTimeField(auto_now_add=True)

class VehicleImagesModel(models.Model):
    vehicle_id = models.CharField(max_length=50, null=True)
    img = models.FileField(upload_to='vehicle/images/%Y/%m/%d/', max_length=100)

    creation_date = models.DateTimeField(auto_now_add=True)


class ShippingCompanyModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم شركة الشحن")
    contact_info = models.TextField(verbose_name="معلومات الاتصال")
    tracking_url = models.URLField(verbose_name="رابط التتبع")

    class Meta:
        verbose_name = "شركة شحن"
        verbose_name_plural = "شركات الشحن"

    def __str__(self):
        return self.name


class BuyCarOrderModel(models.Model):
    # Customer Information
    name = models.CharField(max_length=100, verbose_name="اسم الكامل")
    email = models.EmailField(verbose_name="البريد الإلكتروني")
    phone = models.CharField(max_length=15, verbose_name="رقم الهاتف")

    # Car Details
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name="car_model", verbose_name="السيارة", blank=True, null=True)
    car_import = models.ForeignKey(CarImportModel, on_delete=models.CASCADE, related_name="car_import_model", verbose_name="السيارة", blank=True, null=True)


    # Order Details
    order_date = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الطلب")
    delivery_date = models.DateTimeField(null=True, blank=True, verbose_name="تاريخ التسليم المتوقع")
    address = models.TextField(verbose_name="عنوان التسليم")
    notes = models.TextField(null=True, blank=True, verbose_name="ملاحظات إضافية")

    # Order Status Choices
    PENDING = 'pending'
    IN_PROGRESS = 'in_progress'
    SHIPPED = 'shipped'
    DELIVERED = 'delivered'
    CANCELED = 'canceled'

    ORDER_STATUS = [
        (PENDING, 'قيد الانتظار'),
        (IN_PROGRESS, 'قيد التنفيذ'),
        (SHIPPED, 'يتم الشحن'),
        (DELIVERED, 'تم التسليم'),
        (CANCELED, 'ملغى'),
    ]

    status = models.CharField(
        max_length=20, 
        choices=ORDER_STATUS, 
        default=PENDING, 
        verbose_name="حالة الطلب"
    )

    # Shipping Information
    shipping_company = models.ForeignKey(ShippingCompanyModel, null=True, blank=True, verbose_name="شركة الشحن", on_delete=models.CASCADE)
    tracking_number = models.CharField(max_length=100, null=True, blank=True, verbose_name="رقم التتبع")
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="تكلفة الشحن")

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاريخ التعديل")

    class Meta:
        verbose_name = "طلب سيارة"
        verbose_name_plural = "طلبات السيارات"
        ordering = ['-order_date']

    def __str__(self):
        return f"طلب رقم {self.id} - {self.name}"


class BuyVehicleOrderModel(models.Model):
    # Customer Information
    name = models.CharField(max_length=100, verbose_name="اسم الكامل")
    email = models.EmailField(verbose_name="البريد الإلكتروني")
    phone = models.CharField(max_length=15, verbose_name="رقم الهاتف")

    # Car Details
    vehicle = models.ForeignKey('VehicleModel', on_delete=models.CASCADE, related_name="car_model", verbose_name="السيارة", blank=True, null=True)

    # Order Details
    order_date = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الطلب")
    delivery_date = models.DateTimeField(null=True, blank=True, verbose_name="تاريخ التسليم المتوقع")
    address = models.TextField(verbose_name="عنوان التسليم")
    notes = models.TextField(null=True, blank=True, verbose_name="ملاحظات إضافية")

    # Order Status Choices
    PENDING = 'pending'
    IN_PROGRESS = 'in_progress'
    SHIPPED = 'shipped'
    DELIVERED = 'delivered'
    CANCELED = 'canceled'

    ORDER_STATUS = [
        (PENDING, 'قيد الانتظار'),
        (IN_PROGRESS, 'قيد التنفيذ'),
        (SHIPPED, 'يتم الشحن'),
        (DELIVERED, 'تم التسليم'),
        (CANCELED, 'ملغى'),
    ]

    status = models.CharField(
        max_length=20, 
        choices=ORDER_STATUS, 
        default=PENDING, 
        verbose_name="حالة الطلب"
    )

    # Shipping Information
    shipping_company = models.ForeignKey(ShippingCompanyModel, null=True, blank=True, verbose_name="شركة الشحن", on_delete=models.CASCADE)
    tracking_number = models.CharField(max_length=100, null=True, blank=True, verbose_name="رقم التتبع")
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="تكلفة الشحن")

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاريخ التعديل")

    class Meta:
        verbose_name = "طلب سيارة"
        verbose_name_plural = "طلبات السيارات"
        ordering = ['-order_date']

    def __str__(self):
        return f"طلب رقم {self.id} - {self.name}"
    

class CarRentalModel(models.Model):
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE, verbose_name="السيارة", blank=True, null=True)
    daily_rate = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="سعر الإيجار اليومي")
    weekly_rate = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="سعر الإيجار الأسبوعي")
    monthly_rate = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="سعر الإيجار الشهري")
    availability = models.BooleanField(default=True, verbose_name="متاحة للتأجير", help_text='عرض السيارة ضمن قائمة السيارات الأيجار')


class RentalOrderModel(models.Model):
    PENDING = 'pending'
    IN_PROGRESS = 'in_progress'
    CONFIRMED = 'confirmed'
    COMPLETED = 'completed'
    CANCELED = 'canceled'

    ORDER_STATUS = [
        (PENDING, 'قيد الانتظار'),
        (IN_PROGRESS, 'جاري التدقيق'),
        (CONFIRMED, 'مؤكد'),
        (COMPLETED, 'مكتمل'),
        (CANCELED, 'ملغى'),
    ]

    customer_name = models.CharField(max_length=100, verbose_name="اسم العميل")
    customer_email = models.EmailField(verbose_name="البريد الإلكتروني")
    customer_phone = models.CharField(max_length=15, verbose_name="رقم الهاتف")
    car_rental = models.ForeignKey(CarRentalModel, on_delete=models.CASCADE, verbose_name="السيارة المحجوزة")
    rental_days = models.CharField(max_length=20, choices=RENTAL_DAYS_TYPES, verbose_name="عدد أيام الإيجار", null=True)
    start_date = models.DateField(verbose_name="تاريخ بدء الإيجار")
    end_date = models.DateField(verbose_name="تاريخ انتهاء الإيجار")
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default=PENDING, verbose_name="حالة الحجز")
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="التكلفة الإجمالية", null=True, blank=True)
    address = models.TextField(verbose_name="عنوان التسليم", null=True)
    notes = models.TextField(null=True, blank=True, verbose_name="ملاحظات إضافية")

    def __str__(self):
        return f"طلب {self.customer_name} ({self.car_rental})"

    def get_cost(self):
        cost = None
        if self.rental_days == '1':
            cost = self.car_rental.daily_rate
        elif self.rental_days == '7':
            cost = self.car_rental.weekly_rate
        elif self.rental_days == '30':
            cost = self.car_rental.monthly_rate
        return cost
    
    def save(self, *args, **kwargs):
        total_cost = self.get_cost()
        print(total_cost, 'total_cost')
        if total_cost:
            self.total_cost = total_cost
            
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "حجز"
        verbose_name_plural = "حجوزات"

# تقسيط
class FinancingPlanModel(models.Model):
    name = models.CharField(max_length=100)  # اسم الخطة
    years = models.PositiveIntegerField(verbose_name='عدد السنوات') #عدد السنوات التي يمكن تقصيتها
    interest_rate = models.FloatField()  # نسبة الفائدة
    max_duration_months = models.PositiveIntegerField()  # مدة السداد القصوى بالأشهر

    def __str__(self):
        return self.name
    
class InstallmentRequestModel(models.Model):
    customer_name = models.CharField(max_length=100, verbose_name="اسم العميل", null=True)
    customer_email = models.EmailField(verbose_name="البريد الإلكتروني", null=True)
    customer_phone = models.CharField(max_length=15, verbose_name="رقم الهاتف", null=True)

    car = models.ForeignKey(CarModel, on_delete=models.CASCADE)  # السيارة
    financing_plan = models.ForeignKey(FinancingPlanModel, on_delete=models.CASCADE)  # خطة التمويل
    created_at = models.DateTimeField(auto_now_add=True)  # تاريخ إنشاء الطلب
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'قيد الانتظار'), ('approved', 'مقبول'), ('rejected', 'مرفوض')],
        default='pending',
    )  # حالة الطلب
    notes = models.TextField(null=True, blank=True, verbose_name="ملاحظات إضافية")

    def get_full_car_price(self):
        car_price = self.car.price
        interest_rate = car_price * Decimal(self.financing_plan.interest_rate / 100)
        full_car_price = interest_rate + car_price
        return full_car_price
    
    def get_payments(self):
        payments = InstallmentPayment.objects.filter(installment_request__id=self.id, status='paid')
        return payments
    
    def get_reminding_car_price(self):
        full_car_price = self.get_full_car_price()
        payments = self.get_payments()
        for payment in payments:
            full_car_price -= payment.amount_paid
        return full_car_price
    
    def get_end_date(self):
        start_date = self.created_at.date()
        end_date = start_date + relativedelta(years=self.financing_plan.years)
        return end_date
    
    def get_reminding_months(self):
        start_date = self.created_at.date()
        end_date = self.get_end_date()
        difference = relativedelta(end_date, start_date)
        months = difference.years * 12 + difference.months
        return months
    
    def calculate_down_payment(self):
        full_car_price = self.get_reminding_car_price()
        months = self.get_reminding_months()
        down_payment = full_car_price / months
        return int(down_payment) if down_payment > 0 else 0

    def get_payed_months(self):
        full_car_price = self.get_full_car_price()
        reminding_car_price = self.get_reminding_car_price()

        financing_months = self.financing_plan.years * 12
        down_payment = full_car_price / financing_months
        payed_months = 0
        while reminding_car_price > 1:
            reminding_car_price -= down_payment
            payed_months +=1
        return financing_months - payed_months
    
    # def calculate_monthly_installment(self):
    #     principal = self.car.price - self.down_payment
    #     interest = (principal * (self.financing_plan.interest_rate / 100)) / 12
    #     return (principal / self.duration_months) + interest

    # def save(self, *args, **kwargs):
    #     self.monthly_installment = self.calculate_monthly_installment()
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f"Request by {self.customer_name} for {self.car.title} {self.calculate_down_payment()}"
    

class InstallmentPayment(models.Model):
    installment_request = models.ForeignKey(InstallmentRequestModel, on_delete=models.CASCADE)  # الطلب
    payment_date = models.DateField(auto_now_add=True)  # تاريخ الدفع
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='المبلغ')  # المبلغ المدفوع
    status = models.CharField(
        max_length=20,
        choices=[('paid', 'مدفوع'), ('pending', 'قيد انتظار الطلب'), ('late', 'متأخر')],
        default='pending',
    )  # حالة الدفع

    def __str__(self):
        return f"Payment for {self.installment_request.car.title} by {self.installment_request.customer_name}"


class LatePayment(models.Model):
    payment = models.OneToOneField(InstallmentPayment, on_delete=models.CASCADE)  # الدفع المرتبط
    late_fee = models.DecimalField(max_digits=10, decimal_places=2)  # غرامة التأخير
    resolved = models.BooleanField(default=False)  # هل تم حل التأخير؟

    def __str__(self):
        return f"Late Payment: {self.payment.installment_request.car.name} - {self.payment.installment_request.customer.name}"

PaymentTypeChoices = [
    ('1', 'دفع'),
    ('2', 'شحن')
]

class PaymentHistoryModel(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name="العميل", null=True)
    title = models.CharField(max_length=100, verbose_name="اسم العميل", null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=3, help_text="مبلغ المدفوع", verbose_name="المبلغ", null=True)
    action_date = models.DateField(auto_now_add=True)  # تاريخ الدفع
    order_type = models.CharField(
        max_length=20, 
        choices=PaymentTypeChoices, 
        verbose_name="نوع الطلب",
        null=True
    )

    
    def __str__(self):
        return f"{self.user.userprofile.get_full_name} - {self.title}"

    class Meta:
        ordering = ['-id']




SERVICE_CATEGORIES = [
    ('heavy_transport', 'نقل معدات ثقيلة'),
    ('cargo_transport', 'نقل بضائع'),
    ('furniture_transport', 'نقل أثاث'),
    ('refrigerated_transport', 'نقل مبرد'),
    ('raw_material_transport', 'نقل مواد أولية'),
    ('water_transport', 'نقل مياه'),
    ('waste_transport', 'نقل صرف صحي'),
    ('container_transport', 'نقل حاويات'),
]
# قسم متكامل لخدمات السيارات الثقيلة
class VehicleService(models.Model):
    name = models.CharField(max_length=255, verbose_name="اسم الخدمة")
    category = models.CharField(
        max_length=50, choices=SERVICE_CATEGORIES, verbose_name="فئة الخدمة"
    )
    description = models.TextField(verbose_name="وصف الخدمة", blank=True, null=True)
    base_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="السعر الأساسي"
    )

    def __str__(self):
        return self.name
    
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class VehicleModel(models.Model):
    PROVIDER_TYPES = [
        ('individual', 'فرد'),
        ('company', 'شركة'),
    ]

    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name="المالك")
    provider_type = models.CharField(
        max_length=20, choices=PROVIDER_TYPES, verbose_name="نوع المزود"
    )
    name = models.CharField(max_length=255, verbose_name="نوع المركبة")
    brand = models.CharField(
        max_length=20,
        verbose_name="اسم العلامة التجارية",
        help_text="ادخل اسم العلامة التجارية للمركبة.",
        null=True
    )
    model_number = models.CharField(
        max_length=50, 
        verbose_name="رقم الموديل",
        help_text="ادخل رقم الموديل للمركبة.",
        null=True
    )

    energy_type = models.CharField(
        max_length=20,
        choices=FUEL_TYPES,
        verbose_name="نوع الطاقة",
        help_text="اختر نوع الطاقة المستخدمة.",
        null=True
    )
    max_power = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="أقصى قوة (kw)",
        help_text="ادخل أقصى قوة للمركبة بالكيلوواط.",
        null=True
    )
    truck_category = models.CharField(
        max_length=20,
        choices=TRUCK_CATEGORIES,
        verbose_name="فئة الشاحنات",
        help_text="اختر فئة الشاحنة.",
        null=True
    )
    dimensions = models.CharField(
        max_length=100, 
        verbose_name="الحجم (مم)",
        help_text="أدخل أبعاد المركبة (الطول × العرض × الارتفاع).",
        null=True
    )
    empty_weight = models.PositiveIntegerField(
        verbose_name="وزن الشاحنة فارغة (كجم)",
        help_text="أدخل الوزن الفارغ للشاحنة بالكيلوجرام.",
        null=True
    )
    year = models.PositiveIntegerField(
        verbose_name="سنة الصنع",
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(2100)
        ]
    )
    capacity = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="الحمولة (طن)",
        validators=[
            MinValueValidator(0.1),
            MaxValueValidator(100)
        ]
    )
    description = models.TextField(verbose_name="وصف", blank=True, null=True)
    license_number = models.CharField(
        max_length=50, verbose_name="رقم الرخصة", blank=True, null=True
    )
    license_plate = models.CharField(max_length=20, verbose_name="رقم اللوحة", unique=True)
    vehicle_id = models.CharField(max_length=50, default=RandomVehicleIDGen, unique=True, null=True)

    origin = models.CharField(
        max_length=50,
        verbose_name="مكان المنشأ",
        help_text="أدخل البلد الذي تم تصنيع المركبة فيه.",
        null=True
    )

    image = models.ImageField(
        upload_to='vehicles/',
        verbose_name="الصورة الرئيسية",
        blank=True,
        null=True,
        help_text="اختر صورة السيارة بأبعاد لا تزيد عن 1024x1024 بكسل."
    )

    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="السعر",
        default=5,
        help_text="سعر المركبة."
    )

    price_per_km = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="سعر الكيلومتر",
        default=5,
        help_text="سعر النقل لكل كيلومتر."
    )
    loading_cost = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="رسوم التحميل",
        default=20,
        help_text="رسوم التحميل الإضافية."
    )
    unloading_cost = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="رسوم التفريغ",
        default=20,
        help_text="رسوم التفريغ الإضافية."
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء", null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاريخ التعديل", null=True)

    def full_description(self):
        return f"{self.name} - {self.brand} - {self.year} - {self.capacity} طن"

    def calculate_trip_cost(self, distance_km):
        return (self.price_per_km * distance_km) + self.loading_cost + self.unloading_cost

    def __str__(self):
        return f"{self.license_plate} - {self.name}"

    class Meta:
        verbose_name = "مركبة"
        verbose_name_plural = "المركبات"
        ordering = ['-created_at']


class VehicleRentalOrder(models.Model):
    customer_name = models.CharField(max_length=100, verbose_name="اسم العميل", null=True)
    customer_email = models.EmailField(verbose_name="البريد الإلكتروني", null=True)
    customer_phone = models.CharField(max_length=15, verbose_name="رقم الهاتف", null=True)
    notes = models.TextField(null=True, blank=True, verbose_name="ملاحظات إضافية")
    start_address = models.TextField(verbose_name="عنوان التحميل", null=True)
    end_address = models.TextField(verbose_name="عنوان التفريغ", null=True)
    
    service = models.ForeignKey(VehicleService, on_delete=models.CASCADE, verbose_name="الخدمة المطلوبة")
    vehicle = models.ForeignKey(VehicleModel, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="المركبة")
    start_location = models.CharField(max_length=255, verbose_name="نقطة البداية")
    end_location = models.CharField(max_length=255, verbose_name="نقطة الوصول")
    km_count = models.PositiveIntegerField(verbose_name="المسافة بالكيلومتر", null=True, help_text="المسافة التي سوف يقطعها الحاملة")
    date = models.DateField(verbose_name="تاريخ الخدمة")
    time = models.TimeField(verbose_name="وقت الخدمة", blank=True, null=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="التكلفة الإجمالية", blank=True, null=True
    )
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'قيد الانتظار'), ('confirmed', 'تم التأكيد'), ('completed', 'مكتمل'), ('canceled', 'ملغى')],
        default='pending',
        verbose_name="حالة الطلب"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء", null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاريخ التعديل", null=True)

    def __str__(self):
        return f"Booking {self.id} - {self.service.name}"

    def calculate_price(self):
        distance_km = self.calculate_distance()
        price_per_km = self.vehicle.price_per_km  # يمكن تخصيصه بناءً على نوع المركبة
        loading_cost = self.vehicle.loading_cost  # رسوم التحميل
        unloading_cost = self.vehicle.unloading_cost  # رسوم التفريغ
        # base_price = self.vehicle.base_price if self.vehicle else 100
        return (Decimal(distance_km) * price_per_km) + loading_cost + unloading_cost

    def save(self, *args, **kwargs):
        if not self.price:
            self.price = self.calculate_price()
        super().save(*args, **kwargs)

    def calculate_distance(self):
        # استخدم مكتبة لحساب المسافة بين النقاط
        return self.km_count  # افتراضي للمثال
    




OrderTypeChoices = [
    ('buy_car', 'شراء سيارة'),
    ('car_import', 'استراد السيارة'),
    ('car_rental', 'ايجار السيارة'),
    ('car_installment', 'تقسيط السيارة'),
    ('vehicle_rental_order', 'نقل حمولة'),
    ('buy_vehicle', 'شراء مركبة'),
]

class OrderModel(models.Model):
    customer = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name="car_orders", verbose_name="العميل", null=True)
    order_type = models.CharField(
        max_length=20, 
        choices=OrderTypeChoices, 
        verbose_name="نوع الطلب"
    )
    buy_car_order = models.OneToOneField(BuyCarOrderModel, on_delete=models.CASCADE, verbose_name="مودل طلب شراء السيارة", null=True)
    buy_vehicle_order = models.OneToOneField(BuyVehicleOrderModel, on_delete=models.CASCADE, verbose_name="مودل طلب شراء السيارة", null=True)
    car_rental_order = models.OneToOneField(RentalOrderModel, on_delete=models.CASCADE, verbose_name="مودل طلب ايجار السيارة", null=True)
    car_installment_order = models.OneToOneField(InstallmentRequestModel, on_delete=models.CASCADE, verbose_name="مودل طلب تقسيط السيارة", null=True)
    vehicle_rental_order = models.OneToOneField(VehicleRentalOrder, on_delete=models.CASCADE, verbose_name="مودل طلب نقل حمولة", null=True)
    order_id = models.CharField(max_length=50, default=RandomOrderIDGen, null=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاريخ التعديل")