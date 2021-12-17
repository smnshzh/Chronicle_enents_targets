from django.shortcuts import render
from .models import *
import pandas as pd
def data_insert(request):
    path = "Book1.xlsx"
    df = pd.read_excel(path)
    df = pd.read_excel("Book1.xlsx")
    groups = set(df['group'].tolist())
    data = df.values.tolist()
    i=1
    j=1

    for item in data:
        code1= item[0]
        code2 = item[1]
        name = item[2]
        inbox = item[3]
        group = item[4]
        weight = item[5]
        l = item[6]
        w = item[7]
        h = item[8]

        if str(code1) == 'nan':
            code1 = j
            j+=1
        ProductInfo.objects.create(
            code1=int(code2),
            code2=int(code1),
            name = name,
            inBox=int(inbox),
            height=float(h),
            lenght=float(l),
            width=float(w),
            weight=weight,
            group=ProductGroup.objects.get(name=group)
        )


