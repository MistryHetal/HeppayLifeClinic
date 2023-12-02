from email import message
import imp
from io import BytesIO
# from typing_extensions import Self
from django.contrib import admin
import django.contrib.auth.admin
import django.contrib.auth.models
from django.contrib import auth
from django.forms import SelectDateWidget
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
# from import_export.admin import ImportExportModelAdmin
from home.models import *
from django.utils.html import format_html
from django.urls import reverse
from django.urls import path
from django.core.mail import send_mail
from django.conf import settings
from xhtml2pdf import pisa
from django.template import Context, Template

from home.utils import render_to_pdf
from django.template.loader import get_template,render_to_string

class appointmentAdmin(admin.ModelAdmin):
    @admin.action(description='Generate PDF file')
    def generatePDF(modeladmin, request, queryset):

        response = HttpResponse(content_type='application/pdf')

        response['Content-Disposition'] = 'filename="report.pdf"'
        
        template = Template("""{% block content %}
                            <head>
                            <style>
                                .Specification-header-secction {
                                    float: left;
                                    width: 100;
                                    padding-bottom: 30px;
                                    margin-bottom: 30px;
                                    border-bottom: 1px solid #000000;
                                }
                                img{
                                    float: ;
                                    text-align: center;
                                }
                                h1,h3 {
                                    text-align: center;
                                }
                                th{
                                    padding: 5px;
                                    text-align: center;
                                    border: 1px black solid;
                                    font-size: 20px;
                                }
                                td {
                                    font-size: 12px;
                                    padding: 5px;
                                    text-align: center;
                                    border: 1px black solid;
                                }
                            </style>
                            </head>
                            <div>
                                <div class="specification-table-right">
                                    <h1 style="font-size:25px;"><b>HAPPY LIFE CLINIC</b></h1>
                                    <h3 style="font-size:15px;">C/12,Nr Panchavati Socitey,</h3>
                                    <h3 style="font-size:15px;">Odhav, Ahmedabad-382415</h3>
                                </div>
                                <div class="Specification-header-secction">
                                <table class="table table-bordered">
                                    <thead>
                                    <tr>
                                        <th scope="col">ID</th>
                                        <th scope="col">Name</th>
                                        <th scope="col">Date</th>
                                        <th scope="col">Email</th>
                                    </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            {% for ap in appointments %}
                                            <td scope="row">{{ap.id}}</td>
                                            <td>{{ap.fname}}</td>
                                            <td>{{ap.date}}</td>
                                            <td>{{ap.email}}</td>
                                        </tr>
                                        {% endfor %}
                                    </tbody>
                                </table>
                                </div>
                            </div>
                            {% endblock content %}""")
        
        context = Context({'appointments': queryset})
        html = template.render(context)


        pisa_status = pisa.CreatePDF(html, dest=response)
        # if error then show some funy view
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
       
    actions = [generatePDF]
    
    # change_list_template = 'C:/Users/Hetal/OneDrive/Desktop/ProjectNew/final/Clinic/templates/admin/accout/account_action.html'
    list_display = ('fname','lname','email', 'date', 'app_type', 'account_actions' )
    ordering = ('id',)
    search_fields = ('fname','lname', 'email', 'date')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                '<appointment_id>/approve/',
                self.admin_site.admin_view(self.process_approve),
                name='process-approve',
            ),
            path(
                '<appointment_id>/reject/',
                self.admin_site.admin_view(self.process_reject),
                name='process-reject',
            ),
        ]
        return custom_urls + urls

    def account_actions(self, obj):
        return format_html(
            '<a class="btn btn-high btn-success mb-1" href="{}">Approve</a>&nbsp;&nbsp;'
            '<a class="btn btn-high btn-danger mb-1" href="{}">Reject</a>',
            reverse('admin:process-approve', args=[obj.pk]),
            reverse('admin:process-reject', args=[obj.pk]),
        )
    account_actions.short_description = 'Account Actions'
    account_actions.allow_tags = True

    def process_approve(self, request, appointment_id, *args, **kwargs):
        print(appointment_id)
        # INSERT MAIL CODE HERE
        appointment_obj = appointment.objects.get(id=appointment_id)
        print(appointment_obj.app_type)
        if appointment_obj.app_type == 'O':
            print("HEYYY...")
            subject = f'Online Appointment acceptance | Happy Life Clinic'
            message = f'Your online appointment is accepted.  please join this link to meet doctor online.. https://us05web.zoom.us/j/82890688798?pwd=S2E1azRDUlF3RXVjQlZOMm5PMmJSdz09'
            appointment_obj = appointment.objects.get(id=appointment_id)
            email = settings.EMAIL_HOST_USER
            reciepient = [appointment_obj.email]
            send_mail(subject,message,email,reciepient)
        
        else:
            subject = f'Offline Appointment acceptance | Happy Life Clinic'
            message = f'Your appointment is accepted please come on time and meet doctor in Clinic'
            appointment_obj = appointment.objects.get(id=appointment_id)
            email = settings.EMAIL_HOST_USER
            reciepient = [appointment_obj.email]
            send_mail(subject,message,email,reciepient)

        return HttpResponseRedirect('/admin/home/appointment/')

    def process_reject(self, request, appointment_id, *args, **kwargs):
        print(appointment_id)
        subject = f'Appointment Rejected | Happy Life Clinic'
        message = f'Your appointment is rejected, choose another time to book an appointment'
        appointment_obj = appointment.objects.get(id=appointment_id)
        email = settings.EMAIL_HOST_USER
        reciepient = [appointment_obj.email]
        send_mail(subject,message,email,reciepient)

        return HttpResponseRedirect('/admin/home/appointment/')
    
    def clean(self):
        if self.process_approve:
            raise ValidationError({'<a class = "btn btn-primary disabled">Disabled</a>': _('End date cannot be smaller then start date.')})
            
    def has_add_permission(self, request, obj=None):
        return False    

class CampAdmin(admin.ModelAdmin):
    @admin.action(description='Send Camp Details to Users')
    def sendMailtoUsers(modeladmin, request, queryset):
        
        user_list = []

        users = User.objects.all()
        for user in users:
            user_list.append(user.username)

        # user_list = [i for i in user_list if i]
        print(user_list)
        for obj in queryset:

            message = f'''Hello,
            
             Hope this mail finds you well.
             
             This mail is to inform you that we are going to organize {obj.Camp_name}. 

             Camp will be started from {obj.start_date}  to  {obj.end_date}. '''
            # #Then you can send the message. 
            send_mail('Camp Details | Happy Life Clinic', 
                        message,
                        'hetal.mistry.bca@gmail.com',
                        user_list, 
                        fail_silently=False)

    actions = [sendMailtoUsers]


    list_display = ('Camp_name','start_date','end_date')
    ordering = ('start_date',)
    search_fields = ('start_date',)

class MailTextAdmin(admin.ModelAdmin):

    @admin.action(description='Send Mail to Users')
    def sendMailtoUsers(modeladmin, request, queryset):
        
        for obj in queryset:
            user_list = []

            for mail_obj in obj.user.all():
                user_list.append(mail_obj.email)
            print(user_list)

            message = f'{obj.message} : {obj.attachment}'
            # #Then you can send the message. 
            send_mail(str(obj.subject), 
                        message,
                        'hetal.mistry.bca@gmail.com',
                        user_list, 
                        fail_silently=False)

    actions = [sendMailtoUsers]


admin.site.unregister(auth.models.Group)
# admin.site.unregister(auth.models.User)
# Register your models here.
admin.site.register(appointment,appointmentAdmin)
admin.site.register(Camp, CampAdmin)
# admin.site.register(Signup,SignupAdmin)
admin.site.register(feedback,feedbackAdmin)
# admin.site.register(prescription,prescriptionAdmin)
admin.site.register(Mail)  # for prescription
admin.site.register(MailText,MailTextAdmin)   # for prescription

