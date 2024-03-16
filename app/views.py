from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
def show(r):
    return HttpResponse("Django Framework..")

def disp(re,d,g):
    print(type(d))
    return HttpResponse("%s %s"%(d,g))

def home(req):
    if req.method=='POST':
        a=int(req.POST['n1'])
        print(type(a))
        return render(req,'ind.html',{'a':a})
    return render(req,'home.html')

def ind(req):
    x='apple'
    l=[7,8,91,4]
    d=[{'name':'anu','age':12},{'name':'appu','age':22},{'name':'albi','age':18},{'name':'ammu','age':24}]
    return render(req,'ind.html',{'data':x,'l':l})


def index(re):
    return render(re,'index.html')


from .models import *
def reg(request):
    if request.method=='POST':
        n=request.POST['name']
        ph=request.POST['phone']
        e=request.POST['email']
        user=request.POST['username']
        pass_word=request.POST['password']
        try:
            d=register.objects.get(username=user)
            print(d)
            if d is not None:
                messages.success(request,'Already exits')
        except Exception:
            data=register.objects.create(name=n,phone=ph,email=e,username=user,password=pass_word)
            data.save()
            messages.success(request,'saved')
    return render(request,'register.html')

def display(request):
    d=register.objects.all()
    return render(request,'viewuser.html',{'d':d})

def delete(request,d):
    data=register.objects.get(pk=d)
    data.delete()
    return redirect(display)

def update(request,d):
    if request.method=='POST':
        n = request.POST['name']
        ph = request.POST['phone']
        e = request.POST['email']
        user = request.POST['username']
        pass_word = request.POST['password']
        register.objects.filter(pk=d).update(name=n,phone=ph,email=e,username=user,password=pass_word)
        messages.success(request,'Updated successfully')
        return redirect(display)
    data = register.objects.get(pk=d)
    return render(request,'update.html',{'data':data})

def login(request):
    if request.method == 'POST':
        user = request.POST['username']
        pass_word = request.POST['password']
        try:
            data=register.objects.get(username=user)
            if data.password==pass_word:
                request.session['user']=user #setting session id to username
                return redirect(userhome)
            else:
                messages.error(request,'incorrect password')
        except Exception:
            if user=='admin' and pass_word=='admin':
                request.session['admin']=user
                return redirect(adminhome)
            else:
                messages.error(request,'incorrect user')
    return render(request,'login.html')

def adminhome(request):
    if 'admin' in request.session:
        return render(request,'adminhome.html')
    return redirect(login)
def userhome(request):
    if 'user' in request.session:
        data=product.objects.all()
        return render(request,'userhome.html',{'data':data})
    return redirect(login)

def addproduct(request):
    if 'admin' in request.session:
        if request.method=='POST':
            n = request.POST['name']
            ph = request.POST['price']
            e = request.POST['stock']
            f=request.FILES['img']
            data=product.objects.create(product_name=n,price=ph,stock=e,product_image=f)
            data.save()
            messages.success(request,'Added')
        return render(request,'add_product.html')
    return redirect(login)

def display_product(request):
    if 'admin' in request.session:
        data=product.objects.all()
        return render(request,'display_product.html',{'data':data})
    return redirect(login)

def delete_product(request,d):
    if 'admin' in request.session:
        data=product.objects.get(pk=d)
        data.delete()
        messages.success(request,'Deleted')
        return redirect(display_product)
    return redirect(login)

def update_product(request,d):
    if 'admin' in request.session:
        data=product.objects.get(pk=d)
        if request.method == 'POST':
            data.product_name=request.POST['name']
            data.price=request.POST['price']
            data.stock=request.POST['stock']
            data.save()
            messages.success(request,'updated')
            return redirect(display_product)
        return render(request,'update_product.html',{'data':data})
    return redirect(login)

def user_details(request):
    if 'admin' in request.session:
        data=register.objects.all()
        return render(request,'user_details.html',{'data':data})
    return redirect(login)

def logout(request):
    if 'user' in request.session or 'admin' in request.session:
        request.session.flush()
        return redirect(login)

def add_to_cart(request,d):
    if 'user' in request.session:
        p=product.objects.get(pk=d)
        print(p)
        u=register.objects.get(username=request.session['user'])
        print(u)
        data=cart.objects.create(product_details=p,user_details=u)
        data.save()
        messages.success(request,'Item Added to the cart')
        return redirect(display_cart)
    return redirect(login)

def display_cart(request):
    u = register.objects.get(username=request.session['user'])
    data=cart.objects.filter(user_details=u)
    return render(request,'display_cart.html',{'data':data})


from .forms import *

def normal_form(request):
    if request.method=='POST':
        n=normal(request.POST)
        if n.is_valid():
            a=n.cleaned_data['name']
            b=n.cleaned_data['phone']
            c=n.cleaned_data['email']
            d=n.cleaned_data['username']
            e=n.cleaned_data['password']
            data=register.objects.create(name=a,phone=b,email=c,username=d,password=e)
            data.save()
            return HttpResponse("saved")
    n = normal()
    return render(request,'forms.html',{'data':n})


def mform(request):
    if request.method=='POST':
        n=modelform(request.POST,request.FILES)
        if n.is_valid():
            n.save()
            return HttpResponse("saved")
    m=modelform()
    return render(request,'forms.html',{'data':m})
