from django import forms
from django.contrib.auth.models import User
from .models import Staff

class StaffForm(forms.ModelForm):
    # User fields included in the form
    first_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Staff
        # Corrected to match model fields
        fields = ['employee_id','role', 'department', 'specialization', 'phone', 'availability_status', 'shift', 'years_of_experience']
        widgets = {
            'employee_id': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'role': forms.Select(attrs={'class': 'form-select'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'specialization': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'availability_status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'shift': forms.Select(attrs={'class': 'form-select'}),
            'years_of_experience': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        def clean_employee_id(self):
            data = self.cleaned_data['employee_id'].strip()
            if not data:
                raise forms.ValidationError("Employee ID is required.")
            if Staff.objects.filter(employee_id=data).exists():
                raise forms.ValidationError("This Employee ID already exists.")
            return data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name
            self.fields['username'].initial = self.instance.user.username
            self.fields['email'].initial = self.instance.user.email

    def save(self, commit=True):
        staff = super().save(commit=False)

        if not staff.pk:
            # Creating new user and staff
            user = User.objects.create_user(
                username=self.cleaned_data['username'],
                email=self.cleaned_data['email'],
                first_name=self.cleaned_data['first_name'],
                last_name=self.cleaned_data['last_name']
            )
            staff.user = user
        else:
            # Updating existing user fields
            user = staff.user
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.username = self.cleaned_data['username']
            user.email = self.cleaned_data['email']
            user.save()

        if commit:
            staff.save()
        return staff
