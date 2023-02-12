from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label='Identifiant',
                                  max_length=100)
    email = forms.EmailField(label='Email')
    password = forms.CharField(max_length=32,
                               widget=forms.PasswordInput)

    def clean(self):
        pass

    def clean_identifiant(self):
        if self.cleaned_data['username'] == "":
            self.add_error('username', "L'identifiant ne peut pas être vide!")
        return self.cleaned_data['username']

    def clean_email(self):
        if self.cleaned_data['email'] == "":
            self.add_error('email', "L'email ne peut pas être vide!")
        return self.cleaned_data['email']

    def clean_password(self):
        if self.cleaned_data['password'] == "":
            self.add_error('password', "Le mot de passe ne peut pas être vide!")
        return self.cleaned_data['password']
