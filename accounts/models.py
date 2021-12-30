from django.db import models

# Create your models here.
def custom_generate_id():
    try:
        id=Register.objects.count()
        if id is not None:
            return f"KRK{1001+id}"
        else:
            return f"KRK{1001}"
    except Exception as e:
        print(e)

class Register(models.Model):
    id=models.CharField(max_length=10, default=custom_generate_id, primary_key=True,editable=None)
    profile_pic=models.ImageField(upload_to='image/')
    first_name=models.CharField(max_length=50,blank=True ,null=True)
    last_name=models.CharField(max_length=50,blank=True, null=True)
    age=models.IntegerField()
    gender=models.CharField(max_length=10,choices=(('male','male'),('female','female'),('other','other')))
    mobile_num=models.CharField(max_length=13)
    address=models.CharField(max_length=500)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip_code=models.IntegerField()
    
