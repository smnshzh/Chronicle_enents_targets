from django.shortcuts import render,redirect
from .models import *
from events.views import message_error
from django.contrib import messages
def insert_targets(request):
    try:
        # change change access from get to filter
        access = TargetAccess.objects.filter(user_id = request.user.id).first()
        centers = None
        # بررسی دسترسی به مراکز توزیع
        if access:
            centers = access.centers.all()
        month = SetVisitorTarget.Month.choices
        # ارسال درخواست
        if request.method == "POST":
            form = dict(request.POST)
            print(form)
            form.pop('csrfmiddlewaretoken')
            # مرحله اول بررسی مرکز و درصورت تعریف شدن اهداف مرکز اجازه ورود به
            # مرحله بعد و بررسی ویزیتورهای ماه را صادر می کند
            if 'centermonth' in form  :
                if not centers:
                    return redirect('insert_targets')
                month = month[int(form['month'][0]) - 1]
                center = CenterD.objects.get(id = form['center'][0] )

                if not CenterTargetDefinde.objects.filter(center=center, month=month[0]).first() or not center in centers:
                    messages.add_message(request,messages.WARNING,"امکان بررسی اهداف این ماه به دلیل عدم درج اهداف  شعبه انتخابی در ماه انتخابی وجود ندارد یا شما به شعبه انتخابی دسترسی ندارید")
                    return redirect('insert_targets')


                visitors = Visitor.objects.filter(cneter=center,status=True).order_by('superviser')

                supervisers = Superviser.objects.filter(center=center)
                disactive_visitors = Visitor.objects.filter(cneter=center,status=False).order_by('superviser')
                context = {
                    'center':center,
                    'month':month,
                    'visitors':visitors,
                    'disactive_visitors':disactive_visitors,
                    'supervisers':supervisers
                }
                return render(request,'visitorscontrol.html',context=context)
            elif "disactive_visitors" in form:
                form.pop("disactive_visitors")
                center = CenterD.objects.get(id=form['center'][0])
                form.pop('center')
                month = month[int(form['month'][0]) - 1]
                form.pop('month')
                if 'visitor_active' in form:
                    for id in form['visitor_active']:
                        form.pop(id)
                        visitor = Visitor.objects.get(id=int(id))
                        visitor.status = True
                        visitor.save()
                    form.pop('visitor_active')
                for key, value in form.items():

                    visitor = Visitor.objects.get(id=int(key))
                    if visitor.superviser.id != int(value[0]):
                        visitor.superviser = Superviser.objects.get(id=int(value[0]))
                        visitor.save()
                visitors = Visitor.objects.filter(cneter_id=center.id)
                supervisers = Superviser.objects.filter(center=center)
                disactive_visitors = Visitor.objects.filter(cneter=center, status=False).order_by('superviser')

                context = {
                    'center': center,
                    'month': month,
                    'visitors': visitors,
                    'disactive_visitors': disactive_visitors,
                    'supervisers': supervisers
                }
                return render(request, 'visitorscontrol.html', context=context)


            elif "visitorcontrol" in form:
                form.pop("visitorcontrol")
                center = CenterD.objects.get(id = form['center'][0] )
                form.pop('center')
                month = month[int(form['month'][0])-1]
                form.pop('month')
                if 'visitor_active' in form :
                    for id in form['visitor_active']:
                        form.pop(id)
                        visitor = Visitor.objects.get(id=int(id))
                        visitor.status = False
                        visitor.save()
                    form.pop('visitor_active')
                for key , value in form.items():

                    visitor = Visitor.objects.get(id=int(key))
                    if  visitor.superviser.id != int(value[0]):
                        visitor.superviser = Superviser.objects.get(id = int(value[0]))
                        visitor.save()
                visitors = Visitor.objects.filter(cneter_id = center.id)
                pgroups = center.products_group.all()
                is_made_target = SetVisitorTarget.objects.filter(visitor_id__in=[visitor.id for visitor in visitors],
                                                                 month=month[0],
                                                                pgroup_id__in = [pgroup.id for pgroup in pgroups]
                                                                 )
                pgroup_dict = {item.pgroup.id:{} for item in is_made_target}
                for item in is_made_target :
                    pgroup_dict[item.pgroup.id][item.visitor.id]=item.qnty

                context = {
                    'center':center,
                    'month':month,
                    'visitors':visitors.order_by('superviser'),
                    'pgroups': pgroups,
                    'pgroup_dict':pgroup_dict,
                    'seted_targets':is_made_target

                        }
                return render(request, 'settargets.html', context=context)
            elif "set_targets" in form:
                center = CenterD.objects.get(id=form['center'][0])
                month = month[int(form['month'][0])-1]
                form.pop("month")
                form.pop("set_targets")
                form.pop("center")

                visitors = []

                for item in form["visitors"] :
                    if not item in visitors:
                        visitors.append(item)

                form.pop('visitors')

                blanky=[]
                for key , value in form.items():
                    pg = ProductGroup.objects.get(id=int(key))
                    maping = dict(zip(visitors,value))
                    for id , num in maping.items():
                        visitor = Visitor.objects.get(id=int(id))
                        qnty = 0
                        if  num.isnumeric():
                            qnty = int(num)
                        seted_target = SetVisitorTarget.objects.filter(visitor=visitor,
                                                        month = month[0],
                                                        pgroup_id=pg.id
                                                        ).first()
                        if seted_target and seted_target.qnty != qnty  :
                            if qnty == 0:
                                seted_target.delete()
                            else:
                                seted_target.qnty = qnty
                                seted_target.save()
                        elif qnty and not seted_target:
                            SetVisitorTarget.objects.create(visitor=visitor,
                                                            month=month[0],
                                                            pgroup_id=pg.id,
                                                            qnty=qnty
                                                            )
                # context = {
                #     'blanky':blanky
                # }
                return redirect('insert_targets')

        context={
            "access":access,
            'month':month,
            'centers': centers}
        return render(request, 'selectCenterMonth.html', context=context)
    except Exception as e:
         filename=__file__
         message_error(request,e,filename)
    return render(request, 'message_error.html')



def center_targets_definde(request):
    months = CenterTargetDefinde.Month.choices
    centers = CenterD.objects.all()
    pgs = ProductGroup.objects.all()
    if request.method == "POST":
        form = dict(request.POST)
        form.pop('csrfmiddlewaretoken')
        month = form['month'][0]
        form.pop('month')
        sended_centers = form['center']
        form.pop('center')
        for key,value in form.items():
            pg = ProductGroup.objects.get(id=int(key))
            for center , qnt in zip(sended_centers,value):
                qnty = 0
                if qnt :
                    qnty = qnt
                    CenterTargetDefinde.objects.create(
                        center = CenterD.objects.get(id=int(center)),
                        Qnty=int(qnty),
                        Pgroup=pg,
                        month = month[0]


                            )

        print(form)
    context = {
        "months":months,
        "centers":centers,
        "pgs":pgs
    }
    return render(request,'SetCenterTargets.html',context=context)





# def makedata(request):
#     path ='Book1.xlsx'
#     df_visitors = pd.read_excel(path,sheet_name="Sheet1")
#     df_super = pd.read_excel(path,sheet_name="super")
#     df_visitor_list = df_visitors.values.tolist()
#     df_super_list = df_super.values.tolist()
#     # for item in df_super_list:
#     #     Superviser.objects.create(
#     #         code = int(item[0]),
#     #         name = item[1],
#     #         center= CenterD.objects.get(code=int(item[2]))
#     #
#     #     )
#     for item in df_visitor_list :
#         Visitor.objects.create(
#             code = int(item[0]),
#             name = item[1],
#             cneter=CenterD.objects.get(code = int(item[4])),
#             superviser=Superviser.objects.get(code = int(item[6])),
#             line = SaleLine.objects.get(code=int(item[5])),
#             status=True
#         )
#     return redirect('index')