from django.shortcuts import render
import pyodbc
import pandas as pd
import numpy as np
def saleInfo(request):
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.1.12;DATABASE=DSDB_CN_1400;UID=SysTest;PWD=Baraka95@dmin')
    print("connected")
    cursor = cnxn.cursor()
    manufacturer = cursor.execute('SELECT * FROM Manufacturer').fetchall()
    print("cursed")
    goodgroup = None
    groupName = None
    month = None
    if request.method == "POST":
        goodgroup = request.POST["goodgroup"]
        groupName = cursor.execute(f'SELECT * FROM Manufacturer WHERE ID = {int(goodgroup)}').fetchall()[0][1]
        if month :
            month = request.POST["month"]

    Data = None
    if goodgroup and month :
        Data = pd.read_sql(f'SELECT SellId,SellDate,ManufacturerName,ManufacturerId,SellPackQty,DCName FROM SalesReview WHERE ManufacturerId ={int(goodgroup)}',cnxn)


    else:
        Data = pd.read_sql('SELECT SellId,SellDate,ManufacturerName,SellPackQty,DCName FROM SalesReview',cnxn)


    Data["year"]= Data["SellDate"].str[:4]
    Data["month"]=Data["SellDate"].str[5:7]
    Data["day"]=Data["SellDate"].str[9:10]
    if month:
        Data[Data.month == month]
    pivot_all = pd.pivot_table(Data,index="DCName",columns=['year'],values="SellPackQty",aggfunc=np.sum)
    pivot_all["شعبه"] = pivot_all.index



    context= {
        "data": pivot_all,
        "data_list":pivot_all.values.tolist(),
        "columns": pivot_all.columns,
        "manufacturer":manufacturer,
        # 'inData':manfacturer_inData
        'group':groupName,
        'rangeMonth':range(1,13)
    }
    return render(request,"Dash1.html",context)