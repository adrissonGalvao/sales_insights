import sales_insights as insights
import graphic
import json

class Service:
    def __init__(self):
        self.df_main = insights.treating_csv()

    def product_more_sale_country(self,product):
        product_more_sale = insights.product_more_sale_country(self.df_main,product)
        json_data = json.dumps(product_more_sale, indent=4, separators=(',', ' : '), sort_keys=True)
        return json_data

        
service=Service()
df_main =service.df_main 
print(service.product_more_sale_country("United Kingdom"))
#print(insights.product_more_sale(df_main))
#print(insights.best_client(df_main))
#print(insights.price_max_and_min(df_main,'RED TOADSTOOL LED NIGHT LIGHT'))
#print(insights.percentage_product(df_main,'RED TOADSTOOL LED NIGHT LIGHT'))

#data_sale_product=insights.product_sale_date(df_main,'71053','2010-01-01','2010-12-30')
#data_sale_country = insights.percent_product_country(df_main)
#data_price_sale=insights.price_and_quantity_sale_product(df_main,'RED TOADSTOOL LED NIGHT LIGHT') 

#graphic.generate_graphic_sale_date(data_sale_product)
#graphic.generate_graphic_sale_country(data_sale_country)
#graphic.generate_graphic_sale_product(data_price_sale)
   