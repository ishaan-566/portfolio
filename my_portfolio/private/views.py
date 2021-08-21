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
        cards = Vcard.objects.all()
        context = {
            'cards': cards
        }
        return render(request, template, context)
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

def shop(request):
    template = "private/shop.html"
    if request.method == 'POST':
        date = request.POST['entry_date']
        earnings = str(int(request.POST['receive']))
        spend = str(int(request.POST['spend']))
        desc = request.POST['description']
        report = [date, earnings, spend, desc]
        with open('shop_expenditure.csv', 'a') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(report)
            f_object.close()
        return HttpResponse(" ".join(report))

    return render(request, template)

def summary(request):
    template = 'private/summary.html'
    rows = []
    with open('shop_expenditure.csv', 'r') as csvfile:
        csvreader = reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)
    currentMonth = str(datetime.now().month)
    currentYear = str(datetime.now().year)
    df = pd.read_csv("shop_expenditure.csv")
    df['DATE'] = pd.to_datetime(df['DATE'])
    sd = currentYear+'-'+currentMonth+'-'+'01'
    newdf = (df['DATE'] >= sd)
    newdf = df.loc[newdf]
    totalspend = sum(newdf['SPEND'])
    totalearned = sum(newdf['EARNINGS'])
        
    return render(request, template, {'rows': rows, 'spend': totalspend, 'earned': totalearned})
