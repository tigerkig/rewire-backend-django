# from curses import meta
from csv import unregister_dialect
from email.policy import default
from django.db import models
from datetime import datetime
# Create your models here.

class InsuranceType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=225)
    imgPath = models.CharField(max_length=225)
    perDayPrice = models.CharField(max_length=225)

class OrderCard(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(max_length=225)
    phoneNum = models.IntegerField(max_length=225)
    address = models.CharField(max_length=255)
    postalCode = models.CharField(max_length=255)
    locality = models.CharField(max_length=255)
    pickupTime = models.CharField(max_length=255)
    OK = 'ok'
    PENDING = 'pending'
    FAILED = 'failed'

    CHOICES = (
        (OK, 'Ok'),
        (PENDING, 'Pending'),
        (FAILED, 'Failed'),
    )
    status = models.CharField(max_length=255, choices=CHOICES, default=PENDING)
    

class UploadInsurance(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(max_length=225)
    insuranceType = models.CharField(max_length=225)
    insurance_end_date = models.CharField(max_length=225)
    insurer = models.CharField(max_length=225)
    nif = models.CharField(max_length=225)
    citizenCardNum = models.CharField(max_length=225)
    citizenCardValidity = models.CharField(max_length=225)
    idCardUpScreen = models.CharField(max_length=225)
    idCardBackScreen = models.CharField(max_length=225)
    userHeloSignData = models.CharField(max_length=225)
    userHeloSignStatus = models.CharField(max_length=225)
    OK = 'ok'
    PENDING = 'pending'
    FAILED = 'failed'

    CHOICES = (
        (OK, 'Ok'),
        (PENDING, 'Pending'),
        (FAILED, 'Failed'),
    )
    approveStatus = models.CharField(max_length=255, choices=CHOICES, default=PENDING)
    
    def json(self):
        return {
            'id' : self.id,
            'user_id' : self.user_id,
            'insuranceType' : self.insuranceType,
            'insurance_end_date' : self.insurance_end_date,
            'insurer' : self.insurer,
            'nif' : self.nif,
            'citizenCardNum' : self.citizenCardNum,
            'citizenCardValidity' : self.citizenCardValidity,
            'idCardUpScreen' : self.idCardUpScreen,
            'idCardBackScreen' : self.idCardBackScreen,
            'userHeloSignData' : self.userHeloSignData,
            'userHeloSignStatus' : self.userHeloSignStatus,
            'approveStatus' : self.approveStatus,
        }


class CurrentUser(models.Model):
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=500)
    username = models.CharField(max_length=500)
    nif = models.CharField(max_length=500)
    email = models.EmailField(max_length=254,db_index=True)
    token = models.CharField(max_length=500)
    active = models.BooleanField(default=False)
    createdDate = models.DateField(auto_now_add=True)
    last_login = models.DateField(auto_now_add=True)
    updatedDate = models.DateField(auto_now_add=True)

class Email(models.Model):
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=500)
