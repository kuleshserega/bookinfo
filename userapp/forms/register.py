from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from userapp.models.profile import UserProfile
from django import forms


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="First name")
    last_name = forms.CharField(label="Last name")
    avatar = forms.ImageField(label="User photo")

    use_required_attribute = False

    class Meta:
        model = User
        fields = (
            "first_name", "last_name", "email", "avatar")

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': field.label,
                'autocomplete': 'off',
            })

        self.fields['avatar'].widget.attrs.update({
            'class': 'form-control form-file-input',
            'title': 'Choose your photo'
        })

    def clean_email(self):
        data = self.cleaned_data['email']
        try:
            User.objects.get(email__iexact=data)
        except User.DoesNotExist:
            return data

        raise forms.ValidationError("This email has already exists.")

    def clean_avatar(self):
        file = self.cleaned_data['avatar']
        if file:
            if file._size > 15 * 1024 * 1024:
                raise forms.ValidationError(
                    "Image file is too large ( > 15mb ).")
            return file
        else:
            raise forms.ValidationError("Could not read the uploaded file.")

    def save(self):
        user = super(RegisterForm, self).save(commit=False)
        user.username = '%s %s (%s)' % (
            user.first_name, user.last_name, user.email)
        user.save()

        user_profile = UserProfile(
            user=user, avatar=self.cleaned_data['avatar'])
        user_profile.save()
