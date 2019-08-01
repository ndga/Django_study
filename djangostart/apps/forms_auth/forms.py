"""
@file:forms.py
@author:李霞丹
@date：2019/07/29
"""
# 通过django.forms定义表单
from django import forms
from django.contrib.auth.models import User

# 注册表单
class RegisterForm(forms.Form):
    username = forms.CharField(label="用户名",
                               max_length=30,
                               widget=forms.TextInput(
                                   attrs={"size":20,}
                               ))
    email = forms.CharField(label="邮 箱",
                            max_length=30,
                            widget=forms.TextInput(
                                attrs={"size":20}
                            ))
    # 因为Model中的元素默认是会把密码显示出来的，所以在这里重新定义一个password
    password1 = forms.CharField(label="密码1",
                               max_length=30,
                                widget=forms.TextInput(
                                    attrs={"size": 20}
                                ))
    password2 = forms.CharField(label="密码2",
                                max_length=30,
                                widget=forms.TextInput(
                                    attrs={"size": 20}
                                ))

    def clean_username(self):
        """
        对username字段做检查用户名是否已经被注册
        是否重复昵称，注意字段一定要有返回值
        """
        users = User.objects.filter(username__iexact=self.cleaned_data["username"])
        if not users:
            return self.cleaned_data["username"]
        else:
            raise forms.ValidationError("该昵称已经被使用请使用其他的昵称")

    def clean(self):
        """
        验证两次输入的密码是否一次
        对整个表单验证时，不需要返回值
        """
        if self.cleaned_data["password"] != self.cleaned_data["password2"]:
            raise forms.ValidationError("密码不一致！")


# 登录表单
class LoginForm(forms.ModelForm):
    password = forms.CharField(label="密码",
                               max_length=30,
                               widget=forms.PasswordInput(
                                   attrs={"size": 20, }
                               ))

    def clean_username(self):
        user = models.UserInfo.objects.filter(username__iexact=self.cleaned_data["username"])
        if not user:
            raise forms.ValidationError("用户名不存在")
        else:
            return self.cleaned_data["username"]

    class Meta:
        model = models.UserInfo
        exclude = ()
