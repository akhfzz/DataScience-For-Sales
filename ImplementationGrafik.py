import numpy as np 
import pandas as pd
from pandas import ExcelFile
import matplotlib.pyplot as plt

set_plus = {}
set_minus = {}
def TotalProfit(country):
	global set_plus, set_minus
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

	visualp_key_X = set_plus.keys()
	visualp_value_Y = set_plus.values()

	lister_valuep = []
	lister_keyp = []

	for x in visualp_key_X:
		lister_keyp.append(x)
	for y in visualp_value_Y:
		lister_valuep.append(y)

	#bar chart
	plt.figure(figsize=(20,15))
	plt.bar(visualp_key_X, visualp_value_Y, color="blue")
	plt.title("Good Condition")
	plt.xlabel("Profit")
	plt.ylabel("Sub-Category")
	plt.show()

	#pie chart
	plt.pie(lister_valuep[:5],autopct="%1.0f%%",labels=lister_keyp[:5])
	plt.axis("equal")
	plt.title("Total Sale Plus Profit")
	plt.show()


	visualm_key_X = set_minus.keys()
	visualm_value_Y = set_minus.values()

	lister_valuem = []
	lister_keym = []

	for x in visualm_key_X:
		lister_keym.append(x)
	for y in visualm_value_Y:
		lister_valuem.append(y)

	#bar chart
	plt.figure(figsize=(20,15))
	plt.bar(visualm_key_X, visualm_value_Y, color="red")
	plt.title("Low Condition")
	plt.xlabel("Profit")
	plt.ylabel("Sub-Category")
	plt.show()

	#pie chart
	plt.pie(lister_valuem[:5],autopct="%1.0f%%",labels=lister_keym[:5])
	plt.axis("equal")
	plt.title("Total Sale Low Profit")
	plt.show()


TotalProfit("US")
# print(set_plus)