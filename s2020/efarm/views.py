from django.shortcuts import render
from efarm.models import Admin,Employee,Farmer,Customer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def addaefc(request):
    us1 = request.POST['users']
    us2 = request.POST['name']
    us3 = request.POST['sname']
    us4 = request.POST['fname']
    us5 = request.POST['mname']
    us6 = request.POST['email']
    us7 = request.POST['contact']
    us8 = request.POST['address']
    us9 = request.POST['password']
    us10 = request.POST['cpassword']
    if us1=='admin':
        t=Admin(users=us1,name=us2,sname=us3,fname=us4,mname=us5,email=us6,contact=us7,address=us8,password=us9,cpassword=us10)
        t.save()
        return render(request,'register.html')
    elif us1=='employee':
        e=Employee(users=us1,name=us2,sname=us3,fname=us4,mname=us5,email=us6,contact=us7,address=us8,password=us9,cpassword=us10)
        e.save()
        return render(request,'register.html')
    elif us1=='farmer':
        w=Farmer(users=us1,name=us2,sname=us3,fname=us4,mname=us5,email=us6,contact=us7,address=us8,password=us9,cpassword=us10)
        w.save()
        return render(request,'register.html')
    elif us1=='customer':
        w=Customer(users=us1,name=us2,sname=us3,fname=us4,mname=us5,email=us6,contact=us7,address=us8,password=us9,cpassword=us10)
        w.save()
        return render(request,'register.html')
    else:
        return render(request,'home.html')

def admin(request):
    adm = Admin.objects.all()
    return render(request,'adetails.html',{'adm':adm})

def employee(request):
    empl = Employee.objects.all()
    return render(request,'edetails.html',{'empl':empl})

def farmer(request):
    far = Farmer.objects.all()
    return render(request,'fdetails.html',{'far':far})

def customer(request):
    cus = Customer.objects.all()
    return render(request,'cdetails.html',{'cus':cus})

def contact(request):
    return render(request,'contact.html')

def product(request):
    return render(request,'product.html')

def orderd(request):
    return render(request,'orderd.html')

def addp(request):
    return render(request,'addp.html')

def addc(request):
    return render(request,'addc.html')

def productv(request):
    return render(request,'productv.html')