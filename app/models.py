
# Create your models here.
from django.db import models

# Define the Dept model
class Dept(models.Model):
    deptno = models.IntegerField(primary_key=True)
    dname = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.dname


class Emp(models.Model):
    empno = models.IntegerField(primary_key=True) 
    ename= models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    hire_date = models.DateField(auto_now=True)
    sal = models.DecimalField(max_digits=10, decimal_places=3)
    comm =models.DecimalField(max_digits=10, decimal_places=3,null=True,blank=True)
    deptno = models.ForeignKey(Dept, on_delete=models.CASCADE) 
    mgr= models.ForeignKey('self', on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return self.ename
    
class Salgrade(models.Model):
    # salgrade_id = models.IntegerField(primary_key=True)  # Auto increment primary key
    GRADE =models.IntegerField(primary_key=True)
    LOSAL = models.DecimalField(max_digits=10, decimal_places=3)
    HISAL = models.DecimalField(max_digits=10, decimal_places=3)

    # def _str_(self):
    #     return f"Grade: {self.grade} ({self.LOSAL} - {self.HISAL})"

    
