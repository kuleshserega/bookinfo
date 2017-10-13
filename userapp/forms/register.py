from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="First name")
    last_name = forms.CharField(label="Last name")

    use_required_attribute = False

    class Meta:
        model = User
        fields = (
            "first_name", "last_name", "email")

    def __init__(self, request=None, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        for field in self.fields.itervalues():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': field.label,
                'autocomplete': 'off'
            })

    def clean_email(self):
        data = self.cleaned_data['email']
        try:
            User.objects.get(email__iexact=data)
        except User.DoesNotExist:
            return data

        raise forms.ValidationError("This email has already existed.")

    def save(self):
        user = super(RegisterForm, self).save(commit=False)
        user.username = '%s %s (%s)' % (
            user.first_name, user.last_name, user.email)
        user.save()
