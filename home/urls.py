from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from home import views
from .views import HomeTemplateView, generatePDF #AppointmentTemplateView, ManageAppointmentTemplateView

urlpatterns = [
    path("", HomeTemplateView.as_view(template_name='index.html'), name="index"),
    # path("login/", views.login, name='login'),
    #path("Registration/", views.Registration, name='Registration'),
    path('appointment/', views.appointmentView, name='appointment'),
    path("guidance/", views.treatment, name='guidance'),
    path("report/", views.reports, name='report'),
    path("minerals/", views.minerals, name='minerals'),
    path("medicines/", views.medicines, name='medicines'),
    path("events/",views.event, name='events'),
    path("health/", views.health, name='health'),
    # path("make-an-appointment/", AppointmentTemplateView.as_view(), name="appointment"),
    # path("manage-appointments/", ManageAppointmentTemplateView.as_view(), name="manage"),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path("password_reset/", auth_views.PasswordResetView.as_view() ,name='password_reset'),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view() ,name='password_reset_done'),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view() ,name='password_reset_confirm'),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('changePassword', views.changePassword, name='changePassword'),
    path("feedback/", views.feedbackView, name='feedback'),
    path("ViewFeedback/", views.ViewFeedback, name='ViewFeedback'),
    path("history/", views.history, name='history'),
    path("payment/", views.payment, name='payment'),
    # path('generatePDF/', views.generatePDF, name='generatePDF')
]