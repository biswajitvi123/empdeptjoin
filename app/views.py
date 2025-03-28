from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length
from django.db.models import Max,Sum,Min,Avg,Count,Prefetch

def emptodeptdata(request):
    LEDO==Emp.objects.all().select_related('deptno')
    LEDO=Emp.objects.filter(job__startswith ='C')
    LEDO=Emp.objects.filter(ename__endswith ='k')
    LEDO=Emp.objects.filter(job__contains ='C')
    LEDO=Emp.objects.filter(job__regex ='^m\w*')
    LEDO=Emp.objects.filter(sal__gt=5000)
    LEDO=Emp.objects.all()
    LEDO=Emp.objects.filter(sal__lt=5000)
    LEDO=Emp.objects.filter(deptno= 10 )
    LEDO=Emp.objects.order_by('sal')  #asanding
    LEDO=Emp.objects.order_by('-sal') #deseanding
    LEDO=Emp.objects.order_by(Length('ename'))
    LEDO=Emp.objects.order_by(Length('ename').desc())
    LEDO=Emp.objects.filter(job='SALESMAN').select_related('deptno')
    LEDO=Emp.objects.filter(comm__isnull=False).select_related('deptno')
    LEDO=Emp.objects.filter(comm__isnull=True).select_related('deptno')
    LEDO=Emp.objects.filter(mgr__isnull=True).select_related('deptno')
    LEDO=Emp.objects.filter(ename__startswith='s').select_related('deptno')
    LEDO=Emp.objects.all().select_related('deptno')
    LEDO=Emp.objects.filter(sal__gt=2000).select_related('deptno')
    LEDO=Emp.objects.filter(deptno__dname='ACCOUNTING').select_related('deptno')

    LEDO=Emp.objects.select_related('deptno').filter(deptno__dname__in=('ACCOUNTING','SALES'))

    LEDO=Emp.objects.select_related('deptno').filter(deptno__dlocation='DALLAS')

    avgsal=Emp.objects.aggregate(agsal=Avg('sal'))['agsal']
    print(avgsal)

    LEDO=Emp.objects.select_related('deptno').filter(sal__lt=avgsal)

    LEDO=Emp.objects.annotate(loe=Length('ename')).filter(loe=5)
    LEDO=Emp.objects.raw('select * from app_emp where ename="BLAKE"')
    d={'LEDO':LEDO}
    return render(request,'emptodeptdata.html',d)


def dept(request=None):
    LDE=Dept.objects.all()
    d1={'LDE':LDE}
    return render(request,'dept.html',d1)

def salgrade(request=None):
    SDO=Salgrade.objects.all()
    d2={'SDO':SDO}
    return render(request,'salgrade.html',d2)

def emptomgrjoin(request):
    QLEMO=Emp.objects.select_related('mgr').all()
    QLEMO=Emp.objects.select_related('mgr').filter(sal__gt=2000)
    
    QLEMO=Emp.objects.select_related('mgr').filter(mgr__isnull=False)
    
    QLEMO=Emp.objects.select_related('mgr').filter(mgr__sal__gt=2000)
    
    d3={'QLEMO':QLEMO}
    return render(request,'emptomgrjoin.html',d3)


def emptodeptandmgr(request):
   QLEDMO=Emp.objects.all().select_related('deptno','mgr')
   QLEDMO=Emp.objects.select_related('deptno','mgr').filter(ename='BLAKE')
    
   QLEDMO=Emp.objects.select_related('deptno','mgr').filter(deptno__dlocation='CHICAGO')
    
   QLEDMO=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='KING')
   d={'QLEDMO':QLEDMO}
   return render(request,'emptodeptandmgr.html',d)

def emptodeptbypr(request):#all dept and all employees
    QLDO=Dept.objects.prefetch_related('emp_set').all()
    #Only Particular Dept and all the Employees
    QLDO=Dept.objects.prefetch_related('emp_set').filter(dname='RESEARCH')

    #Below Query gives Error
    #QLDO=Dept.objects.prefetch_related('emp_set').filter(emp_set__ename='MARTIN')
    QLDO=Dept.objects.prefetch_related(Prefetch('emp_set',queryset=Emp.objects.filter(ename='MARTIN')))

    averageSalary=Emp.objects.aggregate(agsal=Avg('sal'))
    print(averageSalary)

    
    sumSalary=Emp.objects.aggregate(susal=Sum('sal'))
    print(sumSalary)
    d10averageSalary=Emp.objects.filter(deptno=10).aggregate(d10agsal=Avg('sal'))
    print(d10averageSalary)

    alldeptavgsalary=Emp.objects.values('deptno').annotate(avgsal=Avg('sal'))
    print(alldeptavgsalary)


    d={'QLDO':QLDO}
    return render(request,'emptodeptbypr.html',d)