from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path("register", views.register, name="signupregister"),
    path("registration", views.registration, name="registration"),
    path("userlogin",views.userlogin,name="userlogin"),
    path("transfer", views.transfer, name="transfer"),
    path("checkuserlogin",views.checkuserlogin,name="checkuserlogin"),
    path("viewusers",views.viewusers,name="viewusers"),
    path("deleteuser/<int:uid>",views.deleteuser,name="user/deleteuser"),
    path("transfermoney",views.checktransferMoney,name="transfermoney"),
    path("viewtransactions",views.viewTransactions,name="viewtransactions"),
    path("adminlogin",views.adminlogin,name="adminlogin"),
    path("checkadminlogin", views.checkAdminLogin, name="checkadminlogin"),
    path("checkbalance",views.checkBalance,name="checkbalance"),
    path("dashboard",views.dashboard,name="dashboard"),
    path("profile",views.profile,name="profile"),
    path("navbarofuse",views.navbarofuser,name="navbarofuser"),
    path("debitcardofuser",views.cardsofuser,name="debitcardofuser"),
    path("forgottoupdate",views.forgottoupdate,name="forgottoupdate"),
    path("updatepwdofuser",views.updatepwd,name="updatepwdofuser"),
    path("billpayment",views.BillPayment,name="billpayment"),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)