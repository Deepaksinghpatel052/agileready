from django.urls import path
from . import views


urlpatterns = [
    path('check-user-type', views.check_user_type, name='check_user_type'),
    path('send-request-for-ee', views.send_request_for_ee, name='send_request_for_ee'),
    path('add-data-in-membership-historty', views.add_data_in_membership_historty, name='add_data_in_membership_historty'),
    path('update_payment_status', views.update_payment_status, name='update_payment_status'),
    path('check_exists_package', views.check_exists_package, name='check_exists_package'),
    path('sent-payment-email', views.sent_payment_email, name='sent_payment_email'),
    path('check_payment_status_data', views.check_payment_status_data, name='check_payment_status_data'),

]