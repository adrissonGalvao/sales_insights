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
    df.drop(['InvoiceDate','UnitPrice','CustomerID','Country','StockCode'],axis=1,inplace=True)
    list_quantity=df.groupby(['Description']).sum()
    return list_quantity.max()

df_main=treating_csv()
product_more_sale_country(df_main,"United Kingdom")
product_more_sale(df_main)