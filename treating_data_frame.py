import pandas as pd
import matplotlib.pyplot as plt

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
    
    product_sale_date={"Quantity":[],"Date":[]}
    
    for x in products['InvoiceDate']:
       product_sale_date['Date'].append(x)
    
    for x in products['Quantity']:
       product_sale_date['Quantity'].append(str(x))
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
df_main=treating_csv()

print(product_more_sale_country(df_main,"United Kingdom"))
print(product_more_sale(df_main))
print(best_client(df_main))
print(product_sale_date(df_main,'71053','2010-01-01','2010-12-30'))
print(percentage_product(df_main,'RED TOADSTOOL LED NIGHT LIGHT'))



