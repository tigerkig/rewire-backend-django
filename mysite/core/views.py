import email
from urllib import response
# from os import PRIO_PGRP
import datetime
import os
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from django.contrib import messages
import requests  
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import requires_csrf_token
from django.template.context_processors import csrf
from django.core import serializers
from .models import UploadInsurance, InsuranceType, OrderCard, CurrentUser, Email
from django.core.files.storage import FileSystemStorage
from hellosign_sdk import HSClient
from hellosign_sdk.utils.exception import NoAuthMethod, BadRequest
from django.contrib.auth.hashers import make_password, check_password
from django.conf import settings

API_KEY = settings.API_KEY
CLIENT_ID = settings.CLIENT_ID
TEMPLATE_ID = settings.TEMPLATE_ID
USER_EMAIL = settings.SIGN_CLIENT_EMAIL
USER_NAME = settings.SIGN_CLIENT_NAME
ROLE_NAME = settings.SIGN_ROLE_NAME
CUSTOM_DATE = settings.CUSTOM_DATE
CUSTOM_NAME = settings.CUSTOM_NAME


@api_view(['GET', 'POST'])
@csrf_exempt
def home(request):
    print('123home')
    print(request.path)
    print('end')
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })
        
def signup(request):
    if request.method == 'POST':
        user_name = request.POST.get('name')
        user_nif = request.POST.get('nif')
        user_email = request.POST.get('email')
        user_password = request.POST.get('password')
        if None not in (user_name, user_nif, user_email, user_password):
            if CurrentUser.objects.filter(username=user_nif).exists():
                return JsonResponse({'result': 'registered'})
            elif CurrentUser.objects.filter(email=user_email).exists():
                return JsonResponse({'result': 'registered'})
            else:
                user = CurrentUser(nif=user_nif, username=user_name, password=user_password, email=user_email)
                user.save()
                returnUserId = CurrentUser.objects.filter(email = user_email).values('id')
                
                responseData = {
                    'id' : returnUserId[0],
                    'name': user_name,
                    'nif': user_nif,
                    'email': user_email,
                }
                dump = json.dumps(responseData)
                return HttpResponse(dump, content_type='application/json')
        else : 
            responseData = {""}
            dump = json.dumps(responseData)
            return HttpResponse(dump, content_type='application/json') 

def login(request):
    print('startlogin')
    print(request.path)
    print('endlogin')
    if request.method == 'POST':
        user_email = request.POST.get('email')
        user_password = request.POST.get('password')
        if None not in (user_email, user_password):
            returnUserName = CurrentUser.objects.filter(email = user_email).values('username')
            returnUserNIF = CurrentUser.objects.filter(email = user_email).values('nif')
            returnUserId = CurrentUser.objects.filter(email = user_email).values('id') 
            savedPassword = CurrentUser.objects.filter(email = user_email).values('password')            

            if CurrentUser.objects.filter(email=user_email).exists() and CurrentUser.objects.filter(password=user_password).exists():
                responseData = {
                    'id' : returnUserId[0],
                    'name' : returnUserName[0],
                    'nif' :  returnUserNIF[0],
                    'email' : user_email,
                }
                dump = json.dumps(responseData)
                return HttpResponse(dump, content_type='application/json')
            else : return JsonResponse({'result': 'loginFailed'}) 
        else : return JsonResponse({'result': 'loginFailed'})
    else : return JsonResponse({'result': 'get request'}) 


@csrf_exempt
def insuranceData(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        insuranceType = request.POST.get('insuranceType')
        insurer = request.POST.get('insurer')
        nif = request.POST.get('nif')
        citizenCardNum = request.POST.get('citizenCardNum')
        citizenCardValidity = request.POST.get('citizenCardValidity')
        
        imgUp = request.FILES['imgUp']
        imgBack = request.FILES['imgBack']
        fs = FileSystemStorage()
        filename1 = fs.save(imgUp.name, imgUp)
        filename2 = fs.save(imgBack.name, imgBack)
        uploaded_file_url_1 = fs.url(filename1)
        uploaded_file_url_2 = fs.url(filename2)
        
        if None not in (user_id, insuranceType, insurer, nif, citizenCardNum, citizenCardValidity):
            if UploadInsurance.objects.filter(user_id=user_id, insuranceType=insuranceType).exists():
                return JsonResponse({'result': 'existData'})
            else:
                returnInsuranceData = []
                saveData = UploadInsurance (user_id=user_id, insuranceType=insuranceType, insurer=insurer, nif=nif, citizenCardNum =citizenCardNum, citizenCardValidity = citizenCardValidity, idCardUpScreen = uploaded_file_url_2, idCardBackScreen = uploaded_file_url_1,)
                saveData.save()
                data = [i.json() for i in UploadInsurance.objects.all().filter(user_id = user_id)]
                returnInsuranceData.append(json.dumps(data))
                
                inseranceTypes = []
                for insurance_type in data:
                    inseranceTypes.append(insurance_type["insuranceType"])
                    
                user_insuranceData = []
                for insurance_data in inseranceTypes:
                    data = InsuranceType.objects.filter(name=insurance_data).values()
                    data = data.first()
                    user_insuranceData.append(data)
                
                returnInsuranceData.append(json.dumps(user_insuranceData))   
                return HttpResponse(json.dumps(returnInsuranceData), content_type="application/json")


@csrf_exempt
def forgotPassSendingEmail(request):
    if request.method == "POST":
        user_email = request.POST.get('user_email')
        
        import secrets
        
        token = secrets.token_hex(16)
        
        account = CurrentUser.objects.filter(email = user_email)
        from django.conf import settings
        DOMAIN = settings.DOMAIN
        
        if account :
            account = account.first()
            account.token = token
            account.save()

            token = DOMAIN + '/reset_password/' + token
            
            print(token,'testtoken')

            from django.core import mail
            from django.template.loader import render_to_string
            from django.utils.html import strip_tags
            from django.core.mail import send_mail
            from django.conf import settings
            subject = 'Reset Password'
            html_message = '<p>Please confirm your <a href ={}>reset password</a></p>'.format(token)
            plain_message = strip_tags(html_message)
            from_email = 'From <developstar007@gmail.com>'
            to = str(account.email)
            email = Email.objects.first()
            serverEmail = settings.EMAIL_HOST_USER
            success = send_mail(
            'Password Reset',
            'message',
            serverEmail,
            [to],
            fail_silently = False,
            html_message = html_message,
            )
 
            if success == 1 :  
                return JsonResponse({'result': 'success', 'email':account.email})
            else : 
                return JsonResponse({'result': 'emailError'})
        else : 
            return JsonResponse({'result': 'emailError'})
          
@csrf_exempt
def getInsuranceData(request):
     if request.method == 'POST':
        returnInsuranceData = []
        user_id = request.POST.get('user_id')
        data = [i.json() for i in UploadInsurance.objects.all().filter(user_id = user_id)]
        returnInsuranceData.append(json.dumps(data))   
        inseranceTypes = []
        for insurance_type in data:
            inseranceTypes.append(insurance_type["insuranceType"])
        user_insuranceData = []
        for insurance_data in inseranceTypes:
            data = InsuranceType.objects.filter(name=insurance_data).values()
            data = data.first()
            user_insuranceData.append(data)
        returnInsuranceData.append(json.dumps(user_insuranceData))   
        return HttpResponse(json.dumps(returnInsuranceData), content_type="application/json")
    
def setNewPassword (request) : 
    if request.method == 'POST':
        user_email = request.POST.get('user_email')
        returnToken = request.POST.get('returnToken')
        #user_new_password = make_password(request.POST.get('user_newPassword'))
        user_new_password = request.POST.get('user_newPassword')

        if CurrentUser.objects.filter(token=returnToken).exists():
            CurrentUser.objects.filter(token=returnToken).update(password = user_new_password)
            return JsonResponse({'result': 'updated'})
        else : return JsonResponse({'result': 'failed'})


def orderCardData (request) :
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        phoneNumber = request.POST.get('phoneNumber')
        address = request.POST.get('address')
        postalCode = request.POST.get('postalCode')
        locality = request.POST.get('locality')
        pickupTime = request.POST.get('pickupTime')
        
        if OrderCard.objects.filter(user_id=user_id).exists():
            OrderCard.objects.filter(user_id=user_id).update(phoneNum = phoneNumber, address = address, postalCode = postalCode, locality = locality, pickupTime = pickupTime)
            # return JsonResponse({'result': 'updated'})
            responseData = {
                    'user_id' : user_id,
                    'phoneNumber': phoneNumber,
                    'address': address,
                    'postalCode': postalCode,
                    'locality': locality,
                    'pickupTime': pickupTime,
                }
            dump = json.dumps(responseData)
            return HttpResponse(dump, content_type='application/json')
        else:
            saveData = OrderCard (user_id=user_id, phoneNum = phoneNumber, address = address, postalCode = postalCode, locality = locality, pickupTime = pickupTime)
            saveData.save()
            responseData = {
                    'user_id' : user_id,
                    'phoneNumber': phoneNumber,
                    'address': address,
                    'postalCode': postalCode,
                    'locality': locality,
                    'pickupTime': pickupTime,
                }
            dump = json.dumps(responseData)
            return HttpResponse(dump, content_type='application/json')
            
def helloSignRequest (request):
    if request.method == 'POST':
        monthTxt = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        x = datetime.datetime.now()
        signDate = str(x.day) +  " de " + monthTxt[x.month-1] + " de " + str(x.year)
        customFullName = request.POST.get('user_Name')
        try:
            user_email = USER_EMAIL
            user_name = USER_NAME
            hsclient = HSClient(api_key=API_KEY)
            signers = [{"role_name": ROLE_NAME, "name": user_name, "email_address": user_email}]
            custom_fields = [{CUSTOM_DATE : signDate}, {CUSTOM_NAME : customFullName}]
            sr = hsclient.send_signature_request_embedded_with_template(
                test_mode=True,
                client_id=CLIENT_ID,
                template_id=TEMPLATE_ID,
                title="NDA with Acme Co.",
                subject="The NDA we talked about",
                message="Please sign this NDA and then we can discuss more. Let me know if you have any questions.",
                signing_redirect_url=None,
                signers=signers,
                custom_fields=custom_fields,
                )
            embedded = hsclient.get_embedded_object(sr.signatures[0].signature_id)
        except NoAuthMethod:
            responseData = {
                    'msg': "Please update your settings to include a value for API_KEY.",
                    'result': 'error'
                }
            dump = json.dumps(responseData)
            return HttpResponse(dump, content_type='application/json')
        else:
            responseData = {
                    'client_id': CLIENT_ID,
                    'sign_url': str(embedded.sign_url),
                    'result': 'success'
                }
            dump = json.dumps(responseData)
            return HttpResponse(dump, content_type='application/json')
    else: 
        return JsonResponse({'result': 'error'})
         
@login_required
def secret_page(request):
    return render(request, 'secret_page.html')


class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'secret_page.html'
