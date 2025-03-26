from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length
from django.db.models import Max,Sum,Min,Sal,Avg,Count

def empdeptdata(request):
    LEDO=Emp.objects.all()
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
    d={'LEDO':LEDO}
    return render(request,'empdeptdata.html',d)


def dept(request=None):
    LDE=Dept.objects.all()
    d1={'LDE':LDE}
    return render(request,'dept.html',d1)

def salgrade(request=None):
    SDO=Salgrade.objects.all()
    d2={'SDO':SDO}
    return render(request,'salgrade.html',d2)

def empmgrjoin(request):
    QLEMO=Emp.objects.all().select_related('mgr')
    d3={'QLEMO':QLEMO}
    return render(request,'empmgrjoin.html',d3)


def emptodeptandmgr(request):
    QLEDMO=Emp.objects.all().select_related('deptno','mgr')
    # QLEDMO=Emp.objects.select_related('deptno','mgr').filter(ename='BLAKE')
    d={'QLEDMO':QLEDMO}
    return render(request,'emptodeptandmgr.html',d)

def emptodeptbypr(request):
    QLDO=Dept.objects.prefetch_related('emp_set').all()
    d={'QLDO':QLDO}
    return render(request,'emptodeptbypr.html',d)