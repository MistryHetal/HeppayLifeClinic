# from dataclasses import field
from ast import Return
from distutils.log import error
from http.client import ACCEPTED
from tokenize import Comment
from xml.dom.expatbuilder import Rejecter
from django import forms
# from common.utils import send_email
from django.utils import timezone
from . import errors
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from .models import accept, reject
# from home.views import appointment


GENDER_CHOICES = (
    ('M', 'male'),
    ('F', 'female'),
    ('O', 'others'),
)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    address = forms.CharField()
    dob = forms.DateField()

    class Meta:
        model = User
        fields = ['username', 'email', 'gender', 'address', 'dob', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    address = forms.CharField()
    dob = forms.DateField()

    class Meta:
        model = User
        fields = ['username', 'email', 'gender', 'address', 'dob']


class AcceptRejectForm(forms.Form):
    comment = forms.CharField(
        required=False,
        widget=forms.Textarea,
    )
    send_email = forms.BooleanField(
        required=False,
    )

    @property
    def email_subject_template(self):
        return 'notification_subject.txt'

    @property
    def email_body_template(self):
        raise NotImplementedError()

    def form_reject(self, accept, user):
        raise NotImplementedError()

    def save(self, accept, user):
        try:
            accept, reject = self.form_reject(accept, user)
        except errors.Error as e:
            error_message = str(e)
            self.add_error(None, error_message)
            raise
        
        # if self.cleaned_data.get('send_email', False):
            # send_email(
            #     to=[accept.user.email],
            #     subject_template=self.email_subject_template,
            #     body_template=self.email_body_template,
            #     context={
            #         "accept": accept,
            #         "reject": reject,
            #     }
            # )

    # return accept, reject
        
# class BookForm(AcceptRejectForm):



# class UserLoginForm(AuthenticationForm):
#     def __init__(self, *args, **kwargs):
#         super(UserLoginForm, self).__init__(*args, **kwargs)

#     username = UsernameField(widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': '', 'id': 'hello'}))
#     password = forms.CharField(widget=forms.PasswordInput(
#         attrs={
#             'class': 'form-control',
#             'placeholder': '',
#             'id': 'hi',
#         }
# ))

# class AppointmentForm(forms.ModelForm):
#     fname = forms.CharField(max_length=30)
#     lname = forms.CharField(max_length=30)
#     email =forms.EmailField()
#     mobile = forms.IntegerField()
#     request = forms.CharField(max_length=60)

#     class Meta:
#         model = appointment
#         fields = ['fname', 'lname', 'email', 'mobile', 'request']

class MailForm(forms.Form):
        subject = forms.CharField(max_length=255)
        message = forms.CharField(widget=forms.Textarea)
        attachment = forms.FileField()

        def clean_subject(self):
            if self.cleaned_data["subject"]=="" or self.cleaned_data["subject"]==None:
                raise forms.ValidationError("My text is goes here")
            return self.cleaned_data["subject"]

        def clean_message(self):
            if self.cleaned_data["message"]=="" or self.cleaned_data["message"]==None:
                raise forms.ValidationError("My text is goes here")
            return self.cleaned_data["message"]