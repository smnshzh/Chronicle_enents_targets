from django.shortcuts import render
from .models import *
import pandas as pd


def group_insert(request):
    path="group.xlsx"
    df = pd.read_excel(path)
    groups = df.values.tolist()
    for item in groups:
        ProductGroup.objects.create(
            code= item[0],
            name = item[1],
            maingroup = MainGroup.objects.get(name=item[2])
        )


def product_insert(request):
    path = "goods.xlsx"
    df = pd.read_excel(path)
    data = df.values.tolist()

    for item in data:
        code1= item[0]
        name = item[1]
        inbox = item[2]
        group = item[4]
        weight = item[3]

        if not len(ProductInfo.objects.filter(code1=int(code1) )):
            ProductInfo.objects.create(
                code1=int(code1),
                code2 = 0,
                name = name,
                inBox=int(inbox),
                height=0,
                lenght=0,
                width=0,
                weight=weight,
                group=ProductGroup.objects.get(name=group)
            )


