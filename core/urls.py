from django.urls import path
from .import views

app_name = 'core'

urlpatterns = [
     path('register/', views.UserRegisterView.as_view(), name='register'),
     path('login/', views.LoginView.as_view(), name='login'),
     path('logout/', views.LogoutView.as_view(), name='logout'),
     path('change-password/', views.ChangePasswordView.as_view(), name='change-password'),
     path('reset-password/', views.ResetPasswordView.as_view(), name='reset-password'),
     path('done-password-reset/', views.DonePasswordResetView.as_view(),
          name='done-password-reset'),
     path('confirm-password-reset/<uidb64>/<token>/',
          views.ConfirmPasswordResetView.as_view(), name='confirm-password-reset'),
     path('complete-password-reset/', views.CompletePasswordResetView.as_view(),
          name='complete-password-reset'),
     path('add-user/', views.AddUserView.as_view(), name='add-user'),
     path('activate/<uidb64>/<token>/', views.ActivateAccountView.as_view(), name='activate'),
]