import pandas as pd 
from pandas import ExcelFile

tipe_set = {}
def TotalitySales(country):
	global tipe_set

	read_file = pd.read_excel("gesampel.xls",sheet_name= "Orders")
	customer = list(read_file["Order ID"])

	bikin_lambda = list(filter(lambda x: x[:2] == country,customer)) 

	for data in bikin_lambda:
		split = data.split("-")
		tipe_set[split[1]] = 0
	for i in range(len(bikin_lambda)):
		if bikin_lambda[i][3:7] in tipe_set:
			tipe_set[bikin_lambda[i][3:7]] += 1
TotalitySales("US")			
#print(tipe_set)
print("Then sales for US in 2014 : ", tipe_set["2014"])
print("Then sales for US in 2015 : ", tipe_set["2015"])
print("Then sales for US in 2016 : ", tipe_set["2016"])
print("Then sales for US in 2017 : ", tipe_set["2017"])