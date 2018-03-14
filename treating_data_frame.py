import pandas as pd
from matplotlib import pyplot
import matplotlib.patches as mpatches
from datetime import datetime


def treating_csv():
    df = pd.read_csv('./data_test.csv')
    df.drop('InvoiceNo',axis=1,inplace=True)
    df = df[(df['Quantity'] > 0)]
    return df

def product_more_sale_country(df,country):
    df_country =pd.DataFrame(df[(df['Country'] ==country)])
    df_country.drop(['InvoiceDate','UnitPrice','CustomerID','Country','StockCode'],axis=1,inplace=True)
    list_quantity=df_country.groupby(['Description']).sum()
    product_more_sale={'product':list_quantity['Quantity'].idxmax()}
    return product_more_sale

def product_more_sale(df):
    df_product=df.drop(['InvoiceDate','UnitPrice','CustomerID','Country','StockCode'],axis=1)
    list_quantity=df_product.groupby(['Description']).sum()
    product_more_sale_world = {"product":list_quantity['Quantity'].idxmax()}
    return product_more_sale_world

def best_client(df):
    df_best_client=df.drop(['InvoiceDate','Country','StockCode'],axis=1)
    df_best_client["total"]=  df_best_client.Quantity * df_best_client.UnitPrice

    client_best = df_best_client.groupby(['CustomerID']).sum()
    best_client_price={'CustomerID':client_best['total'].idxmax(),'value_sale':client_best['total'].max()}
    best_client_quantity={'CustomerID':client_best['Quantity'].idxmax(),'value_sale':client_best['Quantity'].max()}
    best_client = {"bigger_price":best_client_price,"bigger_quantity":best_client_quantity}

    return best_client

def product_sale_date(df,product,dt_begin,dt_end):
    df_sale_product=df.drop(['UnitPrice','CustomerID','Country'],axis=1)
    df_sale_product['InvoiceDate']= pd.to_datetime(df['InvoiceDate'])
    df_sale_product['InvoiceDate']= df_sale_product['InvoiceDate'].apply(lambda x: x.strftime('%Y-%m-%d'))
    df_sale_product=pd.DataFrame(df_sale_product[(df_sale_product['StockCode']==product) & ((df_sale_product['InvoiceDate']>=dt_begin) & (df_sale_product['InvoiceDate']<dt_end))])
    products=df_sale_product.groupby(['InvoiceDate']).sum().reset_index().rename(columns={0:'count'})
    
    product_sale_date={"Quantity":[0],"Date":[0]}
    
    for x in products['InvoiceDate']:
        product_sale_date['Date'].append(x)
    
    for x in products['Quantity']:
       product_sale_date['Quantity'].append(x)
   
    return product_sale_date

def percentage_product(df,product):
    df_product_main=df.drop(['InvoiceDate','UnitPrice','CustomerID','Country'],axis=1)

    df_product = pd.DataFrame(df_product_main[(df_product_main['Description'] ==product)])

    sale_product=df_product['Quantity'].sum()

    product_total =df_product_main['Quantity'].sum()
    percentage =perc(sale_product,product_total)
    return percentage

def perc(a,b):
	if b == 0:
		return 0

	p = a/b * 100 
	return round(p,2)
    
def percente_product_country(df):
    df_country = df.groupby(['Country']).sum().reset_index()
    series_country = df_country['Country']
    list_countries={}
    list_sale={}

    for x in series_country:
        list_countries[x]=pd.DataFrame((df[(df['Country'] ==x)]))

    for x in list_countries:
        list_countries[x].drop(['Country','StockCode','Description','InvoiceDate','UnitPrice','CustomerID'],axis=1,inplace=True)
        list_sale[x] = list_countries[x]['Quantity'].sum()

    df_product_main=df.drop(['InvoiceDate','UnitPrice','CustomerID','Country'],axis=1)
    quantity_total = df_product_main['Quantity'].sum()

    for country in list_sale:
        list_sale[country]=perc(list_sale[country],quantity_total)
    list_sale={'list_percent':list_sale,'total':quantity_total}
    print  (list_sale)
    return list_sale

def generate_graph_sale_date(data):
    df_graph = pd.DataFrame({'Product':data['Quantity']},index=data['Date'])

    df_graph.plot()
    pyplot.xlabel("Data")
    pyplot.grid(True)
    pyplot.ylabel("Qauntidade Vendida")
    pyplot.savefig('./graphs/quantity_sale.png')

def generate_graph_sale_country(data):

    list_graph={'index':[],'value':[]}

    for country in data['list_percent']:
        list_graph['index'].append(country)
        list_graph['value'].append(data['list_percent'][country])

    df_graph = pd.Series(list_graph['value'],index=list_graph['index'])
    df_graph.plot.pie(autopct='%.2f%%', fontsize=15,figsize=(10, 10))

    blue_patch = mpatches.Patch(color='black', label='Sale by product')
    red_patch = mpatches.Patch(color='black', label='Total product:'+str(data['total']))
    
    pyplot.xlabel("PERCENTAGE OF SALE BY COUNTRY")
    pyplot.legend(handles=[red_patch,blue_patch])
    pyplot.ylabel("")
    
    pyplot.savefig('./graphs/percente_sale_by_country')


df_main=treating_csv()

print(product_more_sale_country(df_main,"United Kingdom"))
print(product_more_sale(df_main))
print(best_client(df_main))
print(percentage_product(df_main,'RED TOADSTOOL LED NIGHT LIGHT'))
data_sale_product=product_sale_date(df_main,'71053','2010-01-01','2010-12-30')
data_sale_country = percente_product_country(df_main)
generate_graph_sale_date(data_sale_product)
generate_graph_sale_country(data_sale_country)
