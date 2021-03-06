import pandas as pd
from matplotlib import pyplot
import matplotlib.patches as mpatches

def generate_graphic_sale_product(data):
    df_graphic = pd.DataFrame({'Product':data['quantity']},index=data['price'])
    df_graphic.plot()
    pyplot.xlabel("Price by product($)")
    pyplot.ylabel("Amount Sale")
    pyplot.grid(True)
    pyplot.savefig('./static/graphics/generate_graphic_sale_product.png')

def generate_graphic_sale_country(data):

    list_graphic={'index':[],'value':[]}

    for country in data['list_percent']:
        list_graphic['index'].append(country)
        list_graphic['value'].append(data['list_percent'][country])

    df_graphic = pd.DataFrame({'Sale':list_graphic['value']},index=list_graphic['index'])
    pyplot.ylabel("PERCENTAGE OF SALE BY COUNTRY")
    df_graphic.plot.bar(figsize=[15,17])
    pyplot.savefig('./static/graphics/percent_sale_by_country.png')

def generate_graphic_sale_date(data):
    df_graphic = pd.DataFrame({'Sale':data['Quantity']},index=data['Date'])
    df_graphic.plot()
    pyplot.xlabel("Date")
    pyplot.grid(True)
    pyplot.ylabel("Amount Sale")
    pyplot.savefig('./static/graphics/quantity_sale.png')
