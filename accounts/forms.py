from django import forms
from allauth.account.forms import SignupForm


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label="First Name")
    last_name = forms.CharField(max_length=30, label="Last Name")
    telephone = forms.CharField(max_length=20, label="Telephone")
    address = forms.CharField(widget=forms.Textarea, label="Address")
    postcode = forms.CharField(max_length=10, label="Postcode")

    def save(self, request):
        user = super().save(request)

        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.save()

        user.profile.telephone = self.cleaned_data["telephone"]
        user.profile.address = self.cleaned_data["address"]
        user.profile.postcode = self.cleaned_data["postcode"]
        user.profile.save()

        return user
