import datetime

from django.db import models
import datetime

class Registration(models.Model):
    #id=models.AutoField(primary_key=True)
    id = models.BigAutoField(primary_key=True, editable=False)
    fullname=models.CharField(max_length=100,blank=False)
    fathername = models.CharField(max_length=100, blank=False)
    mothername= models.CharField(max_length=100, blank=False)
    gender_choices =(("M","Male") , ("F","Female") , ("Others","Prefer not to say")  )
    gender=models.CharField(blank=False,choices=gender_choices,max_length=10)
    dateofbirth=models.CharField(max_length=20,blank=False)
    email=models.EmailField(max_length=50,blank=False,unique=True)
    username=models.CharField(max_length=50,blank=False,unique=True)
    password = models.CharField(max_length=50, blank=False)
    location = models.CharField(max_length=50, blank=False)
    contactno = models.BigIntegerField(blank=False,unique=True)
    panno=models.BigIntegerField(blank=False,unique=True)
    aadharno= models.CharField(max_length=100, blank=False)
    registrationtime = models.DateTimeField(blank=False,auto_now=True)
    address = models.CharField(max_length=100, blank=False, unique=True)
    amount=models.IntegerField(default=1000)
    customer_image = models.FileField(blank=False,upload_to="customerimages/")
    credit_score = models.IntegerField(default=0)
    class Meta:
        db_table = "registration_table"

    def __str__(self):
        return self.username

class Transfer(models.Model):
    transaction_id=models.AutoField(primary_key=True)
    fromaccount=models.CharField(blank=False, max_length=255)
    toaccount=models.ForeignKey(Registration,on_delete=models.CASCADE,blank=False)
    amount=models.IntegerField(blank=False)
    purpose=models.CharField(max_length=100,blank=False)
    transfertime = models.DateTimeField(blank=False,auto_now=True)

    class Meta:
        db_table="transfer_table"

class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50,unique=True,blank=False)
    password = models.CharField(max_length=50,blank=False)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "admin_table"

class BillPayment(models.Model):
    user = models.ForeignKey(Registration, on_delete=models.CASCADE)
    bill_types = (("E", "Electricity"), ("W", "Water"), ("G", "Gas"))
    bill_type = models.CharField(blank=False,choices=bill_types,max_length=20)
    bill_number = models.CharField(max_length=50)
    amount = models.IntegerField()
    payment_time = models.DateTimeField(blank=False,auto_now=True)

    class Meta:
        db_table="billpayment_table"
