from django.shortcuts import render
import pyrebase
from django.http import HttpResponse
# Create your views here.
from pyasn1.compat.octets import null

config={
    'apiKey': "AIzaSyA63eHaTcbGcDSLDmmJAwjkjo0CF1o4m5w",
    'authDomain': "djangotest-c0d34.firebaseapp.com",
    'databaseURL': "https://djangotest-c0d34-default-rtdb.firebaseio.com",
    'projectId': "djangotest-c0d34",
    'storageBucket': "djangotest-c0d34.appspot.com",
    'messagingSenderId': "151800409397",
    'appId': "1:151800409397:web:a1924876ddabd0252e707c",
    'measurementId': "G-YDQETKQSDW"
}
firebase = pyrebase.initialize_app(config)
auth=firebase.auth()

def hi(request):
    return render(request,'InaBack/HomePage.html')
#def Signing(request):
    #return render(request,'InaBack/Dashboard.html')
def postsign(request):
    email=request.POST.get('userMail')
    password=request.POST.get('pass')
    user=auth.sign_in_with_email_and_password(email,password)
    return render(request, 'InaBack/Dashboard.html')
def insertCollection(request):
    Image=request.POST.get('URL')
    Title=request.POST.get('Title')
    Description = request.POST.get('Description')
    db = firebase.database()
    data = {"Title":Title, "Description":Description,"ImageUrl":Image}
    db.child("Collection").push(data)
    return render(request,'InaBack/Fail.html',{'Image':Image,'Title':Title,'Description':Description})
