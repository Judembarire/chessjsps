from django.http import HttpResponse
import requests
from requests.auth import HTTPBasicAuth
import json
from .credentials import MpesaAccessToken, LipanaMpesaPpassword

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Tshirts, Hoodies ,Goodies, Events


def home(request):
    data = Events.objects.all(),
    context = {"data": data}
    return render(request, 'home.html' , context)

def events(request):
    if request.method=="POST":
        parentsname1=request.POST.get('parent name1')
        membersname1=request.POST.get('member name1')
        adm=request.POST.get('adm no')
        Class=request.POST.get('Class')
        dob=request.POST.get('dob')
        gender= request.POST.get('gender')

        # print(name,email,age,gender)
        query=Events(parentsname1=parentsname1,membersname1=membersname1,adm=adm,Class=Class, dob=dob, gender=gender)
        query.save()
        return redirect("/")

    return render(request,"home.html")


def token(request):
    consumer_key = '77bgGpmlOxlgJu6oEXhEgUgnu0j2WYxA'
    consumer_secret = 'viM8ejHgtEmtPTHd'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token": validated_mpesa_access_token})


def pay(request):
    if request.method == "POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Apen Softwares",
            "TransactionDesc": "Web Development Charges"
        }

    response = requests.post(api_url, json=request, headers=headers)
    return HttpResponse("success")

def shopTshirt(request):
    if request.method=="POST":
        parentsname=request.POST.get('parents name')
        membersname=request.POST.get('members name')
        color=request.POST.get('color')
        size=request.POST.get('size')
        units=request.POST.get('units')

        # print(name,email,age,gender)
        query=Tshirts(parentsname=parentsname,membersname=membersname,color=color,size=size, units=units)
        query.save()
        return redirect("/shop")

    return render(request,"shop.html")

def shopHoodies(request):
    if request.method=="POST":
        parentsname2=request.POST.get('parents name2')
        membersname2=request.POST.get('members name2')
        color2=request.POST.get('color2')
        size2=request.POST.get('size2')
        units2=request.POST.get('units2')

        # print(name,email,age,gender)
        query=Hoodies(parentsname2=parentsname2,membersname2=membersname2,color2=color2,size2=size2, units2=units2)
        query.save()
        return redirect("/shop")

    return render(request,"shop.html")

def shopGoodies(request):
    if request.method=="POST":
        parentsname3=request.POST.get('parents name3')
        membersname3=request.POST.get('members name3')
        item=request.POST.get('item')
        units3=request.POST.get('units3')

        # print(name,email,age,gender)
        query=Goodies(parentsname3=parentsname3,membersname3=membersname3,item=item, units3=units3)
        query.save()
        return redirect("/shop")

    return render(request,"shop.html")



def shop(request):
    data = Tshirts.objects.all(), Hoodies.objects.all(), Goodies.objects.all()
    context = {"data": data}
    return render(request, 'shop.html' , context)
