import matplotlib.pyplot as plt
import treating_data_frame as tdf

x=['1','2','3','4','5']
y=['1','2','3','4','5']

teste = tdf.product_sale_date(df_main,'71053','2010-01-01','2010-12-30')
plt.plot(x,y)
plt.xlabel("X")
plt.ylabel("Y")
#plt.show()
plt.savefig('teste.png')

