from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .validators import validate_username, validate_password
from .models import Comment, CommentLike


# class UserRegistrationForm(forms.Form):
#     username = forms.CharField(label=_('نام کاربری'), max_length=80, required=True)
#     email = forms.EmailField(label=_("ایمیل"), required=True, help_text=_('ایمیل درست وارد کنید'))
#     password = forms.CharField(label=_('رمز عبور'), widget=forms.PasswordInput, required=True)
#     confirm_password = forms.CharField(label=_('تایید رمز عبور'), required=True)
#     first_name = forms.CharField(label=_('نام'))
#     last_name = forms.CharField(label=_('نام خانوادگی'))
#
#     def clean(self):
#         password = self.cleaned_data.get('password')
#         conf_password = self.cleaned_data.get('confirm_password')
#         if password != conf_password:
#             raise ValidationError(_('password is not match'), code='invalid')
#
#     def clean_username(self):
#         username = self.cleaned_data.get('username')
#         validate_username(username)
#         return username
#
#     def clean_password(self):
#         password = self.cleaned_data.get('password')
#         validate_password(password)
#         return password


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        labels = {'content': _('   ')}


# ===============================================================comment with forms.Form
# class CommentForm(forms.Form):
#     content = forms.CharField(label=_("  "), widget=forms.Textarea, required=True)

class UserRegistrationForm(forms.ModelForm):
    password2 = forms.CharField(label=_('تایید رمز عبور'), required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'password2',)
        widgets = {'username': forms.TextInput, 'email': forms.TextInput, 'password': forms.PasswordInput,
                   'first_name': forms.TextInput, 'last_name': forms.TextInput, 'password2': forms.TextInput}
        labels = {'username': _('نام کاربری'), 'email': _('ایمیل'), 'password': _("رمز عبور"),
                  'password2': _("تایید رمز "
                                 "عبور"), 'first_name': _("نام"), 'last_name': _('نام خانوادگی')}
        help_texts = {'email': 'یه ایمیل درست بزن سره جدت'}

    def clean(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise ValidationError(_('پسورد ها نابرابرند'))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            User.objects.get(username=username)
            raise ValidationError(_('نام کاربری در حال حاضر وجود دارد'))
        except User.DoesNotExist:
            pass
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 6:
            raise ValidationError('پسوورد تعداد کاراکتراش کمه')
        return password


class LoginForm(forms.Form):
    username = forms.CharField(label=_('نام کاربری'), max_length=50, required=True)
    password = forms.CharField(label=_('پسوورد'), widget=forms.PasswordInput, required=True)



