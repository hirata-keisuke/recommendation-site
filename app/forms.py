from django import forms

class LoginForm(forms.Form):
    user_name = forms.CharField(label="ユーザー名", max_length=20)
    password = forms.CharField(label="パスワード", max_length=15)
