from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect
import pyrebase
from django.http import HttpResponse
# Create your views here.
from pyasn1.compat.octets import null
from .models import ItemCol

config={
    'apiKey': "AIzaSyDTcgwr90Kyn4nm4MVVyepGkuAJdSAVUjA",
    'authDomain': "inatapis-acf70.firebaseapp.com",
    'databaseURL': "https://inatapis-acf70-default-rtdb.firebaseio.com",
    'projectId': "inatapis-acf70",
    'storageBucket': "inatapis-acf70.appspot.com",
    'messagingSenderId': "352530260417",
    'appId': "1:352530260417:web:ad95962e82e608ce2c0f40",
    'measurementId': "G-90HT2DV4TV"

}
firebase = pyrebase.initialize_app(config)
auth=firebase.auth()

def hi(request):
    return render(request,'InaBack/HomePage.html')
#def Signing(request):
    #return render(request,'InaBack/Dashboard.html')
def signout(request):
    return render(request, 'InaBack/HomePage.html')
def postsign(request):
    email=request.POST.get('userMail')
    password=request.POST.get('pass')
    user=auth.sign_in_with_email_and_password(email,password)
    return render(request, 'InaBack/Dashboard.html')
def gethome(request):
    return render(request, 'InaBack/StartHome.html')
def insertCollection(request):
    Image=request.POST.get('URL')
    Title=request.POST.get('Title')
    Description = request.POST.get('Description')
    db = firebase.database()
    data = {"Title":Title, "Description":Description,"ImageUrl":Image}
    db.child("collection").push(data)
    return render(request, 'InaBack/Dashboard.html')
def showCollection(request):
    db = firebase.database()
    collections=db.child("collection").get()
    list=[]
    listTitle = []
    listDescription = []
    listUrl = []
    KeyList=[]
    q=0
    for x in collections:
        list.append(x.val())
        KeyList.append(x.key())
        q=q+1
    ItemList=[]
    for i in range(0,q):
        listTitle.append(list[i]['Title'])
        listDescription.append(list[i]['Description'])
        listUrl.append(list[i]['ImageUrl'])
        item=ItemCol()
        item.title=list[i]['Title']
        item.imageUrl=list[i]['ImageUrl']
        item.description=list[i]['Description'][0:103]
        item.id=KeyList[i]
        ItemList.append(item)
    return render(request,'InaBack/Fail.html',{'Items':ItemList})
def editItem(request):
    item = request.GET.get('ItemId')
    db = firebase.database()
    collection = db.child("collection").child(item).get().val()
    itemCol = ItemCol()
    itemCol.title = collection['Title']
    itemCol.imageUrl = collection['ImageUrl']
    itemCol.description = collection['Description']
    return render(request, 'InaBack/EditItem.html',{"itemCol":itemCol,"ItemId":item})
def deleteItem(request):
    item=request.GET.get('ItemId')
    db = firebase.database()
    db.child("collection").child(item).remove()

    return redirect('show')
def updateCollection(request):
    item = request.POST.get('ItemId')
    Image = request.POST.get('URL')
    Title = request.POST.get('Title')
    Description = request.POST.get('Description')
    db = firebase.database()
    db.child("collection").child(item).update({"Title":Title,"Description":Description,"ImageUrl":Image})
    return redirect('show')
