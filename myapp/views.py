from datetime import datetime 
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage

from myapp.models import cart, com, det, order, pro, sel

def reg_get(request):
    return render(request,'registraion.html')

def reg_post(request):
    uname=request.POST['uname']
    email=request.POST['email']
    phone=request.POST['phone']
    dob=request.POST['dob']   
    gender=request.POST['gender']
    uplode=request.FILES['uplode']
    password=request.POST['pass']
    f=FileSystemStorage()
    d=datetime.now().strftime("%Y%m%d_%H%M%S")
    f.save(d,uplode)
    path=f.url(d)
    md=det()
    md.uname=uname
    md.email=email
    md.phone=phone
    md.dob=dob
    md.gender=gender
    md.uplode=path
    md.password=password
    md.save()
    return redirect('/')
def login_get(request):
    return render(request,'login.html')

def login_post(request):
    username=request.POST['username']
    password=request.POST['pwd']
    a=det.objects.filter(email=username,password=password)
    b=sel.objects.filter(email=username,Pass=password)
    if a.exists(): 
        c=det.objects.get(email=username,password=password)  
        request.session['Name']=c.uname 
        request.session['lid']=c.id
        return redirect('/home_get')
    elif b.exists():
        d=sel.objects.get(email=username,Pass=password) 
        request.session['name']=d.sname
        request.session['lid']=d.id
        return redirect('/homes_get')
    else:   
        return redirect('/')

        
    

def home_get(requset):
    name=requset.session['Name']
    return render(requset,'home.html',{"data":name})
def sellers_get(request):
    return render(request,'sellerregi.html')

def sellers_post(request):
    sname=request.POST['sname']
    email=request.POST['email']
    phone=request.POST['phone']
    shop=request.POST['shop']
    place=request.POST['place']
    uplode=request.FILES['uplode']
    password=request.POST['Pass']
    f=FileSystemStorage()
    d=datetime.now().strftime("%Y%m%d_%H%M%S")
    f.save(d,uplode)
    path=f.url(d)
    sl=sel()
    sl.sname=sname
    sl.email=email
    sl.phone=phone
    sl.uplode=path
    sl.shop=shop
    sl.place=place
    sl.Pass=password
    sl.save()
    return redirect('/')
def homes_get(request):
    name=request.session['name']
    return render(request,'homes.html',{"data":name})
def views_get(request):
    vi=sel.objects.get(id=request.session['lid'])    
    return render(request,'viewprofil.html',{"data":vi})
def view_get(request):
    si=det.objects.get(id=request.session['lid'])
    return render(request,'viewsse.html',{"data":si})


def editu_get(request):
    ep=det.objects.get(id=request.session['lid'])
    return render(request,'edituser.html',{"data":ep})
def editu_post(request):
    uname=request.POST['uname']
    email=request.POST['email']
    phone=request.POST['phone']
    dob=request.POST['dob']
    gender=request.POST['gender']
    md=det.objects.get(id=request.session['lid'])
    md.uname=uname
    md.email=email
    md.phone=phone
    md.dob=dob
    md.gender=gender
    md.save()
    
    if "uplode" in request.FILES:
        uplode=request.FILES['uplode']
        f=FileSystemStorage()
        d=datetime.now().strftime("%Y%m%d_%H%M%S")
        f.save(d,uplode)
        path=f.url(d)
        md.uplode=path
        md.save()    
    return redirect('/')
def edits_get(requset):
    esp=sel.objects.get(id=requset.session['lid'])
    return render(requset,'editeseller.html',{"data":esp})
def edite_post(request):
    sname=request.POST['sname']
    email=request.POST['email']
    phone=request.POST['phone']
    shop=request.POST['shop']
    place=request.POST['place']
    sl=sel.objects.get(id=request.session['lid'])
    sl.sname=sname
    sl.email=email  
    sl.phone=phone
    sl.shop=shop
    sl.place=place
    sl.save()
    if "uplode" in request.FILES:
        uplode=request.FILES['uplode']
        f=FileSystemStorage()
        d=datetime.now().strftime("%Y%m%d_%H%M%S")
        f.save(d,uplode)
        path=f.url(d)
        sl.uplode=path
        sl.save()
    return redirect('/')

def changeu_get(request):
    chg=det.objects.get(id=request.session['lid'])
    return render(request,'changeuser.html',{"data":chg})
def changeu_post(request):
    
    current_password=request.POST['current_password']
    confirm_password=request.POST['confirm_password']
    new_password=request.POST['new_password']

    chg=det.objects.get(id=request.session['lid'])
    if chg.password == current_password:
        if new_password==confirm_password:
            chg.password=new_password
            chg.save()
            return redirect('/')
        else:
         return redirect('/changes_get') 



def changes_get(request):
    chg=sel.objects.get(id=request.session['lid'])
    return render(request,'changeseller.html',{"data":chg})
def changes_post(request):
    
    current_password=request.POST['current_password']
    confirm_password=request.POST['confirm_password']
    new_password=request.POST['new_password']

    chg=sel.objects.get(id=request.session['lid'])
    if chg.Pass == current_password:
        if new_password==confirm_password:
            chg.Pass=new_password
            chg.save()
            return redirect('/')
        else:
         return redirect('/changes_get')
        
def sndcomp_get(request):
    return render(request,'sndcompl.html')
def sndcomp_post(request):
    co=request.POST['complaint']
    d=datetime.now().date()
    k=com()
    k.complaint=co
    k.date=d
    k.reply="pending"
    k.user_id=request.session['lid']
    k.save()
    return redirect('/home_get')


def viecom_get(request):
    vi=com.objects.filter(user=request.session['lid']) 
    return render(request,'viewcom.html',{"data":vi}) 

def viewcoms_get(request):
    vi=com.objects.all()
    return render(request,'viewcomse.html',{"data":vi})

def sndreply_get(request,id):
    ad=com.objects.get(id=id)
    return render(request,'reply.html',{"data":ad})
def sndreply_post(request):
    re=request.POST['reply']
    id=request.POST['id']
    f=com.objects.get(id=id)
    f.reply=re
    f.save()
    return redirect('/viewcoms_get')

def product_get(request):
    return render(request,'product.html')

def product_post(request):
    name=request.POST['pname']
    price=request.POST['price']
    description=request.POST['description']
    image=request.FILES['image']
    fi=FileSystemStorage()
    da=datetime.now().strftime("%Y%m%d_%H%M%S")
    fi.save(da,image)
    path=fi.url(da)
    p=pro()
    p.pname=name
    p.price=price
    p.description=description
    p.image=path
    p.seller_id=request.session['lid']
    p.save()
    return redirect('/homes_get')

def view_pros_get(request):
    vi=pro.objects.filter(seller_id=request.session['lid'])
    return render(request,'view _pros.html',{"data":vi})


def editpro_get(request,id):
    vi=pro.objects.get(id=id)
    return render(request,'editpro.html',{"data":vi})
def editpro_post(request):
    name=request.POST['pname']
    price=request.POST['price']
    description=request.POST['description']
    id=request.POST['id']
    p=pro.objects.get(id=id)
    p.pname=name
    p.price=price
    p.description=description
    p.save()
    if "image" in request.FILES:
        image=request.FILES['image']
        id=request.POST['id']
        fi=FileSystemStorage()
        da=datetime.now().strftime("%Y%m%d_%H%M%S")
        fi.save(da,image)
        path=fi.url(da)
        p.image=path
        p.save()
    return redirect('/view_pros_get')

def viewprou_get(request):
    si=pro.objects.all()
    return render(request,'view_prou.html',{"data":si})

def qty_get(request,id):
     vi=pro.objects.get(id=id)
    
     return render(request,'qty.html',{"data":vi})
def qty_post(request):
    id=request.POST['id']
    qty=request.POST['qty']
    qt=cart()
    qt.qty=qty
    qt.user_id=request.session['lid']
    qt.product=pro.objects.get(id=id)
    qt.save()
    return redirect('/viewcart_get')

def viewcart_get(request):
    cr=cart.objects.filter(user_id=request.session['lid'])
    total_price=0
    for item in cr:
     total_price+=int(item.product.price)*int(item.qty)
    return render(request,'viewcart.html',{"data":cr,"total_price":total_price})

def delete(request,id):
    cr=cart.objects.filter(id=id).delete()
    return redirect('/viewcart_get')

def buy_get(request,id):
    by=pro.objects.get(id=id)
    return render(request,'oderqty.html',{"data":by})
def buy_post(request):
    qty=request.POST['qty']
    id=request.POST['id']
    p=pro.objects.get(id=id)
    price=int(p.price)*int(qty)
    b=order()
    b.qty=qty
    b.user_id=request.session['lid']
    b.product=pro.objects.get(id=id)
    b.price=price
    b.save()
    return redirect('/viewcart_get')

def vieworderu_get(request):
    vu=order.objects.filter(user_id=request.session['lid'])
    return render(request,'viewoderu.html',{"data":vu})

def buyu_post(request):
    cr=cart.objects.filter(user_id=request.session['lid'])
    for i in cr:
        b = order()
        b.user_id = request.session['lid']
        b.product = i.product
        b.qty = i.qty
        b.price = str(int(i.qty) * float(i.product.price))  
        b.save()
        if b.id:
            i.delete()
    return redirect('/viewcart_get')
def emailexist(request):
    email=request.GET.get('email')
    print(email)
    data=det.objects.filter(email=email)
    if data.exists():
        return JsonResponse({"status":"ok"})
    else:
       return JsonResponse({"status":"no"})
        
def emailexist_get(request):
    email=request.GET.get('email')
    print(email)
    data=sel.objects.filter(email=email)
    print(data)
    if data.exists():
        return JsonResponse({"status":"ok"})
    else:
       return JsonResponse({"status":"no"})
        

    
    









    









    


    




    









        

    
       



    











    







