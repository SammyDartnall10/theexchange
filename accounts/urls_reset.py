from django.urls import path, reverse_lazy
#from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
#    path('', password_reset, {'post_reset_redirect': reverse_lazy('password_reset_done')}, name='password_reset'),
#    path('done/', password_reset_done, name='password_reset_done'),
#    path('<uidb64>[0-9A-Za-z]+-<token>.+)/', password_reset_confirm,{'post_reset_redirect': reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),
#    path('complete/', password_reset_complete, name='password_reset_complete')

    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('<uidb64>[0-9A-Za-z]+-<token>.+)/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]