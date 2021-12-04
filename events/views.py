from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def logIn(request):
    next = request.GET.get ('next')
    form = UserLoginForms (request.POST or None)
    if form.is_valid ( ):
        username = form.cleaned_data.get ('username')
        password = form.cleaned_data.get ('password')
        user = authenticate (username=username, password=password)

        login (request, user)
        if next:
            return redirect (next)
        return redirect ('index')
    context = {
        'form': form,
        'button': "LOG IN",
        'action': 'login'
    }
    return render (request, 'login.html', context)

def out(request):
    logout (request)
    return redirect ('login')

@login_required (login_url='login')
def index(request):


    return render(request,"index.html")
@login_required (login_url='login')
def eventView(request):
    listShow = [request.user.id]
    manager = Access.objects.filter(manager_id=request.user.id)
    for clerk in manager:
        listShow.append(clerk.id)
    events = Event.objects.filter(creator_id__in=listShow)

    context = {
        "events": events
    }
    return render(request,"eventview.html",context=context)
@login_required (login_url='login')
def insertEvent(request):

    user_id = request.user.id
    effect = Access.objects.get(user_id = user_id).affect.all()
    centers = Center.objects.all()


    if request.method == "POST":
        form = dict(request.POST)
        form.pop('csrfmiddlewaretoken')

        try:
            if form['effect'][0] in [str(i.id) for i in effect] :
                e = Event.objects.create(
                    title= form['title'][0],
                    affected = Center.objects.get(id = int(form['affect'][0])) ,
                    eventDate = form['date'][0],
                    description = form['description'][0] ,
                    creator = User.objects.get(id = user_id),
                )
                e.effected.set([Center.objects.get(id=int(i)) for i in form['effect']])
                e.save()
        except Exception as error:
            messages.add_message(request, messages.WARNING, error.__str__())




    context={
        'centers':centers,
        'effect': effect
    }
    return  render(request,"insertevent.html",context=context)


@login_required (login_url='login')
def deleteEvent(request,id):
    access = Access.objects.filter(manager_id = request.user.id).first()
    select_event = Event.objects.get(id=id)
    if select_event.creator.id == request.user.id or request.user.id == access.manager.id :

        if select_event.firstAccept == False:
            select_event.delete()
        else:
            messages.add_message(request, messages.WARNING, "امکان ابطال وضعیت های تایید شده وجود ندارد.(1111)")
    else:
        messages.add_message(request, messages.WARNING, "شما به ابطال این خبر دسترسی ندارید.(1110)")

    return redirect('eventView')

@login_required (login_url='login')
def acceptEvent(request):
    user_id = request.user.id
    access = Access.objects.get(user_id=user_id,isManager=True)
    manager = Access.objects.filter(manager_id = user_id)
    print(Event.objects.filter(creator_id__in=[i.user.id for i in manager],firstAccept=True,secendAccept=False))
    centers = [i.id for i in access.affect.all()]
    affectEvents = Event.objects.filter(affected_id__in= centers,firstAccept=False)
    effectEvents = Event.objects.filter(creator_id__in=[i.user.id for i in manager],firstAccept=True,secendAccept=False)
    if request.method == "POST":
        form = dict(request.POST)
        form.pop('csrfmiddlewaretoken')
        if len(form)>0:
            for item in form :
                if item.endswith('des'):
                    eventItem = Event.objects.get(id=int(item[:item.find("-")]))
                    eventItem.description2 = form[item][0]
                    eventItem.save()
                else:
                    eventItem = Event.objects.get(id=int(item))
                    if eventItem.firstAccept == False:
                        eventItem.firstAccept=True
                        eventItem.save()
                    else:
                        eventItem.secendAccept=True
                        eventItem.save()





    context = {
        "affectEvents":affectEvents,
        "effectEvents":effectEvents,
    }
    return render(request,'acceptevents.html',context=context)


@login_required(login_url="login")
def message_error(request,e,filename):
    MessageError.objects.create(
        user=User.objects.get(id=request.user.id),
        message=f"line :{e.__traceback__.tb_lineno}\n"
                f"file name :{filename}\n"
                f"message : {e.__str__()}\n"
    )
    return render(request,'message_error.html')