import pandas as pd 
from pandas import ExcelFile

tipe_set = {}
set_plus = {}
set_minus = {}

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

def TotalProfit(country):
	global set_minus,set_plus
	
	read_file = pd.read_excel("gesampel.xls",sheet_name= "Orders")
	choice_profit = read_file.filter(items=["Order ID","Sub-Category","Product Name", "Profit"])
	data_extract = choice_profit.loc[choice_profit["Order ID"].str[:2]==country]
	data_tolist = data_extract.values.tolist()

	filter_data_plus = list(filter(lambda x: x[3]>0,data_tolist))
	for plus in filter_data_plus:
		set_plus[plus[1]]= 0
	for i in range(len(filter_data_plus)):
		if filter_data_plus[i][1] in set_plus:
			set_plus[filter_data_plus[i][1]] += filter_data_plus[i][3]

	filter_data_minus = list(filter(lambda x: x[3]<0, data_tolist))
	for minus in filter_data_minus:
		set_minus[minus[1]] = 0
	for i in range(len(filter_data_minus)):
		if filter_data_minus[i][1] in set_minus:
			set_minus[filter_data_minus[i][1]] += filter_data_minus[i][3]

	input("It are products from US which getting plus profit")
	for data_plus in set_plus:
		print(data_plus)

	input("it are products from US wich getting low profit")
	for data_min in set_minus:
		print(data_min)

	total_plus = sum(set_plus.values())
	print("Plus Profit: {0} {1} ".format("$",total_plus))
	total_minus = sum(set_minus.values())
	print("Low Profit: {0} {1} ".format("$",total_minus))
	total_all = total_plus + total_minus
	print("Totality: {0} {1} ".format("$",total_all))
TotalProfit("US")
