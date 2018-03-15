from flask import Flask
from flask import request
from flask import jsonify
from flask import abort
from flask import Response
from flask import render_template
import service as serv
from datetime import datetime, timedelta

app = Flask(__name__)
service = serv.Service()

def get_period(begin, end):
	if begin == None:
		begin = datetime.now()	
	else:
		begin = datetime.strptime(begin, "%Y-%m-%d")

	if end == None:
		end = begin + timedelta(days=1)
		end = end.strftime('%Y-%m-%d')
	
	begin = begin.strftime('%Y-%m-%d')
	return (begin, end)
    
@app.route("/")
def hello():
   return "insights"

@app.route("/product/<product>")
def product_handler(product):
    if product==None:
        abort(400, 'INVALID PARAMETERS')
    
    result = service.product_more_sale_country(product)  	
    return  result

@app.route("/client/")
def best_client():
    result = service.best_client()

    return result

@app.route("/product/price/<product>")
def price_max_and_min(product):
    if product==None:
        abort(400, 'INVALID PARAMETERS')
    result = service.price_max_and_min(product)
    return result

@app.route("/product/percentage/<product>")
def percentage_product(product):
    if product==None:
        abort(400, 'INVALID PARAMETERS')
    result = service.percentage_product(product)
    return result
@app.route('/product/generate_graphic/<data>')
def generate_graphic_sale_date(data):

    begin = request.args.get('begin')
    end = request.args.get('end')
    product = request.args.get('product')

    if product==None or begin==None or end==None:
        abort(400, 'INVALID PARAMETERS')

    period = get_period(begin,end)
    service.generate_graphic_sale_date(product,period[0],period[1])
    img='/static/graphics/quantity_sale.png'
    return render_template("img.html",img=img)

@app.route('/product/generate_graphic_sale_country/')
def generate_graphic_sale_country():
    service.generate_graphic_sale_country()
    img='/static/graphics/percent_sale_by_country.png'
    return render_template("img.html",img=img)

@app.route('/product/generate_graphic_sale_product/<product>')
def generate_graphic_sale_product(product):
    service.generate_graphic_sale_product(product)
    img='/static/graphics/generate_graphic_sale_product.png'
    return render_template("img.html",img=img)

if __name__ == "__main__":
    app.run()

