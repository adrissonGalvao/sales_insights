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
    
    def best_client(self):
        best_client= insights.best_client(self.df_main)

        best_client['bigger_quantity']['value_sale']=str(best_client['bigger_quantity']['value_sale'])
        best_client['bigger_price']['value_sale']=str(best_client['bigger_price']['value_sale'])
        
        json_data = json.dumps(best_client,indent=4, separators=(',', ' : '), sort_keys=True)
        return json_data

    def price_max_and_min(self,product):
        variation_price = insights.price_max_and_min(self.df_main,product)
        json_data = json.dumps(variation_price,indent=4, separators=(',', ' : '), sort_keys=True)
        return json_data

    def percentage_product(self,product):
        percentage_product= insights.percentage_product(self.df_main,product)
        percentage_product= {'percentage':percentage_product,'product':product}
        json_data = json.dumps(percentage_product,indent=4, separators=(',', ' : '), sort_keys=True)
        return json_data
    def generate_graphic_sale_date(self,product_id,dt_begin,dt_end):
        data_sale_product=insights.product_sale_date(self.df_main,product_id,dt_begin,dt_end)
        graphic.generate_graphic_sale_date(data_sale_product)
    
    def generate_graphic_sale_country(self):
        data_sale_country = insights.percent_product_country(self.df_main)
        graphic.generate_graphic_sale_country(data_sale_country)

    def generate_graphic_sale_product(self,product):
        data_price_sale=insights.price_and_quantity_sale_product(self.df_main,product)
        graphic.generate_graphic_sale_product(data_price_sale)

   