
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.decorators.csrf import csrf_exempt
from mysite.core import views
print('attents')

urlpatterns = [
    #path('/login', views.login, name='login'),
    #path('', views.home, name='home'),
    # path('getToken', views.getToken, name = 'getToken'),
    path('api/signup',csrf_exempt(views.signup), name='signup'),
    path('api/login', csrf_exempt(views.login), name='login'),
    path('api/forgot_password', views.forgotPassSendingEmail, name = 'forgotPasswordEmail'),
    path('api/reset_password', views.setNewPassword, name = 'forgotPasswordEmail'),
    path('api/insurance_data', views.insuranceData, name = 'insuranceData'),
    path('api/getInsuranceData', views.getInsuranceData, name = 'getInsuranceData'),
    path('api/orderCardData', views.orderCardData, name = 'orderCardData'),
    path('api/hellosign_request', views.helloSignRequest, name = 'hellosignRequest'),
    
    #path('secret/', views.secret_page, name='secret'),
    #path('secret2/', views.SecretPage.as_view(), name='secret2'),
    #path('accounts/', include('django.contrib.auth.urls')),
    #path('admin/', admin.site.urls),
   # path('', views.login, name='home'),
]
print('test')
print(urlpatterns[0])
