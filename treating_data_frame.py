import pandas as pd


def treating_csv():
    df = pd.read_csv('./data_test.csv')
    df.drop('InvoiceNo',axis=1,inplace=True)
    df = df[(df['Quantity'] > 0)]
    return df

def product_more_sale_country(df,country):
    df_country =pd.DataFrame(df[(df['Country'] ==country)])
    df_country.drop(['InvoiceDate','UnitPrice','CustomerID','Country','StockCode'],axis=1,inplace=True)
    list_quantity=df_country.groupby(['Description']).sum()
    return list_quantity.idxmax()

def product_more_sale(df):
    df_product=df.drop(['InvoiceDate','UnitPrice','CustomerID','Country','StockCode'],axis=1)
    list_quantity=df.groupby(['Description']).sum()
    return list_quantity.max()

def best_client(df):
    df_best_client=df.drop(['InvoiceDate','Country','StockCode'],axis=1)
    df_best_client["total"]=  df_best_client.Quantity * df_best_client.UnitPrice

    client_best = df_best_client.groupby(['CustomerID']).sum()
    best_client_price={'CustomerID':client_best['total'].idxmax(),'value_sale':client_best['total'].max()}
    best_client_quantity={'CustomerID':client_best['Quantity'].idxmax(),'value_sale':client_best['Quantity'].max()}
    best_client = {"bigeer_price":best_client_price,"bigeer_quantity":best_client_quantity}
    
    return best_client

df_main=treating_csv()
product_more_sale_country(df_main,"United Kingdom")
product_more_sale(df_main)
best_client(df_main)