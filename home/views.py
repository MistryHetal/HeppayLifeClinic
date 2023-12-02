import email
from django.views.generic.base import TemplateView
from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMessage, send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login
# from .forms import UserRegisterForm, UserUpdateForm
# from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.core.mail import EmailMessage
from django.conf import settings
from .models import *
from home.models import appointment
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from home.utils import render_to_pdf #created in step 4
# from django.views.generic import ListView
import datetime
from django.template.loader import get_template
# from django.template import Context
# from django.template.loader import render_to_string, get_template

# Create your views here.

APPOINTMENT_CHOICES = (
    ('O', 'online'),
    ('F', 'Offline'),
)

class HomeTemplateView(TemplateView):
    template_name = "index.html"
    
    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        email = EmailMessage(
            subject= f"{name} from Happy Life Clinic.",
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER],
            reply_to=[email]
        )
        email.send()
        return HttpResponse("Email sent successfully!")

# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Your Account has been created! You are now able to log in.')
#             return redirect('login')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'register.html', {'form': form})

def register(request):
    error = ""
    if request.method == 'POST':
        fn = request.POST['firstName']
        ln = request.POST['lastName']
        e = request.POST['email']
        p = request.POST['password']
        c = request.POST['ContactNo']
        ab = request.POST['About']
        role = "ROLE_USER"

        try:
            user = User.objects.create_user(username=e, password=p, first_name=fn, last_name=ln)
            Signup.objects.create(user=user, ContactNo=c, About=ab, Role=role)
            error = "no"
        except:
            error = "yes"
    return render(request, 'register.html', locals())

def user_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['email']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        try:
            if user:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request, 'login.html', locals())
        
    # else:
    #     return redirect('index')
    
# @login_required
# def profile(request):
#     if request.method == 'POST':
#         u_form = UserUpdateForm(request.POST, request.FILES)

#         if u_form.is_valid():
#             u_form.save()
#             messages.success(request, f'Your Account has been updated!!')
#             return redirect('profile')
#     else:
#         u_form = UserUpdateForm()
#     context = {
#         'u_form' : u_form
#     }
#     return render(request, 'profile.html', context)

def profile(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = User.objects.get(id=request.user.id)
    signup = Signup.objects.get(user=user)

    if request.method == "POST":

        fname = request.POST['firstName']
        lname = request.POST['lastName']
        contactNo = request.POST['ContactNo']
        about = request.POST['About']

        signup.user.first_name = fname
        signup.user.last_name = lname
        signup.ContactNo = contactNo
        signup.About = about

        try:
            signup.save()
            signup.user.save()
            error = "no"
        except:
            error = "yes"

        # history.objects.create(user=request.user,)
    return render(request, 'profile.html', locals())

@login_required
def appointmentView(request):
    if request.method == "POST":
        print(type(request.POST['appointment_time']))
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        mobile = request.POST['mobile']
        app_type = request.POST['appo_type']
        appointment_time = request.POST['appointment_time']
        date = request.POST['date']
        request = request.POST['request']
        
        a_form = appointment(fname=fname, lname=lname, email=email, mobile=mobile, app_type=app_type, time=appointment_time,  date=date, request=request)
        a_form.save()

        # send an email
        appointment_data = "FName: " + fname + "LName: " + lname + "Email: " + email + "Phone" + mobile + "Date" + date
        # template = render_to_string('email.html', {'name': fname})
        send_mail(
            'Appointment Request from ' + fname, #subject
            appointment_data,
            email,
            ['hetal.mistry.bca19@gmail.com'],
        )
        # messages.success(request, f'Your Appointment has been booked!!')
        return redirect('index')
    else:
        return render(request, 'appointment.html')
        # ,{
        #     'form': form,
        #     'messageSent': messageSent,}
            

        

# def index(request):
#     #Variable
#     context = {
#         "variable":"this is sent"
#     }
#     return render(request, 'index.html', context)
#     # return HttpResponse("This is Homepage")


# class AppointmentTemplateView(TemplateView):
#     template_name = "appointment.html"

#     def post(self, request):
#         fname = request.POST.get("fname")
#         lname = request.POST.get("fname")
#         email = request.POST.get("email")
#         mobile = request.POST.get("mobile")
#         message = request.POST.get("request")

#         appointment = Appointment.objects.create(
#             first_name=fname,
#             last_name=lname,
#             email=email,
#             phone=mobile,
#             request=message,
#         )

#         appointment.save()

#         messages.add_message(request, messages.SUCCESS, f"Thanks {fname} for making an appointment, we will email you ASAP!")
#         return HttpResponseRedirect(request.path)

# class ManageAppointmentTemplateView(ListView):
#     template_name = "manage-appointments.html"
#     model = Appointment
#     context_object_name = "appointments"
#     login_required = True
#     paginate_by = 3


#     def post(self, request):
#         date = request.POST.get("date")
#         appointment_id = request.POST.get("appointment-id")
#         appointment = Appointment.objects.get(id=appointment_id)
#         appointment.accepted = True
#         appointment.accepted_date = datetime.datetime.now()
#         appointment.save()

#         data = {
#             "fname":appointment.first_name,
#             "date":date,
#         }

#         message = get_template('email.html').render(data)
#         email = EmailMessage(
#             "About your appointment",
#             message,
#             settings.EMAIL_HOST_USER,
#             [appointment.email],
#         )
#         email.content_subtype = "html"
#         email.send()

#         messages.add_message(request, messages.SUCCESS, f"You accepted the appointment of {appointment.first_name}")
#         return HttpResponseRedirect(request.path)


#     def get_context_data(self,*args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         appointments = Appointment.objects.all()
#         context.update({   
#             "title":"Manage Appointments"
#         })
#         return context

def changePassword(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error = ""
    user = request.user
    if request.method == "POST":
        o = request.POST['oldpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if user.check_password(o):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = 'not'
        except:
            error = "yes"
    return render(request, 'changePassword.html', locals())


def treatment(request):
    messages.success(request,'')
    return render(request,'guidance.html')
    # treatment.save()
    #return HttpResponse("This is user profile from page")

def reports(request):
    messages.success(request,'')
    return render(request,'report.html')

def minerals(request):
    messages.success(request,'')
    return render(request,'minerals.html')

def medicines(request):
    messages.success(request,'')
    return render(request,'medicines.html')

def event(request):
    messages.success(request,' ')
    return render(request,'events.html')
    event.save()
    #return HttpResponse("This is user profile from page")

def health(request):
    messages.success(request, ' ')
    return render(request, 'health.html')
    #return HttpResponse("This is user profile form page")

def forgotpass(request):
    return render(request, 'reset_password.html')
    return HttpResponse("This is user profile form page")

@login_required
def feedbackView(request):
    if request.method == "POST":
        email = request.POST['email']
        subject = request.POST['subject']
        datetime = request.POST['time']

        a_feedback = feedback(email = email, subject = subject, datetime = datetime)
        a_feedback.save()

        messages.success(request, f'your feedback is successfully saved')
        return redirect('index')
    else:
        return render(request, 'feedback.html')


def ViewFeedback(request):
    appo = feedback.objects.all()
    print("Myoutput",appo)
    return render(request,'ViewFeedback.html',{'app': appo})

# def history(request):
#     appointment_qs = appointment.objects.filter(fname=id)

#     context = {
#         'appointment_qs': appointment_qs,
#     }
#     # return render(request, "order_history.html", context)
#     return render(request, 'history.html', context)


def history(request):
    print(request.user)
    appo = appointment.objects.filter(email=request.user)
    print("Myoutput",appo)
    return render(request,'history.html',{'app': appo})

@login_required
def payment(request):
    return render(request, 'payment.html')

# def generatePDF(request, id):
#     buffer = io.BytesIO()
#     x = canvas.Canvas(buffer)
#     x.drawString(100, 100, "Let's generate this pdf file.")
#     x.showPage()
#     x.save()
#     buffer.seek(0)
#     return FileResponse(buffer, as_attachment=True, filename='attempt1.pdf')

class generatePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('invoice.html')
        context = {
            "appointment_id": 123,
            "customer_name": "John Cooper",
            "amount": 1399.99,
            "today": "Today",
        }
        html = template.render(context)
        pdf = render_to_pdf('invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")

