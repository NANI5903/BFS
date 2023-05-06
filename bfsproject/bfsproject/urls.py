"""bfsproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.landingpage,name="landingpage"),
    path("welcome",views.welcomepage,name="welcomepage"),
    path("locateus",views.locateus,name="locateus"),
    path("login",views.login,name="login"),
    path("navbar", views.navbar, name="navbar"),
    path("dashboard",views.dashboard,name="dashboard"),
    path("loans",views.loans,name="loans"),
    path("card",views.debitcard,name="card"),
    path("Insurance",views.insurance,name="insurance"),
    path("debitcard",views.debitcard,name="debitcard"),
    path("welcome",views.landing_to_welcome,name="landingtowelcome"),
    path("profile",views.profile,name="profile"),
    path("openaccount",views.openaccount,name="openaccount"),
    # path("transfer",views.transfer,name="transfer"),
    path("savings",views.savings,name="savings"),
    path("transaction",views.transaction,name="transaction"),
    path("welcomelogintologin",views.welcomelogin_to_login,name="welcomelogintologin"),
    path("logintonavbar",views.login_to_navbar,name="logintonavbar"),
    path("navbartodashboard",views.navbar_to_dashboard,name="navbartodashboard"),
    path("navbartotransaction",views.navbar_to_transaction,name="navbartotransaction"),
    path("navbartoloans",views.navbar_to_loans,name="navbartoloans"),
    path("navbartoinsurance",views.navbar_to_insurance,name="navbartoinsurance"),
    path("navbartodebitcard",views.navbar_to_debitcard,name="navbartodebitcard"),
    path("navbartoprofile",views.navbar_to_profile,name="navbartoprofile"),
    path("landingtoopenaccount",views.landing_to_openaacount,name="landingtoopenaccount"),
    path("navbartotransfer",views.navbar_to_transfer,name="navbartotransfer"),
    path('navbartosavings',views.navbar_to_savings,name="navbartosavings"),
    path("navbartologin",views.navbar_to_login,name="navbartologin"),
    path("loanapplication",views.applyLoan,name="loanapplication"),
    path("insuranceapplication",views.applyInsurance,name="insuranceapplication"),
    path("user/",include("userapp.urls")),
    #path("otppage",views.otppage,name="otppage"),
    #path("logintootppage",views.login_to_otppage,name="logintootppage"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
