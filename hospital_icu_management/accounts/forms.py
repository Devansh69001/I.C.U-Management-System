from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    ROLE_CHOICES = [
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
        ('admin', 'Administrator'),
    ]
    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        user = self.get_user()
        role = cleaned_data.get('role')
        if user and hasattr(user, 'staff'):
            if user.staff.role != role:
                raise forms.ValidationError("Selected role does not match your profile.")
        return cleaned_data
