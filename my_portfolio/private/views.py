from private.models import Vcard
from django.shortcuts import render, redirect, HttpResponse
from csv import writer, reader
import pandas as pd
from datetime import datetime


def data(request):
    return render(request, 'private/data.html')

def home(request):
    template = 'private/home.html'
    if request.session.has_key('login'):
        return render(request, template)
    else:
        return redirect('private:login')


def logout(request):
    request.session.flush()
    return redirect('private:login')


def login(request):
    if request.session.has_key('login'):
        return redirect('private:home')

    if request.method == 'POST':
        email = request.POST['uname']
        password = request.POST['password']
        if email == 'ishaan@private.com' and password == 'Ishaan@password':
            request.session['login'] = True
            return redirect('private:home')
        return render(request, "private/login.html", {'error': 'Invalid Username or Password'})
    return render(request, "private/login.html")

import gspread
from oauth2client.service_account import ServiceAccountCredentials

def shop(request):
    template = "private/shop.html"
    if request.method == 'POST':

        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        data = {
        "type": "service_account",
        "project_id": "sheets-323915",
        "private_key_id": "885ac14f63a30c6b4c5961758551525e69cbb4f3",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDAIQTh4EGsWTCA\nUvGW8aMnvaV5Mnsp13NDbqENYOraAzp51GQs3DjkiViKeDeHOPLCAqx27Uoei51k\n+NLWtBPr16EpcSYHUftoioV1ap35XEwaOYPBgOIo9n9e8PLNdplQBVBVvFM31bBL\nSHXEdleBUAv62qfPmlaGZBtY3Uxs+dqLg4YFCem5ugcijAHx68c9qVCRaeHYw3nc\n57uS2uxumAW/bIBbpJQCVMGXll1XNi7/4UDJeoB9t/UNhWi9rxQs/b3RNsky79Kw\nPqETv1FyzymM3oAmG3J9OD/aSxxYGrKA4SFVhHgFQdjVFsTTeYnrz8Eh+JsrxEXf\ntzfeKf8rAgMBAAECggEACSwqYwGasQ3rBQgGClpL8J7wZ6UI1e+4IYfbvttEgGxi\nCM9NNF++hEP9taf/9//jMG8B6TBH9xsG7yX6pDnMWlic6ZvCIIcB9TTpIo4Yr6nV\nOkqfpzKDhEghvu3K8b3lRjmSuHJ5bfN7lgSGFtSS4JS/6wCFvXbABcIsFLsv+w3X\nWBDyT/3sEkcnSyf9Y71fmBZxTV9i5cM7wgiFxpAWeG/tKwkOog3J0qekQiXunLbx\nSETH6FKd1DVkm98WcaclIgBYBucrJMAk0JCdoqPiZ0yFOT2n0AO5CUmgtMFePgDa\nKHW7wsyUsGQmCHtkqfTNFPUu78mKBu0A+u+b7tasLQKBgQD4qgkyDriWrxds6oTg\nVv1CoedwC+Do62ifX8cpqjGV8ceUpnYhqiHUx8JS60ScuZYn9tc1jMQhVbmblbih\nsBXqF2rLje/V7cdkvTtvQQDdAp+j4GAs0WI6dUrL8GBJlaLvbQoWGLU3N4viutsj\nYz6d7BT35PvXUkofxAbtcpSvRwKBgQDFzARvkVVCm1CWBU3D4Cumnw3se38owI/D\nBo+u2jRHS1lbu2kUtKrOyvWT2Z5Cfg1IwpZdIVCB6qbNxD6JHA84awJeZP+ElqPx\nzFTEHAMHneNcIQO25Dt1OzARcJKbuBwjWoqCxfrBP8Dc+SEYcZjAkowB7ZHbCNyg\nYP8GiqAK/QKBgAXDcykc3Dxp3IIiwWetvHsB46peLB1Z73faMXSOxE10aCrS3OQU\n3GnhI2jmmRWE260bdIuCMr2PDhlEFB5zRV7CojALnyZ3N2rnU+xVNl7pA6g5uCDx\nzXQLaetmK+UoubkQ7u3qLrET8YMUz6V3VGk2opnITeoEt0EbOwnf4QBbAoGAAMv5\nmJl1Rndps7EBxzA3/MvXOoSk1n0wFxEHsySd4UukaIIwwiyYI40dwCK4SHxJgWmH\nQYjI0j0nvtxzhAng5dFIiSjO/rG8p1SzYrbaLEWujMh1Q19X/fjnEKrrbEUpl9rd\ng/lYMT8Yf8thHsAWZXAxsDBMzh0TBnJdlKEqU+ECgYBVP1jeJp4Vaj5vhXET5Rql\nITOFK0hOJMO6xKwe1Cvpv5GCsdt+0PCNJsIlbemk+Wb9bCYun7fxlvt4Go7MXp3E\nwnhxgP/Qeh4bweONHDIhJ2FKHQ1/W8uyN9jliKTXzuO+SGjWUexxC6SSykDUDsKE\nj2kBiKbYMZzhTslvw+UYeA==\n-----END PRIVATE KEY-----\n",
        "client_email": "ishaan@sheets-323915.iam.gserviceaccount.com",
        "client_id": "112852381037047092896",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": 'https://www.googleapis.com/robot/v1/metadata/x509/ishaan%40sheets-323915.iam.gserviceaccount.com'
        }
        try:
            creds = ServiceAccountCredentials.from_json_keyfile_dict(data, scope)
            client = gspread.authorize(creds)
            sheet = client.open("shop_expenditure").sheet1 

            python_sheet = sheet.get_all_values()

            date = request.POST['entry_date']
            earnings = str(int(request.POST['receive']))
            spend = str(int(request.POST['spend']))
            desc = request.POST['description']
            report = [date, earnings, spend, desc]
            sheet.insert_row(report,len(python_sheet)+1)
            return render(request, template, context={
                'msg': "[ "+', '.join(report)+" ] following data has been added successfully",
            })
        except:
            return render(request, template, context={
                'err': 'There is some error while processing'
            })

    return render(request, template, context={'err': None, 'msg': None})


def summary(request):
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    data = {
    "type": "service_account",
    "project_id": "sheets-323915",
    "private_key_id": "885ac14f63a30c6b4c5961758551525e69cbb4f3",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDAIQTh4EGsWTCA\nUvGW8aMnvaV5Mnsp13NDbqENYOraAzp51GQs3DjkiViKeDeHOPLCAqx27Uoei51k\n+NLWtBPr16EpcSYHUftoioV1ap35XEwaOYPBgOIo9n9e8PLNdplQBVBVvFM31bBL\nSHXEdleBUAv62qfPmlaGZBtY3Uxs+dqLg4YFCem5ugcijAHx68c9qVCRaeHYw3nc\n57uS2uxumAW/bIBbpJQCVMGXll1XNi7/4UDJeoB9t/UNhWi9rxQs/b3RNsky79Kw\nPqETv1FyzymM3oAmG3J9OD/aSxxYGrKA4SFVhHgFQdjVFsTTeYnrz8Eh+JsrxEXf\ntzfeKf8rAgMBAAECggEACSwqYwGasQ3rBQgGClpL8J7wZ6UI1e+4IYfbvttEgGxi\nCM9NNF++hEP9taf/9//jMG8B6TBH9xsG7yX6pDnMWlic6ZvCIIcB9TTpIo4Yr6nV\nOkqfpzKDhEghvu3K8b3lRjmSuHJ5bfN7lgSGFtSS4JS/6wCFvXbABcIsFLsv+w3X\nWBDyT/3sEkcnSyf9Y71fmBZxTV9i5cM7wgiFxpAWeG/tKwkOog3J0qekQiXunLbx\nSETH6FKd1DVkm98WcaclIgBYBucrJMAk0JCdoqPiZ0yFOT2n0AO5CUmgtMFePgDa\nKHW7wsyUsGQmCHtkqfTNFPUu78mKBu0A+u+b7tasLQKBgQD4qgkyDriWrxds6oTg\nVv1CoedwC+Do62ifX8cpqjGV8ceUpnYhqiHUx8JS60ScuZYn9tc1jMQhVbmblbih\nsBXqF2rLje/V7cdkvTtvQQDdAp+j4GAs0WI6dUrL8GBJlaLvbQoWGLU3N4viutsj\nYz6d7BT35PvXUkofxAbtcpSvRwKBgQDFzARvkVVCm1CWBU3D4Cumnw3se38owI/D\nBo+u2jRHS1lbu2kUtKrOyvWT2Z5Cfg1IwpZdIVCB6qbNxD6JHA84awJeZP+ElqPx\nzFTEHAMHneNcIQO25Dt1OzARcJKbuBwjWoqCxfrBP8Dc+SEYcZjAkowB7ZHbCNyg\nYP8GiqAK/QKBgAXDcykc3Dxp3IIiwWetvHsB46peLB1Z73faMXSOxE10aCrS3OQU\n3GnhI2jmmRWE260bdIuCMr2PDhlEFB5zRV7CojALnyZ3N2rnU+xVNl7pA6g5uCDx\nzXQLaetmK+UoubkQ7u3qLrET8YMUz6V3VGk2opnITeoEt0EbOwnf4QBbAoGAAMv5\nmJl1Rndps7EBxzA3/MvXOoSk1n0wFxEHsySd4UukaIIwwiyYI40dwCK4SHxJgWmH\nQYjI0j0nvtxzhAng5dFIiSjO/rG8p1SzYrbaLEWujMh1Q19X/fjnEKrrbEUpl9rd\ng/lYMT8Yf8thHsAWZXAxsDBMzh0TBnJdlKEqU+ECgYBVP1jeJp4Vaj5vhXET5Rql\nITOFK0hOJMO6xKwe1Cvpv5GCsdt+0PCNJsIlbemk+Wb9bCYun7fxlvt4Go7MXp3E\nwnhxgP/Qeh4bweONHDIhJ2FKHQ1/W8uyN9jliKTXzuO+SGjWUexxC6SSykDUDsKE\nj2kBiKbYMZzhTslvw+UYeA==\n-----END PRIVATE KEY-----\n",
    "client_email": "ishaan@sheets-323915.iam.gserviceaccount.com",
    "client_id": "112852381037047092896",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": 'https://www.googleapis.com/robot/v1/metadata/x509/ishaan%40sheets-323915.iam.gserviceaccount.com'
    }


# https://drive.google.com/uc?export=view&id=18ExT0Y8AHhhD5uJUSnSCOpCMtDMT2R5q

    creds = ServiceAccountCredentials.from_json_keyfile_dict(data, scope)
    client = gspread.authorize(creds)
    sheet = client.open("shop_expenditure").sheet1 

    template = 'private/summary.html'
    python_sheet = sheet.get_all_values()

    currentMonth = str(datetime.now().month)
    currentYear = str(datetime.now().year)
    
    df = pd.DataFrame(python_sheet[1:], columns=python_sheet[0])
    df['DATE'] = pd.to_datetime(df['DATE'])
    sd = currentYear+'-'+currentMonth+'-'+'01'
    newdf = (df['DATE'] >= sd)
    newdf = df.loc[newdf]
    totalspend = sum(map(int, newdf['SPEND']))
    totalearned = sum(map(int, newdf['EARNINGS']))
        
    return render(request, template, {'rows': python_sheet[1:], 'spend': totalspend, 'earned': totalearned})


def cards(request):
    template = 'private/cards.html'
    context = dict()
    card_list = Vcard.objects.all()
    context['cards'] = card_list
    return render(request, template, context)

def card(request, pk):
    card = Vcard.objects.get(pk=pk)
    context = {
        'card': card,
    }
    return render(request, 'private/card-details.html', context)
