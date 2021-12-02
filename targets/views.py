from django.shortcuts import render,redirect
from .models import *
import pandas as pd
import json
def insert_targets(request):
    access = TargetAccess.objects.filter(user_id = request.user.id).first()
    centers = access.centers.all()
    month = SetVisitorTarget.Month.choices
    if request.method == "POST":
        form = dict(request.POST)
        form.pop('csrfmiddlewaretoken')
        if 'centermonth' in form :
            center = CenterD.objects.get(id = form['center'][0] )

            visitors = Visitor.objects.filter(cneter=center,status=True).order_by('superviser')
            month = month[int(form['month'][0])-1]
            supervisers = Superviser.objects.filter(center=center)
            context = {
                'center':center,
                'month':month,
                'visitors':visitors,

                'supervisers':supervisers
            }
            return render(request,'visitorscontrol.html',context=context)
        elif "visitorcontrol" in form:
            form.pop('visitorcontrol')
            center = CenterD.objects.get(id = form['center'][0] )
            form.pop('center')
            month = month[int(form['month'][0])-1]
            form.pop('month')
            if 'visitor_active' in form :
                for id in form['visitor_active']:
                    form.pop(id)
                    visitor = Visitor.objects.get(id=int(id))
                    visitor.status = False
                form.pop('visitor_active')
            for key , value in form.items():
                print(key ,value)
                visitor = Visitor.objects.get(id=int(key))
                if  visitor.superviser.id != int(value[0]):
                    visitor.superviser = Superviser.objects.get(id = int(value[0]))
                    visitor.save()
            visitors = Visitor.objects.filter(cneter_id = center.id)
            pgroups = center.products_group.all()
            context = {
                'center':center,
                'month':month,
                'visitors':visitors.order_by('superviser'),
                'pgroups': pgroups,

                    }
            return render(request, 'settargets.html', context=context)
        elif "set_targets" in form:
            month = month[int(form['month'][0])-1]
            form.pop("month")
            form.pop("set_targets")
            visitors = list(set(form["visitors"]))

            form.pop('visitors')
            blanky=[]
            for key , value in form.items():
                gp = ProductGroup.objects.get(id=int(key))
                maping = dict(zip(visitors,value))
                for id , num in maping.items():
                    blanky.append(gp.name + " برای  " + Visitor.objects.get(id=int(id)).name + " مقدار  " + num+" در ماه  "+
                                  month[1]+ " قرار داده شد. ")

            context = {
                'blanky':blanky
            }
            return render(request,'blanky.html',context=context)

    context={
        "access":access,
        'month':month,
        'centers': centers}
    return render(request,'inserttargets.html',context=context)

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