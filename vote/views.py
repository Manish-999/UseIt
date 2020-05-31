from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from vote.models import votes,record
from django.http import HttpResponseRedirect
from datetime import datetime,timedelta
from django.contrib.auth.models import User

# Create your views here.

@login_required
def start(req):
    if req.method=="POST":
        name=User.objects.get(username=req.POST.get('name'))
        p=votes.objects.get(user=name,topic=req.POST.get('topic'))
        if req.POST.get('value')=='1':
            p.option1=p.option1+1
        elif req.POST.get('value')=='2':
            p.option2=p.option2+1 
        elif req.POST.get('value')=='3':
            p.option3=p.option3+1 
        elif req.POST.get('value')=='4':
            p.option4=p.option4+1 
        p.applied=p.applied+","+req.user.username
        p.save()
    data=votes.objects.all()
    temp=record()
    date=datetime.now()
    u=[]
    i=0
    for x in data:
        if date.date()>=x.date.date()+ timedelta(days=3):
            temp=record(user=x.user,topic=x.topic,choose1=x.choose1,option1=x.option1,choose2=x.choose2,option2=x.option2,choose3=x.choose3,option3=x.option3,choose4=x.choose4,option4=x.option4,applied=x.applied,date=x.date)
            temp.save()
            x.delete()
        else:
            sum=0
            k=[]
            sum=x.option1+x.option2+x.option3+x.option4
            a=(x.option1/sum)*100
            b=(x.option2/sum)*100
            c=(x.option3/sum)*100
            d=(x.option4/sum)*100
            k=[a,b,c,d,'']
            u.append(x) 
            y=x.applied.split(',')
            print(y)
            for z in y:
                if z==req.user.username:
                    k[4]='disabled'
                    break
            u[i].date=k
            i=i+1
            print(u[i-1].date[0])
    return render(req,'vote/index.html',{'data':u})


@login_required
def pool(req):
    if req.method=="POST":
        m=votes.objects.filter(user=req.user,topic=req.POST.get('topic'))
        print(len(m),"-----------")
        if len(m) >=1:
            return render(req,'vote/create.html')
        data=votes(user=req.user, topic=req.POST.get('topic'), choose1=req.POST.get('o1'),choose2=req.POST.get('o2'),choose3=req.POST.get('o3'),choose4=req.POST.get('o4'),option1=1,option2=1,option3=1,option4=1,applied="a,")
        data.save()
        return HttpResponseRedirect("/vote")
    return render(req,'vote/create.html')


@login_required
def result(req):
    data=record.objects.filter(user=req.user)
    u=[]
    i=0
    for x in data:
        u.append(x)
        sum=x.option1+x.option2+x.option3+x.option4
        a=(x.option1/sum)*100
        b=(x.option2/sum)*100
        c=(x.option3/sum)*100
        d=(x.option4/sum)*100
        k=[a,b,c,d]
        u[i].date=k
        i=i+1
    return render(req,'vote/result.html',{"data":u})
