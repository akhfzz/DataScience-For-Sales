import matplotlib.pyplot as plt 
import numpy as np

#pie chart
Pekerjaan = ["Petani","Nelayan","PNS","TNI","Polri","Tenaga Medis"]
jml = [150,200,100,200,50,180]
plt.pie(jml,autopct="%1.0f%%",labels=Pekerjaan, startangle=54)
plt.axis("equal")
plt.title("Pekerja Indonesia")
plt.show()

#bar chart horizontal

kordinat_x = ["A","B","C","D"]
kordinat_y = [23,45,21,30]
plt.barh(kordinat_x,kordinat_y, color="blue")
plt.title("Jumlah sampel")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

#bar chart vertikal
x = ["A","B","C","D"]
y = [23,45,21,30]
plt.bar(x,y,color="grey")
plt.title("Uji Sampel")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

#plot chart
plt.figure(figsize=(7,8))
titik_x = [2,4,5,6,7]
titik_y = [3,2,4,5,6]
titik_z = [4,5,6,8,9]
plt.plot(titik_x, titik_y, "p-", titik_z, titik_x, "bo")
plt.title("Data Corona")
plt.xlabel("x")
plt.ylabel("y")
plt.legend("[dot = x & z, lurus = x & y]", loc="best")
plt.show()

#histogram
data = np.random.random(1000)
plt.hist(data, 10)
plt.show()

#scatter plot
berat = [80,70,56,64,63]
tinggi = [170,168,156,172,173]
plt.scatter(berat,tinggi)
plt.xlim(55,85)
plt.ylim(155,173)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

#gabungan plot figure
data_x = np.array([2,4,6,8,10])
y1 = data_x **2
y2 = data_x + 5

plt.subplot(1,2,1)
plt.plot(data_x,y1)
plt.legend("[y1=x**2]")

plt.subplot(1,2,2)
plt.plot(data_x,y2)
plt.legend("[y2=x+4]")

plt.suptitle("gabungan")
plt.show()
