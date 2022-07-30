from django.http import JsonResponse
from django.shortcuts import render
from django.core import serializers
from .models import data
import pandas as pd
def col2int(colname, df):
    data = []
    for item in df_sale[colname]:
        if isinstance(item, int):
            data.append(item)

        else:
            data.append(0)
    df[colname] = data
def dashboard(request):
    datas = data.objects.all().order_by("date")
    df_sale = pd.read_excel(datas[0].sale.path)
    df_sale.drop(len([df_sale.index]))

    df_sale["کارتن"] = df_sale["تعداد فروش و جایزه-کارتن"]

    df_sale = df_sale[['کد فروشنده'
        , "مرکز توزیع"
        , 'فروشنده'
        , 'کد کالا'
        , 'نام کالا', "کارتن"]]
    df_return = pd.read_excel(datas[0].returnSale.path)
    df_return = df_return[['کد فروشنده'
                            ,"مرکز توزیع"
                            , 'فروشنده'
                            , 'کد کالا'
                            , 'نام کالا'
                            , 'تعداد برگشتی و جایزه برگشتی-کارتن']]
    df_return = df_return.rename(columns={'تعداد برگشتی و جایزه برگشتی-کارتن': "کارتن"})
    box = df_return["کارتن"] * (-1)
    df_return["کارتن"] = box
    concate_sale_return = df_sale.append(df_return)
    pivot = concate_sale_return.groupby(["مرکز توزیع"])["کارتن"].sum()
    pivot = pd.DataFrame(pivot)
    name = datas[0].name
    context = {"sale":df_sale,
               "retuen":df_return,
               "name":name,
               "centers":list(pd.DataFrame(pivot).index),
               "box":list(pivot["کارتن"])}

    return render(request,'Dash1.html',context)

def flex(request):


    return render(request, 'dashboard_with_pivot.html', {})

def pivot_data(request):
    dataset = pd.read_json('json.json')
    data = dataset
    print(data)
    return JsonResponse(data, safe=False)
