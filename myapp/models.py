from django.db import models

class det(models.Model):
    uname=models.CharField( max_length=50)
    email=models.CharField( max_length=50)
    phone=models.CharField( max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    uplode=models.FileField(max_length=100)

class sel(models.Model):
    sname=models.CharField( max_length=50)
    email=models.CharField( max_length=50)
    phone=models.CharField( max_length=50)
    shop=models.CharField( max_length=50)
    place=models.CharField( max_length=50)
    Pass=models.CharField(max_length=50)
    uplode=models.FileField(max_length=100)

class com(models.Model):
    user=models.ForeignKey(det,on_delete=models.CASCADE)
    date=models.DateField()
    reply=models.CharField(max_length=100)
    complaint=models.CharField(max_length=100)  

class pro(models.Model):
    seller=models.ForeignKey(sel,on_delete=models.CASCADE)
    pname=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    image=models.CharField(max_length=50)

class cart(models.Model):
    user=models.ForeignKey(det,on_delete=models.CASCADE)
    product=models.ForeignKey(pro,on_delete=models.CASCADE)
    qty=models.CharField(max_length=50)

class order(models.Model):
    user=models.ForeignKey(det,on_delete=models.CASCADE)
    product=models.ForeignKey(pro,on_delete=models.CASCADE)
    price=models.CharField(max_length=50)
    qty=models.CharField(max_length=50) 

    


    
    


    




    



