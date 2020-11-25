
# Create your models here.
from django.db import models

# Create your models here.




class Member(models.Model):
    employee_name = models.CharField(max_length=60)
    employee_salary= models.CharField(max_length=60)
    employee_age= models.CharField(max_length=60)
    profile_image=models.CharField(max_length=60)
    id_no= models.CharField(max_length=60)
   
    def __str__(self):
        print('vvvnv')
        return self.employee_name



def employees_page(self,request):
        
        return render(request,'home/employees.html',employees)