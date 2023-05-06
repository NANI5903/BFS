from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .forms import *
from .models import *
from django.db.models import Q

# Create your views here.
def register(request):
    return render(request,"openaccount.html")

def registration(request):
    form=RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("landingtowelcome")
            #return HttpResponse("<b>Registration Success</b>")
            #msg = "Successfully Registered"
            #return render(request, "openaccount.html", {"msg": msg})
        else:
            form_errors = form.errors.as_data()
            return render(request, "openaccount.html", {"form": form, "form_errors": form_errors})

    return render(request, "openaccount.html", {"form": form})

def logindemofunction(request):
    return render(request,"login.html")

def userlogin(request):
    return render(request,"userlogin.html")


def checkuserlogin(request):
    uname = request.POST["username"]
    pwd = request.POST["password"]

    if uname=="admin" and pwd=="admin":
        return redirect("viewusers")

    flag = Registration.objects.filter(Q(username=uname) & Q(password=pwd))
    print(flag)

    if (flag):
        user=Registration.objects.get(username=uname)
        print(user)
        request.session["id"] = user.id
        request.session["username"] = user.fullname
        return redirect("navbarofuser")
        #return render(request,"navbar.html",{"id": user.id, "uname": user.username})
    else:
        msg = "Login Failed"
        return render(request, "login.html", {"msg": msg})



def viewusers(request):
    userdata = Registration.objects.all()
    usercount = Registration.objects.count()
    return render(request,"viewusers.html",{"users":userdata,"count":usercount})

def deleteuser(request,uid):
    Registration.objects.filter(id=uid).delete()
    return redirect("viewusers")

def checkBalance(request):
    if "id" in request.session:
        accnumb=request.session["id"]
        flag = Registration.objects.filter(Q(id=accnumb)).values()
        balance=flag.amount
        return render(request,"dashboard.html",{"balance":balance})

def viewTransactions(request):
    if "username" in request.session:
        username = request.session["username"]
        transfers = Transfer.objects.filter(toaccount__username=username)
        return render(request, "transactions.html", {"transfers": transfers})


def transfer(request):
    form = TransferForm()
    if request.method == "POST":
        formdata = TransferForm(request.POST)
        if formdata.is_valid():
            formdata.save()
            return render(request, "transfer.html", {"transferform": form})
        else:
            return render(request, "transfer.html", {"transferform": form})
    return render(request, "transfer.html", {"transferform": form})

class Registrations:
    pass

def dashboard(request):
    cid=request.session["id"]
    customer=Registration.objects.get(id=cid)
    return render(request,"dashboard.html",{"customer":customer})

def profile(request):
    cid=request.session["id"]
    customer=Registration.objects.get(id=cid)
    image_url = "/media/customerimages/" + str(customer.customer_image)
    return render(request,"profile.html",{"cid":id,"customer":customer,"image_url": image_url})

def navbarofuser(request):
    cid=request.session["id"]
    customer=Registration.objects.get(id=cid)
    return render(request,"navbar.html",{"cid":cid,"customer":customer})

def cardsofuser(request):
    cid=request.session["id"]
    customer=Registration.objects.get(id=cid)
    return render(request, "debitcard.html", {"cid": cid, "customer": customer})

def forgottoupdate(request):
    cid = request.session["id"]
    cname = request.session["fullname"]
    return render(request, "empchangepwd.html", {"cid": cid, "cname": cname})

def updatepwd(request):
    cid=request.session["id"]

    accno=request.POST["id"]
    cemail=request.POST["email"]
    cnumb=request.POST["contact-number"]
    cpwd=request.POST["current-password"]
    npwd=request.POST["new-password"]

    flag=Registration.objects.filter(Q(id=cid)&Q(id=accno)&Q(email=cemail)&Q(contactno=cnumb)&Q(password=cpwd))

    if flag:
        Registration.objects.filter(id=accno).update(password=npwd)
        msg = "Password Updated Successfully"
        return render(request, "updatepwd.html", {"msg": msg})
    else:
        msg = "Details are Incorrect"
        return render(request, "empchangepwd.html", {"msg": msg})


def checktransferMoney(request):
    if request.method == 'POST':
        transferform = TransferForm(request.POST)
        if transferform.is_valid():
            fromaccount = transferform.cleaned_data['fromaccount']
            toaccount = transferform.cleaned_data['toaccount']
            amount = transferform.cleaned_data['amount']
            purpose = transferform.cleaned_data['purpose']
            try:
                fromuser = Registration.objects.get(username=fromaccount)
                touser = Registration.objects.get(username=toaccount)
            except Registration.DoesNotExist:
                return HttpResponse("Account Not Found")
            if fromuser.amount >= amount:
                fromuser.amount -= amount
                touser.amount += amount
                fromuser.save()
                touser.save()
                transaction = Transfer(fromaccount=fromaccount, toaccount=touser, amount=amount, purpose=purpose)
                transaction.save()
                msg = "Transaction Successful"
                return render(request, 'transfer.html', {'transferform': transferform, 'msg': msg})
            else:
                msg = "Insufficient Balance"
                return render(request, 'transfer.html', {'transferform': transferform, 'msg': msg})
        else:
            transferform = TransferForm()
            return render(request, 'transfer.html', {'transferform': transferform})


def adminlogin(request):
    return render(request,"adminlogin.html")

def checkAdminLogin(request):
    uname = request.POST["ausername"]
    pwd = request.POST["apassword"]

    flag = Admin.objects.filter(Q(username__exact=uname) & Q(password__exact=pwd))
    print(flag)

    if flag:
        admin = Admin.objects.get(username=uname)
        print(admin)
        request.session["auname"] = admin.username
        return redirect("viewusers")
    else:
        msg = "Login Failed"
        return render(request, "adminlogin.html", {"msg": msg})


def create_bill_payment(request):
    form = BillPaymentForm(request.POST or None)
    if form.is_valid():
        bill_payment = form.save(commit=False)
        bill_payment.user = request.user
        bill_payment.save()
        # Do any additional processing if necessary
        return redirect('home')  # Or any other URL you want to redirect to
    context = {'form': form}
    return render(request, 'savings.html', context)


def billPayment(request):
    if "username" in request.session:
        username = request.session["username"]
        user = get_object_or_404(Registration, username=username)

        if request.method == "POST":
            bill_type = request.POST["bill_type"]
            bill_number = request.POST["bill_number"]
            amount = request.POST["amount"]

            if int(amount) > user.amount:
                msg = "Insufficient balance"
                return render(request, "savings.html", {"msg": msg})

            bill_payment = BillPayment(
                user=user,
                bill_type=bill_type,
                bill_number=bill_number,
                amount=amount,
            )
            bill_payment.save()

            user.amount -= int(amount)
            user.save()

            msg = "Payment successful"
            return render(request, "savings.html", {"msg": msg})

        else:
            return render(request, "savings.html")


