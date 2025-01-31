from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, DealerProfile

class UserSignUpModelForm(forms.ModelForm):
    password = forms.CharField(label='password', max_length=254, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'your name...'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'your last name...'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'name@example.com'})
        }

class UserProfileSignUpModelForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'gender']

        widgets = {
            'phone_number': forms.TextInput(attrs={'class':'form-control', 'placeholder':'phone number'}),
            'gender': forms.Select(attrs={'class':'form-control', 'placeholder':'your gender...'})
        }


class EditDealerProfileModelForm(forms.ModelForm):
    class Meta:
        model = DealerProfile
        fields = [
            'dealer_name',
            'description',
            'address',
            'website',
            'opening_hours',
            'city',
            'location',
        ]
        widgets = {
            'dealer_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'أدخل اسم المعرض/الشركة'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'اكتب وصفًا مختصرًا عن المعرض',
                'rows': 3
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'أدخل عنوان المعرض'
            }),
            'img_base64': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'أدخل الصورة بصيغة Base64 (اختياري)',
                'rows': 3
            }),
            'website': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'أدخل رابط الموقع الإلكتروني (اختياري)'
            }),
            'opening_hours': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'مثل: 9:00 صباحًا - 9:00 مساءً'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'أدخل المدينة'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'حدد الموقع الجغرافي (اختياري)'
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }

        help_texts = {
            'img_base64': 'يمكنك رفع الصورة بصيغة Base64 (اختياري)',
            'website': 'رابط الموقع الإلكتروني للمعرض إذا كان متوفرًا',
            'opening_hours': 'حدد ساعات عمل المعرض'
        }


    def clean_dealer_name(self):
        dealer_name = self.cleaned_data.get('dealer_name')
        if len(dealer_name) < 3:
            raise forms.ValidationError("اسم المعرض/الشركة يجب أن يكون أطول من حرفين.")
        return dealer_name

class LoginForm(forms.Form):
    email = forms.EmailField(label='email', max_length=254, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'name@example.com'}))
    password = forms.CharField(label='password', max_length=254, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
