from django.shortcuts import render


def landingpage(request):
    return render(request,'landingpage.html')

def welcomepage(request):
    return render(request,'welcome.html')

def landing_to_welcome(request):
    return render(request,'welcome.html')

def locateus(request):
    return render(request,'locateus.html')

def landing_to_locateus(request):
    return render(request,'locateus.html')

def login(request):
    return render(request,'login.html')

def otppage(request):
    return render(request,'otppage.html')

def dashboard(request):
    return render(request,'dashboard.html')

def welcomelogin_to_login(request):
    return render(request,'login.html')

def navbar(request):
    return render(request,'navbar.html')

def savings(request):
    return render(request,'savings.html')

# def transfer(request):
#     return render(request,'transfer.html')

def applyLoan(request):
    return render(request,"loanapplication.html")

def applyInsurance(request):
    return render(request,"insuranceapplication.html")

def openaccount(request):
    return render(request,'openaccount.html')

def landing_to_openaacount(request):
    return render(request,'openaccount.html')

def login_to_navbar(request):
    return render(request,'navbar.html')

def navbar_to_dashboard(request):
    return render(request,'dashboard.html')

def navbar_to_transaction(request):
    return render(request,'transactions.html')

def navbar_to_loans(request):
    return render(request,'loans.html')

def navbar_to_insurance(request):
    return render(request,'insurance.html')

def navbar_to_debitcard(request):
    return render(request,'debitcard.html')

def navbar_to_profile(request):
    return render(request,'profile.html')

def navbar_to_transfer(request):
    return render(request,'transfer.html')

def navbar_to_savings(request):
    return render(request,'savings.html')

def transaction(request):
    return render(request,'transactions.html')

def loans(request):
    return render(request,'loans.html')

def insurance(request):
    return render(request,'insurance.html')

def debitcard(request):
    return render(request,'debitcard.html')

def profile(request):
    return render(request,'profile.html')

def navbar_to_login(request):
    return render(request,'login.html')








'''def login_to_otppage(request):
    return render(request,'otppage.html')'''

