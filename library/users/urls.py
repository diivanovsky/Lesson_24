from django.urls import path
from users import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('edit_user/', views.edit_user_profile, name='edit_user'),
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]
