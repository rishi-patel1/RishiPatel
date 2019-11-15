import matplotlib.pyplot as mpl
x=[1,2,3,4,5,6,7,8,9,10,11,12]
y=[211000,183300,224700,222700,209600,201400,295500,361400,234000,266700,412800,300200]

mpl.plot(x,y)
mpl.xlabel('Month Number')
mpl.ylabel('Profit in dollars')
mpl.title('Company profit per month')
mpl.show()


face_cream=[2500,2630,2140,3400,3600,2760,2980,3700,3540,1990,2340,2900]
face_wash=[1500,1200,1340,1130,1740,1555,1120,1400,1780,1890,2100,1760]
mpl.bar(x,face_cream,label='Face Cream sales data')
mpl.bar(x,face_wash,label='Face Wash sales data')
mpl.xlabel('Month Number')
mpl.ylabel('Sales units in number')
mpl.title('Bar graph')
mpl.legend()
mpl.show()



toothpaste=[5200,5100,4550,5870,4560,4890,4780,5860,6100,8300,7300,7400]
bathing_soap=[9200,6100,9550,8870,7760,7490,8980,9960,8100,10300,13300,14400]
shampoo=[1200,2100,3550,1870,1560,1890,1780,2860,2100,2300,2400,1800]
moisturizer=[1500,1200,1340,1130,1740,1555,1120,1400,1780,1890,2100,1760]
values=[sum(face_cream),sum(face_wash),sum(toothpaste),sum(bathing_soap),sum(shampoo),sum(moisturizer)]
labels=['face_cream','face_wash','toothpaste','bathing_soap','shampoo','moisturizer']
mpl.axis('equal')
mpl.title('Sales data')
mpl.pie(values,labels=labels,autopct='%0.1f%%')
mpl.legend(labels)
mpl.show()



mpl.plot([],[],label='face_cream',linewidth=5,color='purple')
mpl.plot([],[],label='face_wash',linewidth=5,color='pink')
mpl.plot([],[],label='toothpaste',linewidth=5,color='red')
mpl.plot([],[],label='bathing_soap',linewidth=5,color='black')
mpl.plot([],[],label='shampoo',linewidth=5,color='green')
mpl.plot([],[],label='moisturizer',linewidth=5,color='yellow')
mpl.stackplot(x,face_cream,face_wash,toothpaste,bathing_soap,shampoo,moisturizer,colors=['purple','pink','red','black','green','yellow'])
mpl.xlabel('Month number')
mpl.ylabel('Sales units in number')
mpl.title('All product sales data using stack plot')
mpl.legend()
mpl.show()





bins=[150000,175000,200000,225000,250000,300000,350000]
mpl.hist(y,bins,histtype='bar')
mpl.xlabel('Profit range in dollars')
mpl.ylabel('Actual profit in dollars')
mpl.title('Profit data')
mpl.plot([],[],label='Profit data',color='blue',linewidth=5)
mpl.legend()
mpl.show()
