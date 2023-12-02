from dataclasses import fields
from http.client import ACCEPTED
from io import BytesIO
from pyexpat import model
from tempfile import template
from tkinter.tix import Tree
from django.core.files import File
from secrets import choice
from tkinter import Button
from turtle import mode
from django.db import models
from django.contrib import admin 
from asyncio.windows_events import NULL
from django.contrib.auth.models import User
from django.http import request
from datetime import date, datetime
from django.core.mail import send_mail
from django.shortcuts import render
from django.db.models import CheckConstraint, Q, F
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


# Create your models here.

GENDER_CHOICES = (
    ('M', 'male'),
    ('F', 'female'),
    ('O', 'others'),
)

APPOINTMENT_CHOICES = (
    ('O', 'online'),
    ('F', 'Offline'),
)

class Signup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ContactNo = models.CharField(max_length=10, null=True)
    About = models.CharField(max_length=450, null=True)
    Role = models.CharField(max_length=150, null=True)
    RegDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name

class SignupAdmin(admin.ModelAdmin):
    list_display = ('user', 'About', 'Role')
    ordering = ('user',)
    search_fields = ('user','Role')

    def has_add_permission(self, request, obj=None):
        return False

# class treatement(models.Model):
#     treatement_type = models.CharField(max_length=50)
#     description = models.CharField(max_length=50)
#     prescription = models.CharField(max_length=50)
#     def __str__(self):
#         return  self.treatement_type

# class treatementAdmin(admin.ModelAdmin):
#     list_display = ('treatement_type','description', 'prescription')
#     ordering = ('treatement_type',)
#     search_fields = ('treatement_type','prescription')

class Camp(models.Model):
    start_date = models.DateTimeField(help_text="DD-MM-YYYY",null=True)
    end_date = models.DateTimeField(help_text="DD-MM-YYYY",null=True)
    Camp_name = models.CharField(max_length=50, default='Camp')

    class Meta:
        constraints = [
            # Ensures constraint on DB level, raises IntegrityError (500 on debug=False)
            CheckConstraint(
                check=Q(end_date__gt=F('start_date')), name='check_start_date'
            )
        ]
   

    def clean(self):
        # Ensures constraint on model level, raises ValidationError
        if self.start_date > self.end_date:
            # raise error for field
            raise ValidationError({'end_date': _('End date cannot be smaller then start date.')})

# class schedule(models.Model):
#     schedule_date = models.DateField()
#     schedule_stime = models.TimeField()
#     schedule_etime = models.TimeField()
#     def __str__(self) -> str:
#         return f'{self.schedule_date}'

# class scheduleAdmin(admin.ModelAdmin):
#     list_display =  ('schedule_date','schedule_stime', 'schedule_etime')
#     ordering = ('schedule_date',)
#     search_fields = ('schedule_date','schedule_stime')

# class medicine(models.Model):
#     medicine_name = models.CharField(max_length=50)
#     medicine_price = models.IntegerField()
#     medicine_qty = models.IntegerField()
#     medicine_desc = models.CharField(max_length=150)
#     medicine_exdate = models.DateField()
#     def __str__(self):
#         return  self.medicine_name

# class medicineAdmin(admin.ModelAdmin):
#     list_display = ('medicine_name','medicine_price', 'medicine_qty', 'medicine_desc', 'medicine_exdate')
#     ordering = ('medicine_name',)
#     search_fields = ('madicine_name','madicine_price')

# class report(models.Model):
#     report_name = models.CharField(max_length=50)
#     def __str__(self):
#         return  self.report_name

# class reportAdmin(admin.ModelAdmin):
#     list_display = ('report_name',)
#     ordering = ('report_name',)
#     search_fields = ('report_name',)

class appointment(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    app_type = models.CharField(choices=APPOINTMENT_CHOICES, max_length=50, default='F')
    time = models.CharField(max_length=50, null=True )
    date = models.DateField(auto_now=False, null=True)
    request = models.TextField(blank=True)
    
    def generate_obj_pdf(instance_id):
        obj = appointment.objects.get(id=instance_id)
        context = {'instance': obj}
        # pdf = render_to_pdf('pdf/template.html', context)
        filename = "YourPDF_Order{}.pdf" %(obj.slug)
        obj.pdf.save(filename, File(BytesIO()))

    def __str__(self):
        return  self.fname

class appointmentAdmin(admin.ModelAdmin):
    list_display = ('fname','lname','email','mobile', 'date', 'request' )
    ordering = ('fname',)
    search_fields = ('fname','lname', 'email')

    def account_actions(self, obj):
        return 

class feedback(models.Model):
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=245)
    datetime = models.DateTimeField(auto_now_add=True, help_text="DD-MM-YYYY", null=True)

    def _str_(self):
        return  self.email

class feedbackAdmin(admin.ModelAdmin):
    list_display = ('email','subject', 'datetime')
    ordering = ('email',)
    search_fields = ('email','subject', 'datetime')

class history(models.Model):
    class Meta():
        db_table = 'histroy'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

# class prescription(models.Model):
#     model = User
#     email = models.CharField(max_length=50, default="Type Patient Email..")
#     details = models.CharField(max_length=200, default="Type Advice..")
#     context_object_name = "user"
#     template_name = 'templates/prescription (1).html'

#     def __str__(self):
#         return  self.email

class appointmentAdmin(admin.ModelAdmin):
    list_display = ('email', 'send_actions' )
    # ordering = ('date',)
    search_fields = ('email',)

    def send_actions(self, obj):
        return 

class Mail(models.Model):
    id=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    email=models.EmailField(max_length=255,help_text="To email Happy Life Clinic",verbose_name="Email")
    timestamp=models.DateTimeField(default=datetime.now,help_text="H Clinicletter list",verbose_name="Happy Life Clinic")
    delete_link=models.SlugField(max_length=255,null=True,blank=True)
    def __unicode__(self):
        return self.email

    class Meta:
        verbose_name = "Prescription User"
        verbose_name_plural = "Precription Users"

    def __str__(self):
        return  self.email

class MailText(models.Model):
        subject = models.CharField(max_length=50, help_text="Type Patient Email..")
        message = models.CharField(max_length=50, help_text="Type Patient Email..")
        attachment = models.CharField(max_length=250, help_text="Type Patient prescription..")
        user = models.ManyToManyField(Mail)

        class Meta:
            verbose_name = "Prescription to send"
            verbose_name_plural = "Prescription to send"

        def __str__(self):
            return  self.attachment

