from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    # Custom method to indicate successful login
    def set_login_success(self):
        self.login_success = True
